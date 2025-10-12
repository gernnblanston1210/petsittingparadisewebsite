# to run, first run this cmd    cd '.\James - python\'
# and thi8s cmd this cmd        cd .\website_2\
# and finaly this cmd           streamlit run website2.py


import streamlit as st
from PIL import Image, ImageOps


# ---- IMAGE IMPORTS ----
img_pet_pics1 = Image.open('images/IMG_0314.jpeg')
img_pet_pics2 = Image.open('images/IMG_0311.jpeg')
img_pet_pics3 = Image.open('images/IMG_0280.jpeg')
img_pet_pics4 = Image.open('images/IMG_3831.PNG')
img_pet_pics5 = Image.open('images/IMG_1013.jpeg')


st.set_page_config(page_title="MyWebpage", page_icon=":green_heart:", layout="wide")

# ---- LOCAL CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")




# ---- HEADER SECTION ----

with st.container():
    st.subheader("Hi, I am James :wave:")
    st.title('About my business')
    st.write('Welcome to Pet Sitting Paradise; the best and cheapest pet sitting business in NYC.')
    st.write('[To learn more about me, go to my other site. You may need to wake it up >] (https://jamesplevine01.streamlit.app/)')

# ---- FIRST SECTION ----
with st.container():
    st.write('---')
    st.title('Why you should choose Pet Sitting Paradise instead of other pet sitting businesses:')
    st.write('#1 It is the cheapest pet sitting business in NYC.')
    st.write('#2 Even though it is the cheapest, we still take great care of your lovely animals.')
    st.write('#3 Any animals who are guests at Pet Sitting Paradise will be in paradise while you are away.')
    st.write('#4 I have animals of my own, so I know how to take care of pets and to get them to love me.')

# ---- SECOND SECTION ----
with st.container():
    st.write('---')
    st.title('Pictures of my pets')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.title('Here are my current pets')
        st.image(ImageOps.exif_transpose(img_pet_pics1))
        st.image(ImageOps.exif_transpose(img_pet_pics2))
        st.image(ImageOps.exif_transpose(img_pet_pics5))
        st.title('In loving memory of fluffy and Milky Way:cry:')
        st.image(ImageOps.exif_transpose(img_pet_pics3))
        st.image(ImageOps.exif_transpose(img_pet_pics4))
   

   #---- contact from ----
with st.container():
    st.write("---")
    st.subheader("Contact me right here if you have any questions or you would like to book pet sitting.")
    st.subheader("Please use your real email so I can respond to you.")
    st.subheader("I will get back to you soon.")
    

    st.html("""
    
<form action="https://api.web3forms.com/submit" method="POST">

    <!-- Replace with your Access Key -->
    <input type="hidden" name="access_key" value="2c4432c8-0d95-4ab4-8d29-39914939bae4">

    <!-- Form Inputs. Each input must have a name="" attribute -->
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="your message here" required></textarea>
    

    <!-- Honeypot Spam Protection -->
    <input type="checkbox" name="botcheck" class="hidden" style="display: none;">

    <!-- Custom Confirmation / Success Page -->
    <!-- <input type="hidden" name="redirect" value="https://mywebsite.com/thanks.html"> -->

    <button type="submit">Submit Form</button>

</form>
   """)
        





