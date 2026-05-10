import requests

url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': 'bef20e34acfdf00f9c7b56cfc6694183',
    'redirect_uri': 'https://localhost:3000',
    'code': 'e4PA8Dk8crSDO1o9codAneYpAVHtY1T7azASLleEvN5uu8XevCSsIQAAAAQKDSKZAAABnfLZp_F-jFVpBnvzXw' # 주의: 한 번 쓰면 폐기되니 바로 실행하세요!
}
response = requests.post(url, data=data)
print(response.json())