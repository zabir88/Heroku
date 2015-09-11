import os
from flask import Flask, render_template, request, redirect
from twilio.rest import TwilioRestClient 


app = Flask(__name__) # Creating the app instance

#Credentials from the twilio account to access the api and also my twilio number 
account_sid= 'AC5a5875ff049577324bde1a9af5d6b87c'
account_token= '82284d75af39c723ebfc7bb97d31d0dc'
twilio_number = '+13478460702' # My Twilio number 
client = TwilioRestClient(account_sid, account_token)

@app.route('/') # When you go to top page of app, this is what it will execute
def index():
    return render_template('form.html')
  
@app.route("/submit-form/", methods = ['POST']) 
def submit_number():
    number = request.form['number']
    user_number = "+1"+number # Switch to your country code of choice
    client.messages.create(to=user_number, from_ = twilio_number, body = "Hello! How you been? Hope all is well.") # Replace body with your message of choice
    return redirect('/messages/')
  
@app.route("/messages/")
def list_messages():
    return render_template('messages.html')
    
    
if __name__ == '__main__': # If we're executing this app from the command line
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    