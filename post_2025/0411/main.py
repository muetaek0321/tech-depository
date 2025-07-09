from pathlib import Path

import streamlit as st
import yaml
from streamlit_authenticator.controllers import AuthenticationController


# 定数
AUTH_FILE_PATH = Path("auth.yaml")

with open(AUTH_FILE_PATH, mode="r") as f:
    auth = yaml.safe_load(f)

st.session_state.auth_controller = AuthenticationController(auth['credentials'])


# 認証情報がある場合はリセット
if "authentication_status" in st.session_state:
    del st.session_state.authentication_status
if "messages" in st.session_state:
    del st.session_state.messages
    del st.session_state.chats


def login_button(username: str, password: str) -> None:
    """ログインのボタン
    """
    if st.button("ログイン", use_container_width=True, type='primary'):
        auth_ok = st.session_state.auth_controller.login(username, password)
        # ログイン成功
        if auth_ok:
            st.switch_page("./pages/page.py")
        # ログイン失敗
        else:
            st.error("ユーザ名またはパスワードが間違っています。", icon="🚨")
    

st.title("パスワード認証デモ")

st.write("ログインを試してみる！")
with st.container(border=True):
    st.markdown(f"ユーザー名：")
    username = st.text_input(" ", label_visibility="collapsed", key="username_login")
    st.markdown(f"パスワード：")
    password = st.text_input(" ", type='password', label_visibility="collapsed", key="password_login")

    # ログインボタン
    login_button(username, password)

st.divider()

col1, col2 = st.columns([2, 1])
with col1:
    st.write("ユーザ登録する！")
with col2:
    if st.button("新規登録", use_container_width=True):
        st.switch_page("./pages/signup.py")
    
