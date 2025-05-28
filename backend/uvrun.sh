#!/bin/bash

# This script starts the backend server.
uv run uvicorn src.main:app --port 8080 --reload
