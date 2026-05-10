import requests

# 1. 카카오 디벨로퍼스에서 설정한 정보
client_id = "bef20e34acfdf00f9c7b56cfc6694183"  # 여기에 발급받은 REST API 키 입력
redirect_uri = "https://localhost:3000" # 설정한 Redirect URI 입력
auth_code = "방금_브라우저에서_받은_인가_코드" # 브라우저 주소창에서 복사한 코드 입력
# https://kauth.kakao.com/oauth/authorize?client_id=bef20e34acfdf00f9c7b56cfc6694183&redirect_uri=https://localhost:3000&response_type=code&scope=talk_message
# 위 링크에 접속해서 code= 뒷부분 복사해서 auth code에 삽입

# 2. 토큰 요청
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "authorization_code",
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "code": auth_code,
}

response = requests.post(url, data=data)
tokens = response.json()

# 3. 결과 출력
if "access_token" in tokens:
    print("✅ 토큰 발급 성공!")
    print(f"ACCESS_TOKEN: {tokens['access_token']}")
    print(f"REFRESH_TOKEN: {tokens['refresh_token']}")  # <--- 이 값을 GitHub Secrets에 등록!
else:
    print("❌ 발급 실패:")
    print(tokens)