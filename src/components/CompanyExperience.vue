<template>
  <section>
    <h2>工作经历</h2>
    <div>
      <p>
        <strong class="text-lg">
          <!-- 深圳市趣虹科技有限公司｜前端开发工程师｜2023.06 - 至今 -->
          深圳市xx科技有限公司｜前端开发工程师｜2023.06 - 至今
        </strong>
      </p>
    </div>
    <p>
      <!-- <strong> Hotchat web｜基于 vue3 的IM社交平台｜开发与维护｜2023.09 - 至今 </strong> -->
      <strong> 【核心项目】WebApp / WeApp（多运行形态的客户端级 Web 应用） </strong>
    </p>
    <!-- <ul>
      <li>
        项目基于前端 Vue3 框架，所用主要库有 Vue-Router + Swiper + Axios + Protobufjs +
        SCSS + Pinia + Agora + vue-i18n + Webpack
      </li>
      <li>
        项目开发过程中，
        1）使用Protobufjs对接口数据进行加密，保证用户数据在传输过程的<strong>隐私和安全</strong>；
        2）使用 vue-i18n 实现国际化，解决多语言切换问题 ； 3）使用 Agora SDK
        实现音视频通话功能，提高用户社交体验； 4）使用 Swiper
        实现轮播图功能和手写骨架屏，提高网站的视觉效果；
        5）使用register-service-worker为网站添加PWA功能，使得网站可以离线访问，让用户体验更加接近原生应用；
        6）使用lib-flexible搭配 postcss-pxtorem
        实现移动端适配，<strong>解决移动端适配问题</strong>； 7）为网站添加
        robots.txt，代码进行SEO优化，Lighthouse分数
        <strong> 从60优化变成92分 </strong>
        8）对代码进行性能处理，Lighthouse 性能指标分析
        <strong>从40优化到80分，网站FCP从3.8s提升到1.4s</strong>
      </li>
      <li>
        基于 Vue 3 构建
        WebApp，负责核心业务模块的开发与维护，实现与客户端一致的主要功能体验
      </li>
    </ul> -->
    <ul>
      <li>
        负责 WebApp / WeApp 的核心业务开发与维护，
        基于统一的前端代码体系，支持多种运行形态的业务交付
      </li>
      <li>
        应用形态覆盖：
        <strong
          >Web 直访 / App 内嵌 WebView / iOS 马甲包 / PWA / Telegram Mini App</strong
        >
      </li>
      <li>
        2025 年 Q2季度尾末开启 WeApp 内嵌包相关业务建设， 采用客户端外壳 + WebApp
        业务内核的混合架构方案， 提升业务形态扩展能力
      </li>
      <li>
        通过多页面形态拆分与能力隔离，兼顾平台合规要求与业务功能落地，
        提升整体交付的稳定性与可控性
      </li>
      <li>
        熟练使用 JSBridge 与客户端进行双向通信，
        完成登录态同步、支付能力、页面跳转、状态回传等核心交互
      </li>
      <li>
        针对 iOS WebView 场景，解决 fullscreen 全屏模式适配问题， 包括 Safe
        Area、安全区、沉浸式状态栏及页面高度异常等问题
      </li>
      <li>
        基于 PWA 能力（Service Worker / Cache / Manifest），
        支持离线访问与资源缓存，增强类原生体验
      </li>
      <li>
        适配 Telegram Mini App 运行环境，处理平台生命周期、
        容器限制及交互规范差异，保障核心业务能力可用
      </li>
      <li>
        技术栈：Vue3 / Vue-Router / Pinia / Axios / SCSS / Webpack / vue-i18n / Protobufjs
        / Agora
      </li>
      <li>
        使用 Protobufjs 对接口数据进行序列化与加密， 保障数据传输过程中的安全性与隐私性
      </li>
      <li>
        持续进行性能与体验优化， Lighthouse 评分由 60 提升至 92， FCP 从 3.8s 优化至 1.4s
      </li>
    </ul>
    <p><strong>【并行支援】运营管理平台（后台系统）</strong></p>
    <ul>
      <li>
        负责多个 App 项目的业务迭代 H5 与运营活动页开发，
        覆盖日常业务优化、拉新促活及阶段性运营活动等场景
      </li>
      <li>
        采用 Monorepo 架构统一管理 H5 与活动项目， 使用 Turbo
        进行任务编排与构建优化，提升多项目协作与维护效率
      </li>
      <li>注重活动页面的高精度 UI 还原， 在保证视觉一致性的同时兼顾性能与多端适配表现</li>
      <li>
        抽离并维护公共业务组件、通用样式与工具库，
        降低重复开发成本，提升整体代码一致性与可维护性
      </li>
      <li>
        基于 Plop 定制活动页与业务迭代模板， 实现页面结构、基础配置与规范的快速生成，
        显著提升高频迭代场景下的开发效率
      </li>
      <li>
        技术栈：Vue 3 / Vue-Router / Pinia / Vite / Vant / amfe-flexible / postcss-pxtorem
        / Sass / Axios / vue-i18n
      </li>
      <li>
        配合 ESLint + Prettier + Husky + lint-staged，
        建立统一的代码规范与提交校验流程，保障工程质量
      </li>
    </ul>
    <ul>
      <li>
        参与公司多个运营管理平台的前端开发与维护，
        支撑内容管理、活动配置、主播管理及数据监控等核心运营场景
      </li>
      <li>
        基于 Element UI 构建通用后台页面，
        实现表格列表、增删查改、表单校验及权限控制等基础能力
      </li>
      <li>
        使用 ECharts 5 实现运营数据与业务指标的可视化展示，
        提升运营人员对数据趋势与异常情况的感知效率
      </li>
      <li>
        接入声网（Agora）SDK，实现直播拉流状态监控，
        支持对主播直播状态的实时感知与异常监测
      </li>
      <li>
        对接第三方 AI 平台能力，实现主播头像上传后的自动美图与处理流程，
        提升运营配置效率与内容质量
      </li>
      <li>
        在工程层面对测试环境与正式环境进行区分，
        通过主题色等视觉标识明确环境差异，降低误操作风险
      </li>
    </ul>
    <p><strong>【并行支援】业务迭代 H5 / 运营活动页（Monorepo 工程体系）</strong></p>
    <ul>
      <li>
        负责多个 App 项目的业务迭代 H5 与运营活动页开发，
        覆盖日常业务优化、拉新促活及阶段性运营活动等场景
      </li>
      <li>
        采用 Monorepo 架构统一管理 H5 与活动项目， 使用 Turbo
        进行任务编排与构建优化，提升多项目协作与维护效率
      </li>
      <li>注重活动页面的高精度 UI 还原， 在保证视觉一致性的同时兼顾性能与多端适配表现</li>
      <li>
        抽离并维护公共业务组件、通用样式与工具库，
        降低重复开发成本，提升整体代码一致性与可维护性
      </li>
      <li>
        基于 Plop 定制活动页与业务迭代模板， 实现页面结构、基础配置与规范的快速生成，
        显著提升高频迭代场景下的开发效率
      </li>
      <li>
        技术栈：Vue 3 / Vue-Router / Pinia / Vite / Vant / amfe-flexible / postcss-pxtorem
        / Sass / Axios / vue-i18n
      </li>
      <li>
        配合 ESLint + Prettier + Husky + lint-staged，
        建立统一的代码规范与提交校验流程，保障工程质量
      </li>
    </ul>
  </section>
</template>
