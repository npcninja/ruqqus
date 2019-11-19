from ruqqus.classes import *
from ruqqus.helpers.wrappers import *

from ruqqus.__main__ import app, db

@app.route("flagged/posts", methods=["GET"])
@admin_level_required(3)
def flagged_posts(v):

    page=max(1, int(request.args.get("page", 1)))

    posts = db.query(Submission).filter(Submission.flag_count>=1)order_by(text("flag_count desc")).offset(25*(page-1)).limit(26)

    listing=[p for p in posts]
    next_exists=len(listing==26)
    listing=listing[0:25]
