
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args,**kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __repr__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        from portfolio.database import session
        session.add(self)
        session.commit()

    def delete(self):
        from portfolio.database import session
        session.delete(self)
        session.commit()

    @classmethod
    def all(cls):
        from portfolio.database import session
        return session.query(cls).all()

    @classmethod
    def get(cls, id):
        from portfolio.database import session
        return session.query(cls).get(id)

    @classmethod
    def filter(cls, **kwargs):
        from portfolio.database import session
        return session.query(cls).filter_by(**kwargs).all()

    @classmethod
    def first(cls, **kwargs):
        from portfolio.database import session
        return session.query(cls).filter_by(**kwargs).first()

    @classmethod
    def last(cls, **kwargs):
        from portfolio.database import session
        return session.query(cls).filter_by(**kwargs).last()

    @classmethod
    def count(cls):
        from portfolio.database import session
        return session.query(cls).count()

    @classmethod
    def delete_all(cls):
        from portfolio.database import session
        session.query(cls).delete()
        session.commit()

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance.save()
        return instance

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

class Message(BaseModel, Base):
    __tablename__ = 'messages'
    #id = Column(Integer, primary_key=True)
    message = Column(String(1000), nullable=False)
    sender = Column(String(100), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize message"""
        super().__init__(*args, **kwargs)
        

        

class SecretMessage(BaseModel, Base):
    __tablename__ = 'secretmessage'
    message = Column(String(1000), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize message"""
        super().__init__(*args, **kwargs)
