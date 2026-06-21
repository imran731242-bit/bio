from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

emotes = [
    {"name": "LOL", "image": "lol.gif"},
    {"name": "Dance", "image": "dance.gif"},
    {"name": "Wave", "image": "wave.gif"}
]

@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html', emotes=emotes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "1234":
            session['user'] = username
            return redirect('/')
    return render_template('login.html')

@app.route('/admin')
def admin():
    if 'user' not in session:
        return redirect('/login')
    return render_template('admin.html', emotes=emotes)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)