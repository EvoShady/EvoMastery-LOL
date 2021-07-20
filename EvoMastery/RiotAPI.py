import RiotConsts as Consts
import requests

DEFAULT_REGION = 'europe_west'
BASEURL = 'base'
API_KEY = 'api_key'
SUMMONER_V4_BY_NAME = 'summoner_v4_by_name'
ID = 'id'
CHAMPION_MASTERY_V4_BY_SUMMONER = 'champion_mastery_v4_by_summoner'


class RiotAPI(object):

    def __init__(self, region=Consts.REGIONS[DEFAULT_REGION]):
        self.region = region

    def _request(self, specific_api_url):
        response = requests.get(
            Consts.URLS[BASEURL].format(
                region=self.region,
                specific_api_url=specific_api_url,
                api_key=Consts.API_KEY[API_KEY],
            )
        )
        return response.json()

    def summoner_v4_by_name(self, summoner_name):
        specific_api_url = Consts.URLS[SUMMONER_V4_BY_NAME].format(
            summonerName=summoner_name,
        )
        return self._request(specific_api_url)

    def champion_mastery_v4_by_summoner(self, summoner_name):
        encrypted_summoner_id = self.summoner_v4_by_name(summoner_name)
        specific_api_url = Consts.URLS[CHAMPION_MASTERY_V4_BY_SUMMONER].format(
            encryptedSummonerId=encrypted_summoner_id[ID]
        )
        return self._request(specific_api_url)
