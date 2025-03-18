import streamlit as st
from face_emotion import get_emotion
from get_songs import fetch_songs


st.text_input("Singer", key="singer")
# st.text_input("Language", key="language")

# You can access the value at any point with:

emotion = None
if st.button("Get Emotion"):
    emotion = get_emotion()
    # emotion
singer = st.session_state.singer
songs = []

if emotion:
    songs = fetch_songs(emotion=emotion, singer=singer)

# Create Cards of Links of youtube to listen to songs
if songs:
    for i, (song, album) in enumerate(songs):
        sg = song.replace(" ", "+")
        link = "https://www.youtube.com/results?search_query={}".format(sg)
        if singer:
            by = f"+by+{singer.replace(' ', '+')}"
            link+=by
        st.markdown("<h4 style='text-align: center;'> <a href={}>{}-{} </a> </h4>".format(link,i+1,song), unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; color:grey'> {} - {} </h6>".format(singer, album), unsafe_allow_html=True)
        



