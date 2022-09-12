from email import header
from operator import index
from flask import Flask, request, render_template, jsonify
from model import SentimentRecommenderModel

app = Flask(__name__)

sentiment_model = SentimentRecommenderModel()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods =['POST','GET'])
def prediction():
    user = request.form['userName']
    user = user.lower()
    items = sentiment_model.getSentimentRecommendations(user)

    if(not(items is None)):
        print(f"retrieving items---{len(items)}")
        print(items)
        return render_template("index.html",column_name = items.columns.values, row_data = list(items.values.tolist()),zip = zip)
    else:
        return render_template("index.html", message = "User Name doesn't exists, No product recommendations at this point of time!")


@app.route('/predictSentiment',methods=['POST','GET'])
def predict_sentiment():
    review_text = request.form["reviewText"]
    print(review_text)
    predict_sentiment = sentiment_model.classify_sentiment(review_text)
    print(predict_sentiment)
    return render_template("index.html",sentiment = predict_sentiment)

if __name__ == '__main__':
    app.run(debug=True)