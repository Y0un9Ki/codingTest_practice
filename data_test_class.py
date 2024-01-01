import pandas as pd

POST_MAN={
    'a': [
        1436, 1300, -1, 316, 1575, -1, -1, -1, -1, -1, -1, 26, -1, -1, -1, -1,
        47, 24766, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1,
      ],
      'b': [
        1443, 1158, -1, 350, 1573, -1, -1, -1, -1, -1, -1, 28, -1, -1, -1, -1,
        47, 23668, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1,
      ],
      'c': [
        1459, 1316, -1, 394, 1575, -1, -1, -1, -1, -1, -1, 27, -1, -1, -1, -1,
        47, 24614, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1,
      ],
      'd': [
        1461, 1144, -1, 361, 1575, -1, -1, -1, -1, -1, -1, 28, -1, -1, -1, -1,
        47, 24277, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1,
      ],
      'e': [
        1443, 1158, -1, 350, 1573, -1, -1, -1, -1, -1, -1, 28, -1, -1, -1, -1,
        47, 23668, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1,
      ],
      'f': [
        1397, 1198, -1, 339, 1574, -1, -1, -1, -1, -1, -1, 24, -1, -1, -1, -1,
        47, 22297, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1,
      ],
}


def minus_data(dict):
    for idx,value in enumerate(dict.values()): #==> dict는 enumerate 함수를 못쓰지만 values 메서드를 사용해서 리스트로 변환했다.
        for v in value[:]: # 리스트의 복사본을 만들어줘서 반복문을 사용. value를 변하는 값으로 반복문 안에 넣고 싶을 때 복사본을 넣어서 변하지 않게 만들어준다.
            if v ==-1:
                value.remove(v)
                
    return dict

data = minus_data(POST_MAN)

df = pd.DataFrame(data) # ==> 데이터 타입 에러 잘 보기
print(df)
