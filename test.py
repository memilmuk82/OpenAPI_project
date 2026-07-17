import os

import requests


API_URL = 'https://ws.bus.go.kr/api/rest/pathinfo/getPathInfoByBusNSub'


def get_service_key():
    service_key = os.environ.get('SEOUL_OPENAPI_SERVICE_KEY')
    if not service_key:
        raise RuntimeError('SEOUL_OPENAPI_SERVICE_KEY 환경 변수를 설정해야 합니다.')
    return service_key


def request_path(service_key, session=requests):
    params = {
        'serviceKey': service_key,
        'startX': '126.890001872801',
        'startY': '37.5757542035555',
        'endX': '127.04249040816',
        'endY': '37.5804217059895',
    }
    response = session.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    return response


def main():
    response = request_path(get_service_key())
    print(response.content)


if __name__ == '__main__':
    try:
        main()
    except RuntimeError as error:
        raise SystemExit(str(error)) from error
