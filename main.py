from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/image_mars')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars3.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <div>Вот она какая красная планета</div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
