from flask import Flask, render_template, request
import nltk
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
    cln_data = text_preprocess(text_in)
    word_cnt = len(cln_data)
    return render_template('home.html', word_count = f"Number of words in given text: {word_cnt}")

if __name__ == '__main__':
    app.run()
