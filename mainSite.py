from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')

def landing_page():
	return render_template('landingPage.html', name='hello')

if __name__ == "__main__":
	app.run(debug=True)

