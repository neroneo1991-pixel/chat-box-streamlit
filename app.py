import streamlit as st
import pandas as pd
from datetime import datetime
import os

FILE = "chat.csv"

# Nếu chưa có file thì tạo
if not os.path.exists(FILE):
    pd.DataFrame(columns=["time", "user", "msg"]).to_csv(FILE, index=False)

st.title("💬 Chat Box Demo")

# Nhập tên user
user = st.text_input("Tên của bạn:", "")

# Nhập tin nhắn
msg = st.text_input("Nhập tin nhắn:")

if st.button("Gửi"):
    if user and msg:
        df = pd.read_csv(FILE)
        new_row = {"time": datetime.now().strftime("%H:%M:%S"),
                   "user": user, "msg": msg}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(FILE, index=False)
        st.experimental_rerun()

# Hiển thị tin nhắn
df = pd.read_csv(FILE)
for _, row in df.iterrows():
    st.write(f"[{row['time']}] **{row['user']}**: {row['msg']}")
