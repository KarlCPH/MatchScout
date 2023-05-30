# from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import FastAPI
import requests
from database import crud
from database.models import League, Fixture
from database import SessionLocal

# from schemas import FixtureList

app = FastAPI()


@app.get("/fetch-and-save-data")
async def fetch_and_save_data():
    url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

    headers = {
        'X-RapidAPI-Key': "e6d9bef1dbmsh4c9d3d9453e2dd0p1dc980jsn89e8f3761f19",
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    # League IDs for La Liga, Premier League, and Serie A
    league_ids = [140, 39, 135]

    # Create a database session
    db = SessionLocal()

    for league_id in league_ids:
        query_params = {
            'id': league_id
        }

        response = requests.get(url, headers=headers, params=query_params)
        data = response.json()

        # Process the data and save to the database
        league_data = data['response'][0]
        league = League(
            id=league_data['league']['id'],
            name=league_data['league']['name'],
            country=league_data['country']['name']
        )
        crud.create_league(db, league)  # Pass the db argument

    # Close the database session
    db.close()

    return {"message": "Data fetched and saved successfully."}


@app.get("/fetch-and-save-fixtures")
async def fetch_and_save_fixtures():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups"

    headers = {
        'X-RapidAPI-Key': "e6d9bef1dbmsh4c9d3d9453e2dd0p1dc980jsn89e8f3761f19",
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # Create a database session
    db = SessionLocal()

    for fixture_data in data['response']:
        fixture = Fixture(
            id=fixture_data['fixture']['id'],
            team_name=fixture_data['team']['name'],
            team_logo=fixture_data['team']['logo'],
            team_colors=fixture_data['team']['colors'],
            formation=fixture_data['formation'],
            start_xi=fixture_data['startXI'],
            substitutes=fixture_data['substitutes'],
            coach_id=fixture_data['coach']['id'],
            coach_name=fixture_data['coach']['name'],
            coach_photo=fixture_data['coach']['photo']
        )
        crud.create_fixture(db, fixture)  # Pass the db argument

    # Close the database session
    db.close()

    return {"message": "Fixtures fetched and saved successfully."}


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": exc.errors()})
