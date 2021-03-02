import http.client
import json
import requests
import sys, os
from datetime import datetime, timedelta

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
url = "https://www.coworker.com/ajax/spaces"

def main():
	resp1 = []
	for_loop_max = get_pages()
	for x in range(for_loop_max):
		payload='city_id=0&country_id=81&filter_duration_metric_types=all&filter_meeting_room_capacity=0&filter_price_end=600&filter_price_start=0&filter_resource_types=all&network_code=&page_num='+ str(x) + '&view_mode=list'
		headers = {
		  'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
		  'Accept': '*/*',
		  'X-Requested-With': 'XMLHttpRequest',
		  'sec-ch-ua-mobile': '?0',
		  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
		  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		y = json.loads(response.text)
		resp1 = resp1 + y["mapSpaces"]
	prettyPrintJson = json.dumps(resp1, indent=4, sort_keys=True)
	print(prettyPrintJson)
	filename1 = datetime.now().strftime("%Y%m%d-%H%M%S")
	outF = open(os.path.join(__location__, filename1 + '.json'), "w")
	outF.writelines(prettyPrintJson)
	outF.close()


def get_pages():
	payload='city_id=0&country_id=81&filter_duration_metric_types=all&filter_meeting_room_capacity=0&filter_price_end=600&filter_price_start=0&filter_resource_types=all&network_code=&page_num=*&view_mode=list'
	headers = {
	  'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
	  'Accept': '*/*',
	  'X-Requested-With': 'XMLHttpRequest',
	  'sec-ch-ua-mobile': '?0',
	  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
	  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	y = json.loads(response.text)
	max_numPages = int(y["numPages"])
	return max_numPages

main()