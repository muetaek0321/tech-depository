import streamlit as st


@st.dialog("ログアウト")
def logout_dialog() -> None:
    """ログアウトの確認ダイアログ
    """
    st.write("ログアウトしますか？")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("OK", use_container_width=True):
            st.session_state.auth_controller.logout()
            st.switch_page("./main.py")
    with col2:
        if st.button("キャンセル", use_container_width=True):
            st.rerun()


st.text("ログイン成功！")

st.divider() # 区切り線          
if st.button("ログアウト", use_container_width=True, type='primary'):
    logout_dialog()
