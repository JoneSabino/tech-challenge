from datetime import timedelta, datetime
import var
import requests
import csv


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
        date_time, exact_time = str.split(raw_time, ' ')
        h_time, ms = str.split(exact_time, '.')
        h, m, s = str.split(h_time, ':')
        t = h_time
        # lt = time.localtime()

        values = {
            "seq": validated_ledger['seq'],
            "current_time": t,  # To use cur. local time, uncomment the 'lt' var and use time.strftime("%H:%M:%S", lt)
            # "exact_time": datetime.strptime(exact_time, '%H:%M:%S.%f').time(),
            "h": float(h),
            "m": float(m),
            "s": float(s),
            "ms": float(ms)
        }
        return values

    @staticmethod
    def calculate_time(values, count):
        zero = timedelta(hours=0, minutes=0, seconds=0)
        sum_times = timedelta(hours=0, minutes=0, seconds=0)

        if count < 1:
            var.tmp_time = timedelta(hours=float(values['h']), minutes=float(values['m']),
                                     seconds=float(values['s']), microseconds=float(values['ms']))
        else:
            current_time = timedelta(hours=float(values['h']), minutes=float(values['m']),
                                     seconds=float(values['s']), microseconds=float(values['ms']))

            var.delta = current_time - var.tmp_time

            if var.delta != zero:
                var.exec_times.append(var.delta)

            var.tmp_time = current_time

            if count == var.MAX - 1:
                var.exec_times.sort()
                print('Max time: ', var.exec_times[-1])
                print('Min time: ', var.exec_times[0])
                for x in var.exec_times:
                    sum_times += x
                print('Avg time: ', sum_times / len(var.exec_times))

    @staticmethod
    def write_csv(values):
        """
        Writes the dict values in a .csv file

        :param values: A dict containing sequence number and current local time
        """
        with open('resource.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([values['seq'], values['current_time']])
