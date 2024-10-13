import streamlit as st
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def sin_deg(angle):
    return math.sin(math.radians(angle))

def cos_deg(angle):
    return math.cos(math.radians(angle))

def tan_deg(angle):
    return math.tan(math.radians(angle))

# Streamlit app
st.title("Calculator with Arithmetic and Trigonometric Functions")

# Arithmetic Operations
st.header("Arithmetic Operations")
num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f")
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    st.success(f"Result: {result}")

# Trigonometric Functions
st.header("Trigonometric Functions")
angle = st.number_input("Enter angle in degrees:", format="%.2f")
trig_function = st.selectbox("Select function:", ["Sine", "Cosine", "Tangent"])

if st.button("Calculate Trig"):
    if trig_function == "Sine":
        result = sin_deg(angle)
    elif trig_function == "Cosine":
        result = cos_deg(angle)
    elif trig_function == "Tangent":
        res
