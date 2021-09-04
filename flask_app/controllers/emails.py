from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email

@app.route("/")
def index():
    emails = Email.get_all_emails()
    return render_template('index.html', all_emails= emails)

@app.route('/showEmails')
def showEmails():
    return render_template('showEmails.html', showEmails= Email.get_all_emails())

@app.route('/create_email', methods=['POST'])
def create_email():
    data ={
        'email': request.form['email']
    }
    if(not Email.is_valid_email(data["email"])):
        return redirect('/')    
    Email.save_email(data)
    return redirect('/showEmails')
