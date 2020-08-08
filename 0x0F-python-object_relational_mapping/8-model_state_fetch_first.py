#!/usr/bin/python3
"""[summary]
    """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    # HERE: no SQL query, only objects!
    session = Session()

    state1 = session.query(State).first()
    if state1 is None:
        print("Nothing")
    else:
        print("{}: {}".format(state1.id, state1.name))

    session.close()
