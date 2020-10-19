#!flask/bin/python
from flask import Flask, render_template, send_from_directory

# Networking requirements
import socket
import os
import git

# run on ip address of machine
# print ip address to terminal
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = "0.0.0.0"
    try:
        s.connect(("10.255.255.255", 1))  # try to connect to bogon ip to get ip of machine
        ip = s.getsockname()[0]  # returns ip address of server on local network
    except:
        pass
    finally:
        s.close()
    return ip


# Set up Flask App, define page request and response handling here

# Get today's date
# todays_date = str(date.today().strftime("%d-%m-%Y"))

# File path of local machine
DIR = os.getcwd()

# Creates a flask app
app = Flask(__name__)

###########################################################
####### ERROR Handling ####################################
###########################################################

# File Not Found Error
@app.errorhandler(404)
def file_not_found(e):
    return render_template("404.html"), 404

# Method not allowed Error
@app.errorhandler(405)
def method_not_allowed(e):
    return render_template("405.html"), 405

# Server Error
@app.errorhandler(500)
def method_not_allowed(e):
    return render_template("500.html"), 500

###########################################################
####### Routing Handling ##################################
###########################################################

# Home Page
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# Work Experience Page
@app.route("/work_experience", methods=["GET"])
def work_exp():
    return render_template("work_experience.html")

# Education Page
@app.route("/education", methods=["GET"])
def edu():
    return render_template("education.html")

# Achievements Page
@app.route("/achievements", methods=["GET"])
def achieve():
    return render_template("achievements.html")

# Projects Page
@app.route("/projects", methods=["GET"])
def project():
    return render_template("projects.html")

# Interests Page
@app.route("/interests", methods=["GET"])
def interests():
    return render_template("interests.html")

# Browser Icon
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(DIR, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

###########################################################
####### Git Web Hook Routing ##############################
###########################################################

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./CV-Website')
        origin = repo.remotes.origin
        repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return '', 200

    else:
        return '', 400

###########################################################
###########################################################

