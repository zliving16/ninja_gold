from flask import Flask, request, redirect, url_for, session, render_template
import random
import collections

#  Create a new Flask project called ninja_gold
app = Flask(__name__)
key = "admin"
app.secret_key = key


#  Create the template as shown in the wireframe above, with 4 separate forms
#  Have the root route render this page
@app.route('/')
def main():
    if 'totalgold' not in session:
        session['totalgold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    
    if 'lengthlist' not in session:
        session['lengthlist']=len(session['activity'])-1   

    return render_template('index.html', totalgold=session['totalgold'],i=session['activity'], activity=session['activity'], lenlist=session['lengthlist'])

#  Have the "/process_money" POST route increase/decrease the user's gold by an appropriate amount and redirect to the root route
@app.route('/process', methods=['POST'])
def process_money():
    # logic for adding/subtracting gold
    place = request.form['place']
    if place == 'farm':
        golddelta=random.randint(10,20)
    elif place == 'Cave':
        golddelta=random.randint(5,10)
    elif place == 'House':
        golddelta=random.randint(2,5)
    elif place == 'Casino':
        if session['totalgold'] > 0:
            golddelta=random.randint(-50,50)
        else: golddelta=0
    session['totalgold'] += golddelta
    # session['place'] = place
    if golddelta>0:
        word = 'Got'
        color = 'green'
    else:
        word = 'Lost'
        color = 'red'
        golddelta *= -1
    session['activity'].append(f"<li style='color:{color};'>{word} {golddelta} gold from {place}</li>")
    if 'lengthlist' not in session:
        session['lengthlist']=len(session['activity'])-1 
    session['lengthlist']=len(session['activity'])-1   
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')
#  NINJA BONUS: Display all the activities performed by the user in a log on the HTML, as shown in the wireframe
#  NINJA BONUS: Have the activities be color-coded as shown above (+ money is green, - money is red)
#  NINJA BONUS: Add a reset button to restart the game
#  SENSEI BONUS: Have the activities display in descending order, with the most recent activity first
#  SENSEI BONUS: Provide winning parameters to the game--for example, a user must obtain 500 gold in less than 15 moves. Only display the reset button once the user has won or lost.
#  SENSEI BONUS: Complete the "/process_money" route without 4 conditional statements (i.e. without doing if farm...elif cave...etc.)


if __name__ == "__main__":
    app.run(debug=True)
