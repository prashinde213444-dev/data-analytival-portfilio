import streamlit as st
import requests

ESP32_IP = "http://192.168.4.1"

st.title("ESP32 IOT DASHBORD")
st.write("controll your hardware from a modern python interface.")

col1, col2 = st.columns(2)

with col1:
    if st.button("Turn led on",use_container_width=True):

        try:
            requests.get(f"{ESP32_IP}/1",timeout=2)

            st.success("LED IS NOW ON")

        except:
            st.error("could not reach ESP32")


with col2:
    if st.button("Turn led off",use_container_width=True):
        try:
            requests.get(f"{ESP32_IP}/0",timeout=2)

            st.warning("Led is now off")

        except:
            st.error("could not reach esp32")