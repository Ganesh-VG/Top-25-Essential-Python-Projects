from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return{column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafes=random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    cafe_list = [cafes.to_dict() for cafes in all_cafes]
    return jsonify(cafe=cafe_list)


@app.route("/search/<loc>", methods=["GET"])
def search_cafe(loc):
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc))
    loc_cafes = result.scalars().all()
    if loc_cafes:
        cafe_loc_list = [cafes.to_dict() for cafes in loc_cafes]
        return jsonify(cafe=cafe_loc_list)
    else:
        return jsonify(error={"Not-Found": "Sorry, we don't have a cafe at that location"}),404


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update_price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new price."})
    else:
        return jsonify(error={"Not-Found": "Sorry, we don't have a cafe with that id"}), 404


@app.route("/report_closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        if request.args.get("api-key") == "TopSecretAPIKey":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."})
        else:
            return jsonify(response={"error": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    else:
        return jsonify(error={"Not-Found": "Sorry, we don't have a cafe with that id"}), 404


if __name__ == '__main__':
    app.run(debug=True)
