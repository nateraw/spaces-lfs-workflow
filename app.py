import os
import sys
from subprocess import call

import streamlit as st
from huggingface_hub import Repository


def run_cmd(command):
    try:
        print(command)
        call(command, shell=True)
    except KeyboardInterrupt:
        print("Process interrupted")
        sys.exit(1)


st.title("Spaces LFS Workflow")

if os.environ.get("DO_DOWNLOAD_CACHE") and 'cache_is_downloaded' not in st.session_state:
    with st.spinner("Downloading cache..."):
        repo = Repository(local_dir="cache_dir", clone_from='nateraw/fairface', repo_type='dataset')

st.write(os.listdir('.'))
st.write(os.listdir('./cache_dir'))
run_cmd('ls -lash cache_dir/')
