#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from server.app import app, db
from server.models import Message

fake = Faker()

usernames = [fake.first_name() for i in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    with app.app_context():
        # Clear existing messages
        db.session.query(Message).delete()
        
        # Create new messages
        messages = []
        for i in range(20):
            message = Message(
                body=fake.sentence(),
                username=rc(usernames),
            )
            messages.append(message)

        db.session.add_all(messages)
        db.session.commit()
        print(f"✅ Successfully seeded {len(messages)} messages!")

if __name__ == '__main__':
    make_messages()