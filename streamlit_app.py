import streamlit as st
import io

from docx import Document

def main():
    st.title("File Upload and Process App")
    # File uploader widget
    uploaded_file = st.file_uploader("Choose a Word file")

    if uploaded_file is not None:
        # To read content of the uploaded file
        doc = Document(uploaded_file)
        para = doc.add_paragraph("Generated from Streamlit App")
        output = io.BytesIO()
        doc.save(output)

        # Display the processed content (optional)
        st.write("New paragraph added to the doc.")

        # Providing a link to download the new file
        st.download_button(label="Download Processed File",
                           data=output.getvalue(),
                           file_name="output.docx",
                           mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

if __name__ == "__main__":
    main()
