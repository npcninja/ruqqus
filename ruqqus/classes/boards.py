import time
from sqlalchemy import *
from sqlalchemy.orm import relationship

from ruqqus.helpers.base36 import *
from ruqqus.__main__ import Base, db, cache


class Boards(Base):
    __tablename__ = "boards"
    id = Column(BigInteger, primary_key=True)
    board_name = Column(String, default=None)
    is_banned = Column(Boolean, default=False)
    created_utc = Column(Integer, default=None)
    #mods = relationship('MODs', lazy="dynamic", backref="users")
    submissions = relationship("Submission", lazy="dynamic", backref="boards")
    subscriptions = relationship("Subscriptions", lazy="dynamic", backref="boards")

    def __init__(self, *args, **kwargs):
        if "created_utc" not in kwargs:
            kwargs["created_utc"] = int(time.time())

        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Boards(id={self.id}, board_id={self.board_id}, mods={self.mods})>"


    @cache.memoize(timeout=30)
    def sortlist(sort="hot", page=1):

        cutoff=int(time.time())-(60*60*24*30)

        posts = db.query(Submission).filter(Submission.created_utc>=cutoff,
                                            Submission.is_banned==False,
                                            Submission.stickied==False,
                                            Submission.board_id==self.id)

        if sort=="hot":
            posts=posts.order_by(text("submissions.rank_hot desc"))
        elif sort=="new":
            posts=posts.order_by(Submission.created_utc.desc())
        elif sort=="fiery":
            posts=posts.order_by(text("submissions.rank_fiery desc"))
        elif sort=="top":
            posts=posts.order_by(text("submissions.score desc"))

        posts=[x.id for x in posts.offset(25*(page-1)).limit(25).all()]

        return posts
        

    def frontpage(v):

        page=int(request.args.get("page",1))

        sort_method=request.args.get("sort", "hot")

        #get list of ids
        ids = frontlist(sort=sort_method, page=page)

        #assemble list of tuples
        i=1
        tups=[]
        for x in ids:
            tups.append((x, i))
            i+=1

        #tuple string
        tups = str(tups).lstrip("[").rstrip("]")
            

        #hit db for entries
        posts=db.query(Submission
                       ).from_statement(
                           text(f"""
                            select submissions.*, submissions.ups, submissions.downs
                            from submissions
                            join (values {tups}) as x(id, n) on submissions.id=x.id order by x.n"""
                                )).all()
        

        #If page 1, check for sticky
        if page==1:
            sticky =[]
            sticky=db.query(Submission).filter_by(stickied=True).first()
            if sticky:
                posts=[sticky]+posts
        
        return render_template("home.html", v=v, listing=posts, sort_method=sort_method)
