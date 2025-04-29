import json
import string
import nltk
import random
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

# Download once
nltk.download('stopwords')

class Chatbot:
    def __init__(self, dataset_path):
        with open(dataset_path, 'r') as file:
            data = json.load(file)

        self.stop_words = set(stopwords.words('english'))
        self.raw_questions = [item['question'] for item in data]
        self.answers = [item['answer'] for item in data]
        self.questions = [self.preprocess(q) for q in self.raw_questions]

        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

        # Optional model saving
        joblib.dump(self.vectorizer, "model/vectorizer.pkl")
        joblib.dump(self.question_vectors, "model/vectors.pkl")

    def preprocess(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = text.split()
        tokens = [word for word in tokens if word not in self.stop_words]
        return ' '.join(tokens)

    def get_response(self, user_input, threshold=0.3):
        user_input_clean = self.preprocess(user_input)
        user_vector = self.vectorizer.transform([user_input_clean])
        similarity = cosine_similarity(user_vector, self.question_vectors)
        idx = similarity.argmax()

        if similarity[0][idx] > threshold:
            return self.answers[idx]
        else:
            return random.choice([
                "I'm not sure I understand. Could you rephrase?",
                "Can you ask that differently?",
                "I'm still learning. Try asking something else!"
            ])
