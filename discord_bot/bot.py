import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from database import crud
import asyncio
from database import SessionLocal

# Load environment variables from .env file
load_dotenv()

# Retrieve the value of an environment variable
token = os.environ.get("DISCORD_TOKEN")

# Create a new bot instance with intents
intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


# Event handlers
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


# Command definition
@bot.command()
async def premier_league_teams(ctx):
    # Create a database session
    db = SessionLocal()

    # Fetch all the teams in the Premier League from the database
    league = crud.get_league_by_name(db, "Premier League")
    teams = crud.get_teams_by_league(db, league.id)

    # Format the team names
    team_names = "\n".join([team.name for team in teams])

    # Send the team names as a response in Discord
    await ctx.send(f"Teams in the Premier League:\n{team_names}")

    # Close the database session
    db.close()


@bot.command()
async def leagues(ctx):
    leagues = crud.get_all_leagues()  # Implement the corresponding CRUD function

    response = "Leagues:\n"
    for league in leagues:
        response += f"{league.name} - {league.country}\n"

    await ctx.send(response)


@bot.command()
async def fixtures(ctx):
    db = SessionLocal()
    fixtures = crud.get_all_fixtures(db)

    if fixtures:
        for fixture in fixtures.items:
            # Format the fixture information as desired
            message = f"Fixture ID: {fixture.id}\nTeam: {fixture.team_name}\nFormation: {fixture.formation}"
            await ctx.send(message)
    else:
        await ctx.send("No fixtures found.")

    db.close()


# Function to run the bot
async def start_bot():
    await bot.start("MTA5MzUxNjE1NTE2MDkwMzcwMg.GlQUsT.g2NIwvrsAvI7h6WoH11i2x-YuQvbCriYy2N96U")


def run_bot():
    asyncio.run(start_bot())
