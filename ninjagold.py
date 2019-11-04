from flask import Flask, render_template, request, redirect, session
import random 
app= Flask(__name__)
app.secret_key='admin'

@app.route('/')
def main():
    if 'totalgold' not in session:
        session['totalgold']


if request.form['cave']=='Cave':
    golddelta=random.randint(5,10)
    session['totalgold']+= golddelta







if __name__ == "__main__":
    app.run(debug=True)
