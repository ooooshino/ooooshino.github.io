<template>
  <section>
    <h2>项目经历</h2>

    <p><strong>xx（客户端级 WebApp 多渠道交付）｜核心前端开发｜2023 - 至今</strong></p>
    <ul>
      <li>负责 WebApp / WeApp 核心业务开发与维护，基于统一前端代码体系支撑多运行形态持续交付。</li>
      <li>
        应用形态覆盖 Web 直访、App 内嵌 WebView、iOS 马甲包、PWA、Telegram Mini App，保障核心功能一致性与可用性。
      </li>
      <li>推进 WeApp 内嵌包建设，采用“客户端外壳 + WebApp 业务内核”模式，提升业务扩展效率并兼顾平台合规要求。</li>
      <li>熟练使用 JSBridge 与客户端双向通信，落地登录态同步、支付能力、页面跳转、状态回传等关键交互链路。</li>
      <li>针对 iOS WebView 处理 fullscreen 适配问题，覆盖 Safe Area、沉浸式状态栏与页面高度异常等典型场景。</li>
      <li>基于 PWA（Service Worker / Cache / Manifest）增强离线访问与资源缓存能力，提升弱网场景可用性。</li>
      <li>
        设计并维护多渠道构建脚本，支持从渠道配置目录自动识别并构建，覆盖 170 个渠道配置，降低手工切换配置与发版风险。
      </li>
      <li>落地构建优化策略（splitChunks、runtimeChunk、gzip、defer、drop console/debugger），提升首屏加载与缓存命中表现。</li>
      <li>实现头像预加载工具与进度阈值策略（默认加载 50% 即可渲染），优化列表场景首屏可用体验。</li>
      <li>通过 Protobufjs 进行协议序列化与数据处理，提升数据传输安全性与协议处理效率。</li>
      <li>持续进行性能优化，Lighthouse 评分由 60 提升至 92，FCP 从 3.8s 优化至 1.4s。</li>
      <li><strong>技术栈：</strong>Vue 3 / Vue Router / Pinia / Axios / SCSS / Webpack / PWA / JSBridge / Protobufjs / vue-i18n / Agora。</li>
    </ul>

    <p><strong>xx → xx-monorepo（活动与业务 H5 工程平台升级）｜前端工程化建设｜2023 - 至今</strong></p>
    <ul>
      <li>接手存量 xx 独立项目群（项目相互独立、各自维护依赖与构建），推动工程平台化升级。</li>
      <li>
        在保留业务连续性的前提下，将多业务 H5 项目逐步整合为 xx-monorepo，基于 pnpm workspace + Turbo 建立统一构建链路与依赖管理机制。
      </li>
      <li>
        原项目群覆盖活动、邀请、支付、榜单、规则等高频场景，涉及 238 个独立 H5 子项目配置（仓库内 package 配置统计）。
      </li>
      <li>
        除平台化改造外，持续支援业务迭代与活动交付，面向混合 App 场景输出 WebView H5 页面，保障业务需求快速上线。
      </li>
      <li>
        通过 Plop 模板生成器沉淀活动页/普通页脚手架，标准化项目初始化流程，减少重复搭建与配置偏差，提升新项目起盘效率。
      </li>
      <li>抽离并复用公共包（`@kissu/utils` / `@kissu/styles`），统一 Bridge 与样式能力，提升多项目复用效率。</li>
      <li>打通 staging/production 双环境构建约定与 Jenkins 接入文档，降低多人协作下发布不确定性。</li>
      <li>建设 React + TypeScript + Vite 活动模板，补齐非 Vue 技术栈能力，为后续多技术栈接入提供基础。</li>
      <li>推动活动模板工程化升级（ESLint/Prettier/Husky/lint-staged）并统一构建约定，提升代码一致性与交付稳定性。</li>
      <li><strong>技术栈：</strong>Vue 3 / React / Vite / Turbo / pnpm workspace / Plop / Sass / postcss-pxtorem / ESLint / Prettier / Jenkins / Vant。</li>
    </ul>

    <p><strong>xx（运营管理后台）｜后台前端开发｜2023 - 至今</strong></p>
    <ul>
      <li>参与运营管理后台核心模块开发，覆盖统计报表、配置管理、用户与主播管理等运营链路。</li>
      <li>维护 8 条并行分支，对应 8 个运营平台版本，支撑多平台差异化配置与同步迭代发布。</li>
      <li>基于 Vue2 + Vuex + Vue Router + Element UI 构建后台交互与权限路由流程，提升运营配置效率。</li>
      <li>接入多类报表下载与 Excel 导入导出能力，支撑运营数据分析与日常对账场景。</li>
      <li>接入 Agora SDK 用于 1v1 通话过程监控与巡检，提升异常识别与运营干预效率。</li>
      <li>参与富文本配置、图表可视化、视频巡检等模块迭代，增强后台数据洞察与内容运营能力。</li>
      <li><strong>技术栈：</strong>Vue 2 / Vuex / Vue Router / Element UI / Axios / ECharts / xlsx / Agora。</li>
    </ul>
  </section>
</template>
