import json
from bcolors import bcolors


def main():
    with open("matches.json") as matches_file:
        matches_json = json.load(matches_file)
        
    with open("scores.json") as scores_file:
        scores_json = json.load(scores_file)
    # print(matches_json['Matches'][0]['teams'])

    matches = matches_json['Matches']
    match_data = {}
    teams = set()
    for match in matches:
        match_num = match['matchNumber']
        match_teams = match['teams']
        for team in match_teams:
            team_station = team['station']
            team_num = team['teamNumber']
            teams.add(team_num)
            if team_station == 'Red1':
                r1 = team_num
            if team_station == 'Red2':
                r2 = team_num
            if team_station == 'Red3':
                r3 = team_num
            if team_station == 'Blue1':
                b1 = team_num
            if team_station == 'Blue2':
                b2 = team_num
            if team_station == 'Blue3':
                b3 = team_num
        match_data[match_num] = {'Red': [r1, r2, r3], 'Blue': [b1, b2, b3]}
        print(f"Match {match_num}: {bcolors.FAIL}{r1: >4} {r2: >4} {r3: >4} {bcolors.ENDC}| {bcolors.OKBLUE}{b1: >4} {b2: >4} {b3: >4}{bcolors.ENDC}")
    # print(match_data)
    # print(teams, len(teams))

    # team_stats = dict.fromkeys(teams, {'Taxis': 0, 'Low': 0, 'Mid': 0, 'High': 0, 'Traversal': 0})
    team_stats = {team: {'Taxis': 0, 'None': 0, 'Low': 0, 'Mid': 0, 'High': 0, 'Traversal': 0} for team in teams}

    scores = scores_json['MatchScores']
    print(len(scores))
    for match in scores:
        match_num = match['matchNumber']
        alliances = match['alliances']
        for alliance in alliances:
            alliance_color = alliance['alliance']
            for robot_num in range(3):
                if alliance[f'taxiRobot{robot_num + 1}'] == "Yes":
                    team_stats[match_data[match_num][alliance_color][robot_num]]['Taxis'] += 1
                hangar_state = alliance[f'endgameRobot{robot_num + 1}']
                team_stats[match_data[match_num][alliance_color][robot_num]][hangar_state] += 1

    # print(team_stats)
    for team, stats in team_stats.items():
        print(f"{team: >4}: Taxis: {stats['Taxis']: >2}, None: {stats['None']: >2}, Low: {stats['Low']: >2}, Mid: {stats['Mid']: >2}, High: {stats['High']: >2}, Traversal: {stats['Traversal']: >2}")

    with open('stats.csv', 'w') as stats_file:
        stats_file.write("Team, Taxis, None, Low, Mid, High, Traversal\n")
        for team, stats in team_stats.items():
            stats_file.write(f"{team}, {stats['Taxis']}, {stats['None']}, {stats['Low']}, {stats['Mid']}, {stats['High']}, {stats['Traversal']}\n")  

if __name__ == "__main__":
    main()