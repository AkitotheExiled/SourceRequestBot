
from sqlalchemy import Column, String, DateTime,create_engine, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import timezone, timedelta, datetime
Base = declarative_base()
import static

class Database:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{static.DATABASE_NAME}")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)
        self.commit()


    def commit(self):
        self.session.commit()

    def close(self):
        self.engine.dispose()



class Posts(Base):
    __tablename__ = 'posts'

    id = Column(String(30), primary_key=True)
    comment_id = Column(String(30), unique=True)
    author = Column(String())
    date_check = Column(DateTime())
    is_replied = Column(Boolean(), default=False)

    def __init__(self, id, author, date_check, comment_id, is_replied=False):
        self.id = id
        self.author = author
        self.date_check = date_check
        self.is_replied = is_replied
        self.comment_id = comment_id



