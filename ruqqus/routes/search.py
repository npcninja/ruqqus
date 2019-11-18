from ruqqus.classes import *

from flask import *
from ruqqus.__main__ import app, db

@app.route("/search", methods=["GET"])
@auth_desired
def search(v):

    term=request.form.get("q")
    page=max(1, int(request.args.get("page", 1)))

    term="%"+term+"%"

    search = db.query(Submission).filter_by(is_banned=False, is_deleted=False).filter(Submission.title.ilike(term)).offset(25*(page-1))
    
    total=search.count()
    results=search.limit(26)

    next_exists=(len(results)==26)
    results=results[0:25]

    #return render_template("search_results.html", v=v total=total, listing=results, next_exists=next_exists)
