POST_MAN = {
    "product_data": {
        "name": 'laptop',
        "rating": [
          1221, -1 , 1222, -1, 1223, 46, 1224, -1, 1225, 46, 1226,
          -1, 1227, 46, 1228, -1, 1229, 46, 1230, -1, 1231, 46,
        ]
    },
}

# dictionary rating data 
# 날짜, 평점 데이터 각각분리 후 날짜별 평점 그래프화
Rating = {
    'date':[1221, 1222 , 1223],
    'rating':[0, 4.6, 0 , 4.5]
}

# 여기서 또 하나 깨달아야 할점 : 나는 항상 조건문과 반복문으로 계속해서 만들생각만 했는데 함수를 정의해서 비슷한 상황에 함수만 불러온다면 
# 더 좋은 코드를 만들 수 있다. 이점 항상 유념하자!

def add_data(list):
    RESULT={}
    date_list=[]     # ==> 1. 부분
    rating_list=[]   # ==> 1. 부분
    for idx, value in enumerate(list):  # ==> 2.부분
        if idx%2==0:
            date_list.append(value)
        else:
            if value<0:
                rating_list.append(0)
            else:
                rating_list.append(value/10)
                

    RESULT['date']=date_list
    RESULT['rating']=rating_list
    return RESULT
    
    

add_data(POST_MAN["product_data"]['rating'])



print('RESULT : ' , add_data(POST_MAN["product_data"]['rating']))


# TIL
# 1. dictionary에서 append와 같은 리스트메서드가 없기에 리스트로 변환후 dictionary로 넣어주었다.
# 2. 리스트에서 인덱스 번호와 그 인덱스 번호에 해당하는 value값을 알기위해 enumerate()라는 함수를 사용.
# 2. why? dictionary에서 append와 같은 리스트메서드가 없기에 리스트로 변환 후 
# 2.      인덱스 번호에 따라 dating_list와 rating_list로 나눈 후에 결과값을 보여주기 위해