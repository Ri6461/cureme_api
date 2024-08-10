#!/bin/bash

function main() {
	if [[ ! -d ./.venv ]]; then
		pip install -U pip uv
		uv venv
		source .venv/bin/activate
		uv pip install -Ur requirements.txt
		deactivate
	fi
	source .venv/bin/activate
	uvicorn app.app:api --host 0.0.0.0 --port 8888;
	deactivate
	rm -rf __pycache__ app/__pycache__ app/routers/__pycache__ app/models/__pycache__ app/crud/__pycache__ app/schemas/__pycache__
	exit 0
}

if [[ -f ./.env ]]; then
	main
else
	echo "Please check .env.example, and make changes to it then save it as .env first."
	exit 1
fi

