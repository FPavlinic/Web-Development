# used libraries
from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

# look for .env file
load_dotenv("C:/Users/pavli/PycharmProjects/PORTFOLIO/.env.txt")

# email log in data
MY_EMAIL = os.getenv("NOBODY_GMAIL_USER")
MY_PASSWORD = os.getenv("NOBODY_GMAIL_PASS")

# get posts for the blog
blog_url = "https://api.npoint.io/ac46cacd002386f60c70"
all_posts = requests.get(blog_url).json()

# create Flask object
app = Flask(__name__)


# home page
@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)


# about page
@app.route('/about')
def about():
    return render_template('about.html')


# contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# read a post on its page
@app.route("/post/<index>")
def get_post(index):
    requested_post = None
    for blog_post in all_posts:
        if int(blog_post['id']) == int(index):
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


# fill the contact form
@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    name = request.form['person']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    if request.method == "POST":
        send_email(name, email, phone, message)
        return render_template("contact.html", message_sent="Successfully sent your message")
    else:
        return render_template("contact.html")


# send the data from the form via email
def send_email(name, email, phone, message):
    email_text = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:  # connect to gmail server
        connection.starttls()  # make connection secure
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)  # log in to gmail
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="pavlinicf@gmail.com",
                            msg=email_text.encode('utf-8'))  # encode message to support all characters


# run web app
if __name__ == "__main__":
    app.run(debug=True)
