import requests # type: ignore

headers = {
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1IiwiZXhwIjoxNzc1MTUzMDc1fQ.KDYARgyWf_IW35ihi0DO9Km47namkJSv1Xhv-Eym2FE"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers= headers)

print(requisicao)
print(requisicao.json())