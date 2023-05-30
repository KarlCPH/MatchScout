#from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.orm import declarative_base, sessionmaker

# create engine
#engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/dbname")

# create session
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()


# define model
#class Leagues(Base):
#    __tablename__ = "leagues"
#
#    id = Column(Integer, primary_key=True, index=True)
#    name = Column(String)
#    country = Column(String)


# create tables
#Base.metadata.create_all(bind=engine)
