import os

import streamlit as st
from huggingface_hub import Repository


st.title("Spaces LFS Workflow")

if os.environ.get("DO_DOWNLOAD_CACHE") and 'cache_is_downloaded' not in st.session_state:
    with st.spinner("Downloading cache..."):
        repo = Repository(local_dir="cache_dir", clone_from='nateraw/fairface', repo_type='dataset')

st.write(os.listdir('.'))
st.write(os.listdir('./cache_dir'))
