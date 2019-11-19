from sqlalchemy import *
from ruqqus.__main__ import Base, db, cache

from .submission import *
from .comment import *
from .user import *

class Flag(Base):

    __tablename__="flags"

    post_id=Column(Integer, ForeignKey(Submission.id))
    user_id=Column(Integer, ForeignKey(User.id))    

    def __repr__(self):

        return f"<Flag(id={self.id})>"
