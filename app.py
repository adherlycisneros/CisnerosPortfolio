import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message 

app = Flask(__name__) 

# Load mail configuration from environment variables
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Create email message
        msg = Message(subject, sender=os.environ.get('MAIL_USERNAME'), recipients=[os.environ.get('MAIL_USERNAME')])
        msg.body = f"From: {name} \nEmail: {email} \n\n{message}"
        mail.send(msg)

        return render_template('index.html', success=True) 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

