from re import findall
from os import mkdir, path

import pandas as pd
import statsapi
from requests import get

import constants


def clean_pl_export(pl_df:pd.DataFrame):
    # Remove empty rows and columns
    pl_df.dropna(how='all', inplace=True)
    pl_df.dropna(how='all', axis=1, inplace=True)

    # Promote the first row to headers
    new_header = pl_df.iloc[0] # grab the first row for the header
    pl_df = pl_df[1:] # take the data less the header row
    pl_df.columns = new_header # set the header row as the df header

    # Remove columns with irrelevant text and name the first column
    column_numbers = [x for x in range(pl_df.shape[1])][1:-3]  # list of columns' integer indices
    pl_df = pl_df.iloc[:, column_numbers] # return selected columns
    pl_df.rename(columns={pl_df.columns[0]: 'Team Position'}, inplace=True)

    # Remove bench coaches
    pl_df = pl_df.loc[pl_df['Team Position'] != 'BC']
    return pl_df


# TODO: Optimize to just get a list of all teams rather than requesting for every player
def get_team_id(team_search_value):
    team_search_value = team_search_value.upper()
    if team_search_value.upper() in constants.TEAM_LOOKUP_VALUES.keys():
        team_search_value = constants.TEAM_LOOKUP_VALUES[team_search_value]
    lookup_results = statsapi.lookup_team(team_search_value)
    if len(lookup_results) == 1:
        return lookup_results[0]['id']
    elif len(lookup_results) == 0:
        raise ValueError(f'Got no results from API for team search value {team_search_value}')
    else:
        raise ValueError(f'Got more than 1 result from API for team search value {team_search_value}: {lookup_results}')


def load_dataframe(filename) -> pd.DataFrame:
    return pd.read_csv(path.join(constants.DATA_OUTPUT_PATH, filename))


def lookup_player_stats(player_name):
    lookup_results = statsapi.lookup_player(player_name, season=2023)
    if len(lookup_results) != 1:
        raise ValueError(f'Did not receive one result from statsapi for player name {player_name}: {lookup_results}')
    player_id = lookup_results[0]['id']
    player_stats = statsapi.player_stat_data(player_id)
    return player_stats


def save_dataframe(dataframe, filename):
    if not path.exists(constants.DATA_OUTPUT_PATH):
        mkdir(constants.DATA_OUTPUT_PATH)
    dataframe.to_csv(path.join(constants.DATA_OUTPUT_PATH, filename), index=False)


def search_for_player(search_value):
    lookup_results = get(f'{constants.STATSAPI_PEOPLE_SEARCH_PATH}?names={search_value}&hydrate=currentTeam', timeout=30).json()['people']
    return next((player for player in lookup_results), None)
