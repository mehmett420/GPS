import requests
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']  #ip_request.json() => {ip: '127.0.0.1'}
print(my_ip)
geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
print({'organization': geo_data['organization']})

# {
# "area_code": "0",
# "continent_code": "NA",
# "country": "United States",
# "country_code": "US",
# "country_code3": "USA",
# "ip": "198.975.33.4",
# "latitude": "37.7510",
# "longitude": "-97.8220",
# "organization": "AS15169 Google Inc.",
# "timezone": ""
# }
