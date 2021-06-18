import requests
import RiotConsts as Consts
from RiotAPI import RiotAPI


class SummonerProfile(object):

    def __init__(self, summoner_name, region):
        self.region = region
        self.summoner_name = summoner_name
        self.summoner_level = 'Unknown'

    def _set_summoner_level(self, summoner_level):
        self.summoner_level = summoner_level
        return self

    def get_summoner_encrypted_id_by_name(self):
        api = RiotAPI()
        summoner_by_name_response = api.summoner_v4_by_name(self.summoner_name)
        summoner_encrypted_id = summoner_by_name_response['id']
        self._set_summoner_level(summoner_by_name_response['summonerLevel'])
        return summoner_encrypted_id
