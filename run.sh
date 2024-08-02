#!/bin/bash

function main() {
	source .venv/bin/activate
	uvicorn app.app:api --host 0.0.0.0 --port 8888 --reload;
	deactivate
	exit 0
}

if [[ -f ./.env ]]; then
	main
else
	echo "Please check .env.example, and make changes to it then save it as .env first."
	exit 1
fi

