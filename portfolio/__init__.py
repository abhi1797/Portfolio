from flask import Flask, render_template,abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-10nq.onrender.com",
    },
    {
        "name": "E-commerce website using flask",
        "thumb": "img/E-commerce.jpeg",
        "hero": "img/E-commerce-hero.jpg",
        "categories": ["Python", "Html", "CSS", "Sqlite3"],
        "slug": "shopzilla",
        "prod": "https://github.com/abhi1797/ShopZillaa",
    },
    {
        "name": "Weather Tracker Golang",
        "thumb": "img/weather1.jpg",
        "hero": "img/weather-hero1.jpg",
        "categories": ["Golang"],
        "slug": "weather-tracker",
        "prod": "https://github.com/abhi1797/Weather-Tracker-Golang",
    },
    
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html",
                           project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404