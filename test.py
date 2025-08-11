import streamlit as st
import subprocess
import sys
import pkg_resources
from db import create_database, insert_code, get_code, get_all_data_as_dataframe

# DATABASE SETUP
db_file = "codes.db"
create_database(db_file)  # Ensure db and table exist

# Example utility
import hashlib
def hash_to_id(code):
    return hashlib.sha256(code.encode('utf-8')).hexdigest()[:10]

def safe_exec(code):
    """Execute code safely with error handling"""
    local_env = {}
    try:
        if not code.strip():
            st.warning("No code to execute")
            return False
        exec(code, {}, local_env)
        st.session_state.last_execution_success = True
        return True
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.session_state.last_execution_success = False
        return False

def install_package(package):
    """Install package using pip"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            capture_output=True, text=True, timeout=300
        )
        if result.returncode == 0:
            st.session_state.installed_packages = [d.project_name for d in pkg_resources.working_set]
            return True, "Success"
        return False, result.stderr
    except Exception as e:
        return False, str(e)

def get_packages():
    """Get installed packages"""
    try:
        return sorted([d.project_name for d in pkg_resources.working_set])
    except:
        return []

# --- Streamlit UI ---

st.set_page_config(layout="wide", page_title="Python IDE", page_icon="🛠️")
st.title("🛠️ Python IDE with Package Manager")

for key in ['error_log', 'last_execution_success', 'installed_packages']:
    if key not in st.session_state:
        st.session_state[key] = [] if 'log' in key or 'packages' in key else True

# LOAD EXISTING SCRIPTS
try:
    df = get_all_data_as_dataframe(db_file)
    option = None
    if df is not None and not df.empty:
        option = st.selectbox('Select script:', df['name'].tolist(), index=None)
except:
    df = None
    st.info("No saved scripts found")

# HANDLE SCRIPT LOADING
code = ""
name = ""
try:
    if option and df is not None:
        selected = df[df['name'] == option].iloc[0]
        snippet_id = selected['hashcode']
        name = selected['name']
        code = get_code(db_file, snippet_id) or ""
    else:
        code = "print('Hello World!')"
        name = ""
except Exception:
    code = "print('Hello World!')"
    name = ""

# MAIN LAYOUT
view_mode = st.session_state.get('viewMode') # you may adapt this as needed

if view_mode == 'view':
    st.subheader("Output")
    safe_exec(code)
else:
    left, right = st.columns([1, 1])
    with left:
        st.subheader("Code Editor")
        col1, col2 = st.columns([3, 1])
        with col1:
            name = st.text_input("Script Name", value=name or "", placeholder="Enter name...")
        with col2:
            save = st.button("💾 SAVE", type="primary")
        code = st.text_area("Code", value=code, height=400)
        # SAVE
        if name and save:
            try:
                snippet_id = hash_to_id(code)
                insert_code(db_file, snippet_id, name, code)
                st.success("Script saved!")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Save failed: {e}")
    with right:
        st.subheader("Output")
        if st.session_state.last_execution_success:
            st.success("Ready")
        safe_exec(code)

# SIDEBAR - PACKAGE MANAGER
with st.sidebar:
    st.header("📦 Package Manager")
    # Install packages
    with st.expander("Install Package"):
        pkg = st.text_input("Package name:", placeholder="e.g., numpy")
        if st.button("Install") and pkg:
            with st.spinner(f"Installing {pkg}..."):
                success, msg = install_package(pkg)
                if success:
                    st.success(f"{pkg} installed!")
                    st.experimental_rerun()
                else:
                    st.error(f"Failed: {msg}")
    # Popular packages
    popular = ['numpy', 'pandas', 'matplotlib', 'requests', 'scikit-learn']
    selected = st.selectbox("Popular packages", [""] + popular)
    if selected and st.button("Install selected"):
        with st.spinner(f"Installing {selected}..."):
            success, msg = install_package(selected)
            if success:
                st.success(f"{selected} installed!")
                st.experimental_rerun()
            else:
                st.error(f"Failed: {msg}")
    # Installed packages list
    st.subheader("Installed Packages")
    if st.button("Refresh"):
        st.session_state.installed_packages = get_packages()
        st.experimental_rerun()
    if not st.session_state.installed_packages:
        st.session_state.installed_packages = get_packages()
    search = st.text_input("Search", placeholder="Filter packages...")
    packages = [p for p in st.session_state.installed_packages if search.lower() in p.lower()] if search else st.session_state.installed_packages
    for pkg in packages[:15]:  # Show first 15
        st.text(f"- {pkg}")
    if len(packages) > 15:
        st.info(f"... and {len(packages) - 15} more")