from sqlalchemy import *
from ruqqus.__main__ import Base, db, cache

from .submission import *
from .comment import *
from .user import *

class Flag(Base):

    __tablename__="flags"

    id=Column(Integer, primary_key=True)
    post_id=Column(Integer, ForeignKey(Submission.id))
    user_id=Column(Integer, ForeignKey(User.id))
    created_utc=Column(Integer)

    def __repr__(self):

        return f"<Flag(id={self.id})>"

class CommentFlag(Base):

    __tablename__="commentflags"

    id=Column(Integer, primary_key=True)
    post_id=Column(Integer, ForeignKey(Submission.id))
    comment_id=Column(Integer, ForeignKey(Comment.id))
    created_utc=Column(Integer)

    def __repr__(self):

        return f"<CommentFlag(id={self.id})>"
