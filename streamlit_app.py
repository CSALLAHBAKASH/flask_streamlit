import streamlit as st

def main():
    st.title("Streamlit App")
    
    # Add your Streamlit code here
    st.write("Hello, Streamlit!")
    
    # Example of a Streamlit widget
    name = st.text_input("Enter your name")
    st.write(f"Hello, {name}!")

if __name__ == '__main__':
    main()