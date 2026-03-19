#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path

import yaml


def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=True)


def getenv(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def load_config(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Missing config: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def copy_source(src_root: Path, dst_root: Path, excludes: list[str]) -> None:
    if dst_root.exists():
        shutil.rmtree(dst_root)
    dst_root.mkdir(parents=True, exist_ok=True)

    excluded = set(excludes)
    for item in src_root.iterdir():
        if item.name in excluded:
            continue
        if item.name == ".git":
            continue
        target = dst_root / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def remove_paths(root: Path, paths: list[str]) -> None:
    for rel in paths:
        p = root / rel
        if not p.exists():
            continue
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()


def iter_text_files(root: Path, exts: set[str]):
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in exts:
            yield p


def sanitize_text(text: str, replacements: list[dict], line_drop_patterns: list[str]) -> str:
    out = text
    for rule in replacements:
        pat = rule.get("pattern")
        repl = rule.get("replacement", "XX")
        if not pat:
            continue
        out = re.sub(pat, repl, out, flags=re.MULTILINE)

    if line_drop_patterns:
        regs = [re.compile(pat, re.IGNORECASE) for pat in line_drop_patterns]
        lines = []
        for line in out.splitlines():
            if any(reg.search(line) for reg in regs):
                continue
            lines.append(line)
        out = "\n".join(lines) + ("\n" if out.endswith("\n") else "")

    return out


def sanitize_files(root: Path, cfg: dict) -> None:
    exts = set(cfg.get("text_file_extensions", []))
    replacements = cfg.get("replacements", [])
    line_drop_patterns = cfg.get("line_drop_patterns", [])

    for f in iter_text_files(root, exts):
        text = f.read_text(encoding="utf-8", errors="ignore")
        sanitized = sanitize_text(text, replacements, line_drop_patterns)
        if sanitized != text:
            f.write_text(sanitized, encoding="utf-8")


def clean_repo_keep_git(repo_dir: Path) -> None:
    for item in repo_dir.iterdir():
        if item.name == ".git":
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def copy_into_repo(src: Path, repo: Path) -> None:
    for item in src.iterdir():
        target = repo / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def main() -> int:
    repo_root = Path(getenv("SOURCE_REPO_ROOT", ".")).resolve()
    config_path = Path(getenv("SANITIZE_CONFIG", "config/public_sanitize.yaml")).resolve()
    tmp_root = Path(getenv("TMP_DIR", ".tmp")).resolve()

    public_repo_url = getenv("PUBLIC_REPO_URL")
    public_branch = getenv("PUBLIC_REPO_BRANCH", "main")
    commit_message = getenv("PUBLISH_COMMIT_MESSAGE", "chore(发布): 同步脱敏简历")
    git_user_name = getenv("GIT_AUTHOR_NAME", "resume-publisher")
    git_user_email = getenv("GIT_AUTHOR_EMAIL", "resume-publisher@users.noreply.github.com")

    if not public_repo_url:
        print("[publish_public] PUBLIC_REPO_URL is required")
        return 2

    cfg = load_config(config_path)
    build_dir = tmp_root / "public_build"
    public_repo_dir = tmp_root / "public_repo"

    excludes = cfg.get("sync_exclude", [])
    copy_source(repo_root, build_dir, excludes)
    remove_paths(build_dir, cfg.get("remove_paths", []))
    sanitize_files(build_dir, cfg)

    if public_repo_dir.exists():
        shutil.rmtree(public_repo_dir)
    run(["git", "clone", "--depth", "1", "--branch", public_branch, public_repo_url, str(public_repo_dir)])

    clean_repo_keep_git(public_repo_dir)
    copy_into_repo(build_dir, public_repo_dir)

    run(["git", "config", "user.name", git_user_name], cwd=public_repo_dir)
    run(["git", "config", "user.email", git_user_email], cwd=public_repo_dir)
    run(["git", "add", "-A"], cwd=public_repo_dir)

    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=public_repo_dir,
        capture_output=True,
        text=True,
        check=True,
    )
    if not status.stdout.strip():
        print("[publish_public] no changes to publish")
        return 0

    run(["git", "commit", "-m", commit_message], cwd=public_repo_dir)
    run(["git", "push", "origin", public_branch], cwd=public_repo_dir)
    print("[publish_public] published")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
