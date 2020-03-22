from itertools import permutations

def solution(s):
    answer = 0

    new_s = list(s)
    for i in range(2,len(s)+1):
        pm = list(permutations(s, i))
        for j in pm:
            if len(j) <= len(s):
                new_s.append(''.join(j))
    new_s = list(set([int(x) for x in new_s]))
    
    if new_s.count(1):
        new_s.remove(1)
    if new_s.count(0):
        new_s.remove(0)

    for x in new_s:
        i = 2
        while i*i <= x: 
            if x % i == 0:
                answer -= 1
                break
            i+=1
        answer += 1
    
    return answer

if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result = solution("011")
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()