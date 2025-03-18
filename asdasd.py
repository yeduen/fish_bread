#관리자 모드
def admin_mode():
    while True:
        bread_type = input("추가할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '종료' 입력 : ")
        if bread_type == "종료":
            break
        if bread_type in stock:
            bread_count = int(input("추가할 갯수를 입력하세요 : ")) #5개 입력
            stock[bread_type] += bread_count #stock[bread_type] = stock[bread_type] + bread_count
            print(f"{bread_type}의 재고가 {bread_count}개 추가되어 현재 {stock[bread_type]}개 입니다.")
        else:
            print("올바른 메뉴를 입력해주세요.")