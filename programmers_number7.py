# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.

# def solution(s):
#     answer = True
#     p_number=s.count('p')
#     y_number=s.count('y')
#     if p_number==y_number:
#         answer
#     elif p_number and y_number==0:
#         answer
#     else:
#         answer=False
#     return answer

# def solution(s):
#     answer = True
#     p_number=s.count('p','P')
#     y_number=s.count('y','Y')
#     if p_number != y_number:
#         answer=False
#     return answer

def solution(s):
    answer = True
    P_number=s.count('P')
    p_number=s.count('p')
    Y_number=s.count('Y')
    y_number=s.count('y')
    if P_number+p_number!=Y_number+y_number:
        answer=False
    return answer

def solution(s):
    answer = True
    if s.count('P')+s.count('p') != s.count('Y')+s.count('y'):
        answer=False
    return answer