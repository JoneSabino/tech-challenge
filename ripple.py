import requests
import csv
import time


class Ripple:
    @staticmethod
    def get_server_info():
        """
        Makes the API call to ripple server

        :rtype: dict
        :return: The full response JSON
        """
        body = {
            "method": "server_info",
            "params": [{}]
        }

        r = requests.post('http://s1.ripple.com:51234/', json=body)
        response = r.json()

        return response

    @staticmethod
    def get_values(response):
        """
        Extracts the relevant data of the response parameter

        :rtype: dict
        :param response: JSON API response
        :return: A dict with the sequence and local current time
        """
        info = response['result']['info']
        validated_ledger = info['validated_ledger']
        raw_time = info['time']
        time_tmp = str.split(raw_time, ' ')
        time_tmp = str.split(time_tmp[1], '.')
        t = time_tmp[0]
        # lt = time.localtime()

        values = {
            "seq": validated_ledger['seq'],
            "current_time": t  # To use cur. local time, uncomment the 'lt' var and use time.strftime("%H:%M:%S", lt)
        }
        return values

    @staticmethod
    def write_csv(values):
        """
        Writes the dict values in a .csv file

        :param values: A dict containing sequence number and current local time
        """
        with open('resource.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([values['seq'], values['current_time']])
