from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
    return render_template("index.html", all_books=all_books)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/form-entry", methods=["POST"])
def form_entry():
    if request.method == "POST":
        with app.app_context():
            # db.create_all()
            books = Books(
                title=request.form['book_name'],
                author=request.form['author'],
                rating=request.form['rating']
            )
            db.session.add(books)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/<index>", methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        index = request.form["id"]
        book_to_update = db.get_or_404(Books, index)
        book_to_update.rating = request.form["edit"]
        db.session.commit()
        return redirect(url_for('home'))
    detail = db.session.execute(db.select(Books).where(Books.id == index)).scalar()
    return render_template("edit.html", detail=detail)


@app.route("/delete/<index>")
def delete(index):
    book_to_delete = db.get_or_404(Books, index)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

