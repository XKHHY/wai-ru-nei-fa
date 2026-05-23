#!/usr/bin/env python3
"""
外儒内法 — 周末复盘模板生成器
输出本周复盘表格和评分维度
"""

import datetime

def weekly_review():
    today = datetime.date.today()
    # 找到本周五
    friday = today + datetime.timedelta(days=(4 - today.weekday()) % 7)
    week_str = friday.strftime("%Y-W%W")
    
    print(f"=== 外儒内法 周末复盘 | {week_str} ===")
    print()
    print("| 维度 | 评分(1-5) | 说明 |")
    print("|------|-----------|------|")
    print("| 期望判断准确度 | | 我猜对的次数占比 |")
    print("| 定位坚守程度 | | 我被带偏的次数 |")
    print("| 情绪标签速度 | | 多快完成策略/表达分类 |")
    print("| 功耗分配满意度 | | 精力花在了值得的地方吗 |")
    print("| 内法审计诚实度 | | 有没有自欺 |")
    print()
    print("本周关键决策回顾：")
    for i in range(1, 4):
        print(f"  {i}. 场景：___")
        print(f"     期望→定位→同理→行动→结果：___")
        print()
    print("反模式自查：")
    print("  □ 是否全儒无法（老好人）？")
    print("  □ 是否全法无儒（刺猬）？")
    print("  □ 是否儒法倒置？")
    print("  □ 是否框架武器化？")
    print("  □ 是否框架瘫痪？")
    print()
    print("下周调整：___")

if __name__ == "__main__":
    weekly_review()