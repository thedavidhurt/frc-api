# frc-api
Read and process data from The Blue Alliance API

## Setup
### Python environment setup
1. Open a Powershell terminal in frc-api
2. python -m venv .venv
3. .venv/Scripts/Activate.ps1
4. python -m pip install -r requirements.txt

### API authentication setup
1. Create an account on https://www.thebluealliance.com/account
2. Generate a Read API Key
3. Copy creds_template.py to creds.py
4. Insert username and password into creds.py

## Run
1. Open a Powershell terminal in frc-api
2. .venv/Scripts/Activate.ps1
3. python frc-api.py
4. python process_matches_YYYY.py
