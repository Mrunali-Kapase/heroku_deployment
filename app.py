from flask import Flask, render_template, request
import nltk
from nltk import FreqDist

nltk.download('punkt')
import string

punct = string.punctuation
def text_preprocess(data):
    clean_word = [word for word in nltk.word_tokenize(data) if word not in punct]
    return clean_word


app = Flask(__name__)

@app.route('/')
def wrd_cnt():
    return render_template('home.html')

@app.route('/count', methods=['post'])
def cnt():
    text_in = request.form.get('txt')
    print(text_in)
    
    sen_cnt = len(nltk.sent_tokenize(text_in))
    cln_data = text_preprocess(text_in)
    word_cnt = len(cln_data)
    freq = dict(FreqDist(nltk.word_tokenize(text_in)))
    return render_template('home.html', sen_count = f"Number of Sentences in given text: {sen_cnt}", word_count = f"Number of words in given text: {word_cnt}", freq_all = f"Frequencies of words in given text: {freq}")
    

if __name__ == '__main__':
    app.run(debug=True)