import streamlit as st
import periodictable as pt

st.title("实验室化学称量助手 🧪")

formula_str = st.text_input("请输入化学式", "Ba2Cu3O7")
moles = st.number_input("计划摩尔量 (mol)", value=0.01, format="%.4f")

if st.button("开始计算"):
    formula = pt.formula(formula_str)
    total_mass = formula.mass * moles
    st.write(f"### 总质量: {total_mass:.4f} g")
    
    # 自动生成表格
    data = []
    for element, count in formula.atoms.items():
        data.append({
            "元素": str(element),
            "原子数": count,
            "需称量 (g)": f"{element.mass * count * moles:.4f}"
        })
    st.table(data)