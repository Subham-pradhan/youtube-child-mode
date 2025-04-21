import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

# Sample training data
data = {
    'text': [
        'Funny cartoon for kids', 'How to make drugs at home', 'New Marvel movie trailer',
        'Horror movie review', 'Safe educational video', 'Violence in the streets', 
        'How to deal with bullying', 'Naked celebrity pictures', 'Healthy food for kids',
        'Murder mystery series', 'Racist comments and jokes'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

joblib.dump(model, 'safe_content_model.pkl')
print("Model trained and saved as 'safe_content_model.pkl'")
