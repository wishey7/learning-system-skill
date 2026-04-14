# Learning System Skill

交互式学习系统，通过 AI 生成文章、提问、分析反馈的迭代闭环，帮助用户深入掌握任意知识。

## 简介

这是一个基于 AI 的交互式学习系统，通过迭代式文章生成、互动提问、反馈分析的闭环流程实现深度学习。

## 功能特点

- **迭代式学习闭环**：生成文章 → 提问 → 用户反馈 → 分析 → 针对性生成
- **三类提问设计**：概念理解题、应用题、延伸思考题
- **个性化学习路径**：根据用户回答动态调整内容
- **知识网络化**：支持双向链接，构建知识网络
- **掌握度评估**：明确的评估标准和归档条件

## 适用场景

- 系统性学习某个课题或概念
- 深度阅读书籍并掌握核心思想
- 学习新的专业知识领域
- 构建个人知识体系

## 安装使用

### 前置要求

- Python 3.6+
- 扣子平台或支持 Skill 的 AI 环境

### 使用步骤

1. 初始化学习项目：
```bash
python scripts/init_learning.py --topic "反脆弱"
```

2. 生成文章并保存：
```bash
python scripts/save_article.py \
  --topic "反脆弱" \
  --article-num 1 \
  --title "什么是反脆弱" \
  --content "文章内容..." \
  --questions "问题列表..."
```

3. 保存用户反馈：
```bash
python scripts/save_feedback.py \
  --topic "反脆弱" \
  --article-num 1 \
  --feedback "用户回答内容..."
```

4. 检查学习进度：
```bash
python scripts/check_progress.py --topic "反脆弱"
```

## 项目结构

```
learning-system/
├── SKILL.md                    # Skill 入口文档
├── scripts/                    # Python 脚本
│   ├── init_learning.py       # 初始化学习项目
│   ├── save_article.py        # 保存文章和提问
│   ├── save_feedback.py       # 保存用户反馈
│   └── check_progress.py      # 检查学习进度
├── references/                 # 参考文档
│   ├── question_templates.md  # 问题模板库
│   └── mastery_criteria.md    # 掌握度评估标准
└── assets/                     # 资源文件
    └── note_template.md       # 学习笔记模板
```

## 学习流程

1. **初始化项目** - 创建学习目录结构
2. **生成第一篇文章** - 深入浅出讲解核心概念
3. **用户学习反馈** - 阅读文章并回答问题
4. **AI 分析反馈** - 评估掌握程度和兴趣方向
5. **迭代生成内容** - 根据反馈生成针对性文章
6. **重复迭代** - 直到完全掌握
7. **归档总结** - 生成学习笔记并构建知识网络

## 学习示例：反脆弱

### 第一轮学习
- 文章：什么是反脆弱
- 提问：5-6个问题（概念理解、应用、延伸思考）

### 第二轮学习
- 根据用户反馈，聚焦"杠铃策略"等薄弱环节

### 归档
- 生成完整学习笔记
- 建立与相关知识的双向链接

## 技术栈

- **语言**：Python 3.6+
- **依赖**：pathlib（Python 标准库）
- **AI 能力**：自然语言生成、逻辑推理、内容分析

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 作者

Created by Wishey

## 致谢

灵感来源于抖音博主siyao

## 联系方式

- GitHub: [wishey7](https://github.com/wishey7)
