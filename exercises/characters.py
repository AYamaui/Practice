

def solution(S, T):
    if S == T:
        return 'EQUAL'

    if len(S) < len(T):
        for idx, char in enumerate(T):

            if idx >= len(S):
                return 'IMPOSSIBLE'
            if char != S[idx]:
                S = S[:idx] + char + S[idx:]
                break
        return 'INSERT {}'.format(char) if S == T else 'IMPOSSIBLE'

    changes = 0
    replaced = None

    for idx, char in enumerate(T):
        if char != S[idx]:

            if replaced is None:
                replaced = S[idx]
                S = S[:idx] + char + S[idx + 1:]
            else:
                S = S[:idx] + replaced + S[idx + 1:]
            changes += 1

            if S == T:
                return 'REPLACE {} {}'.format(replaced, char) if changes < 2 else 'SWAP {} {}'.format(replaced, S[idx - 1])

            if changes > 2:
                return 'IMPOSSIBLE'

    return 'IMPOSSIBLE'



if __name__ == '__main__':
    S = 'nice'
    T = 'niece'
    print(solution(S, T))
    S = 'test'
    T = 'tent'
    print(solution(S, T))
    S = 'form'
    T = 'from'
    print(solution(S, T))
    S = 'o'
    T = 'odd'
    print(solution(S, T))
    S = 'ara'
    T = 'oro'
    print(solution(S, T))
    S = ''
    T = '2'
    print(solution(S, T))
    S = 'abc'
    T = 'bac'
    print(solution(S, T))