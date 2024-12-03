from cabi_api import CaBiApi
from config import config


def get_station_ids(stations): return [station['id']
                                       for station in stations]


print(
    CaBiApi.fetch_station_information(get_station_ids(config['stations'])))
