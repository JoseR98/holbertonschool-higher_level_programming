#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import Base, City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    # Creates instance of the Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Creates session factory bound to that engine
    Session = sessionmaker(bind=engine)
    # Instance of Session class
    session = Session()

    california = State(name="California")
    california.cities = "San Francisco”
    session.add(california)
    session.commit()