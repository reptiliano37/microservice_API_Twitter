from flask import Flask, jsonify
from flask import request
from analysis import sentiment as sentiment

app = Flask(__name__)


@app.route('/sentiment', methods=['POST'])
def sentiment_():
    data = request.json
    print(data)
    json_tweet = {
        'name': data['name'],
        'tag_filter': data['tag_filter'],
        'download_from_date': data['download_from_date']
    }
    result_json = sentiment.sentiment_analysis(json_tweet)
    return jsonify(result_json)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
