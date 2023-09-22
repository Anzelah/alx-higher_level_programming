#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://%s:%s@localhost:3306/%s'
                           % (username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name == state_name)\
        .order_by(State.id).all()

    if results:
        print("{}" .format(results[0].id))
    else:
        print("Not found")
