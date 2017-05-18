"""
takovata-access.log
"""

from urllib.parse import urlparse
import re
import operator


COLUMN_RESP_T = -2
COLUMN_URL = 4

file_name = input()

url_resp_time_dict = {}
with open(file_name, "r", encoding = "utf-8") as f:
    for row in f:
        row = row.split(" ")
        url = urlparse(row[COLUMN_URL])
        url = url[2]
        url = url[5:-1]
        if not url.endswith("/"):
            url += "/"
        # print(url)
        resp_t = row[COLUMN_RESP_T]
        resp_t = float(resp_t[8:-1])
        # print(resp_t)
        # print(url[-4:-2])
        if url[-3:-1] == "ws":
            continue
        else:
            if url in url_resp_time_dict.keys():
                url_resp_time_dict[url].append(resp_t)
            else:
                url_resp_time_dict[url] = [resp_t]
sorted_url_time_list = sorted(url_resp_time_dict.items(), key=operator.itemgetter(1))[::-1]
print(sorted_url_time_list[0][0])
print("{:.3f}".format(sum(sorted_url_time_list[0][1]) / len(sorted_url_time_list[0][1])))



