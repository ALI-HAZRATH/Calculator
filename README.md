# Calculator

🧮 Simple & Stylish Calculator
This is a minimalist and elegant web calculator built using Streamlit, allowing users to perform basic arithmetic operations (Addition, Subtraction, Multiplication, Division) in a clean and user-friendly interface.

🚀 Features
Input two numbers and select an arithmetic operation.

Stylish UI with custom CSS for a modern look.

Real-time results with error handling (e.g., division by zero).

Responsive layout using Streamlit's column system.

📸 Interface Preview



🧱 Tech Stack
Python

Streamlit for building the interactive UI

HTML/CSS for custom styling

📄 Code Breakdown
python
Copy
Edit
import streamlit as st
Initializes the Streamlit module.

python
Copy
Edit
st.set_page_config(...)
Sets page title, icon, and layout.

python
Copy
Edit
st.markdown(..., unsafe_allow_html=True)
Injects custom CSS to style the calculator card and buttons.

python
Copy
Edit
with st.container():
    ...
Wraps the main UI inside a styled container.

python
Copy
Edit
col1, col2 = st.columns(2)
Places the two number inputs side-by-side.

python
Copy
Edit
operation = st.radio(...)
Radio buttons to choose between add, subtract, multiply, divide.

python
Copy
Edit
def calculate(n1, n2, op):
    ...
Defines logic to handle the selected arithmetic operation. Includes a division-by-zero check.

python
Copy
Edit
if st.button("🔍 Calculate"):
    ...
Executes the calculation when the button is pressed and displays the result.

🛠 How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/simple-calculator.git
cd simple-calculator
Install dependencies:

bash
Copy
Edit
pip install streamlit
Run the app:

bash
Copy
Edit
streamlit run app.py
✅ Example
Input: 10 and 2

Operation: ➗ Divide

Output: ✅ Result: 5.0
