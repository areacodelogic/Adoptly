from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import AddPetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "thesecretestofallkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def home_page():

    return render_template("pets.html")


@app.route("/add", methods=["GET", "POST"])
def add_pet():

    form = AddPetForm()

    # import pdb
    # pdb.set_trace()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        # available = form.available.data

        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes
            # available=available,
        )

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}")

        return redirect("/")

    else:
        return render_template("add.html", form=form)
