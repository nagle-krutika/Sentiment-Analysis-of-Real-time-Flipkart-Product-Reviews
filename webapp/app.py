import pickle
from flask import Flask, render_template, request
import preprocessing as pr

# Loading vectorizer
with open("tfidf_vec.pkl", 'rb') as vectorization:
    vector = pickle.load(vectorization)
    
# Loading model
with open("rfc_final.pkl",'rb') as model:
    model = pickle.load(model)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_emotion():
    text = request.form['text']
    text_1=text
    text = pr.read_more(text)
    text = pr.normalization(text)
    text = pr.remove_emoji(text)
    text = pr.remove_punctuation(text)
    text = pr.remove_digit(text)
    text = pr.accented_fixing(text)
    text = pr.auto_correction(text)
    text = pr.contraction_fixing(text)
    text = pr.remove_stopwords(text)
    text = pr.stemming(text)

    x = vector.transform([text]).A
    emotion_label = {0: 'Neutral', 1: 'Negative', 2: 'Positive'}
    
    prediction = int(model.predict(x))
    emotion = emotion_label[prediction]
    
    return render_template('index.html', prediction=f"Text: {text_1} | Emotion: {emotion}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
