from flask import Flask, render_template, redirect, session, request 
from users_model import User

app = Flask(__name__)

# Main page - creating a re-direct to the user's page
@app.route('/')
def index():
    return redirect('/users')

#  Display the current data that is stored in the database and adding it to a table 
@app.route('/users')
def users_show():
    all_users = User.get_all()
    return render_template('users.html',   
                           all_users=all_users)

# Creating this port route to be able to send data over from the form to the database and display it in our main page 
@app.route('/users/create', methods=['POST'])
def posting():
    print(request.form)
    new_user = User.create_one_user(request.form)
    return redirect('/')

#  Display the form page to input the new users being added 
@app.route('/users/new')
def create():
    return render_template('users_new.html')


if __name__=="__main__":
    app.run(debug=True)
