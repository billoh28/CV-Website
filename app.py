#!flask/bin/python
from flask import Flask, request, jsonify, Response, render_template, send_from_directory

# Networking requirements
import socket
import time
import os

def create_cv_page():
    # Set up Flask App, define page request and response handling here
    
    # Get today's date
    # todays_date = str(date.today().strftime("%d-%m-%Y"))

    # File path of local machine
    DIR = os.getcwd()

    # Creates a flask app
    app = Flask(__name__)

    ###########################################################
    ####### ERROR Handling ##################################
    ###########################################################

    # File Not Found Error
    @app.errorhandler(404)
    def file_not_found(e):
        return render_template("404.html"), 404
    
    # Method not allowed Error
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template("405.html"), 405
    
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
    ###########################################################

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

    # return app instance and the IP address the website is running on
    return app, get_ip()

if __name__ == '__main__':
    # If app is run from local program and not being tested from external program
    app, IP = create_cv_page()

    # Run website
    app.run(host=IP, port=8888, debug=True)
