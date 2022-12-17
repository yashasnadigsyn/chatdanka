from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':
        username = request.form['username']
        if len(username) < 5:
            return "Length of username should be 5 to 15 letters <br> <a href='/'>Go back!</a>"
        if len(username) > 15:
            return "Length of username should be 5 to 15 letters <br> <a href='/'>Go back!</a>"
        if any(i in  username for i in "+=\|]}[{';:/?.>,<+-*/)1234567890"):
            return "NO SPECIAL CHARACTERS.. ONLY LETTERS ALLOWED <br> <a href='/'>Go back!</a>"
        else:
            return redirect(url_for("password_page", username=username))
    return render_template("index.html")

@app.route("/username=<username>", methods=['GET', 'POST'])
def password_page(username):
    if request.method == 'POST':
        pin1 = request.form['z']
        try:
            pin1 = int(pin1)
        except:
            return "Only numbers allowed!"
        pin2 = request.form['a']
        try:
            pin2 = int(pin2)
        except:
            return "Only numbers allowed!"
        pin3 = request.form['b']
        try:
            pin3 = int(pin3)
        except:
            return "Only numbers allowed!"
        pin4 = request.form['c']
        try:
            pin4 = int(pin4)
        except:
            return "Only numbers allowed!"
        pin5 = request.form['d']
        try:
            pin5 = int(pin5)
        except:
            return "Only numbers allowed!"
        pin6 = request.form['e']
        try:
            pin6 = int(pin6)
        except:
            return "Only numbers allowed!"
        else:
            finalpin = str(pin1)+str(pin2)+str(pin3)+str(pin4)+str(pin5)+str(pin6)
            if os.path.exists(f"usernames/{username}.txt"):
                with open(f"usernames/{username}.txt", "r") as f:
                    password = f.read()
                    if finalpin == password.strip():
                        return "Ahh! The old user here..."
                    else:
                        return "Hey.. Hacker.."
            else:
                with open(f"usernames/{username}.txt", "w") as f:
                    f.write(finalpin)
                return "Ahh! A new user..."
    return render_template("password_page.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=True)