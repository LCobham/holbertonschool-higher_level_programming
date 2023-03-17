#!/usr/bin/python3
"""
    Print all cities from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    length = len(sys.argv)
    if length < 4:
        print("Incorrect number of args passed.")
        print("USAGE: ./13-model_state_delete_a.py" +
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

    data = session.query(State, City).filter(
                  State.id == City.state_id).order_by(
                    City.id
                  )

    for point in data:
        print(f"{point[0].name}: ({point[1].id}) {point[1].name}")
