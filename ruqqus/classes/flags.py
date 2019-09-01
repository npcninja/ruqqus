from flask import render_template
from sqlalchemy import *
from sqlalchemy.orm import relationship

from ruqqus.__main__ import Base, db

class Flag(Base):

    __tablename__="flags"

    id=Column(BigInteger, primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id"))
    post_id=Column(Integer, ForeignKey("submissions.id"))
    resolved=Column(Boolean, default=False)

    user=relationship("User", uselist=False)
    post=relationship("Submission", uselist=False)

    def resolve(self):

        self.resolved=True
        db.add(self)
        db.commit()
                      

class CommentFlag(Base):

    __tablename__="commentflags"

    id=Column(BigInteger, primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id"))
    comments_id=Column(Integer, ForeignKey("comments.id"))
    resolved=Column(Boolean, default=False)

    user=relationship("User", uselist=False)
    comment=relationship("Comment", uselist=False)

    def resolve(self):

        self.resolved=True
        db.add(self)
        db.commit()
