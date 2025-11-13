

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Julia Language Guide for Economists",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful design
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .block-container {
        padding: 2rem;
    }
    h1, h2, h3 {
        color: #2d3748;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        border: none;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .code-block {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
    }
    .output-block {
        background-color: #f7fafc;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    .info-box {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    .warning-box {
        background: linear-gradient(135deg, #fc466b15 0%, #3f5efb15 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #fc466b;
        margin: 1rem 0;
    }
    .success-box {
        background: linear-gradient(135deg, #11998e15 0%, #38ef7d15 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #11998e;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <h1 style='text-align: center; color: #667eea; font-size: 3rem; margin-bottom: 0;'>
        📊 Comprehensive Julia Language Guide for Economists
    </h1>
    <h3 style='text-align: center; color: #764ba2; margin-top: 0;'>
        Prepared by: Dr. Marwan Roudan
    </h3>
    <p style='text-align: center; font-size: 1.2rem; color: #4a5568;'>
        An interactive, professional guide for students and researchers.
    </p>
    <hr style='border: 2px solid #667eea; margin: 2rem 0;'>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("## 🎯 Main Menu")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Select a section:",
    [
        "🏠 Introduction to Julia",
        "📝 Basics",
        "🔢 Data Types",
        "➕ Arithmetic Operations",
        "🔄 Loops",
        "⚖️ Conditionals",
        "📊 Arrays & DataFrames",
        "📈 Plotting",
        "🎲 Functions",
        "📦 Economic Packages",
        "🔍 Error Handling",
        "💼 Economic Applications"
    ]
)

# Section 1: Introduction
if menu == "🏠 Introduction to Julia":
    st.markdown("## 🏠 Introduction to Julia")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='info-box'>
        <h3>What is Julia?</h3>
        <p style='font-size: 1.1rem; line-height: 1.8;'>
        Julia is a modern, high-performance programming language designed specifically for scientific computing and economic analysis.
        It combines the speed of languages like C with the ease of languages like Python.
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='success-box'>
        <h3>Why Julia for Economists?</h3>
        <ul style='font-size: 1.1rem; line-height: 1.8;'>
        <li>⚡️ Superior speed for complex economic equations</li>
        <li>📊 Powerful libraries for econometric analysis</li>
        <li>🔢 Excellent support for linear algebra and matrices</li>
        <li>🎯 Ease of writing economic models</li>
        <li>🆓 Free and open-source</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Performance comparison chart
        languages = ['Julia', 'Python', 'R', 'MATLAB']
        speed = [1.0, 0.15, 0.12, 0.18]

        fig = go.Figure(data=[
            go.Bar(
                x=languages,
                y=speed,
                marker=dict(
                    color=['#667eea', '#fc466b', '#3f5efb', '#11998e'],
                    line=dict(color='white', width=2)
                ),
                text=[f'{s * 100:.0f}%' for s in speed],
                textposition='auto',
            )
        ])

        fig.update_layout(
            title=dict(
                text='Speed Comparison (Julia = 100%)',
                font=dict(size=20, color='#2d3748')
            ),
            xaxis_title='Programming Language',
            yaxis_title='Relative Speed',
            template='plotly_white',
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class='warning-box'>
        <h3>⚠️ Important Notes</h3>
        <p style='font-size: 1.1rem; line-height: 1.8;'>
        • Julia uses 1-based indexing (not 0-based like Python)<br>
        • It is case-sensitive<br>
        • It needs to compile on the first run (JIT compilation)<br>
        • Use a semicolon (;) to suppress output
        </p>
        </div>
        """, unsafe_allow_html=True)

# Section 2: Basics
elif menu == "📝 Basics":
    st.markdown("## 📝 Basics in Julia")

    st.markdown("""
    <div class='info-box'>
    <h3>Basic Rules:</h3>
    <ul style='font-size: 1.1rem; line-height: 1.8;'>
    <li>📌 Use <code>=</code> to assign values to variables</li>
    <li>📌 Use <code>#</code> for single-line comments</li>
    <li>📌 Use <code>println()</code> to print</li>
    <li>📌 Semicolons at the end of a line are not required (optional)</li>
    <li>📌 Use <code>;</code> at the end of a line to suppress output in the REPL</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    examples = {
        "Basic Variables": {
            "code": """# Defining variables
x = 10
y = 20
name = "Mohammed"  # Julia supports Unicode!
π_value = 3.14159

println("Value of x: ", x)
println("Value of y: ", y)
println("Name: ", name)
println("Value of π: ", π_value)""",
            "output": """Value of x: 10
Value of y: 20
Name: Mohammed
Value of π: 3.14159""",
            "rules": """✅ Rules:
• Variable names can contain Unicode characters.
• Special symbols like π can be used.
• A variable name cannot start with a number.
• Avoid reserved keywords (if, for, while, etc.)."""
        },

        "Basic Operations": {
            "code": """# Simple arithmetic operations
a = 15
b = 4

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
remainder = a % b
power = a ^ 2

println("Addition: ", addition)
println("Subtraction: ", subtraction)
println("Multiplication: ", multiplication)
println("Division: ", division)
println("Remainder: ", remainder)
println("Power: ", power)""",
            "output": """Addition: 19
Subtraction: 11
Multiplication: 60
Division: 3.75
Remainder: 3
Power: 225""",
            "rules": """✅ Rules:
• + for addition
• - for subtraction
• * for multiplication
• / for division
• % for remainder
• ^ for exponentiation"""
        },

        "Strings": {
            "code": """# Working with strings
first_name = "Ahmed"
last_name = "Mahmoud"

# Concatenate strings
full_name = first_name * " " * last_name
println("Full Name: ", full_name)

# String length
println("Number of characters: ", length(full_name))

# Repeat string
println("Repetition: ", first_name ^ 3)""",
            "output": """Full Name: Ahmed Mahmoud
Number of characters: 11
Repetition: AhmedAhmedAhmed""",
            "rules": """✅ Rules:
• Use "" or '' for strings.
• * to concatenate strings.
• ^ to repeat a string.
• length() to calculate the length."""
        }
    }

    for title, content in examples.items():
        with st.expander(f"### {title}", expanded=True):
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown("**Code:**")
                st.code(content["code"], language="julia")

                if st.button(f"▶️ Run", key=f"run_{title}"):
                    st.success("Execution simulated!")

            with col2:
                st.markdown("**Output:**")
                st.markdown(f"<div class='output-block'><pre>{content['output']}</pre></div>", unsafe_allow_html=True)

                st.markdown("**Rules:**")
                st.markdown(f"<div class='info-box'>{content['rules']}</div>", unsafe_allow_html=True)

# Section 3: Data Types
elif menu == "🔢 Data Types":
    st.markdown("## 🔢 Data Types in Julia")

    st.markdown("""
    <div class='info-box'>
    <h3>Main Data Types:</h3>
    <p style='font-size: 1.1rem;'>
    Julia is a dynamically typed language, but it has a rich type system.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # Create visualization
    data_types = {
        'Type': ['Int64', 'Float64', 'String', 'Bool', 'Array', 'Dict'],
        'Description': ['Integers', 'Floating-point numbers', 'Text', 'Boolean', 'Arrays', 'Dictionaries'],
        'Example': ['42', '3.14', '"text"', 'true', '[1,2,3]', 'Dict("a"=>1)'],
        'Economic Use Case': ['Number of units', 'Price', 'Product name', 'Purchase decision', 'Time series', 'Composite data']
    }

    df = pd.DataFrame(data_types)

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(df.columns),
            fill_color='#667eea',
            align='center',
            font=dict(color='white', size=14, family='Arial'),
            height=40
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            fill_color=[['#f7fafc', '#e2e8f0'] * 3],
            align='center',
            font=dict(color='#2d3748', size=12, family='Arial'),
            height=35
        )
    )])

    fig.update_layout(
        title=dict(text='Data Types Table', font=dict(size=20)),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    examples = {
        "Integers": {
            "code": """# Integers
number_of_students = 100
year = 2024

println("Number of students: ", number_of_students)
println("Data type: ", typeof(number_of_students))
println("Year: ", year)

# Conversion
text_number = "250"
converted_number = parse(Int64, text_number)
println("After conversion: ", converted_number)""",
            "output": """Number of students: 100
Data type: Int64
Year: 2024
After conversion: 250""",
            "rules": """✅ Rules:
• Int8, Int16, Int32, Int64 (depending on size).
• Use typeof() to check the type.
• parse() to convert from a string.
• ⚠️ Error: Overflow when exceeding the maximum limit."""
        },

        "Floats": {
            "code": """# Floating-point numbers
price = 99.99
growth_rate = 0.05
interest_rate = 3.5

println("Price: ", price)
println("Data type: ", typeof(price))
println("Growth rate: ", growth_rate * 100, "%")

# Mathematical operations
tax = price * 0.15
println("Tax: ", round(tax, digits=2))""",
            "output": """Price: 99.99
Data type: Float64
Growth rate: 5.0%
Tax: 15.0""",
            "rules": """✅ Rules:
• Float32, Float64 (double precision).
• round() for rounding.
• digits= to specify the number of decimal places.
• ⚠️ Error: Precision errors can occur in operations."""
        },

        "Booleans": {
            "code": """# Boolean values
is_student = true
is_registered = false
age = 20

# Comparisons
is_adult = age >= 18
println("Is adult? ", is_adult)
println("Data type: ", typeof(is_adult))

# Logical operations
is_qualified = is_student && is_adult  # AND
println("Qualified for scholarship? ", is_qualified)

can_register = is_student || is_registered  # OR
println("Can register? ", can_register)""",
            "output": """Is adult? true
Data type: Bool
Qualified for scholarship? true
Can register? true""",
            "rules": """✅ Rules:
• Only `true` and `false`.
• `&&` for the AND operation.
• `||` for the OR operation.
• `!` for negation (NOT).
• `==`, `!=`, `<`, `>`, `<=`, `>=` for comparisons."""
        },

        "Arrays": {
            "code": """# Arrays
prices = [10.5, 20.3, 15.7, 30.2]
years = [2020, 2021, 2022, 2023]

println("Prices: ", prices)
println("Data type: ", typeof(prices))
println("Number of elements: ", length(prices))

# Accessing elements (indexing starts from 1)
println("First price: ", prices[1])
println("Last price: ", prices[end])

# Operations
average = sum(prices) / length(prices)
println("Average: ", round(average, digits=2))""",
            "output": """Prices: [10.5, 20.3, 15.7, 30.2]
Data type: Vector{Float64}
Number of elements: 4
First price: 10.5
Last price: 30.2
Average: 19.18""",
            "rules": """✅ Rules:
• Indexing starts from 1 (very important!).
• `[]` to create an array.
• `[i]` to access an element.
• `end` for the last element.
• `push!()` to add an element.
• ⚠️ Error: BoundsError when accessing out-of-bounds index."""
        },

        "Dictionaries": {
            "code": """# Dictionaries
economic_data = Dict(
    "GDP" => 500.5,
    "Inflation" => 2.5,
    "Unemployment" => 5.2
)

println("Data: ", economic_data)
println("Inflation rate: ", economic_data["Inflation"], "%")

# Add a new element
economic_data["InterestRate"] = 3.0
println("After addition: ", economic_data)

# Check if a key exists
println("Does GDP exist? ", haskey(economic_data, "GDP"))""",
            "output": """Data: Dict("GDP" => 500.5, "Inflation" => 2.5, "Unemployment" => 5.2)
Inflation rate: 2.5%
After addition: Dict("GDP" => 500.5, "Inflation" => 2.5, "Unemployment" => 5.2, "InterestRate" => 3.0)
Does GDP exist? true""",
            "rules": """✅ Rules:
• `Dict()` to create a dictionary.
• `=>` to link a key to a value.
• `[]` to access and add elements.
• `haskey()` to check for existence.
• `keys()` for keys, `values()` for values."""
        }
    }

    for title, content in examples.items():
        with st.expander(f"### {title}", expanded=False):
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown("**Code:**")
                st.code(content["code"], language="julia")

                if st.button(f"▶️ Run", key=f"run_{title}"):
                    st.success("Execution simulated!")

            with col2:
                st.markdown("**Output:**")
                st.markdown(f"<div class='output-block'><pre>{content['output']}</pre></div>", unsafe_allow_html=True)

                st.markdown("**Rules:**")
                st.markdown(f"<div class='info-box'>{content['rules']}</div>", unsafe_allow_html=True)

# Section 4: Arithmetic Operations
elif menu == "➕ Arithmetic Operations":
    st.markdown("## ➕ Advanced Arithmetic Operations")

    st.markdown("""
    <div class='info-box'>
    <h3>Basic and Advanced Arithmetic Operations:</h3>
    </div>
    """, unsafe_allow_html=True)

    # Interactive calculator
    st.markdown("### 🧮 Interactive Calculator")

    col1, col2, col3 = st.columns(3)

    with col1:
        num1 = st.number_input("First Number", value=100.0, key="calc_num1")
    with col2:
        operation = st.selectbox("Operation", ["+", "-", "*", "/", "^", "%", "//"], key="calc_op")
    with col3:
        num2 = st.number_input("Second Number", value=20.0, key="calc_num2")

    if st.button("Calculate"):
        result = None
        op_name = ""
        if operation == "+":
            result = num1 + num2
            op_name = "Addition"
        elif operation == "-":
            result = num1 - num2
            op_name = "Subtraction"
        elif operation == "*":
            result = num1 * num2
            op_name = "Multiplication"
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                op_name = "Division"
            else:
                st.error("⚠️ Error: Cannot divide by zero!")
        elif operation == "^":
            result = num1 ** num2
            op_name = "Exponentiation"
        elif operation == "%":
            result = num1 % num2
            op_name = "Remainder"
        elif operation == "//":
            result = num1 // num2
            op_name = "Integer Division"

        if result is not None:
            st.success(f"### Result of {op_name}: {result:.2f}")

    st.markdown("---")

    examples = {
        "Basic Arithmetic Operations": {
            "code": """# Arithmetic operations on economic variables
principal = 10000
interest_rate = 0.05
number_of_years = 3

# Calculate simple interest
simple_interest = principal * interest_rate * number_of_years
println("Simple Interest: ", simple_interest)

# Calculate compound interest
compound_amount = principal * (1 + interest_rate)^number_of_years
println("Amount with Compound Interest: ", round(compound_amount, digits=2))

# Profit
profit = compound_amount - principal
println("Profit: ", round(profit, digits=2))""",
            "output": """Simple Interest: 1500.0
Amount with Compound Interest: 11576.25
Profit: 1576.25""",
            "rules": """✅ Rules:
• + for addition
• - for subtraction
• * for multiplication
• / for division
• ^ for exponentiation (compound interest)
• round() for rounding"""
        },

        "Mathematical Functions": {
            "code": """# Useful mathematical functions for economists
value = -15.7

# Absolute value
absolute_val = abs(value)
println("Absolute value: ", absolute_val)

# Square root
sqrt_val = sqrt(100)
println("Square root of 100: ", sqrt_val)

# Logarithm (important in economic models)
log_val = log(100)  # Natural log
println("Natural logarithm: ", round(log_val, digits=2))

# Exponential
exp_val = exp(2)
println("e^2: ", round(exp_val, digits=2))

# Maximum and Minimum
numbers = [45, 23, 67, 12, 89]
println("Maximum: ", maximum(numbers))
println("Minimum: ", minimum(numbers))""",
            "output": """Absolute value: 15.7
Square root of 100: 10.0
Natural logarithm: 4.61
e^2: 7.39
Maximum: 89
Minimum: 12""",
            "rules": """✅ Rules:
• abs() for absolute value
• sqrt() for square root
• log() for natural logarithm
• log10() for base-10 logarithm
• exp() for exponential
• maximum(), minimum()
• ⚠️ Error: DomainError for sqrt of a negative number"""
        },

        "Basic Statistics": {
            "code": """# Basic statistics for economic data
using Statistics  # Load the Statistics package

sales = [120, 135, 142, 128, 155, 148, 162, 139]

# Mean
avg = mean(sales)
println("Mean: ", round(avg, digits=2))

# Median
med = median(sales)
println("Median: ", med)

# Standard Deviation
std_dev = std(sales)
println("Standard Deviation: ", round(std_dev, digits=2))

# Variance
variance = var(sales)
println("Variance: ", round(variance, digits=2))

# Sum
total = sum(sales)
println("Total Sales: ", total)""",
            "output": """Mean: 141.12
Median: 140.5
Standard Deviation: 13.85
Variance: 191.84
Total Sales: 1129""",
            "rules": """✅ Rules:
• `using Statistics` for stats functions.
• `mean()` for the average.
• `median()` for the median.
• `std()` for standard deviation.
• `var()` for variance.
• `sum()` for the total sum.
• `length()` for the number of elements."""
        },

        "Array Operations": {
            "code": """# Operations on arrays
prices = [100, 150, 200, 120]
quantities = [5, 3, 2, 8]

# Element-wise multiplication
revenues = prices .* quantities  # Note the dot .
println("Revenues: ", revenues)

# Sum of all elements
total_revenue = sum(revenues)
println("Total Revenue: ", total_revenue)

# Apply a 10% discount
discount = 0.10
prices_after_discount = prices .* (1 - discount)
println("Prices after discount: ", prices_after_discount)

# Add a 15% tax
tax = 0.15
final_prices = prices_after_discount .* (1 + tax)
println("Final prices: ", round.(final_prices, digits=2))""",
            "output": """Revenues: [500, 450, 400, 960]
Total Revenue: 2310
Prices after discount: [90.0, 135.0, 180.0, 108.0]
Final prices: [103.5, 155.25, 207.0, 124.2]""",
            "rules": """✅ Rules:
• Use a `.` before an operator to apply it element-wise.
• `.*` for element-wise multiplication.
• `./` for element-wise division.
• `.+` for element-wise addition.
• `.^` for element-wise exponentiation.
• `round.()` to round each element in an array."""
        }
    }

    for title, content in examples.items():
        with st.expander(f"### {title}", expanded=False):
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown("**Code:**")
                st.code(content["code"], language="julia")

                if st.button(f"▶️ Run", key=f"run_{title}"):
                    st.success("Execution simulated!")

            with col2:
                st.markdown("**Output:**")
                st.markdown(f"<div class='output-block'><pre>{content['output']}</pre></div>", unsafe_allow_html=True)

                st.markdown("**Rules:**")
                st.markdown(f"<div class='info-box'>{content['rules']}</div>", unsafe_allow_html=True)

# Section 5: Loops
elif menu == "🔄 Loops":
    st.markdown("## 🔄 Loops")

    st.markdown("""
    <div class='info-box'>
    <h3>Types of Loops in Julia:</h3>
    <ul style='font-size: 1.1rem; line-height: 1.8;'>
    <li>🔁 <strong>for loop:</strong> To iterate a specific number of times.</li>
    <li>🔁 <strong>while loop:</strong> To iterate as long as a condition is true.</li>
    <li>🔁 <strong>break:</strong> To exit a loop.</li>
    <li>🔁 <strong>continue:</strong> To skip the current iteration.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    examples = {
        "Basic for Loop": {
            "code": """# Simple for loop
println("Printing numbers from 1 to 5:")
for i in 1:5
    println("Number: ", i)
end

# Loop over an array
cities = ["Riyadh", "Jeddah", "Dammam", "Makkah"]
println("\\nCities:")
for city in cities
    println("- ", city)
end

# Loop with a specific step
println("\\nEven numbers from 0 to 10:")
for i in 0:2:10
    println(i)
end""",
            "output": """Printing numbers from 1 to 5:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

Cities:
- Riyadh
- Jeddah
- Dammam
- Makkah

Even numbers from 0 to 10:
0
2
4
6
8
10""",
            "rules": """✅ Rules:
• `for variable in range`.
• `1:5` means from 1 to 5.
• `0:2:10` means from 0 to 10 with a step of 2.
• `end` to terminate the loop block.
• ⚠️ Error: Forgetting `end`."""
        },

        "Economic Application: Compound Interest Calculation": {
            "code": """# Calculate capital growth over the years
initial_capital = 10000
interest_rate = 0.08  # 8%
number_of_years = 10

println("Capital Growth:")
println("Year\\tAmount")
println("----\\t------")

capital = initial_capital
for year in 1:number_of_years
    global capital
    capital = capital * (1 + interest_rate)
    println(year, "\\t", round(capital, digits=2))
end

total_profit = capital - initial_capital
println("\\nTotal Profit: ", round(total_profit, digits=2))""",
            "output": """Capital Growth:
Year	Amount
----	------
1	10800.0
2	11664.0
3	12597.12
4	13604.89
5	14693.28
6	15868.74
7	17138.24
8	18509.3
9	19990.05
10	21589.25

Total Profit: 11589.25""",
            "rules": """✅ Rules:
• Use a for loop for repetitive calculations.
• Update the variable inside the loop.
• `round()` for formatting in each iteration.
• `\\t` creates a tab space for alignment."""
        },

        "while Loop": {
            "code": """# while loop - until a goal is reached
savings_goal = 50000
balance = 0
monthly_saving = 2000
month = 0

println("Savings Plan:")
while balance < savings_goal
    global month, balance
    month += 1
    balance += monthly_saving
    println("Month ", month, ": Balance = ", balance)

    # Safety break to prevent infinite loop
    if month >= 30
        println("Warning: Exceeded 30 months!")
        break
    end
end

println("\\nReached the goal in ", month, " months")""",
            "output": """Savings Plan:
Month 1: Balance = 2000
Month 2: Balance = 4000
...
Month 24: Balance = 48000
Month 25: Balance = 50000

Reached the goal in 25 months""",
            "rules": """✅ Rules:
• `while condition`.
• The condition is checked before each iteration.
• Use `break` to exit.
• `+=` to increment.
• ⚠️ Error: Infinite loop if the condition never becomes false."""
        },

        "Using break and continue": {
            "code": """# Find the first price exceeding 150
prices = [100, 120, 145, 160, 180, 155]

println("Searching for the first price > 150:")
for (index, price) in enumerate(prices)
    if price <= 150
        continue  # Skip low prices
    end

    println("Found! Price ", price, " at index ", index)
    break  # Stop at the first match
end

println("\\nPrinting prices (ignoring negative values):")
prices_with_negatives = [100, -50, 120, -30, 150]
for price in prices_with_negatives
    if price < 0
        continue  # Skip negative values
    end
    println("Valid price: ", price)
end""",
            "output": """Searching for the first price > 150:
Found! Price 160 at index 4

Printing prices (ignoring negative values):
Valid price: 100
Valid price: 120
Valid price: 150""",
            "rules": """✅ Rules:
• `break` to exit the loop immediately.
• `continue` to skip the rest of the current iteration.
• `enumerate()` to get both the index and the value.
• Useful for searching and filtering."""
        },

        "Nested Loops": {
            "code": """# Simple multiplication table (3x3)
println("Multiplication Table:")
for i in 1:3
    for j in 1:3
        result = i * j
        print(i, " × ", j, " = ", result, "\\t")
    end
    println()  # New line after each row
end

# Calculate sales for multiple products and branches
products = ["Product A", "Product B"]
branches = ["Branch 1", "Branch 2"]
prices = [100, 150]

println("\\nSales Report:")
for (i, product) in enumerate(products)
    for (j, branch) in enumerate(branches)
        sales = prices[i] * (i + j)  # Simplified formula
        println(product, " in ", branch, ": ", sales)
    end
end""",
            "output": """Multiplication Table:
1 × 1 = 1	1 × 2 = 2	1 × 3 = 3	
2 × 1 = 2	2 × 2 = 4	2 × 3 = 6	
3 × 1 = 3	3 × 2 = 6	3 × 3 = 9	

Sales Report:
Product A in Branch 1: 200
Product A in Branch 2: 300
Product B in Branch 1: 450
Product B in Branch 2: 600""",
            "rules": """✅ Rules:
• `for` loops can be nested.
• The inner loop completes all its iterations for each single iteration of the outer loop.
• `print()` prints without a new line.
• `println()` prints with a new line.
• `enumerate()` is useful for indexing."""
        }
    }

    for title, content in examples.items():
        with st.expander(f"### {title}", expanded=False):
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown("**Code:**")
                st.code(content["code"], language="julia")

                if st.button(f"▶️ Run", key=f"run_{title}"):
                    st.success("Execution simulated!")

            with col2:
                st.markdown("**Output:**")
                st.markdown(f"<div class='output-block'><pre>{content['output']}</pre></div>", unsafe_allow_html=True)

                st.markdown("**Rules:**")
                st.markdown(f"<div class='info-box'>{content['rules']}</div>", unsafe_allow_html=True)

# Section 6: Conditionals
elif menu == "⚖️ Conditionals":
    st.markdown("## ⚖️ Conditionals")

    st.markdown("""
    <div class='info-box'>
    <h3>Types of Conditional Statements:</h3>
    <ul style='font-size: 1.1rem; line-height: 1.8;'>
    <li>✅ <strong>if:</strong> Execute code if a condition is true.</li>
    <li>✅ <strong>elseif:</strong> An alternative condition to check.</li>
    <li>✅ <strong>else:</strong> Execute if all preceding conditions fail.</li>
    <li>✅ <strong>Logical Operators:</strong> && (AND), || (OR), ! (NOT).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Interactive condition tester
    st.markdown("### 🧪 Interactive Condition Tester")

    col1, col2 = st.columns(2)
    with col1:
        income = st.number_input("Monthly Income", min_value=0, value=5000, step=500)
        expenses = st.number_input("Monthly Expenses", min_value=0, value=3000, step=500)

    with col2:
        st.markdown("### Result:")
        net_income = income - expenses

        if net_income > 2000:
            st.success(f"✅ Excellent! You have a surplus: {net_income}")
            st.info("You can save and invest.")
        elif net_income > 0:
            st.warning(f"⚠️ Good! You have a small surplus: {net_income}")
            st.info("Try to increase your savings.")
        else:
            st.error(f"❌ Warning! You have a deficit: {net_income}")
            st.info("Review your expenses.")

    st.markdown("---")

    examples = {
        "Simple Conditionals (if)": {
            "code": """# Simple condition
price = 150

if price > 100
    println("The price is high")
end

# Condition with else
age = 17

if age >= 18
    println("Adult - can vote")
else
    println("Minor - cannot vote")
end

# Multiple conditions with elseif
grade = 85

if grade >= 90
    println("Excellent: A")
elseif grade >= 80
    println("Very Good: B")
elseif grade >= 70
    println("Good: C")
else
    println("Pass or Fail")
end""",
            "output": """The price is high
Minor - cannot vote
Very Good: B""",
            "rules": """✅ Rules:
• `if condition ... end`.
• `elseif` for additional conditions.
• `else` for the default case.
• Conditions are checked in order.
• Only the block of the first true condition is executed.
• ⚠️ Error: Forgetting `end`."""
        },

        "Comparison Operators": {
            "code": """# Comparison operators
a = 10
b = 20

println("a == b: ", a == b)  # Equal to
println("a != b: ", a != b)  # Not equal to
println("a < b: ", a < b)    # Less than
println("a > b: ", a > b)    # Greater than
println("a <= b: ", a <= b)  # Less than or equal to
println("a >= b: ", a >= b)  # Greater than or equal to

# Economic example
market_price = 95
cost_price = 80

if market_price > cost_price
    profit = market_price - cost_price
    println("\\nThere is a profit: ", profit)
elseif market_price == cost_price
    println("\\nNo profit or loss")
else
    loss = cost_price - market_price
    println("\\nThere is a loss: ", loss)
end""",
            "output": """a == b: false
a != b: true
a < b: true
a > b: false
a <= b: true
a >= b: false

There is a profit: 15""",
            "rules": """✅ Rules:
• `==` for equality.
• `!=` for inequality.
• `<`, `>`, `<=`, `>=` for comparisons.
• The result is always `true` or `false`.
• Can be used in `if` statements."""
        },

        "Logical Operators (AND, OR, NOT)": {
            "code": """# Logical operators
income = 6000
age = 25
has_job = true

# AND (&&) - all conditions must be true
if income > 5000 && age >= 21
    println("Eligible for a large loan")
end

# OR (||) - at least one condition must be true
if income > 8000 || has_job
    println("Eligible for a regular loan")
end

# NOT (!) - inverts the condition
is_registered = false
if !is_registered
    println("You must register first")
end

# Compound conditions
has_excellent_credit = true
if (income > 5000 && age >= 21) || has_excellent_credit
    println("\\nReceived the best interest rate")
end

# Economic example: Investment decision
expected_return = 0.12  # 12%
risk = "low"
duration = 5  # years

if expected_return > 0.10 && risk == "low" && duration >= 3
    println("\\nInvestment Decision: Recommended to invest ✅")
else
    println("\\nInvestment Decision: Consider options carefully ⚠️")
end""",
            "output": """Eligible for a large loan
Eligible for a regular loan
You must register first

Received the best interest rate

Investment Decision: Recommended to invest ✅""",
            "rules": """✅ Rules:
• `&&` for the AND operation (all conditions).
• `||` for the OR operation (at least one condition).
• `!` for the NOT operation (negation).
• Use `()` to group conditions.
• Precedence: `!` then `&&` then `||`."""
        },

        "Application: Company Classification": {
            "code": """# Classify companies based on performance
revenue = 5_000_000  # _ can be used for readability
profit = 800_000
growth_rate = 0.15  # 15%
num_employees = 150

# Calculate profit margin
profit_margin = profit / revenue

println("Company Classification Report")
println("=" ^ 30)

# Classification
classification = ""
if profit_margin >= 0.20 && growth_rate >= 0.15
    classification = "Excellent - Star ⭐⭐⭐"
elseif profit_margin >= 0.15 && growth_rate >= 0.10
    classification = "Very Good - Rising ⭐⭐"
elseif profit_margin >= 0.10 && growth_rate >= 0.05
    classification = "Good - Stable ⭐"
elseif profit_margin >= 0.05
    classification = "Acceptable - Needs improvement ⚠️"
else
    classification = "Weak - Needs restructuring ❌"
end

println("Profit Margin: ", round(profit_margin * 100, digits=2), "%")
println("Growth Rate: ", round(growth_rate * 100, digits=2), "%")
println("Number of Employees: ", num_employees)
println("\\nClassification: ", classification)

# Recommendations
println("\\nRecommendations:")
if profit_margin < 0.10
    println("• Focus on increasing profitability")
end
if growth_rate < 0.05
    println("• Plan for growth strategies")
end
if num_employees > 200
    println("• Review operational efficiency")
end""",
            "output": """Company Classification Report
==============================
Profit Margin: 16.0%
Growth Rate: 15.0%
Number of Employees: 150

Classification: Very Good - Rising ⭐⭐

Recommendations:""",
            "rules": """✅ Rules:
• `_` can be used in numbers for clarity.
• `"=" ^ 30` repeats the character 30 times.
• Combine logical conditions intelligently.
• Use a variable to store the classification result.
• Add recommendations based on conditions."""
        },

        "Ternary Operator": {
            "code": """# Ternary operator: condition ? if_true : if_false
price = 120

# Normal way
status = ""
if price > 100
    status = "High"
else
    status = "Low"
end
println("Normal way: ", status)

# Ternary way (shorter)
ternary_status = price > 100 ? "High" : "Low"
println("Ternary operator: ", ternary_status)

# Example: Calculate discount
quantity = 15
discount = quantity >= 10 ? 0.15 : 0.05
println("\\nQuantity: ", quantity)
println("Discount rate: ", discount * 100, "%")

final_price = price * (1 - discount)
println("Price after discount: ", round(final_price, digits=2))

# Nested ternary operator (avoid over-complication)
grade = 75
level = grade >= 90 ? "Excellent" :
        grade >= 70 ? "Good" : "Acceptable"
println("\\nLevel: ", level)""",
            "output": """Normal way: High
Ternary operator: High

Quantity: 15
Discount rate: 15.0%
Price after discount: 102.0

Level: Good""",
            "rules": """✅ Rules:
• Syntax: `condition ? value_if_true : value_if_false`.
• Useful for simple assignments.
• Shorter than a full if-else block.
• Avoid excessive nesting (it becomes hard to read).
• Use it only for simple conditions."""
        }
    }

    for title, content in examples.items():
        with st.expander(f"### {title}", expanded=False):
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown("**Code:**")
                st.code(content["code"], language="julia")

                if st.button(f"▶️ Run", key=f"run_{title}"):
                    st.success("Execution simulated!")

            with col2:
                st.markdown("**Output:**")
                st.markdown(f"<div class='output-block'><pre>{content['output']}</pre></div>", unsafe_allow_html=True)

                st.markdown("**Rules:**")
                st.markdown(f"<div class='info-box'>{content['rules']}</div>", unsafe_allow_html=True)

# Section 7: Arrays and DataFrames
elif menu == "📊 Arrays & DataFrames":
    st.markdown("## 📊 Arrays & DataFrames")

    st.markdown("""
    <div class='info-box'>
    <h3>Working with Data:</h3>
    <ul style='font-size: 1.1rem; line-height: 1.8;'>
    <li>📋 <strong>Arrays:</strong> 1D and multi-dimensional arrays.</li>
    <li>📊 <strong>DataFrames:</strong> Tabular data structures like in Excel or R.</li>
    <li>🔧 <strong>Operations:</strong> Performing operations on data.</li>
    <li>📈 <strong>Analysis:</strong> Analyzing economic data.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    examples = {
        "1D Arrays (Vectors)": {
            "code": """# Create a 1D array
prices = [100, 150, 200, 175, 225]
println("Prices: ", prices)

# Accessing elements (1-based indexing!)
println("First price: ", prices[1])
println("Last price: ", prices[end])
println("Third price: ", prices[3])

# Modify an element
prices[2] = 160
println("After modification: ", prices)

# Add an element
push!(prices, 250)  # Adds to the end
println("After addition: ", prices)

# Remove the last element
pop!(prices)
println("After removal: ", prices)

# Array information
println("\\nNumber of elements: ", length(prices))
println("Type: ", typeof(prices))""",
            "output": """Prices: [100, 150, 200, 175, 225]
First price: 100
Last price: 225
Third price: 200
After modification: [100, 160, 200, 175, 225]
After addition: [100, 160, 200, 175, 225, 250]
After removal: [100, 160, 200, 175, 225]

Number of elements: 5
Type: Vector{Int64}""",
            "rules": """✅ Rules:
• `[]` to create an array.
• Indexing starts from 1 (important!).
• `[i]` to access an element.
• `end` for the last element.
• `push!()` to add to the end.
• `pop!()` to remove from the end.
• `!` indicates that the function modifies the array.
• ⚠️ Error: BoundsError on out-of-bounds access."""
        },

        "Operations on Arrays": {
            "code": """# Advanced operations on arrays
sales = [120, 135, 142, 128, 155, 148]

# Statistics
using Statistics

println("Mean: ", round(mean(sales), digits=2))
println("Median: ", median(sales))
println("Maximum: ", maximum(sales))
println("Minimum: ", minimum(sales))
println("Sum: ", sum(sales))

# Sorting
sorted_sales = sort(sales)
println("\\nSorted ascending: ", sorted_sales)

desc_sales = sort(sales, rev=true)
println("Sorted descending: ", desc_sales)

# Filtering
high_sales = filter(x -> x > 140, sales)
println("\\nSales > 140: ", high_sales)

# Transformation (map)
sales_in_thousands = map(x -> x / 1000, sales)
println("In thousands: ", sales_in_thousands)

# Slicing
first_three = sales[1:3]
println("\\nFirst 3 days: ", first_three)""",
            "output": """Mean: 138.0
Median: 138.5
Maximum: 155
Minimum: 120
Sum: 828

Sorted ascending: [120, 128, 135, 142, 148, 155]
Sorted descending: [155, 148, 142, 135, 128, 120]

Sales > 140: [142, 155, 148]

In thousands: [0.12, 0.135, 0.142, 0.128, 0.155, 0.148]

First 3 days: [120, 135, 142]""",
            "rules": """✅ Rules:
• `sort()` for sorting (doesn't modify original).
• `sort!()` for in-place sorting (modifies original).
• `rev=true` for descending order.
• `filter(condition, array)` for filtering.
• `map(function, array)` for transformation.
• `[start:end]` for slicing.
• `->` for anonymous (lambda) functions."""
        },

        "Multi-dimensional Arrays": {
            "code": """# 2D array (Matrix)
# Sales for 3 products over 4 months
sales_matrix = [
    120 135 142 128;  # Product 1
    90  95  88  92;   # Product 2
    150 145 160 155   # Product 3
]

println("The Matrix:")
println(sales_matrix)

# Dimensions
println("\\nDimensions: ", size(sales_matrix))
println("Number of rows: ", size(sales_matrix, 1))
println("Number of columns: ", size(sales_matrix, 2))

# Accessing elements
println("\\nSales of Product 1 in Month 2: ", sales_matrix[1, 2])
println("Sales of Product 3 in Month 4: ", sales_matrix[3, 4])

# A full row (product)
println("\\nSales of Product 2: ", sales_matrix[2, :])

# A full column (month)
println("Sales in Month 3: ", sales_matrix[:, 3])

# Sum for each product
println("\\nTotal for each product:")
for i in 1:size(sales_matrix, 1)
    total = sum(sales_matrix[i, :])
    println("Product ", i, ": ", total)
end

# Sum for each month
println("\\nTotal for each month:")
for j in 1:size(sales_matrix, 2)
    total = sum(sales_matrix[:, j])
    println("Month ", j, ": ", total)
end""",
            "output": """The Matrix:
3×4 Matrix{Int64}:
 120  135  142  128
  90   95   88   92
 150  145  160  155

Dimensions: (3, 4)
Number of rows: 3
Number of columns: 4

Sales of Product 1 in Month 2: 135
Sales of Product 3 in Month 4: 155

Sales of Product 2: [90, 95, 88, 92]
Sales in Month 3: [142, 88, 160]

Total for each product:
Product 1: 525
Product 2: 365
Product 3: 610

Total for each month:
Month 1: 360
Month 2: 375
Month 3: 390
Month 4: 375""",
            "rules": """✅ Rules:
• 2D array: `[row1; row2; row3]`
• Or with spaces: `[1 2; 3 4]`
• `[i, j]` to access an element.
• `[i, :]` for a full row.
• `[:, j]` for a full column.
• `size()` for dimensions.
• Indexing is 1-based for both rows and columns."""
        },

        "DataFrames": {
            "code": """# Working with DataFrames (like Excel)
using DataFrames

# Create a DataFrame
data = DataFrame(
    Product = ["Wheat", "Rice", "Barley", "Corn"],
    Price = [150.5, 180.0, 120.0, 140.5],
    Quantity = [1000, 800, 1200, 950],
    Country = ["KSA", "Egypt", "Jordan", "KSA"]
)

println("The DataFrame:")
println(data)

# DataFrame info
println("\\nNumber of rows: ", nrow(data))
println("Number of columns: ", ncol(data))
println("Column names: ", names(data))

# Accessing a column
println("\\nPrices: ", data.Price)
# or
println("Prices (method 2): ", data[:, :Price])

# Add a new column
data.Revenue = data.Price .* data.Quantity
println("\\nAfter adding Revenue column:")
println(data)

# Filtering
println("\\nProducts from KSA:")
ksa_products = filter(row -> row.Country == "KSA", data)
println(ksa_products)

# Sorting
println("\\nSorted by Price:")
sorted_data = sort(data, :Price, rev=true)
println(sorted_data)

# Statistics
println("\\nAverage Price: ", round(mean(data.Price), digits=2))
println("Total Revenue: ", sum(data.Revenue))""",
            "output": """The DataFrame:
4×4 DataFrame
 Row │ Product  Price    Quantity  Country
     │ String   Float64  Int64     String
─────┼─────────────────────────────────────
   1 │ Wheat    150.5       1000   KSA
   2 │ Rice     180.0        800   Egypt
   3 │ Barley   120.0       1200   Jordan
   4 │ Corn     140.5        950   KSA

Number of rows: 4
Number of columns: 4
Column names: ["Product", "Price", "Quantity", "Country"]

Prices: [150.5, 180.0, 120.0, 140.5]
Prices (method 2): [150.5, 180.0, 120.0, 140.5]

After adding Revenue column:
[DataFrame with Revenue column]

Products from KSA:
[Rows for KSA]

Sorted by Price:
[Sorted DataFrame]

Average Price: 147.75
Total Revenue: 578975.0""",
            "rules": """✅ Rules:
• `using DataFrames` to load the library.
• `DataFrame()` to create a table.
• `.` to access a column.
• `[:, :name]` is an alternative way to access a column.
• `filter()` for filtering rows.
• `sort()` for sorting.
• `nrow()`, `ncol()` for counts.
• Add a column: `df.new_col = ...`
• ⚠️ Use `.*` for element-wise operations on columns."""
        },

        "Practical Application: Sales Analysis": {
            "code": """# Comprehensive sales data analysis
using DataFrames, Statistics

# Sales data
sales_df = DataFrame(
    Day = 1:7,
    Sales = [1200, 1350, 980, 1420, 1560, 1380, 1290],
    Costs = [800, 900, 650, 950, 1040, 920, 860],
    Customers = [45, 52, 38, 55, 60, 53, 49]
)

# Calculate profit
sales_df.Profit = sales_df.Sales .- sales_df.Costs

# Calculate profit margin
sales_df.ProfitMargin = (sales_df.Profit ./ sales_df.Sales) .* 100

# Average spend per customer
sales_df.AvgCustomerSpend = sales_df.Sales ./ sales_df.Customers

println("Weekly Sales Report")
println("=" ^ 50)
println(sales_df)

# Statistics
println("\\nStatistical Analysis:")
println("-" ^ 50)
println("Average Daily Sales: ", round(mean(sales_df.Sales), digits=2))
println("Average Daily Profit: ", round(mean(sales_df.Profit), digits=2))
println("Average Profit Margin: ", round(mean(sales_df.ProfitMargin), digits=2), "%")
println("Highest Sales: ", maximum(sales_df.Sales))
println("Lowest Sales: ", minimum(sales_df.Sales))

# Best and worst day
best_day = sales_df[argmax(sales_df.Sales), :]
worst_day = sales_df[argmin(sales_df.Sales), :]

println("\\nBest Day: Day ", best_day.Day, " with sales of ", best_day.Sales)
println("Worst Day: Day ", worst_day.Day, " with sales of ", worst_day.Sales)

# Totals
println("\\nTotals:")
println("Total Sales: ", sum(sales_df.Sales))
println("Total Profit: ", sum(sales_df.Profit))
println("Total Customers: ", sum(sales_df.Customers))""",
            "output": """Weekly Sales Report
==================================================
7×7 DataFrame
 Row │ Day  Sales  Costs  Customers  Profit  ProfitMargin  AvgCustomerSpend
[Full DataFrame]

Statistical Analysis:
--------------------------------------------------
Average Daily Sales: 1311.43
Average Daily Profit: 454.29
Average Profit Margin: 34.65%
Highest Sales: 1560
Lowest Sales: 980

Best Day: Day 5 with sales of 1560
Worst Day: Day 3 with sales of 980

Totals:
Total Sales: 9180
Total Profit: 3180
Total Customers: 352""",
            "rules": """✅ Rules:
• `.-` for element-wise subtraction.
• `./` for element-wise division.
• `.*` for element-wise multiplication.
• `argmax()` for the index of the maximum value.
• `argmin()` for the index of the minimum value.
• Use DataFrames for structured data.
• Calculate key metrics (profit margin, averages, etc.)."""
        }
    }

    for title, content in examples.items():
        with st.expander(f"### {title}", expanded=False):
            col1, col2 = st.columns([1, 1])

            with col1:
                st.markdown("**Code:**")
                st.code(content["code"], language="julia")

                if st.button(f"▶️ Run", key=f"run_{title}"):
                    st.success("Execution simulated!")

            with col2:
                st.markdown("**Output:**")
                st.markdown(f"<div class='output-block'><pre>{content['output']}</pre></div>", unsafe_allow_html=True)

                st.markdown("**Rules:**")
                st.markdown(f"<div class='info-box'>{content['rules']}</div>", unsafe_allow_html=True)

# Section 8: Plotting
elif menu == "📈 Plotting":
    st.markdown("## 📈 Plotting in Julia")

    st.markdown("""
    <div class='info-box'>
    <h3>Plotting Libraries in Julia:</h3>
    <ul style='font-size: 1.1rem; line-height: 1.8;'>
    <li>📊 <strong>Plots.jl:</strong> The main library for plotting.</li>
    <li>📈 <strong>StatsPlots.jl:</strong> For statistical plots.</li>
    <li>🎨 <strong>PlotlyJS.jl:</strong> For interactive plots.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Interactive Examples")

    # Example 1: Line chart for time series
    years = list(range(2015, 2025))
    gdp = [450, 470, 495, 510, 525, 505, 520, 560, 595, 630]

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=years,
        y=gdp,
        mode='lines+markers',
        name='GDP',
        line=dict(color='#667eea', width=3),
        marker=dict(size=10, color='#764ba2')
    ))

    fig1.update_layout(
        title='Gross Domestic Product (GDP) Growth (2015-2024)',
        xaxis_title='Year',
        yaxis_title='GDP (in Billions)',
        template='plotly_white',
        hovermode='x unified'
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.code("""
# Line plot for time series
using Plots

years = 2015:2024
gdp = [450, 470, 495, 510, 525, 505, 520, 560, 595, 630]

plot(years, gdp, 
    label="GDP",
    xlabel="Year",
    ylabel="GDP (in Billions)",
    title="GDP Growth",
    lw=3,  # line width
    marker=:circle,
    markersize=8,
    legend=:topleft,
    color=:blue)
    """, language="julia")

    # Example 2: Bar chart
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    sales = [45000, 38000, 52000, 41000, 49000]

    fig2 = go.Figure(data=[
        go.Bar(
            x=products,
            y=sales,
            marker=dict(
                color=sales,
                colorscale='Viridis',
                showscale=True
            ),
            text=sales,
            textposition='auto',
        )
    ])

    fig2.update_layout(
        title='Product Sales',
        xaxis_title='Product',
        yaxis_title='Sales',
        template='plotly_white'
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.code("""
# Bar chart for sales
using Plots

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = [45000, 38000, 52000, 41000, 49000]

bar(products, sales,
    title="Product Sales",
    xlabel="Product",
    ylabel="Sales",
    legend=false,
    color=:viridis,
    fillalpha=0.8)
    """, language="julia")

    # Example 3: Pie chart
    categories = ['Salaries', 'Rent', 'Raw Materials', 'Marketing', 'Other']
    values = [45, 20, 18, 12, 5]

    fig3 = go.Figure(data=[go.Pie(
        labels=categories,
        values=values,
        hole=.3,
        marker=dict(colors=['#667eea', '#764ba2', '#fc466b', '#3f5efb', '#11998e'])
    )])

    fig3.update_layout(
        title='Distribution of Expenses',
        template='plotly_white'
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.code("""
# Pie chart for expenses
using Plots

categories = ["Salaries", "Rent", "Raw Materials", "Marketing", "Other"]
values = [45, 20, 18, 12, 5]

pie(categories, values,
    title="Distribution of Expenses",
    legend=:outerbottom,
    l=0.5)
    """, language="julia")

    # Example 4: Multiple lines
    months = list(range(1, 13))
    sales_2023 = [120, 135, 142, 128, 155, 148, 162, 139, 175, 182, 195, 210]
    sales_2024 = [125, 140, 148, 135, 162, 155, 170, 148, 185, 192, 205, 220]

    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=months,
        y=sales_2023,
        mode='lines+markers',
        name='2023',
        line=dict(color='#667eea', width=2)
    ))
    fig4.add_trace(go.Scatter(
        x=months,
        y=sales_2024,
        mode='lines+markers',
        name='2024',
        line=dict(color='#fc466b', width=2)
    ))

    fig4.update_layout(
        title='Monthly Sales Comparison',
        xaxis_title='Month',
        yaxis_title='Sales (in Thousands)',
        template='plotly_white',
        hovermode='x unified'
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.code("""
# Multiple line plot for comparison
using Plots

months = 1:12
sales_2023 = [120, 135, 142, 128, 155, 148, 162, 139, 175, 182, 195, 210]
sales_2024 = [125, 140, 148, 135, 162, 155, 170, 148, 185, 192, 205, 220]

plot(months, sales_2023, 
    label="2023",
    lw=2,
    marker=:circle,
    color=:blue)

plot!(months, sales_2024,
    label="2024",
    lw=2,
    marker=:square,
    color=:red,
    xlabel="Month",
    ylabel="Sales (in Thousands)",
    title="Monthly Sales Comparison")
    """, language="julia")

    st.markdown("""
    <div class='warning-box'>
    <h3>⚠️ Important Notes:</h3>
    <ul style='font-size: 1.1rem;'>
    <li>Use <code>plot()</code> to create a new plot.</li>
    <li>Use <code>plot!()</code> to add to an existing plot (note the `!`).</li>
    <li><code>savefig("name.png")</code> to save the plot.</li>
    <li>You can customize colors, sizes, and styles.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Section 9: Functions
elif menu == "🎲 Functions":
    st.markdown("## 🎲 Functions")

    st.markdown("""
    <div class='info-box'>
    <h3>The Importance of Functions:</h3>
    <p style='font-size: 1.1rem; line-height: 1.8;'>
    Functions help you organize and reuse your code. In Julia, functions are very fast and easy to define.
    </p>
    </div>
    """, unsafe_allow_html=True)

    examples = {
        "Basic Function Definitions": {
            "code": """# Define a simple function
function add(a, b)
    return a + b
end

result = add(10, 20)
println("10 + 20 = ", result)

# Function without an explicit return (last line is returned)
function multiply(x, y)
    x * y
end

println("5 × 6 = ", multiply(5, 6))

# Shorthand function syntax (for simple functions)
square(x) = x^2
println("Square of 7 = ", square(7))

# Function with a default argument
function greet(name="Guest")
    println("Hello, ", name)
end

greet("Ahmed")
greet()  # Uses the default value""",
            "output": """10 + 20 = 30
5 × 6 = 30
Square of 7 = 49
Hello, Ahmed
Hello, Guest""",
            "rules": """✅ **Rules:**
<ul>
    <li><code>function name(params) ... end</code> to define a function.</li>
    <li><code>return</code> to explicitly return a value.</li>
    <li>The last expression in a function is automatically returned.</li>
    <li>Shorthand syntax: <code>name(x) = expression</code>.</li>
    <li>Default arguments: <code>param=value</code>.</li>
    <li>Call a function: <code>function_name(arguments)</code>.</li>
</ul>"""
        },

        "Economic Functions": {
            "code": """# Function to calculate simple interest
function simple_interest(principal, rate, term)
    interest = principal * rate * term
    total_amount = principal + interest
    return interest, total_amount  # Return multiple values
end

# Using the function
i, t = simple_interest(10000, 0.05, 3)
println("Interest: ", i)
println("Total Amount: ", t)

# Function to calculate compound interest
function compound_interest(principal, rate, term)
    principal * (1 + rate)^term
end

result = compound_interest(10000, 0.05, 3)
println("\\nWith compound interest: ", round(result, digits=2))

# Function to calculate growth rate
function growth_rate(start_value, end_value)
    ((end_value - start_value) / start_value) * 100
end

growth = growth_rate(1000, 1200)
println("Growth rate: ", round(growth, digits=2), "%")""",
            "output": """Interest: 1500.0
Total Amount: 11500.0

With compound interest: 11576.25
Growth rate: 20.0%""",
            "rules": """✅ **Rules:**
<ul>
    <li>You can return multiple values: <code>return x, y, z</code>.</li>
    <li>Receive multiple values: <code>a, b, c = my_function()</code>.</li>
    <li>Use functions to avoid code repetition.</li>
    <li>Functions make code more organized and readable.</li>
</ul>"""
        },

        "Functions with Keyword Arguments": {
            "code": """# Function with keyword arguments
function financial_report(revenue, expenses;
                          tax_rate=0.15,
                          company_name="Not Specified")

    profit = revenue - expenses
    tax = profit * tax_rate
    net_profit = profit - tax

    println("=" ^ 40)
    println("Financial Report: ", company_name)
    println("-" ^ 40)
    println("Revenue: ", revenue)
    println("Expenses: ", expenses)
    println("Profit before tax: ", profit)
    println("Tax (", tax_rate * 100, "%): ", tax)
    println("Net Profit: ", net_profit)
    println("=" ^ 40)

    return net_profit
end

# Call without optional arguments (uses defaults)
financial_report(100000, 70000)

println("\\n")

# Call with optional arguments specified
financial_report(100000, 70000,
                 tax_rate=0.20,
                 company_name="Success Inc.")""",
            "output": """========================================
Financial Report: Not Specified
----------------------------------------
Revenue: 100000
Expenses: 70000
Profit before tax: 30000
Tax (15.0%): 4500.0
Net Profit: 25500.0
========================================


========================================
Financial Report: Success Inc.
----------------------------------------
Revenue: 100000
Expenses: 70000
Profit before tax: 30000
Tax (20.0%): 6000.0
Net Profit: 24000.0
========================================
""",
            "rules": """✅ **Rules:**
<ul>
    <li>A semicolon <code>;</code> separates positional and keyword arguments.</li>
    <li>Define keyword arguments: <code>name=default_value</code>.</li>
    <li>When calling, pass them by name: <code>arg_name=value</code>.</li>
    <li>The order of keyword arguments does not matter.</li>
    <li>You can provide some and let others use their default values.</li>
</ul>"""
        },

        "Advanced Functions": {
            "code": """# Function that accepts an array
function get_statistics(data)
    using Statistics # Import the statistics library

    results = Dict(
        "Mean" => mean(data),
        "Median" => median(data),
        "Maximum" => maximum(data),
        "Minimum" => minimum(data),
        "StdDev" => std(data)
    )
    return results
end

sales = [120, 135, 142, 128, 155, 148, 162]
stats = get_statistics(sales)
println("Statistics:")
for (key, value) in stats
    println(key, ": ", round(value, digits=2))
end

# Function that accepts another function as an argument (Higher-order function)
function apply_discount(prices, discount_function)
    return map(discount_function, prices)
end

prices = [100, 200, 150, 300]
# Define a 10% discount function (anonymous function)
discount_10_percent = x -> x * 0.9
prices_after_discount = apply_discount(prices, discount_10_percent)

println("\\nOriginal Prices: ", prices)
println("After 10% discount: ", prices_after_discount)

# Special discount: 20% off for prices over 150
special_discount = x -> x > 150 ? x * 0.8 : x
special_discount_prices = apply_discount(prices, special_discount)
println("With special discount: ", special_discount_prices)""",
            "output": """Statistics:
Mean: 141.43
Median: 142.0
Maximum: 162
Minimum: 120
StdDev: 14.58

Original Prices: [100, 200, 150, 300]
After 10% discount: [90.0, 180.0, 135.0, 270.0]
With special discount: [100, 160.0, 150, 240.0]""",
            "rules": """✅ **Rules:**
<ul>
    <li>Functions can return complex data structures like <code>Dict</code>.</li>
    <li><b>Higher-order functions</b> are functions that take other functions as arguments.</li>
    <li><code>-></code> is used to define anonymous functions.</li>
    <li><code>map(f, array)</code> applies a function <code>f</code> to every element of an array.</li>
    <li>Using higher-order functions makes code more flexible and reusable.</li>
</ul>"""
        },

        "Documentation and Help": {
            "code": """# Documenting a function using a docstring
\"\"\"
    calculate_roi(investment, revenue)

    Calculates the Return on Investment (ROI).

    # Arguments
    - `investment`: The amount invested.
    - `revenue`: The revenue generated from the investment.

    # Returns
    - The ROI as a percentage.

    # Example
    ```julia
    roi = calculate_roi(10000, 12000)
    println("ROI: ", roi, "%")
    ```
\"\"\"
function calculate_roi(investment, revenue)
    ((revenue - investment) / investment) * 100
end

# Using the function
roi = calculate_roi(50000, 65000)
println("Return on Investment: ", round(roi, digits=2), "%")

# Function with Type Assertion
function safe_divide(a::Number, b::Number)
    if b == 0
        println("Error: Cannot divide by zero")
        return nothing # Return a null value
    end
    return a / b
end

result = safe_divide(10, 2)
println("\\n10 ÷ 2 = ", result)
println("Attempting to divide by zero:")
error_result = safe_divide(10, 0)
""",
            "output": """Return on Investment: 30.0%

10 ÷ 2 = 5.0
Attempting to divide by zero:
Error: Cannot divide by zero""",
            "rules": """✅ **Rules:**
<ul>
    <li>Use <code>\"\"\"...\"\"\"</code> before a function definition to create a docstring.</li>
    <li><code>::Type</code> to specify the expected data type of an argument.</li>
    <li><code>nothing</code> is the value used to represent "no value".</li>
    <li>Good documentation is essential for large projects and collaboration.</li>
    <li>In the Julia REPL, type <code>?function_name</code> to view its documentation.</li>
</ul>"""
        }
    }

    for title, content in examples.items():
        with st.expander(f"**{title}**", expanded=False):
            col1, col2 = st.columns([1.1, 0.9])

            with col1:
                st.markdown("**Code:**")
                st.code(content["code"], language="julia")

                if st.button(f"▶️ Run (Simulated)", key=f"run_{title}"):
                    st.toast(f"Output for '{title}' displayed!", icon="🎉")

            with col2:
                st.markdown("**Expected Output:**")
                st.markdown(f"<div class='output-block'><pre>{content['output']}</pre></div>", unsafe_allow_html=True)

                st.markdown(f"<div class='info-box'>{content['rules']}</div>", unsafe_allow_html=True)

# Placeholder for future sections
elif menu in ["📦 Economic Packages", "🔍 Error Handling", "💼 Economic Applications"]:
    st.markdown(f"## {menu}")
    st.info("This section is under construction. Please check back later!")
    st.image("https://via.placeholder.com/800x400.png?text=Coming+Soon", caption="Content for this section will be added soon.")


# Footer for all pages
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%); border-radius: 15px;'>
    <h2 style='color: #667eea;'>🎓 Dr. Marwan Roudan</h2>
    <p style='font-size: 1.2rem; color: #4a5568;'>
        Comprehensive Julia Guide for Economists
    </p>
    <p style='color: #718096;'>
        Designed with care for students and researchers in economics.
    </p>
    <p style='margin-top: 1rem; color: #667eea; font-weight: bold;'>
        📧 For inquiries and technical support
    </p>
</div>
""", unsafe_allow_html=True)

