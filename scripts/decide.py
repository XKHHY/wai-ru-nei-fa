#!/usr/bin/env python3
"""
外儒内法 — 事件触发决策辅助
交互式走完四步分析流程
"""

def decide():
    print("=== 外儒内法 事件触发决策辅助 ===")
    print()
    
    print("① 期望：他人/组织对我真正的盼望是什么？")
    expectation = input("  → ")
    print("  身份权重：日结工___% / 学徒___% / 合伙人___%")
    identity = input("  → ")
    print()
    
    print("② 定位：我的综合判断是什么？")
    print("  能干什么：")
    capability = input("  → ")
    print("  要不要干：")
    willingness = input("  → ")
    print("  底线在哪：")
    bottom_line = input("  → ")
    print()
    
    print("③ 同理：我能理解对方的动机吗？")
    empathy = input("  → ")
    print("  与我的定位是否背离？")
    conflict = input("  → ")
    print()
    
    print("④ 行动：成本可接受吗？")
    print("  可选动作：")
    print("    a) 迎合 — 期望与定位相符")
    print("    b) 控距 — 期望与定位不符")
    print("    c) 重新定义 — 找第三条路")
    print("    d) 逃离 — 成本不可接受")
    action = input("  → 选择: ")
    print()
    
    print("=== 决策输出 ===")
    print(f"期望：{expectation}（{identity}）")
    print(f"定位：{capability} / {willingness} / 底线：{bottom_line}")
    print(f"同理：{empathy} — {'背离' if conflict else '一致'}")
    actions = {'a': '迎合', 'b': '控距', 'c': '重新定义', 'd': '逃离'}
    print(f"行动：{actions.get(action, '未选择')}")
    print()
    
    # Anti-pattern check
    print("反模式自查：")
    if action == 'a' and not capability:
        print("  ⚠️  全儒无法风险：你选了迎合但没说清自己能干什么")
    if action == 'b' and not empathy:
        print("  ⚠️  全法无儒风险：你选了控距但没理解对方动机")
    print()

if __name__ == "__main__":
    decide()