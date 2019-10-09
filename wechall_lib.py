import requests
from beautifultable import BeautifulTable

#Get score for a player
def get_score(player):
    req_params ="username="+player
    resp = requests.get(url="https://www.wechall.net/wechall.php", params=req_params)
    response_text = resp.text
    return prettify_score(response_text)


def get_score_for_list_of_players(player_list):
    players = {}
    for player in player_list:
        players.update(get_score(player))
    return players


def prettify_score(response_text):
    res = response_text.split(" ")
    username = res[0]
    score = res[21]
    score = score[:-1]
    user_score = {username: int(score)}
    return user_score


#Get sites that players play
def get_sites(player):
    req_params = "username=!sites%20"+player
    resp = requests.get(url="https://www.wechall.net/wechall.php", params=req_params)
    return resp.text


def sort_player_touple_list(player_list):
    players = get_score_for_list_of_players(player_list)
    player_score_touple = [(k, v) for k, v in players.items()]
    player_score_touple.sort(key=lambda x: x[1], reverse=True)
    return player_score_touple


#Returns scoreboard for a list of wechall players
def build_scoreboard(player_list):
    player_scores=sort_player_touple_list(player_list)

    table = BeautifulTable()
    table.column_headers=["rank","username","score"]
    for i in range(len(player_scores)):
        user= player_scores[i][0]
        score= player_scores[i][1]
        table.append_row([i+1, user, score])
    return table

