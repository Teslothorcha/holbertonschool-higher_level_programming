#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
"""
create
class to relate with
database
"""
if __name__ == "__main__":
    try:
        if sys.argv[3]:
            engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(sys.argv[1], sys.argv[2], sys.argv[3]))

            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()

            que = session.query(State, City).filter(State.id == City.state_id)\
                                            .order_by(City.id).all()

            for a, b in que:
                print("{}: ({}) {}".format(a.name, b.id, b.name))
            session.close()
    except:
        pass
