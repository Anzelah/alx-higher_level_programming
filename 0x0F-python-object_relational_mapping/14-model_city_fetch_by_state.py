#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
#from sqlalchemy.orm import relationship

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
#    State.cities = relationship("City", back_populates="states")
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()
    for r in results:
        print("{}: ({}) {}" .format(r[0].name, r[1].id, r[1].name))
