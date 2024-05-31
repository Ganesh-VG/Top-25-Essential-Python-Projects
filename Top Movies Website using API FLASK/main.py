from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

api_token = "<GET YOUR API TOKEN BY SIGNING IN TO TMDB>"

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Movie-collection.db"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)


class EditForm(FlaskForm):
    new_rating = StringField('Your Rating out of 10. eg:7.5', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    sort_movie = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    for all_movie in sort_movie:
        all_movie.ranking = all_movie.id
        db.session.commit()
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    return render_template("index.html", all_data=result)


@app.route("/delete")
def delete():
    index_del = request.args.get('id')
    book_to_delete = db.get_or_404(Movie, index_del)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = EditForm()
    index = request.args.get('id')
    book_to_update = db.get_or_404(Movie, index)
    if request.method == "POST":
        book_to_update.rating = edit_form.new_rating.data
        book_to_update.review = edit_form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if request.method == "POST":
        parameters = {
            "query": add_form.movie_title.data,
        }
        headers = {
            "Authorization": api_token
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters, headers=headers)
        response.raise_for_status()
        try:
            mdata = response.json()
            data = mdata["results"][0]
        except IndexError:
            return redirect(url_for('add'))
        second_movie = Movie(
                title=data["original_title"],
                year=data["release_date"],
                description=data["overview"],
                rating=data["vote_average"],
                ranking="none",
                review="To be added",
                img_url=f"https://image.tmdb.org/t/p/w500{data['backdrop_path']}"
            )
        db.session.add(second_movie)
        db.session.commit()
        index = db.session.execute(db.select(Movie).where(Movie.title == data["original_title"])).scalar()
        return redirect(url_for('edit', id=index.id))
    return render_template("add.html", form=add_form)


if __name__ == '__main__':
    app.run(debug=True)


