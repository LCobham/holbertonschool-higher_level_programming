#!/usr/bin/python3
"""
   Add a state to the states table in hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    length = len(sys.argv)
    if length < 4:
        print("Incorrect number of args passed.")
        print("USAGE: ./12-model_state_update_id_2.py" +
              "username password database db_name")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1],
                            sys.argv[2],
                            sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    to_update = session.query(State).filter(
                State.id == 2).update(
                    {"name": "New Mexico"})
    session.commit()
