from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('base.html')

@my_app.route('/bob', methods = ['GET', 'POST'])
def bob():
    
    print request.method
    print request.headers
    usernameR = ""
    if request.method == "POST":
        usernameR = request.form['username']
    return render_template('one.html', method = request.method, username = usernameR)
    
    
if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
