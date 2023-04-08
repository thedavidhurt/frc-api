import base64
import json
import requests
import creds

def main(username: str, api_key: str, season: int, event_code: str):
    base_url = "https://frc-api.firstinspires.org/v3.0"

    # Create credentials
    credential_string = f"{username}:{api_key}"
    credentials = base64.b64encode(bytes(credential_string, encoding='utf-8')).decode('utf-8')

    # Check API status
    response = check_api(base_url)
    if response.json()['status'] == 'normal':
        print("API up")
    else:
        print("API error:")
        print_json(response.text)
        return

    # Get and write matches
    response = get_match(base_url, credentials, season, event_code, "Qualification", None)
    json_formatted = format_json(response.text)
    with open('matches.json', 'w') as matches_file:
        matches_file.write(json_formatted)

    # Get and write scores
    response = get_scores(base_url, credentials, season, event_code, "Qualification", None)
    json_formatted = format_json(response.text)
    with open('scores.json', 'w') as scores_file:
        scores_file.write(json_formatted)
    # print_json(response.text)
    
    # response = get_season_info(base_url, credentials, season)
    # print_json(response.text)
        

def check_api(base_url):
    payload={}
    headers = {}

    print(base_url)
    response = requests.request("GET", base_url, headers=headers, data=payload)
    return response


def get_match(base_url, credentials, season, event_code, tournament_level, match_number):
    url = f"{base_url}/{season}/matches/{event_code}?tournamentLevel={tournament_level}"

    if match_number is not None:
        url = f"{url}&matchNumber={match_number}"

    payload={}
    headers = {
    'Authorization': f'Basic {credentials}',
    'If-Modified-Since': ''
    }

    print(url)
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    return response


def get_scores(base_url, credentials, season, event_code, tournament_level, match_number):
    url = f"{base_url}/{season}/scores/{event_code}/{tournament_level}"

    if match_number is not None:
        url = f"{url}&matchNumber={match_number}"

    payload={}
    headers = {
    'Authorization': f'Basic {credentials}',
    'If-Modified-Since': ''
    }

    print(url)
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    return response


def get_season_info(base_url, credentials, season):
    url = f"{base_url}/{season}"

    payload={}
    headers = {
    'Authorization': f'Basic {credentials}',
    'If-Modified-Since': ''
    }

    print(url)
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def print_json(json_text):
    print(format_json(json_text))


def format_json(json_text):
    return json.dumps(json.loads(json_text), indent=4)


if __name__ == "__main__":
    season = 2022
    event_code = "ALHU"
    username = creds.username
    api_key = creds.api_key
    main(username, api_key, season, event_code)


# "https://frc-api.firstinspires.org/v3.0/2020/matches/ARLI?tournamentLevel=Qualification"
# "https://frc-api.firstinspires.org/v3.0/2022/matches/alhu?tournamentLevel=Qualification"