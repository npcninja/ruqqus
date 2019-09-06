from flask import *
from ruqqus.classes import *
from ruqqus.helpers.wrappers import *
from ruqqus.helpers.sanitize import *
from ruqqus.mail import *
from ruqqus.__main__ import db, app

@app.route("/settings/profile", methods=["POST"])
@auth_required
@validate_formkey
def settings_profile_post(v):

    updated=False

    if request.form.get("new_password"):
        if request.form.get("new_password") != request.form.get("cnf_password"):
            return render_template("settings.html", v=v, error="Passwords do not match.")

        if not v.verifyPass(request.form.get("old_password")):
            return render_template("settings.html", v=v, error="Incorrect password")

        v.passhash=v.hash_password(request.form.get("new_password"))
        updated=True
                                  

    if request.form.get("over18") != v.over_18:
        updated=True
        v.over_18=bool(request.form.get("over18", None))

    if request.form.get("bio") != v.bio:
        updated=True
        bio = request.form.get("bio")
        v.bio=bio

        v.bio_html=sanitize(bio)

    if updated:
        db.add(v)
        db.commit()

        return render_template("settings_profile.html", v=v, msg="Your settings have been saved.")

    else:
        return render_template("settings_profile.html", v=v, error="You didn't change anything.")

@app.route("/settings/security", methods=["POST"])
@auth_required
@validate_formkey
def settings_security_post(v):

    updated=False

    if request.form.get("new_password"):
        if request.form.get("new_password") != request.form.get("cnf_password"):
            return render_template("settings_security.html", v=v, error="Passwords do not match.")

        if not v.verifyPass(request.form.get("old_password")):
            return render_template("settings_security.html", v=v, error="Incorrect password")

        v.passhash=v.hash_password(request.form.get("new_password"))

        db.add(v)
        db.commit()
        
        return render_template("settings_security.html", v=v, msg="Your password has been changed.")

    if request.form.get("new_email"):
        new_email = request.form.get("new_email")
        if new_email == v.email:
            return render_template("settings_security.html", v=v, error="That's already your email!")

        send_verification_email(v, email=new_email)

        return render_template("settings_security.html", v=v, msg=f"Verify your new email address {new_email} to complete the email change process.")
        


        
