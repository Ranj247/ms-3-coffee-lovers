import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Create instance of Flask
app = Flask(__name__)

# Set up configurations for MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Create an instance of PyMongo
mongo = PyMongo(app)


# All Recipes
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# -------------------------------CREDIT-------------------------------
# Inspiration for own project came from Code Institute, mini project
# 'flask task manager', functionalities being used and customised
# through out the project.


# Register a New User
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please choose another")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Log In Existing User
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Profile Username
@app.route("/profile/<username>/", methods=["GET", "POST"])
def profile(username):
    if session["user"] == username:
        # Get the session user's username from DB
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # Get the recipes created by this user
        recipes = list(mongo.db.recipes.find({"created_by": username}))
        return render_template(
            "profile.html", username=username,
            recipes=recipes)


# Log Out
@app.route("/logout")
def logout():
    # Remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add Recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_method": request.form.get("coffee_brew_method"),
            "roast_level": request.form.get("roast_level"),
            "grind_of_bean": request.form.get("grind_of_bean"),
            "quantity_of_coffee": request.form.get("quantity_of_coffee"),
            "brew_time": request.form.get("brew_time"),
            "recipe_description": request.form.get("recipe_description"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    coffee_brew_methods = mongo.db.coffee_brew_methods.find().sort(
        "method_name", 1)
    roast_levels = [
        "Light", "Light-Medium", "Medium", "Medium-Dark", "Dark", "French"]
    grind_of_beans = [
        "Fine", "Fine-Medium", "Medium", "Medium-Coarse", "Coarse"
    ]
    quantity_of_coffees = [
        "1 tablespoons of coffee (7g)", "2 tablespoons of coffee (14g)",
        "3 tablespoons of coffee (21g)", "4 tablespoons of coffee (28g)",
        "5 tablespoons of coffee (35g)", "6 tablespoons of coffee (42g)"
    ]
    brew_times = [
        "1 minute", "2 minutes", "3 minutes", "4 minutes",
        "5 minutes", "6 minutes", "7 minutes", "8 minutes",
        "9 minutes", "10 minutes"
        ]
    return render_template(
        "add_recipe.html", coffee_brew_methods=coffee_brew_methods,
        roast_levels=roast_levels, grind_of_beans=grind_of_beans,
        quantity_of_coffees=quantity_of_coffees,
        brew_times=brew_times
        )


# Edit Recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        update_recipe = {
            "recipe_method": request.form.get("coffee_brew_method"),
            "roast_level": request.form.get("roast_level"),
            "grind_of_bean": request.form.get("grind_of_bean"),
            "quantity_of_coffee": request.form.get("quantity_of_coffee"),
            "brew_time": request.form.get("brew_time"),
            "recipe_description": request.form.get("recipe_description"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, update_recipe)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    coffee_brew_methods = mongo.db.coffee_brew_methods.find().sort(
        "method_name", 1
        )
    roast_levels = [
        "Light", "Light-Medium", "Medium", "Medium-Dark", "Dark", "French"
        ]
    grind_of_beans = [
        "Fine", "Fine-Medium", "Medium", "Medium-Coarse", "Coarse"
        ]
    quantity_of_coffees = [
        "1 tablespoons of coffee (7g)", "2 tablespoons of coffee (14g)",
        "3 tablespoons of coffee (21g)", "4 tablespoons of coffee (28g)",
        "5 tablespoons of coffee (35g)", "6 tablespoons of coffee (42g)"
        ]
    brew_times = [
        "1 minute", "2 minutes", "3 minutes", "4 minutes",
        "5 minutes", "6 minutes", "7 minutes", "8 minutes",
        "9 minutes", "10 minutes"
        ]
    return render_template(
        "edit_recipe.html", recipe=recipe,
        coffee_brew_methods=coffee_brew_methods, roast_levels=roast_levels,
        grind_of_beans=grind_of_beans,
        quantity_of_coffees=quantity_of_coffees, brew_times=brew_times
        )


# Delete Recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


# Manage Brew Methods: only admin has access to this page
@app.route("/get_coffee_brew_methods")
def get_coffee_brew_methods():
    coffee_brew_methods = list(
        mongo.db.coffee_brew_methods.find().sort("method_name", 1)
        )
    return render_template(
        "coffee_brew_methods.html",
        coffee_brew_methods=coffee_brew_methods
        )


# Add Brew Method allow admin to add new category to db
@app.route("/add_coffee_brew_method", methods=["GET", "POST"])
def add_coffee_brew_method():
    if request.method == "POST":
        coffee_brew_method = {
            "method_name": request.form.get("coffee_brew_method")
        }
        mongo.db.coffee_brew_methods.insert_one(coffee_brew_method)
        flash("New Brew Method Added")
        return redirect(url_for("get_coffee_brew_methods"))

    return render_template("add_coffee_brew_method.html")


# Edit Brew Method allows admin to edit category
@app.route(
    "/edit_coffee_brew_method/<coffee_brew_method_id>",
    methods=["GET", "POST"]
    )
def edit_coffee_brew_method(coffee_brew_method_id):
    if request.method == "POST":
        submit = {
            "method_name": request.form.get("coffee_brew_method")
        }
        mongo.db.coffee_brew_methods.update(
            {"_id": ObjectId(coffee_brew_method_id)},
            submit
            )
        flash("Brew Method Successfully Updated")
        return redirect(url_for("get_coffee_brew_methods"))

    coffee_brew_method = mongo.db.coffee_brew_methods.find_one(
        {"_id": ObjectId(coffee_brew_method_id)}
        )
    return render_template(
        "edit_coffee_brew_method.html", coffee_brew_method=coffee_brew_method
        )


# Delete Brew Method allows admin to delete category
@app.route(
    "/delete_coffee_brew_method/<coffee_brew_method_id>",
    methods=["GET", "POST"]
    )
def delete_coffee_brew_method(coffee_brew_method_id):
    mongo.db.coffee_brew_methods.remove(
        {"_id": ObjectId(coffee_brew_method_id)}
        )
    flash("Brew Method Successfully Deleted")
    return redirect(url_for("get_coffee_brew_methods"))


# Search Recipes
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# Set how & where to run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
