from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json['text']
    polarity = TextBlob(text).sentiment.polarity
    return jsonify({ 'sentiment': polarity })

if __name__ == '__main__':
    app.run(port=5000)
