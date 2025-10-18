#!/bin/bash
# Install system dependencies
apt-get update
apt-get install -y libpq-dev python3-dev gcc

# Install Python dependencies
pip install -r backend/requirements.txt
