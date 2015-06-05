## Installation

Python 3.4+

```bash
pip install -r requirements.txt
```


## Run

```bash
# debug
python server.py

# listen to all interfaces
python -m bottle -b 0.0.0.0:8888 server:app
```


## Play

Visit `/test/` to init database.

`/question/` list all available questions.

`/gameadmin/` start a new game.

`/play/` for player to enter the game.

`/judge/` show the status for the current game. Auto reload for every 2 seconds.
