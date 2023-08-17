# we will import requests
import requests

# we will retrieve from a holiday-listing site all US holidays in 2023
url = 'https://date.nager.at/api/v2/publicholidays/2023/US'
r = requests.get(url)

# we'll unpack that JSON into Python dicts
# print(r.content)
# print(r.json())    # in requests, json is a method that turns JSON -> dicts!

# we'll iterate over those dicts and display them nicely
for one_holiday in r.json():
    print(one_holiday['date'])
    print(f'\t{one_holiday["localName"]}')
