from bottle import post, request
import re
from datetime import datetime
import pdb

questions = {}

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    question = request.forms.get('QUESTION')
    
    if not mail or not username or not question:
        return "Please fill in all fields"
    
    email_pattern = r'^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, mail):
        return "Invalid email format"
    
    questions[mail] = question
    
    pdb.set_trace()
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"""Thanks, {username}! 
            The answer to your question will be sent to {mail}. 
            Access Date: {current_date}
            Your question: {question}"""