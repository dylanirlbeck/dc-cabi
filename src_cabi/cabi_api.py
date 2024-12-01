# import board
# from adafruit_matrixportal.network import Network
import requests
from config import config

# Keeping a global reference for thisi
# _network = Network(status_neopixel=board.NEOPIXEL)


class CaBiApi:
    def fetch_station_information(station_ids: [str]) -> [dict]:
        return CaBiApi._fetch_station_information(station_ids)

    def _fetch_station_information(station_ids: [str]) -> [dict]:
        try:
            api_url = config['cabi_api_url']
            station_information_raw = CaBiApi._network_fetch(
                api_url)  # returns a json
            station_information_cleaned = CaBiApi._filter_station_information_by_id(
                station_information_raw, station_ids)
            return list(map(
                lambda station: {'num_classic':
                                 str(int(station['num_bikes_available']) -
                                     int(station['num_ebikes_available'])),
                                 'num_electric': station['num_ebikes_available']},
                station_information_cleaned
            ))

        except RuntimeError:
            pass

    # TODO to replace with adafruit_matrixportal.network.fetch method
    def _network_fetch(api_url: str) -> [dict]:
        # return _network.fetch(api_url).json()
        response = requests.get(api_url)
        return response.json()

    def _filter_station_information_by_id(data: dict, target_station_ids: [str]) -> [dict]:
        """
        Filter stations by matching station IDs using a lambda function.

        :param data: JSON data containing stations
        :param target_station_ids: List of station IDs to filter
        :return: List of matching station dictionaries
        """
        return list(filter(
            lambda station: station['station_id'] in target_station_ids,
            data['data']['stations']
        ))
