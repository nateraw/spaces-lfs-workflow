import os
import shutil
import sys
from subprocess import call

import streamlit as st
from huggingface_hub import Repository

CACHE_DIR = 'cache_dir/'


def run_cmd(command):
    """Runs CLI commands from Python, with outputs printed to shell"""
    try:
        print(command)
        call(command, shell=True)
    except KeyboardInterrupt:
        print("Process interrupted")
        sys.exit(1)


def download_cache(cache_dir: str, repo_name: str):
    """Clones a repo from HuggingFace Hub to a cache directory"""
    if os.environ.get("DO_DOWNLOAD_CACHE") and 'cache_is_downloaded' not in st.session_state:
        with st.spinner("Downloading cache..."):
            repo = Repository(local_dir=cache_dir, clone_from=repo_name, repo_type='dataset')
            # repo.git_pull()  # Needed?


def main():
    st.title("Spaces LFS Workflow")
    download_cache('cache_dir', 'nateraw/fairface')
    st.write(os.listdir('.'))
    st.write(os.listdir('./cache_dir'))
    st.json(os.environ)
    run_cmd('ls -lash cache_dir/')


if __name__ == '__main__':
    main()
