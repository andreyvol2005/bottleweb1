from bottle import post, request, response
import re
from datetime import datetime
import json
import os

JSON_FILE = 'data.json'

def validate_q(question):
    question = question.strip()
    
    if not question:    
        return "Question cannot be empty"
    
    if len(question) < 4:
        return "Question is too short (minimum 4 characters)"
    
    if question.isdigit():
        return "Question cannot consist of only digits"
    
    if not any(c.isalpha() for c in question):
        return "Question must contain at least one letter"
    
    return None

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    question = request.forms.get('QUESTION').strip()
    
    if not mail or not username or not question:
        return "Please fill in all fields"
    
    email_pattern = r'^[a-zA-Z][a-zA-Z0-9._%+-]{4,}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, mail):
        return "Invalid email format"
    
    if validate_q(question):
        return validate_q(question);
    
    data = {}
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
                
    if 'users' not in data:
        data['users'] = {}
        
    if mail not in data['users']:
        data['users'][mail] = {
            'username': username,
            'questions': [],
            'last_access': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
    if question not in data['users'][mail]['questions']:
        data['users'][mail]['questions'].append(question)
        data['users'][mail]['last_access'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(JSON_FILE, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)

        return f"""Thanks, {username}!<br>
                The answer to your question will be sent to {mail}.<br>
                Access Date: {datetime.now().strftime("%Y-%m-%d")}<br>
                Your question: {question}"""
    else:
        return "This question already exists in our database"