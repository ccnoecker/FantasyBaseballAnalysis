DATA_OUTPUT_PATH = './data'

HITTER_FACTORS_MAPPING = {
    'Right': 'RHB',
    'Left': 'LHB',
    'Switch': 'All'
}
PITCHER_POSITIONS = ['SP', 'RP']

ALL_PLAYERS_FILENAME = 'all-players.csv'
FANTASYPROS_PLAYERS_FILENAME = 'fantasypros-player-rankings.csv'
OWNED_PLAYERS_FILENAME = 'owned-players.csv'
OWNED_PLAYERS_IDS_FILENAME = 'owned-players-with-ids.csv'
PARK_FACTORS_FILENAME = 'park-factors.csv'
TEAM_FILENAME = 'team.csv'

STATSAPI_BASE_URL = 'https://statsapi.mlb.com/api/v1'
STATSAPI_PEOPLE_SEARCH_PATH = f'{STATSAPI_BASE_URL}/people/search'

# Make sure statsapi.lookup_player() returns one single correct value for the lookup value added here
PLAYER_LOOKUP_VALUES = {
    'ADiaz': 'Alexis Díaz',
    'AGimenez2B': 'Andrés Giménez',
    'CEstevez': 'Carlos Estévez',
    'CRodon': 'Carlos Rodón',
    'CSanchez': 'Cristopher Sánchez',
    'EDiaz': 'Edwin Díaz',
    'EJimenez': 'Eloy Jiménez',
    'EPerez': 'Eury Pérez',
    'ERodriguez': 'Eduardo Rodriguez',
    'JBerrios': 'José Berríos',
    'JButto': 'José Buttó',
    'JDominguez': 'Jasson Domínguez',
    'JDMartinez': 'J.D. Martinez',
    'JMontgomery': 'Jordan Montgomery',
    'JRodriguez': 'Julio Rodríguez',
    'KManzardo': 'Kyle Manzardo',
    'MHarrisII': 'Michael Harris II',
    'NVelazquez': 'Nelson Velázquez',
    'PLopez': 'Pablo López',
    'RaSuarez': 'Ranger Suárez',
    'RLopez': 'Reynaldo López',
    'RStephenson': 'Robert William Stephenson',
    'THernandez': 'Teoscar Hernández',
    'VScottII': 'Victor Scott II'
}

TEAM_LOOKUP_VALUES = {
    'ARI': 'Diamondbacks',
    'CHW': 'White Sox',
    'LAA': 'Angels',
    'LAD': 'Dodgers',
    'SDP': 'Padres',
    'SFG': 'Giants'
}

# Can be looked up by running statsapi.get('sports', {})
SPORT_IDS = {
    'MLB': 1,
    'AAA': 11
}
