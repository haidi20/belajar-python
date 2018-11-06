from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '573e98412730e223da3db9973f803028'

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
def home():
	return render_template('home.html', posts = posts)

@app.route('/about')
def about():
	return render_template('about.html', title = "about")

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='login', form=form)
	

if __name__ == "__main__":
	app.run(debug=True)