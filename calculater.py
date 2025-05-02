import streamlit as st

# Page configuration
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

# Custom CSS for style
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 0.5em 2em;
        }
    </style>
""", unsafe_allow_html=True)

# Main container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    # Title
    st.markdown("## 🧮 Simple & Stylish Calculator")

    # Input columns
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("🔢 First Number", format="%.2f", key="num1")
    with col2:
        num2 = st.number_input("🔢 Second Number", format="%.2f", key="num2")

    # Operation selection
    operation = st.radio("Choose Operation", ["➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide"], horizontal=True)

    # Calculation logic
    def calculate(n1, n2, op):
        if "Add" in op:
            return n1 + n2
        elif "Subtract" in op:
            return n1 - n2
        elif "Multiply" in op:
            return n1 * n2
        elif "Divide" in op:
            if n2 == 0:
                return "❌ Error: Division by zero"
            return n1 / n2

    # Calculate button
    if st.button("🔍 Calculate"):
        result = calculate(num1, num2, operation)
        st.success(f"✅ Result: {result}")

    st.markdown('</div>', unsafe_allow_html=True)
