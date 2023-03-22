from flask import Flask, render_template, redirect, url_for, request

from emailverify import EmailVerify



app = Flask(__name__)


email_messages = ["Test"]

@app.route("/")
def main():
    return render_template("index.html", email_messages=email_messages)

@app.route("/verify", methods=["POST"])
def verify():
    email = request.form['email_message']

    message = EmailVerify(email)

    email_messages[0]= message

    return redirect("/")
 
if __name__ == "__main__":
    app.run()