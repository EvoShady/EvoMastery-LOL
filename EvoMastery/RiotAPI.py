import RiotConsts as Consts
import requests


class RiotAPI(object):

    def __init__(self, region=Consts.REGIONS['europe_west']):
        self.region = region

    def _request(self, specific_api_url):
        response = requests.get(
            Consts.URLS['base'].format(
                region=self.region,
                specific_api_url=specific_api_url,
                api_key=Consts.API_KEY['api_key'],
            )
        )
        return response.json()

    def summoner_v4_by_name(self, summoner_name):
        specific_api_url = Consts.URLS['summoner_v4_by_name'].format(
            summonerName=summoner_name,
        )
        return self._request(specific_api_url)
