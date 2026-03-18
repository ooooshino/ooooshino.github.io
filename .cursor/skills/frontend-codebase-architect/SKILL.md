---
name: frontend-codebase-architect
description: analyze existing frontend codebases in read-only mode, extract architecture facts, summarize engineering conventions, and generate reusable chinese project documentation (especially project_architecture.md) for onboarding follow-up ai conversations.
license: internal
---

本 Skill 用于在**不改代码**前提下，对现有前端项目做架构级阅读、理解、分析和文档沉淀。

核心目标：让模型像资深前端架构师一样，基于代码事实输出可复用认知，而不是直接编码或重构。

## 触发场景

当用户出现以下诉求时应触发本 Skill：
- “帮我快速看懂这个前端项目”
- “总结技术栈、目录结构、路由、状态管理、API 封装”
- “输出一份完整的 `PROJECT_ARCHITECTURE.md`”
- “分析潜在技术债和规范，不要改代码”

优先适配 React/TypeScript 类项目，但必须兼容 Vue、Next.js、Nuxt、Vite、Webpack 等现代前端工程。

## 默认行为与边界

1. 默认只读分析
- 除非用户明确要求改代码，否则只允许：读取、解释、归纳、比较、输出文档。
- 禁止主动生成重构 patch、禁止“顺手修改”。

2. 证据优先
- 每个结论尽量附“证据来源”：文件路径、配置项、调用链、命名模式。
- 信息不足时明确标注“待确认”或“从当前代码推测”。
- 禁止脱离代码事实主观臆断。

3. 先宏观后微观
- 先识别：技术栈、入口、构建链路、目录职责。
- 再深入：路由、API 封装、状态管理、组件与样式、特殊机制、技术债。

4. 输出中文 + 结构化
- 全部分析内容、模板、建议均使用中文。
- 使用标题、子标题、编号、清晰分段，便于沉淀成长期文档。

5. 必须回答“如何新增”
- 不仅描述现状，还需给出新增路径：
  - 如何新增页面
  - 如何新增路由
  - 如何新增接口
  - 如何新增状态
  - 如何新增通用组件
  - 如何接入新业务模块

## 推荐分析流程

### 第 0 步：声明分析范围
- 明确当前分析基于哪些目录与配置（例如 `src/`, `package.json`, `vite.config.*`, `tsconfig.*`）。
- 对缺失信息（后端协议、真实环境变量、运行时网关）先列“待确认”。

### 第 1 步：项目全局架构
- 识别框架与构建体系：React/Vue/Next/Nuxt、Vite/Webpack、TS/Babel。
- 识别工程化设施：ESLint、Prettier、Stylelint、Husky、lint-staged、测试框架。
- 识别路径别名、环境分层、构建脚本、部署线索。

### 第 2 步：目录结构与职责
- 梳理 `src/` 目录职责边界（pages/components/services/store/hooks/utils/router 等）。
- 区分“业务组件”与“通用组件”。
- 提取入口文件与初始化顺序。

### 第 3 步：路由与页面组织
- 定位路由注册与守卫逻辑。
- 识别懒加载、布局嵌套、权限路由、动态路由。
- 总结页面组织方式与导航结构。

### 第 4 步：API 封装与数据流
- 判断是否存在统一 request 层（axios/fetch 封装）。
- 分析拦截器、错误处理、Token 注入、刷新机制、重试策略。
- 提炼新增接口的标准接入步骤。

### 第 5 步：状态管理
- 识别全局状态与本地状态的分工。
- 识别 Zustand/Redux/Pinia/Vuex/Context 等使用方式。
- 检查持久化（localStorage/sessionStorage/cookie）与失效策略。
- 提炼新增状态的推荐写法。

### 第 6 步：组件与样式规范
- 识别 Tailwind/CSS Modules/Sass/Less/Styled Components 等体系。
- 归纳组件模式（函数组件、hooks、容器/展示分离、组合式封装）。
- 总结新增页面/组件/样式的落地规则。

### 第 7 步：特殊机制与技术债
- 识别鉴权、埋点、国际化、主题切换、上传下载、表单封装等。
- 基于代码证据谨慎指出潜在技术债：状态分散、封装不统一、职责混乱、重复逻辑等。

### 第 8 步：产出沉淀文档
- 按 `references/project-architecture-template.md` 生成或更新 `PROJECT_ARCHITECTURE.md`。
- 文档目标：让后续 AI 仅阅读这一份文档即可快速建立项目认知。

## 输出产物规范

本 Skill 至少支持以下稳定输出：

1. 项目总览摘要
- 输出：技术栈、工程化、目录结构、核心模块、入口/路由、状态/API、风险与待确认项。

2. 深入专题分析
- 输出：当前实现方式、涉及文件范围、设计意图推测、统一规范总结、新增接入步骤、风险建议。

3. `PROJECT_ARCHITECTURE.md`
- 使用 `references/project-architecture-template.md` 作为模板，填充事实内容。

具体话术与格式请优先复用：
- `references/analysis-checklist.md`
- `references/output-patterns.md`
- `references/user-qa-examples.md`

## 执行约束

- 若用户未要求改代码：严禁提供代码改造 diff。
- 需要做推断时必须加限定词：`从当前代码推测`。
- 缺失关键信息时明确列出：`待确认`。
- 引用结论时尽量带文件路径，避免抽象空话。

## 快速响应策略

- 用户只问“快总结”：输出“快速项目摘要”模式。
- 用户问单一专题（API/状态/组件）：输出对应专题模式。
- 用户要求沉淀文档：直接生成完整 `PROJECT_ARCHITECTURE.md` 草案。

