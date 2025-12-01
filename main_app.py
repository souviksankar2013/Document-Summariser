import streamlit as st
import app_lib as glib

st.set_page_config(page_title="Document Summarization", layout="wide")

# ---- Center Title ----
st.markdown(
    """
    <h1 style='text-align: center;'>Document Summarizer using Amazon Bedrock</h1>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: white; margin-bottom: 20px;'>
        Created by Souvik Sankar Mitra for AI For Bharat Event
    </div>
    """,
    unsafe_allow_html=True
)

# ---- Two columns ----
left_col, right_col = st.columns([1, 1.2])

# ---------------- LEFT SIDE ----------------
with left_col:
    st.header("Input")

    uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf", "docx"])

    input_text = st.text_area("How would you like the document summarized?")

    summarize_button = st.button("Summarize", type="primary")

# ---------------- RIGHT SIDE ----------------
with right_col:
    st.header("Summary Output")

    # Scrollable container for the summary
    st.markdown(
        """
        <style>
            .summary-box {
                height: 500px;
                overflow-y: scroll;
                padding: 15px;
                border: 1px solid #444;
                border-radius: 8px;
                background-color: #161a1d;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    if summarize_button:
        if not uploaded_file:
            st.warning("Please upload a document before summarizing.")
        else:
            with st.spinner("Processing document..."):
                file_bytes = uploaded_file.read()
                response_content = glib.get_summary(file_bytes, input_text)

                st.markdown(
                    f"<div class='summary-box'>{response_content}</div>",
                    unsafe_allow_html=True
                )
