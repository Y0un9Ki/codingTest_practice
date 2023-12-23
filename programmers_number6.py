def solution(n):
    answer = []
    n_str=str(n)
    for i in n_str:
        answer.append(int(i))
    answer.reverse()
    return print(answer)