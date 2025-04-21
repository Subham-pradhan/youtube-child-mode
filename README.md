# youtube-child-mode
👶 YouTube Child Mode Viewer

This project is a YouTube Video Filter App built using Python, Streamlit, and the YouTube Data API.
It allows users to search YouTube videos either by channel ID or keywords, and filters out adult or unsafe content using a custom-trained machine learning model.

-------------------------
🚀 Features
-------------------------
- 🔍 Search YouTube videos by channel ID or keywords
- 🧠 Filters content using:
  - A bad keyword filter (e.g. "violence", "sex", etc.)
  - A machine learning model trained on clean vs unsafe text
- 📹 Displays only child-safe videos with clean titles & descriptions
- 💡 Lightweight and easy to deploy on Streamlit Cloud

-------------------------
🧠 Machine Learning Model
-------------------------
- Model used: MultinomialNB (Naive Bayes)
- Trained on labeled examples (safe vs unsafe) using TfidfVectorizer
- Saved with joblib as safe_content_model.pkl

-------------------------
🛠️ How to Run Locally
-------------------------
1. Clone the repo:
   git clone https://github.com/your-username/youtube-child-mode.git
   cd youtube_child_mode

2. Create virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Train the model (optional - already trained model included):
   python train_model.py

5. Run the app:
   streamlit run ui_app.py

-------------------------
☁️ Deploy to Streamlit Cloud
-------------------------
1. Push your project to GitHub
2. Go to https://streamlit.io/cloud
3. Click "Deploy" and connect your GitHub repo
4. Add your API_KEY as a secret or use st.secrets["API_KEY"]
5. Done! 🎉

-------------------------
🔐 Security Warning
-------------------------
Never expose your YouTube API Key in public repos!
Use st.secrets or a .env file and python-dotenv to load it securely.

-------------------------
📂 Project Structure
-------------------------
youtube_child_mode/
|
├── api_utils.py         # YouTube API fetching by keyword or channel
├── content_filter.py    # Keyword-based filter
├── train_model.py       # ML model training script
├── video_filter.py      # Combines keyword + ML filtering
├── ui_app.py            # Streamlit UI
├── safe_content_model.pkl  # Trained model
├── requirements.txt     # Python dependencies
└── README.txt           # Project documentation

-------------------------
📜 License
-------------------------
This project is open-source and free to use for educational and non-commercial purposes.
