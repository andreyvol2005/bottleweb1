from bottle import post, request
import re
from datetime import datetime

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    
    if not mail or not username:
        return "Please fill in all fields"
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, mail):
        return "Invalid email format"
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date: {current_date}"