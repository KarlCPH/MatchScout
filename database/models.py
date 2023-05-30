from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()


class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country = Column(String)


class Fixture(Base):
    __tablename__ = "fixtures"

    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, nullable=False)
    team_logo = Column(String)
    team_colors = Column(JSON)
    formation = Column(String)
    start_xi = Column(JSON)
    substitutes = Column(JSON)
    coach_id = Column(Integer)
    coach_name = Column(String)
    coach_photo = Column(String)

    def __repr__(self):
        return f"<Fixture(id={self.id}, team_name='{self.team_name}', formation='{self.formation}')>"
