# 🎬 Movie Recommendation System

Welcome to the Movie Recommendation System! This project uses NLP techniques and machine learning to recommend similar movies based on storyline descriptions. Built using Python, Streamlit, and cosine similarity, it features an interactive UI with poster displays to enhance the user experience. 🚀

---

## 📁 Dataset

- **Source:** [tmdb_5000_movies.csv](https://www.kaggle.com/)
- **Features Used:** `title`, `overview`, and other metadata
- **Preprocessing Tool:** `Pandas`

---

## 🧠 Tech Stack & Workflow

### 📊 Flowchart Overview
Kaggle Movie Dataset 📂  
        ⬇️  
Data Cleaning & Preprocessing 🧹 (using Pandas)  
        ⬇️  
TF-IDF Vectorization ✍️ (Scikit-learn)  
        ⬇️  
Cosine Similarity Calculation 🧠  
        ⬇️  
Model Serialization with Pickle 🥒  
        ⬇️  
Streamlit UI Development 💻  
        ⬇️  
Poster Fetching using TMDB API 🖼️  
        ⬇️  
Display Top 5 Recommendations 🎯

🛠️ Tools & Libraries Used
🐍 Python

📊 Pandas

🤖 Scikit-learn (TfidfVectorizer, cosine_similarity)

🥒 Pickle

🌐 Streamlit

🌄 TMDB API (for movie posters)

🚀 How It Works
User selects a movie from a dropdown.

Model fetches its vectorized form using TF-IDF.

Cosine similarity is calculated between the selected movie and all others.

Top 5 most similar movies are retrieved.

Movie posters are fetched using the TMDB API.

🎉 Recommendations are shown in a beautiful and user-friendly interface.

📸 UI Preview

![image](https://github.com/user-attachments/assets/76db5fd4-1bc5-4597-9492-7af052c0ee19)

📦 Run Locally
Prerequisites
Python 3.7+

Install dependencies:
pip install streamlit pandas scikit-learn requests

Start Streamlit App
streamlit run app.py

✨ Features
Dropdown-based movie selection

Recommendations based on storyline similarity

Integrated movie posters for immersive UX

Fast and responsive interface using Streamlit

📚 Learnings
Applied TF-IDF + Cosine Similarity for NLP-based recommendations

Model serialization using Pickle

API integration with error handling

Frontend development with Streamlit

📌 Future Scope
Add filters (genre, release year)

Include user ratings or collaborative filtering

Deploy on cloud platforms (e.g., Heroku, Streamlit Sharing)

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

🧑‍💻 Author
Your Name: Humaira Fathima N

Portfolio

LinkedIn: www.linkedin.com/in/humairafathima-n-778415295

Email: humaira2004super@gmail.com

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.












