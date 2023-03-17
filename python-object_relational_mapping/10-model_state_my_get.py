#!/usr/bin/python3
"""
   List all states from the states table in hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    length = len(sys.argv)
    if length < 5:
        print("Incorrect number of args passed.")
        print("USAGE: ./10-model_state_my_get.py " +
              "username password database db_name state")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1],
                            sys.argv[2],
                            sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == sys.argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
