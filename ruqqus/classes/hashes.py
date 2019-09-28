import time
from sqlalchemy import *
from ruqqus.__main__ import Base, db


class Hashes(Base):
    __tablename__ = "hashes"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    hash = Column(String, default=None)
    created_utc = Column(Integer, default=None)

    def __init__(self, *args, **kwargs):
        if "created_utc" not in kwargs:
            kwargs["created_utc"] = int(time.time())

        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Hashes(id={self.id}, uid={self.user_id}, hash={self.hash})>"