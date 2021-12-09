from flask import Flask, request, render_template, g, redirect, Response, url_for

import os

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


# data
posts = [
    {"name": "Influenza Smith", "attributes": ["WOC"], "connection": "2nd", "text": "I had a really great experience with Dr. Kim, who is a woman of color like myself. She took really great care of my skin and adressed problems specific to my skin type. On top of that, she knows and understands problems that people of my ethnic background face. I definitely feel comfortable entrusting her with my health!", \
        "link": "Dr. Martha Kim"},
    {"name": "Varicella Shah", "attributes": ["anxiety", "South Asian"], "connection": "1st", "text": "I want to spread the word about BetterHelp. I have been struggling with my anxiety as of late, and I wanted to find a therapist that is  South Asian, like myself. I had such great luck with this platform in finding someone who understands my cultural context. High recommend to anyone seeking out affordable counseling!"}
]

doctors = {
    "Dr. Martha Kim" : {
        "mutual_friends": 35, "mutual_doctors": 2, "attributes": ["Dermatology", "WOC", "holistic"], "accepting_patients": True
    },
    "Anne Pepper, M.D.": {
        "mutual_friends": 23, "mutual_doctors": 3, "attributes": ["Dermatology", "Calm"], "accepting_patients": False
    },
    "Dr. McStuffins, M.D.": {
        "mutual_friends": 15, "mutual_doctors": 0, "attributes": ["Dermatology", "Straight-Forward"], "accepting_patients": False
    }
}

my_groups = [
    {"name": "WOC", "members": 1280, "friends": 18, "image": "woc.jpeg"},
    {"name": "South Asian", "members": 5321, "friends": 42, "image": "southasian.png"},
    {"name": "Anxiety", "members": 10384, "friends": 9, "image": "anxiety.jpeg"},
    {"name": "Student", "members": 9421, "friends": 53, "image": "student.jpeg"}
]

discover_groups = [
    {"name": "Latinx", "members": 9421, "friends": 53, "image": "latinx.jpeg"},
    {"name": "Chicago", "members": 496, "friends": 2, "image": "chicago.png"},
    {"name": "Expecting Mothers", "members": 102, "friends": 0, "image": "pregnant.jpeg"},
    {"name": "Transgender", "members": 58, "friends": 1, "image": "transgender.jpeg"},
    {"name": "Teachers", "members": 12578, "friends": 22, "image": "teachers.jpeg"}
]

# routes
@app.route('/')
def index():
  return redirect('/login')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/loginaction', methods=['POST'])
def login_action():
    return redirect(url_for('landing'))

@app.route('/createaccount')
def createaccount():
    return render_template("create_account.html")

@app.route('/addnewuseraction', methods=['POST'])
def addnewuser():
    return redirect(url_for('landing'))

@app.route('/landing')
def landing():
    return render_template("landing.html", posts=posts, doctors=doctors)

@app.route('/doctor_matches')
def doctor_matches():
    return render_template("doctor_matches.html", doctors=doctors, doctor_names=list(doctors.keys()))

@app.route('/search_groups')
def search_groups():
    return render_template("search_groups.html", my_groups=my_groups, discover_groups=discover_groups)

@app.route('/explore')
def explore():
    return render_template("explore.html", posts=posts, doctors=doctors)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", my_groups=my_groups)



