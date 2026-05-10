import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_today_bible():
    today_str = datetime.now().strftime("%Y-%m-%d")
    # 주소 뒤에 파라미터를 명확히 붙입니다.
    url = f"https://sum.su.or.kr:8888/bible/today"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
    }
    
    try:
        # 세션을 사용하여 접속 (쿠키 문제 해결 가능성)
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8' 
        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. 제목 및 범위
        title = soup.select_one('#bible_text').get_text(strip=True) if soup.select_one('#bible_text') else "제목 없음"
        bible_range = soup.select_one('#bibleinfo_box').get_text(strip=True) if soup.select_one('#bibleinfo_box') else "범위 없음"
        
        # 2. 본문 추출 (가장 강력한 셀렉터 사용)
        body_list = []
        
        # 방법 A: li 태그 내부의 텍스트들을 직접 조합
        items = soup.find_all('li', id=lambda x: x and x.startswith('li_'))
        
        if not items:
            # 방법 B: 클래스명으로 직접 접근
            items = soup.select('ul#body_list > li')

        for li in items:
            # 구절 번호와 텍스트를 각각 찾음
            v_num = li.find(class_='bible_verse')
            v_text = li.find(class_='bible_text')
            
            if v_num and v_text:
                num = v_num.get_text(strip=True)
                content = v_text.get_text(strip=True)
                # 제목과 겹치는지 확인 후 추가 (제목이 본문에 중복 포함되는 것 방지)
                if content != title:
                    body_list.append(f"{num} {content}")
        
        body_text = "\n".join(body_list)

        # 3. 해설 추출
        summary = soup.select_one('#daily_caption').get_text(strip=True) if soup.select_one('#daily_caption') else ""
        content = soup.select_one('#daily_content').get_text(strip=True) if soup.select_one('#daily_content') else ""
        explanation = f"{summary}\n\n{content}".strip() or "해설을 가져오지 못했습니다."

        return {
            "title": title,
            "range": bible_range,
            "body": body_text,
            "explanation": explanation
        }

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    data = get_today_bible()
    
    if "error" not in data:
        # 본문이 비어있을 경우 원본 HTML 일부를 출력해서 디버깅
        if not data['body']:
            print("❌ 본문 데이터를 찾을 수 없습니다. 사이트가 로딩되지 않았을 수 있습니다.")
        else:
            final_output = (
                f"📖 성경 범위: {data['range']}\n"
                f"📌 소제목: {data['title']}\n"
                f"{'='*40}\n"
                f"📝 본문 내용:\n{data['body']}\n"
                f"{'='*40}\n"
                f"💡 해설 및 묵상:\n{data['explanation']}"
            )
            print(final_output)
    else:
        print(f"에러 발생: {data['error']}")