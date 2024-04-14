#!/usr/bin/python3
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from portfolio.models import *

engine = create_engine('sqlite:///portfolio.db', echo=True)

Base = declarative_base()

from portfolio.database import session, init_db


us = session.query(User).all()
#print(u)
phone_number = "766567666"
user_details = []
for u in us:
    if u.phone_number == phone_number:
        user_details.append(u.name)
        user_details.append(u.id)
        user_details.append(u.longitude)
print(user_details)
#print(dir(u))
print(type(u))
#print(help(u))



# Optionally, add some data to the table
Session = sessionmaker(bind=engine)
session = Session()

from models import Message
# Example: Adding a message to the 'messages' table
new_message = Message("Happy Birthday!", "Akin")
session.add(new_message)
session.commit()

# Close the session
session.close()

'''

import requests
url = "http://127.0.0.1:5000/api/v1/verify/code"
data = {
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZV9udW1iZXIiOiIwNzA2NTcyNzQxMyIsIm90cCI6NDE3OTA3LCJleHAiOjE3MTMwMDg3MzV9.uxXhzMPvvCgdrojjS_cwaxWwdEIM-ydFrU1dLSkva4g',
    'otp': 417907
}

headers = {
    'Content-Type': 'application/json',
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print("Response:", response.text,
          "responseCode: ",  response.status_code
          )