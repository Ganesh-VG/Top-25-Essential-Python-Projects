from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from csv import writer


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Location URL', validators=[DataRequired(), URL(message="Please enter the valid URL")])
    open = StringField('open time', validators=[DataRequired()])
    closing = StringField('closing time', validators=[DataRequired()])
    coffee = SelectField(u'coffee rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️',  '☕️☕️☕️☕️☕️'], validators=[DataRequired()])
    wifi = SelectField(u'Wifi rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪',  '💪💪💪💪💪'], validators=[DataRequired()])
    power = SelectField(u'Power outlet rating', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌',  '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


'''
To add cafe to the website please type "/add" along with the url
'''

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    login_form = CafeForm()
    if login_form.validate_on_submit():
        row_list = [login_form.cafe.data, login_form.location.data, login_form.open.data, login_form.closing.data, login_form.coffee.data, login_form.wifi.data, login_form.power.data]
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(row_list)
    return render_template('add.html', form=login_form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


@app.route('/cafes/<int:index>')
def url(index):
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_urls = []
        for row in csv_data:
            list_of_urls.append(row[1])
    return redirect(list_of_urls[index])


if __name__ == '__main__':
    app.run(debug=True)
