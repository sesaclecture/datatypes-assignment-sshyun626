# ==========================
# assignment_drama_template.py (학생용 템플릿)
# 조건: 함수/조건문/반복문 금지. 변수 선언과 input(), print()만 사용.
# ==========================

drama1 = {
    "제목": "도깨비",          
    "장르": "판타지",           
    "주제": "불멸의 삶을 끝내기 위해 인간 신부가 필요한 도깨비, 그와 기묘한 동거를 시작한 기억상실증 저승사자 그런 그들 앞에 '도깨비 신부'라 주장하는 '죽었어야 할 운명'의 소녀가 나타나며 벌어지는 신비로운 낭만 설화",          
    "방영기간": "2016-12-02 ~ 2017-01-21",       
    "배우": ["공유", "김고은", "이동욱"],           
    "명대사": "\"누구의 인생이건 신이 머물다 가는 순간이 있다\""           
}

drama2 = {
    "제목": "시그널",            
    "장르": "스릴러",           
    "주제": "간.절.함.이..보.내.온..신.호 우리의 시간은 이어져 있다. 과거로부터 걸려온 간절한 신호로 연결된 현재와 과거의 형사들이 오래된 미제 사건들을 다시 파헤친다!",           
    "배우": ["이제훈", "김혜수", "조진웅"],           
    "명대사": "우리는 서로의 기억 속에 살아가고 있다."          
}

new_title = input("새 드라마 제목: ")  

new_genre = input("새 드라마 장르: ")
new_theme = input("새 드라마 주제: ")
new_period = input("새 드라마 방영기간(예: 2024-01-01 ~ 2024-02-01): ")
new_actors_input = input("새 드라마 배우들(쉼표로 구분): ")
new_quote_raw = input("인상 깊었던 대사(따옴표 없이 입력): ")

new_actors = new_actors_input.split(",")
new_quote = f"\"{new_quote_raw}\""

drama3 = {
    "제목": new_title,
    "장르": new_genre,
    "주제": new_theme,
    "방영기간": new_period,
    "배우": new_actors,
    "명대사": new_quote
}


upd_title = input("수정(덮어쓰기)할 제목(대상: drama2): ")  
upd_genre = input("수정할 장르: ")
upd_theme = input("수정할 주제: ")
upd_period = input("수정할 방영기간: ")
upd_actors_input = input("수정할 배우들(쉼표로 구분): ")
upd_quote_raw = input("수정할 명대사(따옴표 없이 입력): ")

upd_actors = upd_actors_input.split(",")
upd_quote = f"\"{upd_quote_raw}\""

drama2["제목"] = upd_title
drama2["장르"] = upd_genre
drama2["주제"] = upd_theme
drama2["방영기간"] = upd_period
drama2["배우"] = upd_actors
drama2["명대사"] = upd_quote

print("\n[드라마 1]")
print(f"제목: {drama1['제목']}")
print(f"장르: {drama1['장르']}")
print(f"주제: {drama1['주제']}")
print(f"방영기간: {drama1['방영기간']}")
print(f"배우: {drama1['배우']}")
print(f"명대사: {drama1['명대사']}")

print("\n[드라마 2]  # 수정 후")
print(f"제목: {drama2['제목']}")
print(f"장르: {drama2['장르']}")
print(f"주제: {drama2['주제']}")
print(f"방영기간: {drama2['방영기간']}")
print(f"배우: {drama2['배우']}")
print(f"명대사: {drama2['명대사']}")

print("\n[드라마 3]  # 새로 추가")
print(f"제목: {drama3['제목']}")
print(f"장르: {drama3['장르']}")
print(f"주제: {drama3['주제']}")
print(f"방영기간: {drama3['방영기간']}")
print(f"배우: {drama3['배우']}")
print(f"명대사: {drama3['명대사']}")
