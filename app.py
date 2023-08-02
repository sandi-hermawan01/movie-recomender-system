import pickle
import streamlit as st
import requests


st.set_page_config(page_title="Movie Recommendation", page_icon=":movie_camera:", layout="wide")

# ---- Header ----
with st.container():
    a, b, c ,d ,e, f, g, h, i, j = st.columns(10)

    with a:
        st.image("images/EtSadis.png")
        st.write("---")
    with b:
        st.title(" ")
        
with st.container():
    left_column,mid, right_column = st.columns(3)

    with left_column:
        st.image("images/Poster3.png")
    with mid:
        st.image("images/Poster3.1.png")
    with right_column:
        st.image("images/Poster2.1.jpg")

st.write("---")

#memanggil model yang sudah dibuat
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))
movie_list = movies['title'].values
movie_tags = movies['tags'].values

#Scraping poster movie
#API KEY harus di isi dengan API Key yang berbeda/api key milik sendiri
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ecf946973debc61acc63c35c571d5318&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

#Fungsi rekomendasi saat search
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[0:16]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)


    return recommended_movie_names,recommended_movie_posters

#Fungsi rekomendasi For You
def foryou(movie1):
    index1 = movies[movies['title'] == movie1].index[0]
    distances1 = sorted(list(enumerate(similarity[index1])), reverse=True, key=lambda x: x[1])
    foryou_movie_names = []
    foryou_movie_posters = []

    for a in distances1[17:31]:
        # fetch the movie poster
        movie_id = movies.iloc[a[0]].movie_id
        foryou_movie_posters.append(fetch_poster(movie_id))
        foryou_movie_names.append(movies.iloc[a[0]].title)

    return foryou_movie_names,foryou_movie_posters



selected_movie = st.selectbox(
    "Type or select the movie title you want",movie_list
)

st.subheader(f"For You")

if selected_movie:
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6, col7, col8= st.columns(8)
    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])
    with col6:
        st.image(recommended_movie_posters[5])
        st.text(recommended_movie_names[5])
    with col7:
        st.image(recommended_movie_posters[6])
        st.text(recommended_movie_names[6])
    with col8:
        st.image(recommended_movie_posters[7])
        st.text(recommended_movie_names[7])

    col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(8)
    with col9:
        st.image(recommended_movie_posters[8])
        st.text(recommended_movie_names[8])
    with col10:
        st.image(recommended_movie_posters[9])
        st.text(recommended_movie_names[9])
    with col11:
        st.image(recommended_movie_posters[10])
        st.text(recommended_movie_names[10])
    with col12:
        st.image(recommended_movie_posters[11])
        st.text(recommended_movie_names[11])
    with col13:
        st.image(recommended_movie_posters[12])
        st.text(recommended_movie_names[12])
    with col14:
        st.image(recommended_movie_posters[13])
        st.text(recommended_movie_names[13])
    with col15:
        st.image(recommended_movie_posters[14])
        st.text(recommended_movie_names[14])
    with col16:
        st.image(recommended_movie_posters[15])
        st.text(recommended_movie_names[15])

    
st.subheader(f"That you might miss")

if selected_movie:
    foryou_movie_names,foryou_movie_posters = foryou(selected_movie)
    colA, colB, colC, colD, colE, colF, colG= st.columns(7)
    with colA:
        st.image(foryou_movie_posters[0])
        st.text(foryou_movie_names[0])
    with colB:
        st.image(foryou_movie_posters[1])
        st.text(foryou_movie_names[1])
    with colC:
        st.image(foryou_movie_posters[2])
        st.text(foryou_movie_names[2])
    with colD:
        st.image(foryou_movie_posters[3])
        st.text(foryou_movie_names[3])
    with colE:
        st.image(foryou_movie_posters[4])
        st.text(foryou_movie_names[4])
    with colF:
        st.image(foryou_movie_posters[5])
        st.text(foryou_movie_names[5])
    with colG:
        st.image(foryou_movie_posters[6])
        st.text(foryou_movie_names[6])

    
    colH, colI, colJ, colK, colL, colM, colN = st.columns(7)
    with colH:
        st.image(foryou_movie_posters[7])
        st.text(foryou_movie_names[7])
    with colI:
        st.image(foryou_movie_posters[8])
        st.text(foryou_movie_names[8])
    with colJ:
        st.image(foryou_movie_posters[9])
        st.text(foryou_movie_names[9])
    with colK:
        st.image(foryou_movie_posters[10])
        st.text(foryou_movie_names[10])
    with colL:
        st.image(foryou_movie_posters[11])
        st.text(foryou_movie_names[11])
    with colM:
        st.image(foryou_movie_posters[12])
        st.text(foryou_movie_names[12])
    with colN:
        st.image(foryou_movie_posters[13])
        st.text(foryou_movie_names[13])

st.write("---")

with st.container():
    st.write("---")
    st.header("About")
    st.subheader("Kami dari kelompok EtSadis")
    st.write(
            """
            EtSadis merupakan nama kelompok sekaligus nama aplikasi, tidak ada arti khusus dari EtSadis, 
            dikarenakan EtSadis merupakan kumpulan huruf awal dari setiap anggota kelompok `E`ga `T`atang `Sa`ndi `Di`on `S`ylvania
            """
        )
    st.write("#")

    image_column, text_column,x,y,z = st.columns((1, 2, 3, 4, 5))
    with image_column:
        st.image("images/Ega.png")

    with text_column:
        st.subheader("Ega Permana")
        st.write(
            """
            Ega Permana bertugas sebagai Project Manager dan Modelling
            """
        )

    image_column, text_column,x,y,z = st.columns((1, 2, 3, 4, 5))
    with image_column:
        st.image("images/tatang.png")

    with text_column:
        st.subheader("Tatang Bukhori")
        st.write(
            """
            Tatang Bukhori bertugas sebagai Modeling dan Deployment
            """
        )
    
    image_column, text_column,x,y,z = st.columns((1, 2, 3, 4, 5))
    with image_column:
        st.image("images/sandi.png")

    with text_column:
        st.subheader("Sandi Hermawan")
        st.write(
            """
            Sandi Hermawan bertugas sebagai Modeling dan Deployment
            """
        )

    image_column, text_column,x,y,z = st.columns((1, 2, 3, 4, 5))
    with image_column:
        st.image("images/Dion.png")

    with text_column:
        st.subheader("M Dian Purnama")
        st.write(
            """
            M Dian Purnama bertugas sebagai UI/UX Design
            """
        )
    
    image_column, text_column,x,y,z = st.columns((1, 2, 3, 4, 5))
    with image_column:
        st.image("images/sylvania.png")

    with text_column:
        st.subheader("Sylvania Diva Jezreelia")
        st.write(
            """
            Sylvania Diva Jezreelia bertugas sebagai UI/UX Design
            """
        )