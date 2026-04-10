#!/usr/bin/env python3
"""
初始化学习项目目录结构

功能：
- 创建学习课题的目录结构
- 初始化进度追踪文件
- 返回项目路径信息
"""

import argparse
import json
from pathlib import Path
from datetime import datetime


def init_learning_project(topic: str) -> dict:
    """
    初始化学习项目
    
    Args:
        topic: 学习课题名称（如"反脆弱"、"机器学习基础"等）
    
    Returns:
        包含项目信息的字典
    """
    # 定义基础学习目录
    base_dir = Path("learning_notes")
    project_dir = base_dir / topic
    
    # 创建目录结构
    articles_dir = project_dir / "articles"
    feedback_dir = project_dir / "feedback"
    
    articles_dir.mkdir(parents=True, exist_ok=True)
    feedback_dir.mkdir(parents=True, exist_ok=True)
    
    # 初始化进度文件
    progress_file = project_dir / "progress.json"
    
    progress_data = {
        "topic": topic,
        "start_time": datetime.now().isoformat(),
        "articles_count": 0,
        "current_article": 0,
        "mastery_level": "未开始",
        "concepts_mastered": [],
        "concepts_learning": [],
        "learning_history": []
    }
    
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(progress_data, f, ensure_ascii=False, indent=2)
    
    return {
        "success": True,
        "project_path": str(project_dir),
        "articles_dir": str(articles_dir),
        "feedback_dir": str(feedback_dir),
        "progress_file": str(progress_file),
        "message": f"学习项目 '{topic}' 初始化成功"
    }


def main():
    parser = argparse.ArgumentParser(description="初始化学习项目")
    parser.add_argument("--topic", required=True, help="学习课题名称")
    
    args = parser.parse_args()
    
    result = init_learning_project(args.topic)
    
    # 输出结果（JSON格式，便于智能体解析）
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
