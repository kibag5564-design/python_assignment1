# path : loop\\while_mission.py
# module : loop.while_mission

# 함수명: sungjuk_process

sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

def sungjuk_process():
    prompt = '''
    ***원하는 메뉴 번호를 선택하세요
    1. 추가
    2. 삭제
    3. 출력
    4. 끝내기
    '''

    while True:
        print(prompt)
        no = int(input('입력:'))

        if no == 1:
            add_list()

        if no == 2:
            del_list()

        if no == 3:
            save_list()

        if no == 4:
            print('성적관리 프로그램 종료')
            break

def add_list():
    sno = int(input('번호:'))
    sname = str(input('이름:'))
    score = int(input('점수:'))

    sungjuk_list.append = [sno, sname, score]
    print('새로운 학생정보가 추가되었습니다.')

def del_list():
    print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')

    lst = len(sungjuk_list)
    if lst >= 3:
        lst.remove
        print('{lst)번 위치의 아이템이 제거되었습니다')
        print('현재 저장된 아이템의 갯수는 2개 입니다')
    
    

def save_list():
    st = int(input('입력:'))
    
    if st:
        open(st)

    