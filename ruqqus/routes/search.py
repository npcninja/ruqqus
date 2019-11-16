from ruqqus.classes import *

from flask import *
from ruqqus.__main__ import app, db

@app.route("/search", methods=["GET"])
def search():

    term=request.args.get("q")
    page=max(1, int(request.args.get("page", 1)))

    term="%"+term+"%"

    results=db.query(Submission).filter(Submission.title.ilike(term)).offset(25*(page-1)).limit(25)

    
