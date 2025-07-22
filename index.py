import streamlit as st
import base64
import io
from pre_process_data import main_fun
from IPython.display import HTML

with open('styles.css') as f:
              css = f.read()
              st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def add_bg_from_local(file):
    if file.endswith('.mp4'):
        video_file = io.open(file, 'rb')
        video_bytes = video_file.read()
        encoded_string = base64.b64encode(video_bytes).decode('utf-8')
        mime_type = 'video/mp4'
      
    else:
        with io.open("./static/3.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            mime_type = 'image/jpeg'

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('data:{mime_type};base64,{encoded_string}') no-repeat fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local('./static/123.jpg')


# video_html = """
# 		<style>
# 		#myVideo {
# 		  position: fixed;
# 		  right: 0;
# 		  bottom: 0;
# 		  min-width: 100%; 
# 		  min-height: 100%;
# 		}

# 		.content {
# 		  position: fixed;
# 		  bottom: 0;
# 		  background: rgba(0, 0, 0, 0.5);
# 		  color: #f1f1f1;
# 		  width: 100%;
# 		  padding: 20px;
# 		}

# 		</style>	
# 		<video autoplay muted loop id="myVideo">
# 		  <source src="https://assets.mixkit.co/videos/preview/mixkit-blue-particle-background-8221-large.mp4")>
# 		  Your browser does not support HTML5 video.
# 		</video>
#         """
#<source src="https://assets.mixkit.co/videos/preview/mixkit-blue-particle-background-8221-large.mp4")>
#st.markdown(video_html, unsafe_allow_html=True)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

title_style = """
        h1:hover {
        cursor: pointer;
        text-shadow: 2px 2px 2px #ccc !important;
        color: Blue !important;
        font-weight: bold;
        transition: color 0.2s ease-in-out;
    }
"""



submit_button_style = """
    div.stButton>button {
        background-color: #3F51B5;
        color: white;
        font-size: 18px;
        font-family: 'Montserrat', sans-serif;
        border-radius: 5px;
        padding: 10px;
        border: none;
        box-shadow: 2px 2px 2px #ccc;
        transition: all 0.2s ease-in-out;
    }

    div.stButton>button:hover {
        cursor: pointer;
        background-color: #1A237E;
        color: #FFC107;
        transform: scale(1.1);
    }
"""

st.markdown(f"<style>{submit_button_style}</style>", unsafe_allow_html=True)
             
txt_box = "Enter your complaint. It will be sent to the related department." 
with st.form(key='output'):
    st.markdown(f"<style>{title_style}</style>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-weight: 900; font-size: 55px; margin: 0 0 20px; font-family: Verdana, Lucida Grande; color: #3F51B5;'>Financial Complains <br> Classification</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin: 0; font-size: 20px; font-family: Arial, Lucida Grande; color: #333;'><em>Submit Your Financial Complaint</em></p>", unsafe_allow_html=True)
    complaint = st.text_area(txt_box,height=250, placeholder="Type your complain here...")
    submit_button = st.form_submit_button(label='Get Topic')

    if submit_button:
        if complaint == "":
            print("Please Enter Complain")
        else:
            data = str(complaint)
            output = main_fun(data)
            message = "Thank You for Reaching Us..!!"
            st.write(f'<div style="display: inline-block; color: #3F51B5;">{message}</div>', unsafe_allow_html=True)
            st.write("""<p class='blink'>Your Complain is sent to """ + str(output) + " Department</p>", unsafe_allow_html=True)