from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message 

app = Flask(__name__) 
 
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cisnerosprojects@outlook.com'
app.config['MAIL_PASSWORD'] = 'toetvyvyaujztkom'
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        msg = Message (subject, sender = 'cisnerosprojects@outlook.com', recipients = ['cisnerosprojects@outlook.com'])
        msg.body = f"From: {name} \nEmail: {email} \n\n{message}"
        mail.send(msg)

        return render_template('index.html', success=True) 
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)