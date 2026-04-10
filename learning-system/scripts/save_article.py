#!/usr/bin/env python3
"""
保存生成的文章和提问

功能：
- 保存文章内容到指定目录
- 更新学习进度文件
- 返回文章文件路径
"""

import argparse
import json
from pathlib import Path
from datetime import datetime


def save_article(topic: str, article_num: int, title: str, content: str, questions: str) -> dict:
    """
    保存文章和提问
    
    Args:
        topic: 学习课题名称
        article_num: 文章序号（第几篇文章）
        title: 文章标题
        content: 文章内容
        questions: 提问内容（JSON字符串或纯文本）
    
    Returns:
        包含保存结果的字典
    """
    # 定位项目目录
    base_dir = Path("learning_notes")
    project_dir = base_dir / topic
    articles_dir = project_dir / "articles"
    progress_file = project_dir / "progress.json"
    
    # 检查项目是否存在
    if not project_dir.exists():
        return {
            "success": False,
            "error": f"学习项目 '{topic}' 不存在，请先初始化项目"
        }
    
    # 生成文章文件名（格式：01-什么是反脆弱.md）
    article_filename = f"{article_num:02d}-{title}.md"
    article_file = articles_dir / article_filename
    
    # 构建文章内容
    full_content = f"""# {title}

**学习课题**：{topic}  
**文章序号**：第 {article_num} 篇  
**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

{content}

---

## 思考与练习

{questions}

---

## 你的回答

请在下方写下你的思考和回答：

**概念理解题回答**：


**应用题回答**：


**延伸思考题回答**：

"""
    
    # 保存文章
    with open(article_file, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    # 更新进度文件
    if progress_file.exists():
        with open(progress_file, 'r', encoding='utf-8') as f:
            progress_data = json.load(f)
        
        progress_data["articles_count"] = article_num
        progress_data["current_article"] = article_num
        progress_data["mastery_level"] = "学习中"
        
        # 添加学习记录
        progress_data["learning_history"].append({
            "article_num": article_num,
            "title": title,
            "time": datetime.now().isoformat(),
            "status": "已生成"
        })
        
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(progress_data, f, ensure_ascii=False, indent=2)
    
    return {
        "success": True,
        "article_file": str(article_file),
        "article_num": article_num,
        "title": title,
        "message": f"第 {article_num} 篇文章 '{title}' 保存成功"
    }


def main():
    parser = argparse.ArgumentParser(description="保存文章和提问")
    parser.add_argument("--topic", required=True, help="学习课题名称")
    parser.add_argument("--article-num", type=int, required=True, help="文章序号")
    parser.add_argument("--title", required=True, help="文章标题")
    parser.add_argument("--content", required=True, help="文章内容")
    parser.add_argument("--questions", required=True, help="提问内容")
    
    args = parser.parse_args()
    
    result = save_article(
        args.topic,
        args.article_num,
        args.title,
        args.content,
        args.questions
    )
    
    # 输出结果
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
