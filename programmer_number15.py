# 길이가 같은 배열 A, B 두개가 있습니다. 
# 각 배열은 자연수로 이루어져 있습니다.
# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 
# 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 
# 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. 
# (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)
# 예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면
# A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
# A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
# A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
# 즉, 이 경우가 최소가 되므로 29를 return 합니다.
# 배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

def solution(A,B):
    answer = 0
    while 0<len(A):             #==> 이 풀이법은 효율성이 안좋음.
        answer+=min(A)*max(B)
        A.remove(min(A))
        B.remove(max(B))

    return answer



def solution(A,B):
    answer = 0
    A.sort()                  ==> 효율성이 좋다.
    B.sort()
    b=B[::-1]             
    for i,j in zip(A,b):    #==> zip 내장함수 사용법을 잘 알아두자. 
        answer+=i*j         # zip(*iterable)은 동일한 개수(길이)로 이루어진 데이터(리스트로 들어옴)들을 묶어서 보낼때 쓰인다.
                            # 예시로) list(zip([1, 2, 3], [4, 5, 6])) 이것의 결과값은 [(1,4),(2,5),(3,6)]으로 나오게 된다.
                            # [(1,4),(2,5),(3,6)]에서 i[0]=1,j[0]=4  i[1]=2,j[1]=5... 이런식으로 들어간다.
                            # 즉 우리가 for문에서 여러개의 변수를 한번에 곱해줄 때 쓰일 수 있다.
    return answer



def solution(A,B):                  # ==>진짜 효율 안좋은 풀이법
    answer = 0
    list_a=[]
    list_b=[]
    for i in A:
        list_a.append(i)
    for j in B:
        list_b.append(j)
    while 0<len(list_a):
        answer+=min(list_a)*max(list_b)
        list_a.remove(min(list_a))
        list_b.remove(max(list_b))


    return answer