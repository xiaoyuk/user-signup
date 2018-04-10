from flask import Flask, request, redirect, render_template

import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True




@app.route("/")
def display_signup_form():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if username == '':
       username_error = 'username can not be empty!'
    else:
        if ' ' in username:
            username_error = 'username can not contain space character!'
            
        else:
            if len(username) < 3:
                username_error = 'username length cannot be less than 3 characters!'
                
            else:
                if len(username) > 20:
                    username_error ='username length cannot exceed 20 characters!'
                    
    
    if password == '':
        password_error = 'password can not be empty!'
    else:
        if ' ' in password:
            password_error = 'password can not contain space character!'
            password = ''
        else:
            if len(password) < 3:
                password_error = 'password length cannot be less than 3 characters!'
                password = ''
            else:
                if len(password) > 20:
                    password_error ='password length cannot exceed 20 characters!'
                    password = ''

    if verify_password == '':
        verify_password_error = 'verify password can not be empty!'
    else:
        if verify_password != password:
            verify_password_error = 'password does not match!'
            verify_password = ''

    if email != '':
        if '@' not in email:
            email_error = 'email should contain @!'
            
        else:
            if '.' not in email:
                email_error = 'email should contain . !'
                
    
    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', username_error = username_error, password_error = password_error, verify_password_error = verify_password_error,
            email_error=email_error, username=username, password=password, verify_password=verify_password, email=email)



    
app.run()

