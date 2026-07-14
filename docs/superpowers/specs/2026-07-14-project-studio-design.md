# Project Studio — 多项目全生命周期管理仓库设计

**日期：** 2026-07-14
**状态：** ✅ 已实施

## 背景

随着 AI 项目数量增长（预计 15+），需要一个统一的仓库来管理：
1. **前期设计文档** — 需求、架构、技术方案
2. **后期宣传物料** — 各平台推广文案、短视频脚本、发布说明
3. **个人品牌资产** — Logo、配色、简介模板、可复用文案片段

## 设计决策

- **方案 C（混合型）胜出**：兼顾项目深度和横向管理效率
- **仓库名**：`project-studio`（简洁专业，与 studio/ 目录呼应）
- **GitHub**：`cyk111/project-studio`
- **纯个人使用**：无需协作权限设计
- **各项目源码独立仓库**：本仓库只存"元内容"

## 目录结构

```
project-studio/
├── projects/
│   ├── active/                    # 🟢 开发中
│   ├── completed/                 # ✅ 已完成
│   └── incubating/                # 💡 想法孵化
├── studio/
│   ├── brand-kit/                 # 品牌资产
│   ├── templates/                 # 文档模板
│   └── snippets/                  # 可复用文案片段
├── archive/                       # 🗄️ 归档
├── dashboard.md                   # 📊 全局仪表盘
└── README.md
```

### 单项目结构

```
project-slug/
├── README.md                      # 项目卡片
├── design/
│   ├── 01-vision.md
│   ├── 02-architecture.md
│   ├── 03-features.md
│   └── 04-dev-log.md
├── promotion/
│   ├── platform-strategy.md
│   ├── xiaohongshu/
│   ├── douyin/
│   ├── twitter/
│   └── assets/
├── launch/
│   ├── release-notes.md
│   ├── changelog.md
│   └── landing-page.md
└── retrospect.md
```

### 工作流

```
新想法 → incubating/ → vision.md
      ↓
active/ → 设计文档 → 开发
      ↓
promotion/ + launch/ → 发布
      ↓
completed/ → retrospect.md
```

## 交付内容

- [x] GitHub 仓库初始化 & 推送
- [x] 完整目录结构
- [x] 5 个文档模板（项目 README、设计文档、小红书、抖音、发布说明）
- [x] 3 个文案片段库（钩子、CTA、标签）
- [x] 品牌资产管理模板
- [x] 全局仪表盘

## 仓库地址

https://github.com/cyk111/project-studio
