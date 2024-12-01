from cabi_api import CaBiApi
from config import config

print(
    CaBiApi.fetch_station_information(config['station_ids'])
)
