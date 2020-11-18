from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

import json

input_file = open ('src/my_data.json')
json_array = json.load(input_file)
transaction_list = []
task_list=[]

for project in json_array:
    #print(project['transactions'])
    if(project['transactions']):
        #print(project['transactions'])
        for transaction in project['transactions'] :
            #print(transaction)
            transaction_list.append(transaction)
            if(transaction['tasks']):
                for task in transaction['tasks'] :
                    print(task)
                    task_list.append(task)
    
@app.route("/")
@app.route("/projects")
def projects():
    return render_template('projects.html', title='Projects', posts=json_array)

@app.route("/addProject")
def add_projects():
    return render_template('new_project.html', title='Add Project')

@app.route("/transactions")
def transactions():
    return render_template('transactions.html', title='Transactions', posts=transaction_list)

@app.route("/tasks")
def tasks():
    return render_template('tasks.html', title='Tasks', posts=task_list)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)