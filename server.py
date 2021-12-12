from flask import Flask, request, render_template, g, redirect, Response, url_for

import os

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


# data
posts = [
    {"name": "Influenza Smith", "attributes": ["WOC"], "connection": "2nd", "text": "I had a really great experience with Dr. Kim, who is a woman of color like myself. She took really great care of my skin and adressed problems specific to my skin type. On top of that, she knows and understands problems that people of my ethnic background face. I definitely feel comfortable entrusting her with my health!", \
        "link": "Dr. Martha Kim", "profile_link": "influenza-smith"},
    {"name": "Varicella Shah", "attributes": ["anxiety", "South Asian"], "connection": "1st", "text": "I want to spread the word about BetterHelp. I have been struggling with my anxiety as of late, and I wanted to find a therapist that is  South Asian, like myself. I had such great luck with this platform in finding someone who understands my cultural context. High recommend to anyone seeking out affordable counseling!", \
    "profile_link": "varicella-shah"}
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

@app.route('/profiles/influenza-smith')
def profiles1():
    return render_template("influenza.html")

@app.route('/profiles/varicella-shah')
def profiles2():
    return render_template("varicella.html")

@app.route('/visitors_profile')
def visitors_profile():
    return render_template("visitors_profile.html")

@app.route('/dashboard')
def dashboard_page():
    return render_template("dashboard.html")
@app.route('/explore')
def explor_page():
    return render_template("explore.html", posts=posts, doctors=doctors)

@app.route('/doctor_matches')
def doctor_matches():
    print(list(doctors.keys()))
    return render_template("doctor_matches.html", doctors=doctors, doctor_names=list(doctors.keys()))
