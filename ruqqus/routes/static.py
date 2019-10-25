import time
from ruqqus.helpers.wrappers import *
from flask import *

from ruqqus.__main__ import app
from ruqqus.classes import *

#take care of misc pages that never really change (much)
@app.route('/assets/<path:path>')
def static_service(path):
    return send_from_directory('assets', path+".html")

@app.route("/robots.txt", methods=["GET"])
def robots_txt():
    return send_file("./assets/robots.txt")

@app.route("/settings", methods=["GET"])
@auth_required
def settings(v):
    return redirect("/settings/profile")

@app.route("/settings/profile", methods=["GET"])
@auth_required
def settings_profile(v):
    return render_template("settings_profile.html", v=v)

@app.route("/settings/security", methods=["GET"])
@auth_required
def settings_security(v):
    return render_template("settings_security.html", v=v)

@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return send_file("./assets/images/logo/ruqqus_logo_square_white_fill.png")

@app.route("/my_info",methods=["GET"])
@auth_required
def my_info(v):
    return render_template("my_info.html", v=v)

@app.route("/notifications", methods=["GET"])
@auth_required
def notifications(v):
    return v.notifications_unread(page=request.args.get("page","1"),
                                   include_read=request.args.get("all",False))

@app.route("/submit", methods=["GET"])
@is_not_banned
def submit_get(v):
    return render_template("submit.html", v=v)

@app.route("/favicon.ico")
def favicon_ico():
    return send_from_directory('assets', "images/favicon.ico")

@app.route("/about/<path:path>")
@auth_desired
def about_path(v):
    return render_template(safe_join("about", path))
    return 
