#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    # empty db first
    with session.begin():
        session.query(Game).delete()
    # instantiate 2 game objects
        game1 = Game(title="Crash Bandicot", genre = "fantasy", platform = "nintendo", price = 12)
        game2 = Game(title="Tomb Raider", genre = "fantasy", platform = "nintendo", price = 12)
        # add them all to the session
        session.bulk_save_objects([game1, game2], return_defaults=True)
    # session.add_all([game1, game2])

    # commit the session
    # session.commit()
    print(session.query(Game).count())
    print(session.query(Game).first())
    print(session.query(Game).order_by(Game.id.desc()).first())
