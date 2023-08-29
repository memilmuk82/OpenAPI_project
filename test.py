import requests


url = 'http://ws.bus.go.kr/api/rest/pathinfo/getPathInfoByBusNSub'
params = dict()
params['serviceKey'] = '6mPvZ8EhqQCDjTJ94qLHvp1RhezITVhvdIZcoLmSuGzuE6pS3hkAFcbO3mKPGocTc5n06x1OwNl81g+U+idARQ=='
params['startX'] = '126.890001872801'
params['startY'] = '37.5757542035555'
params['endX'] = '127.04249040816'
params['endY'] = '37.5804217059895'
response = requests.get(url, params=params)

print(response.content)