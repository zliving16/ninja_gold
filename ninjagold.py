from flask import Flask, request, redirect, url_for, session, render_template
from os import urandom
from random import randint

#  Create a new Flask project called ninja_gold
app = Flask(__name__)
key = urandom(16)
app.secret_key = key


#  Create the template as shown in the wireframe above, with 4 separate forms
#  Have the root route render this page
@app.route('/')
def main():
    if 'totalgold' not in session:
        session['totalgold'] = 0
    return render_template('index.html', gold=session['totalgold'])

#  Have the "/process_money" POST route increase/decrease the user's gold by an appropriate amount and redirect to the root route
@app.route('/process')
def process_money():
    # logic for adding/subtracting gold
    if request.form['cave']=='Cave':
        golddelta=randint(5,10)
        session['totalgold'] += golddelta
    return redirect('/')

#  NINJA BONUS: Display all the activities performed by the user in a log on the HTML, as shown in the wireframe
#  NINJA BONUS: Have the activities be color-coded as shown above (+ money is green, - money is red)
#  NINJA BONUS: Add a reset button to restart the game
#  SENSEI BONUS: Have the activities display in descending order, with the most recent activity first
#  SENSEI BONUS: Provide winning parameters to the game--for example, a user must obtain 500 gold in less than 15 moves. Only display the reset button once the user has won or lost.
#  SENSEI BONUS: Complete the "/process_money" route without 4 conditional statements (i.e. without doing if farm...elif cave...etc.)


if __name__ == "__main__":
    app.run(debug=True)
