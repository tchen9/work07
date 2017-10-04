from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "this is not secure"

@app.route('/')
def home():
	return render_template('form.html', title = 'Main')

@app.route('/welcomePage', methods=['POST','GET'])
def welcome():
	print request.form['user']
        user = request.form['user']
        if user == 'hello':
                if request.form['password'] == 'secret':
                        return render_template('input.html', title = user + "'s", user = user, method = request.method)
                else:
                        return render_template('fail.html', message = "Sorry, wrong password")
        else:
                return render_template('fail.html', message = "Sorry, wrong username")

if __name__ == "__main__":
	app.debug = True
	app.run()
