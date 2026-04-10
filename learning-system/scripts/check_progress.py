#!/usr/bin/env python3
"""
检查学习进度

功能：
- 读取学习项目的进度信息
- 统计学习数据
- 返回进度报告
"""

import argparse
import json
from pathlib import Path


def check_progress(topic: str) -> dict:
    """
    检查学习进度
    
    Args:
        topic: 学习课题名称
    
    Returns:
        包含进度信息的字典
    """
    # 定位项目目录
    base_dir = Path("learning_notes")
    project_dir = base_dir / topic
    progress_file = project_dir / "progress.json"
    
    # 检查项目是否存在
    if not project_dir.exists():
        return {
            "success": False,
            "error": f"学习项目 '{topic}' 不存在"
        }
    
    # 读取进度文件
    if not progress_file.exists():
        return {
            "success": False,
            "error": "进度文件不存在"
        }
    
    with open(progress_file, 'r', encoding='utf-8') as f:
        progress_data = json.load(f)
    
    # 统计文章和反馈数量
    articles_dir = project_dir / "articles"
    feedback_dir = project_dir / "feedback"
    
    article_files = list(articles_dir.glob("*.md")) if articles_dir.exists() else []
    feedback_files = list(feedback_dir.glob("*.md")) if feedback_dir.exists() else []
    
    # 构建进度报告
    progress_report = {
        "success": True,
        "topic": progress_data.get("topic", topic),
        "start_time": progress_data.get("start_time", "未知"),
        "mastery_level": progress_data.get("mastery_level", "未开始"),
        "articles": {
            "total": len(article_files),
            "current": progress_data.get("current_article", 0),
            "files": [f.name for f in sorted(article_files)]
        },
        "feedback": {
            "total": len(feedback_files),
            "files": [f.name for f in sorted(feedback_files)]
        },
        "concepts": {
            "mastered": progress_data.get("concepts_mastered", []),
            "learning": progress_data.get("concepts_learning", [])
        },
        "learning_history": progress_data.get("learning_history", []),
        "project_path": str(project_dir)
    }
    
    return progress_report


def main():
    parser = argparse.ArgumentParser(description="检查学习进度")
    parser.add_argument("--topic", required=True, help="学习课题名称")
    
    args = parser.parse_args()
    
    result = check_progress(args.topic)
    
    # 输出结果
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
