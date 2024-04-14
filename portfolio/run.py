import uuid
from datetime import datetime

class Base:
    id = uuid.uuid4()
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __repr__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

class User(Base):
    name = None
    email = ""
    phone_number = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


b = User(name = 'Akin', email='akin@gmail.com')
print(b)
User.name = b.name
print(User.name)
print(b.email)
print(User.id)