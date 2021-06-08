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

    def test_func(self):
        specific_api_url = Consts.URLS['champion_v3']
        return self._request(specific_api_url)
