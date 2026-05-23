#!/usr/bin/env python3
"""
外儒内法 — 晨间启动清单生成器
输出今日身份权重和定位校准提醒
"""

import datetime

def morning_check():
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"=== 外儒内法 晨间启动 | {today} ===")
    print()
    print("今日身份权重：")
    print("  日结工 ___%  /  学徒 ___%  /  合伙人 ___%")
    print()
    print("今日定位：")
    print("  能干什么：___")
    print("  底线在哪：___")
    print()
    print("30秒自检：当情绪升起时立刻填——")
    print("  ① 期望：他要什么？")
    print("  ② 定位：我要什么？")
    print("  ③ 信号：这是策略层还是表达层？")
    print("  ④ 判断：迎合 / 控距 / 重新定义")
    print()
    print("提醒：80%的日常决策用速查卡，只有20%走完整四步。")

if __name__ == "__main__":
    morning_check()