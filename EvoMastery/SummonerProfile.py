from RiotAPI import RiotAPI

SUMMONER_LEVEL = 'summonerLevel'
UNKNOWN = 'Unknown'


class SummonerProfile(object):

    def __init__(self, summoner_name, region):
        self.region = region
        self.summoner_name = summoner_name
        self.summoner_level = UNKNOWN
        self.__get_api_data_for_summoner_profile()

    def __set_summoner_level(self, summoner_level):
        self.summoner_level = summoner_level
        return self

    def __get_api_data_for_summoner_profile(self):
        riot_api = RiotAPI()
        summoner_by_name_response = riot_api.summoner_v4_by_name(self.summoner_name)
        self.__set_summoner_level(summoner_by_name_response[SUMMONER_LEVEL])
