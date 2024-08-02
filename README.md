# CureMe Medical App's REST API

> Bascially, what the name says..

### [How tos](#how-to)

![CureMe Medical App's Logo](./app/static/cureme.png "CureMe Medical App's Logo")

## How to

### Host the API

1. Make sure, there's postgreSQL avaiable and running.
2. Populate `.env` taking reference from `.env.example` file, and make sure you provide empty DB (while, making sure the empty DB exists.)
3. Create a virtual environment within same directory, persoanlly I prefer `uv` for achieving it.
4. Install all the project dependencies listed on `requirements.txt` file via `uv pip install -r requirements.txt`
5. Finally, after everything above looks great. Run `run.sh` file, then the REST API must be available on port `4444`.

### Perform Unit Tests

1. Make soure you're the project virtual environment.
2. Either run `pytest` or `./test.sh` bash script.
