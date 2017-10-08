from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "this is not secure"

@app.route('/')
def home():
        if 'user' in session:
                return render_template("input.html", user = session['user'], method = request.method)
        else:
	        return render_template('form.html', title = 'Main')

@app.route('/welcomePage', methods=['POST','GET'])
def welcome():
	print request.form['user']
        user = request.form['user']
        if user == 'bob':
                if request.form['password'] == 'secret':
                        session['user'] = request.form['user']
                        return render_template('input.html', title = user + "'s", user = user, method = request.method)
                else:
                        return render_template('fail.html', message = "Sorry, wrong password")
        else:
                return render_template('fail.html', message = "Sorry, wrong username")

@app.route('/logout')
def logout():
        session.pop('user')
        return redirect(url_for('home'))

if __name__ == "__main__":
	app.debug = True
	app.run()
