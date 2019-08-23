from flask import render_template
from sqlalchemy import *
from sqlalchemy.orm import relationship

from ruqqus.__main__ import Base, db

class Badge(Base):

    __tablename__="badge_list"

    id = Column(BigInteger, primary_key=True)
    name=Column(String(64))
    description=Column(String(64))
    icon=Column(String(64))

    @property
    def path(self):

        return f"/assets/images/badges/{self.icon}"
    
