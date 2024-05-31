from flask import Flask, render_template, request
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import smtplib

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

posts = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/form-entry", methods=["POST"])
def receive_data():
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)
    chrome_driver = Service("YOUR CHROMEDRIVER PATH")
    driver = webdriver.Chrome(service=chrome_driver, options=chrome_option)
    driver.get("YOUR GOOGLE FORM LINK")
    time.sleep(5)
    name = driver.find_element(By.CSS_SELECTOR,"div.Qr7Oae:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    name.send_keys(f"{request.form['name']}")
    email = driver.find_element(By.CSS_SELECTOR,"div.Qr7Oae:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    email.send_keys(f"{request.form['email']}")
    phone = driver.find_element(By.CSS_SELECTOR,"div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    phone.send_keys(f"{request.form['phone']}")
    message = driver.find_element(By.CSS_SELECTOR,"div.Qr7Oae:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    message.send_keys(f"{request.form['message']}")
    submit = driver.find_element(By.CSS_SELECTOR,".Y5sE8d > span:nth-child(3)")
    submit.click()
    time.sleep(3)
    driver.quit()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="YOUR TO ADDRESS",
                            msg=f"Subject:Hello\n\nContact request\nName:{request.form['name']}\nEmail:{request.form['email']}\nPhone:request.form['phone']\nMessage:request.form['message']")
    return render_template("display.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
