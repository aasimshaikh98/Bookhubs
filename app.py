import streamlit as st
from PIL import Image
import pandas as pd
import random
a = random.randint(1,221000)
image=Image.open('logo.png')
st.image(image)
st.title("-- Book Recommender System 📚 --")
st.markdown("Tailors book suggestions based on users' preferences."
" Employs collaborative filtering algorithms to find like-minded readers."
" Provides a curated list of books, enhancing the reading experience.")
st.subheader("Enter your Name")
user_name = st.text_input("")
Item_based = pd.read_csv('https://github.com/aasimshaikh98/BookHub/blob/master/item_based.csv?raw=true')
b='\U0001F4D6'
p="\u270D\ufe0f"
book=""
genres = ["Art", "Business", "Children's","Classics", "Comedy", "Comics", "Crime", "Ebooks", "Fantasy", "Fiction",
          "History", "Horror","Mystery", "Philosophy", "Poetry", "Psychology","Romance", "Science", "Suspense", "Sports", "Thriller", "Travel"]
if user_name:
    st.subheader("Select your Age")
    age = st.slider("", 10, 60)
    if age:
        st.subheader(f"Here are few recommendations for a {age} year old")
        for i in range(a, a+3):
            st.write(f"{b} {Item_based.iloc[i]['Book-Title']}  --- {p}{Item_based.iloc[i]['Book-Author']} ")       
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Select your favorite genres")
        select_genres = st.multiselect("",genres)
        if select_genres:
            st.subheader("Which Book are you looking for?")
            col=st.columns(1)
            book=col[0].text_input("Enter something related to the book you're looking !!!","")
        if book:
            st.subheader("Filter by ⭐ Ratings")
            rating = st.slider("", 0, 5)
            if rating:
                for i in range(a,a+100):
                    if(Item_based.iloc[i]['Mean-Rating'] == rating):
                        st.write(f"{b} {Item_based.iloc[i]['Book-Title']}  --- {Item_based.iloc[i]['Mean-Rating']}---{p}{Item_based.iloc[i]['Book-Author']} ")     
                    #if ("{Item_based.iloc[i]['Mean-Rating']}"==rating):          
        st.markdown("<hr>", unsafe_allow_html=True)
