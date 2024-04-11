import os
import streamlit as st
def main():
    st.set_page_config(page_title="Green")
    st.header("Sustainability Bot (draft)")

    # Specify the filename without the directory path
    filename = "example.pdf"
    
    # Assuming the file is located in the same directory as the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        # Process the file
        raw_text = get_pdf_text(file_path)
    else:
        print(f"File '{filename}' not found in the script directory.")

def get_pdf_text(file_path):
    # Implement your function to extract text from the PDF file
    pass

if __name__ == "__main__":
    main()
