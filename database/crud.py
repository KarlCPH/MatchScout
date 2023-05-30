from sqlalchemy.orm import Session
from . import models, schemas


def create_league(db: Session, league: models.League):
    db.add(league)
    db.commit()
    db.refresh(league)
    return league


def get_all_leagues(db: Session):
    leagues = db.query(models.League).all()
    return schemas.LeagueList(items=leagues)


def get_league_by_name(db: Session, league_name: str):
    return db.query(models.League).filter(models.League.name == league_name).first()


def get_teams_by_league(db: Session, league_id: int):
    return db.query(models.Team).filter(models.Team.league_id == league_id).all()


def create_fixture(db: Session, fixture: models.Fixture):
    db.add(fixture)
    db.commit()
    db.refresh(fixture)
    return fixture


def get_fixture_by_id(db: Session, fixture_id: int):
    return db.query(models.Fixture).filter(models.Fixture.id == fixture_id).first()


def get_all_fixtures(db: Session):
    fixtures = db.query(models.Fixture).all()
    return schemas.FixtureList(items=fixtures)
