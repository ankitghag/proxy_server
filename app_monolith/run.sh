#!/bin/bash
export APP_PORT="$1"
if [ "$2" = "main_app" ]; then
    uv run uvicorn main_app:app --reload --port "$1"
else
    uv run uvicorn main:app --reload --port "$1"
fi
