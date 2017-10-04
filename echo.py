from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('form.html', title = 'Main')

@app.route('/welcomePage', methods=['POST','GET'])
def welcome():
	print request.headers
	print request.method
	print request.form
	print request.form['user']
	return render_template('input.html', title = request.form['user'] + "'s", user = request.form['user'], method = request.method)


if __name__ == "__main__":
	app.debug = True
	app.run()