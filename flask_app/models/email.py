
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails;"

        results = connectToMySQL('emails_schema').query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails

    @classmethod
    def save_email(cls, data ):
        query = "INSERT INTO emails ( email , created_at, updated_at ) VALUES ( %(email)s, NOW() , NOW() );"
        return connectToMySQL('emails_schema').query_db( query, data )

    @staticmethod
    def is_valid_email(email):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email): 
            flash("Invalid email address!")
            is_valid = False
        else:
            flash(f"The email address you entered {email} is a VALID email address! Thank You!")
        return is_valid
        



