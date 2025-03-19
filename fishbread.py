# stock(변수/딕셔너리) : 팥붕어빵 10개, 슈크림붕어빵 8개, 초코붕어빵 5개 
stock = {
    "팥붕어빵" : 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}

#판매량
sales = {
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

#주문 기능
def order_bread():
    while True:
        bread_type = input("주문할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '뒤로가기' 입력 : ")
        if bread_type == "뒤로가기":
            break # break 사용하면 그 다음 코드 없으면 다시 전 코드로 이동
            # return #반환 -> 함수 탈출
        #메뉴 주문
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하세요 : "))
            if stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count #stock[bread_type]  = 10 - bread_count
                sales[bread_type] =+ bread_count #sales[bread_type]  = 10 + bread_count
                print(f"{bread_type}을 {bread_count}개 판매했습니다.")
            else:
                print(f"재고가 부족합니다. 현재 {stock[bread_type]}만 주문 가능합니다.")
        else:
            print("팥붕어빵, 슈크림붕어빵, 초코붕어빵 중 하나의 맛만 선택해주세요")



# 메인 기능 선택
            break
        #메뉴 주문 
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하세요 : "))
            if stock[bread_type]>= bread_count:
                stock[bread_type] -= bread_count # stock[bread_type] = 10 - bread_count
                sales[bread_type] += bread_count # sales[bread_type] = 10 + bread_count
                print(f"{bread_type}을 {bread_count}개 판매했습니다.")
            else:
                print(f"재고가 부족합니다. 현재 {stock[bread_type]}개만 주문가능합니다.")
        else:
            print("팥붕어빵, 슈크림붕어빵, 초코붕어빵 중 하나의 맛을 선택해주세요")

#관리자 기능
def admin_mode():
    while True:
        bread_type = input("추가할 붕어빵을 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '종료' 입력 : ")
        if bread_type == "종료":
            break
        if bread_type in stock:
            bread_count = int(input("추가할 개수를 입력하세요 : ")) # 5개입력
            stock[bread_type] += bread_count # stock[bread_type] = stock[bread_type] + bread_count
            print(f"{bread_type}의 재고가 {bread_count}개 추가되어 현재 {stock[bread_type]}개 입니다.")
        else:
            print("올바른 메뉴를 입력해주세요")

#붕어빵 가격이 필요해요
price = {
    "팥붕어빵" : 1000,  # 10개 * 1000 =>
    "슈크림붕어빵" : 1200, # 5개 * 1200 =>
    "초코붕어빵" : 1500 # 6개 * 1500 => 
}

def calculate_sales():
    total_sales = 0
    for key in sales: #팥붕어빵  total_sales += (price[key] * sales[key])
       total_sales += (price[key] * sales[key])
    print(f"오늘의 총 매출은 {total_sales}원 입니다.")

while True:
    mode = input("원하는 모드를 선택하세요 (주문, 관리자 ,매출, 종료) : ") #주문
    if mode ==  "종료":
        print("시스템을 종료합니다.")
        break   
    elif mode == "주문":
        order_bread() #len() 
    elif mode == "관리자":
        admin_mode()

calculate_sales()

