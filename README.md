# OpenAPI_project

서울시 버스 경로 API 호출 예제입니다. 인증값은 소스 코드에 저장하지 않고 `SEOUL_OPENAPI_SERVICE_KEY` 환경 변수로 전달합니다.

```bash
python -m pip install -r requirements.txt
export SEOUL_OPENAPI_SERVICE_KEY='<발급받은 값>'
python test.py
```

실제 인증값은 Git에 커밋하지 마세요.
