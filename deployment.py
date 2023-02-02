import streamlit as st
import pickle
import pandas as pd

def recommend (song):
    song_index = song[song['song_name'] == song].index[0]
    distances = similarity[song_index]
    song_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_songs=[]
    for i in song_list:
        recommended_songs.append(song.iloc[i[0]].song_name)
    return recommended_songs

song_dict = pickle.load(open('songs_dict.pkl','rb'))
song = pd.DataFrame(song_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Song-Recommendation')

selected_songs = st.selectbox(
'How would you like to be contacted?',
song['song_name'].values)

if st.button('recommend'):
    recommendations = recommend(selected_songs)
    for i in recommendations:
        st.write(i)
