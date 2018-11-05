from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author': 'haidi',
		'title': 'blog pertamax',
		'content': 'first comment',
		'date_posted': 'oktober 25, 2018'
	},
	{
		'author': 'nata',
		'title': 'blog keduax',
		'content': 'second comment',
		'date_posted': 'oktober 26, 2018'
	}
]

@app.route('/')
@app.route('/home')
def index():
	return render_template('home.html', posts = posts)

@app.route('/about')
def about():
	return render_template('about.html', title = "about")

if __name__ == "__main__":
	app.run(debug=True)