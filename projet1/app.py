from flask import Flask, request
from flask import render_template
from flask import*
app = Flask(__name__)

#====================================================================================================================
#gestion de la page de connection 
@app.route('/')
def index():
	error = None
	if request.method == 'POST':
		if request.form['pseudo'] != 'admin' or request.form['pass']!='admin':
			error = 'Invalid Credentials.Please try again'
			session['logout']=True
return render_template('/login.html')


if __name__ == '__main__':
		app.run(debug=False,host = "127.0.0.1",port=4000)
