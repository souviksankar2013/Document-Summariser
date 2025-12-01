import streamlit as st
import app_lib as glib

st.set_page_config(page_title="Document Summarization")
st.title("Document Summarization")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf", "docx"])

# --- Summary Instructions ---
input_text = st.text_area("How would you like the document summarized?")

# --- Summarize Button ---
summarize_button = st.button("Summarize", type="primary")

if summarize_button:
    st.subheader("Summary")

    if not uploaded_file:
        st.warning("Please upload a document before summarizing.")
    else:
        with st.spinner("Processing document..."):
            # Read file content
            file_bytes = uploaded_file.read()

            # Pass content + instructions to your summarizer
            response_content = glib.get_summary(file_bytes, input_text)

            st.write(response_content)


