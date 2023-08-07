# Dyntos
Discord bot for the Kid Icarus: Uprising Multiplayer.

## Features
The bot has limited features, and the use case is pretty much exclusively limited to our discord server, but here they are:

| Command | Description                                                                 |
| ------- | --------------------------------------------------------------------------- |
| calc    | Calculates the value of a weapon.                                           |
| fusion  | Calculates the fusion result of two weapons.                                |
| search  | Searches for how a weapon can be used in a fusion, depending on parameters. |
| score   | Adds a score for a chapter.                                                 |
| chapter | Displays a chapter, its drops, and the top five member scores.              |
| slap    | Displays an image of a member being slapped.                                |
| uwuify  | Makes text all funky 🤨                                                     |

## Installation
If for whatever reason you're wanting to run the bot yourself, there are a few things you'll need first.

You'll need to install [Python](https://www.python.org/downloads/) and include `pip` in your installation. Running the following commands will install all the dependencies.
```
git clone https://github.com/SchuyBlu/dyntos.git
cd ./dyntos
pip install -r requirements.txt
```
You'll also need to create a [discord application](https://discord.com/developers/applications) and give it the `bot`, `applications.commands`, and `Administrator` scopes. You'll need to generate a token for the bot and place it in a file named `.env` at the root of the project in this format:
```
TOKEN=<your-token-here>
```
With that, you can call `run.sh` if you're on some flavor of UNIX, or `python main.py` if you're on Windows.
