import streamlit as st
import pandas as pd
import base64
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load data and train model efficiently using caching
@st.cache_data
def load_and_train():
    df = pd.read_csv("Amazon.csv").dropna(subset=['Title'])
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['Title'])
    return df, vectorizer, tfidf_matrix

df, vectorizer, tfidf_matrix = load_and_train()

# 2. Build the Web Interface
st.title("🌱 Eco-Friendly Product Finder")
import streamlit as st

# --- NEW BACKGROUND FUNCTION ---
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: linear-gradient(rgba(55, 55, 55, 0.65), rgba(55, 55, 55, 0.65)), 
             url("data:image/jpg;base64,{encoded_string}");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Call the function with the exact name of the file you saved
add_bg_from_local("bg_image.jpg")
# -----------------------------------
st.write("Discover sustainable alternatives for your everyday products :) ")

# Search bar for the user
user_query = st.text_input("What item are you looking for?", placeholder="e.g., reusable coffee cup")

# 3. Recommendation Logic & Display
if st.button("Find Alternatives"):
    if user_query:
        # Vectorize the user's search
        query_vec = vectorizer.transform([user_query])
        
        # Calculate similarity
        similarity_scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
        
        # --- THE FIX: Check if the best match is actually a match ---
        if similarity_scores.max() == 0:
            st.warning("No matches found for those terms. Try searching for everyday items like 'cup', 'bag', or 'soap'!")
        else:
            top_indices = similarity_scores.argsort()[-3:][::-1]
            recommendations = df.iloc[top_indices]
            
            st.subheader("Top Sustainable Matches:")
            
            # Display results cleanly 
            for index, row in recommendations.iterrows():
                with st.container():
                    st.write(f"**{row['Title']}**") # Ensure this matches your column name!
                    st.write(f"Price: {row['Price']} | Rating: {row['ratings']} ⭐")
                    st.write(f"[View Product]({row['alinknormal_URL']})")
                    st.divider()
    else:
        st.warning("Please enter a product to search for.")
