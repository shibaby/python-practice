from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	return '<h1>Home</h1>'
	
@app.route('/signin', methods = ['GET'])
def signin_form():
	return '''<form action = 'signin' method = 'post'>
		<p><input name = 'username'/></p>
		<p><input name = 'password' type = 'password'/></p>
		<p><button type = 'submit'>Sign In</button></p>
		</form>'''

@app.route('/signin', methods = ['POST'])
def sigin():
	return '<p>username: %s</p><p>password: %s</p>' % (request.form['username'], request.form['password'])
	
if __name__ == '__main__':
	app.run()