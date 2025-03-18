sales ={
    "팥붕어빵":0,
    "슈크림붕어빵":0,
    "초코붕어빵":0
}


#붕어빵 가격이 필요
price ={
    "팥붕어빵":1000,
    "슈크림붕어빵":1200,
    "초코붕어빵":1500
}

def calculate_sales():
    total_sales = 0
    for key in sales: #sales의 key값을 꺼내온다
        total_sales += (price[key] * sales[key])
    print(f"오늘의 총 매출은 {total_sales}입니다.")

while True:
    mode = input("원하는 모드를 선택하세요 (주문, 관리자, 종료) :")
    if mode == "종료":
        print("시스템을 종료합니다.")
        break
    elif mode == "주문":
        order_bread()
    elif mede == "관리자":
        admin_mode()

calculate_sales()      

           