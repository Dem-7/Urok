from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_quote')
def get_quote():
    try:
        # Используем Forismatic API
        response = requests.get(
            "https://api.forismatic.com/api/1.0/",
            params={
                "method": "getQuote",
                "format": "json",
                "lang": "ru"
            },
            timeout=5
        )
        response.raise_for_status()

        data = response.json()
        return jsonify({
            'quote': data['quoteText'],
            'author': data.get('quoteAuthor', 'Неизвестный автор')
        })
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Ошибка: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)