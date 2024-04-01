import pandas as pd
import statsapi
from os import mkdir, path

import constants


def lookup_team_id(team_name):
    lookup_results = statsapi.lookup_team(team_name)
    if len(lookup_results) != 1:
        raise ValueError(f'Did not receive one result from statsapi for team name {team_name}: {lookup_results}')
    return lookup_results[0]['id']


def lookup_player_stats(player_name):
    lookup_results = statsapi.lookup_player(player_name, season=2023)
    if len(lookup_results) != 1:
        raise ValueError(f'Did not receive one result from statsapi for player name {player_name}: {lookup_results}')
    player_id = lookup_results[0]['id']
    player_stats = statsapi.player_stat_data(player_id)
    return player_stats


def load_dataframe(filename) -> pd.DataFrame:
    return pd.read_csv(path.join(constants.DATA_OUTPUT_PATH, filename))


def save_dataframe(dataframe, filename):
    if not path.exists(constants.DATA_OUTPUT_PATH):
        mkdir(constants.DATA_OUTPUT_PATH)
    dataframe.to_csv(path.join(constants.DATA_OUTPUT_PATH, filename), index=False)
