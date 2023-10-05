from sqlalchemy import String, DateTime, Integer, Boolean
from sqlalchemy import Column, ForeignKey
from datetime import datetime

class JWTInfo():
    __tablename__ = 'jwt_info'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(UserInfo.id))
    jwt_token = Column(String, nullable=False)
    record_time = Column(DateTime, default=datetime.now())
    disable = Column(Boolean, default=False)
    disable_time = Column(DateTime, nullable=True)

