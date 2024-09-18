import streamlit as st
import io

def main():
    st.title("File Upload and Process App")
    # File uploader widget
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        # To read content of the uploaded file
        content = uploaded_file.getvalue()
        content = content.decode("utf-8")  # decoding to string if it's binary
        
        # Taking the first 100 characters from the uploaded file
        processed_content = content[:100]
        
        # Creating a new file-like object containing the processed content
        new_file = io.StringIO(processed_content)
        
        # Display the processed content (optional)
        st.write("Here's the first 100 characters of your file:")
        st.text(processed_content)
        
        # Providing a link to download the new file
        st.download_button(label="Download Processed File",
                           data=new_file.getvalue(),
                           file_name="processed_file.txt",
                           mime="text/plain")

if __name__ == "__main__":
    main()
