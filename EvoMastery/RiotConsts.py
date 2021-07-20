import RiotAPIKey as APIKey

API_KEY = {
    'api_key': APIKey.API_KEY['api_key']
}

URLS = {
    'base': 'https://{region}.api.riotgames.com{specific_api_url}?api_key={api_key}',
    'summoner_v4_by_name': '/lol/summoner/v4/summoners/by-name/{summonerName}', # https://developer.riotgames.com/apis#summoner-v4
    'champion_mastery_v4_by_summoner' : '/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}' # https://developer.riotgames.com/apis#champion-mastery-v4
}

REGIONS = {
    'europe_west': 'euw1',
    'europe_north_and_east': 'eune1'
}
