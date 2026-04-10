#!/usr/bin/env python3
"""
保存用户反馈

功能：
- 保存用户对文章的回答
- 更新学习进度
- 返回反馈文件路径
"""

import argparse
import json
from pathlib import Path
from datetime import datetime


def save_feedback(topic: str, article_num: int, feedback: str) -> dict:
    """
    保存用户反馈
    
    Args:
        topic: 学习课题名称
        article_num: 文章序号
        feedback: 用户回答内容
    
    Returns:
        包含保存结果的字典
    """
    # 定位项目目录
    base_dir = Path("learning_notes")
    project_dir = base_dir / topic
    feedback_dir = project_dir / "feedback"
    progress_file = project_dir / "progress.json"
    
    # 检查项目是否存在
    if not project_dir.exists():
        return {
            "success": False,
            "error": f"学习项目 '{topic}' 不存在"
        }
    
    # 生成反馈文件名
    feedback_filename = f"feedback_{article_num:02d}.md"
    feedback_file = feedback_dir / feedback_filename
    
    # 构建反馈内容
    feedback_content = f"""# 学习反馈 - 第 {article_num} 篇文章

**学习课题**：{topic}  
**反馈时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

{feedback}

---

*此文件记录了用户对第 {article_num} 篇文章的回答，用于后续分析和迭代学习*
"""
    
    # 保存反馈
    with open(feedback_file, 'w', encoding='utf-8') as f:
        f.write(feedback_content)
    
    # 更新进度文件
    if progress_file.exists():
        with open(progress_file, 'r', encoding='utf-8') as f:
            progress_data = json.load(f)
        
        # 更新对应文章的学习记录
        for record in progress_data["learning_history"]:
            if record["article_num"] == article_num:
                record["status"] = "已学习"
                record["feedback_time"] = datetime.now().isoformat()
                break
        
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(progress_data, f, ensure_ascii=False, indent=2)
    
    return {
        "success": True,
        "feedback_file": str(feedback_file),
        "article_num": article_num,
        "message": f"第 {article_num} 篇文章的反馈保存成功"
    }


def main():
    parser = argparse.ArgumentParser(description="保存用户反馈")
    parser.add_argument("--topic", required=True, help="学习课题名称")
    parser.add_argument("--article-num", type=int, required=True, help="文章序号")
    parser.add_argument("--feedback", required=True, help="用户回答内容")
    
    args = parser.parse_args()
    
    result = save_feedback(args.topic, args.article_num, args.feedback)
    
    # 输出结果
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
