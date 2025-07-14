from flask import Flask, render_template, redirect, request, session, url_for
from auth import users, register_user, authenticate_user
from data import PRODUCTS

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def home():
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if authenticate_user(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('products'))
        return 'Login failed'
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if register_user(request.form['username'], request.form['password']):
            return redirect(url_for('login'))
        return 'User already exists'
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/products')
def products():
    username = session.get('username')
    return render_template('products.html', products=PRODUCTS, username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

