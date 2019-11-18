from ruqqus.classes import *
from ruqqus.helpers.wrappers import *

from flask import *
from ruqqus.__main__ import app, db

@app.route("/search", methods=["GET"])
@auth_desired
def search(v):

    term=request.args.get("q")
    sort=request.args.get("sort", "hot").lower()
    
    page=max(1, int(request.args.get("page", 1)))

    term="%"+term+"%"

    posts = db.query(Submission).filter_by(is_banned=False, is_deleted=False).filter(Submission.title.ilike(term))

    if sort=="hot":
        posts=posts.order_by(text("submissions.rank_hot desc"))
    elif sort=="new":
        posts=posts.order_by(Submission.created_utc.desc())
    elif sort=="fiery":
        posts=posts.order_by(text("submissions.rank_fiery desc"))
    elif sort=="top":
        posts=posts.order_by(text("submissions.score desc"))
        
    total=posts.count()
    posts=[x.id for x in posts.offset(25*(page-1)).limit(26).all()]
    
    next_exists=(len(posts)==26)
    results=posts[0:25]

    return render_template("search.html", v=v, total=total, listing=results, sort_method=sort, next_exists=next_exists)
