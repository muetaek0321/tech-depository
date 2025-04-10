from pathlib import Path

import streamlit as st
import yaml
from streamlit_authenticator.utilities.hasher import Hasher


# 定数
AUTH_FILE_PATH = Path("auth.yaml")
REQUIRED_MARK = "<span style='color: red'>*</span>"


@st.dialog("ユーザ登録")
def complate_signup_alert() -> None:
    """ユーザ登録完了を知らせるアラート
    """
    st.write("ユーザ登録が完了しました。")
    _, col2 = st.columns(2)
    with col2:
        if st.button("OK", use_container_width=True):
            st.switch_page("./main.py")


st.title("新規ユーザ登録")

st.write("ユーザ名とパスワードを入力してください。")

with st.container(border=True):
    st.markdown(f"ユーザー名{REQUIRED_MARK}：", unsafe_allow_html=True)
    username = st.text_input(" ", label_visibility="collapsed", key="username_signup")
    st.markdown(f"パスワード{REQUIRED_MARK}：", unsafe_allow_html=True)
    password = st.text_input(" ", type='password', label_visibility="collapsed", key="password_signup")
    st.markdown(f"メールアドレス：", unsafe_allow_html=True)
    email = st.text_input(" ", label_visibility="collapsed", key="email")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("登録", use_container_width=True):
            # 認証データが書き込まれたファイルを読み込み
            with open(AUTH_FILE_PATH, mode="r") as f:
                yaml_data = yaml.safe_load(f)
                
                # ユーザデータが空の場合の対処
                if yaml_data["credentials"]["usernames"] is None:
                    yaml_data["credentials"]["usernames"] = dict()
            
            if (username == "") or (password == ""):
                # ユーザ名orパスワードの入力欄が空欄の場合
                st.error("ユーザ名およびパスワードの入力は必須です。", icon="🚨")
            elif username in yaml_data["credentials"]["usernames"].keys():
                # 既に登録済みのユーザ名の場合
                st.error("登録済みのユーザ名と重複しています。<br>別のユーザ名で登録してください。", icon="🚨")
            else:
                # パスワードをハッシュ化
                password_hashed = Hasher.hash(password)
                
                # 認証データファイルに書き込み
                yaml_data["credentials"]["usernames"][username] = {
                    "name": username,
                    "password": password_hashed,
                    "email": email
                }
                with open(AUTH_FILE_PATH, "w") as f:
                    yaml.dump(yaml_data, f)
                    
                # トップ画面に戻る
                complate_signup_alert()

    with col2:
        if st.button("キャンセル", use_container_width=True):
            # 登録せずにトップページに戻る
            st.switch_page("./main.py")


