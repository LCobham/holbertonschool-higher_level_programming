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
    if length < 4:
        print("Incorrect number of args passed.")
        print("USAGE: ./8-model_state_fetch_first.py " +
              "username password database name")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1],
                            sys.argv[2],
                            sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()
    if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
