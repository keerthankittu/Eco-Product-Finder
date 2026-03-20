# Eco-Product-Finder
This project was developed as part of a **Virtual Internship focusing on Artificial Intelligence, Data Analytics, and Green Skills**. 

The Eco-Friendly Product Recommender is a machine-learning-powered web application designed to help users transition to a more sustainable lifestyle. By simply typing an everyday item (e.g., "coffee cup" or "laundry detergent") into the search bar, the underlying AI model processes the text and recommends the top-rated sustainable alternatives available on Amazon.

## ✨ Features
* **Smart Search:** Uses Natural Language Processing (NLP) to understand user queries, even if they don't exactly match the product name.
* **Instant Recommendations:** Displays the top 3 eco-friendly alternatives with their current price, average customer rating, and a direct link to the product.
* **Modern Web Interface:** Built entirely in Python using Streamlit, featuring a custom, low-opacity background for a clean, professional user experience.
* **Efficient Data Handling:** Utilizes caching to ensure the dataset and machine learning model are loaded quickly without redundant processing.

## 🛠️ Tech Stack & Methodologies
* **Language:** Python
* **Frontend/Framework:** Streamlit
* **Data Analytics:** Pandas (for data cleaning and manipulation)
* **Machine Learning:** Scikit-learn (`TfidfVectorizer` for text vectorization and `cosine_similarity` for calculating the closest product matches)

## 📊 The Dataset
This project utilizes the **Sustainable Products Dataset** (sourced from Kaggle), which contains thousands of eco-friendly items scraped directly from Amazon. The dataset includes product titles, prices, customer ratings, and image/product URLs.
