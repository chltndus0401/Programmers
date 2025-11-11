def solution(plans):
    for p in plans:
        h, m = map(int, p[1].split(':'))
        p[1] = h * 60 + m
        p[2] = int(p[2])
    plans.sort(key=lambda x: x[1])
    answer = []
    stack = []
    for i in range(len(plans) - 1):
        name, start, play = plans[i]
        next_start = plans[i + 1][1]
        end = start + play
        if end <= next_start:
            answer.append(name)
            remain = next_start - end
            while stack and remain > 0:
                sname, splay = stack.pop()
                if splay <= remain:
                    answer.append(sname)
                    remain -= splay
                else:
                    stack.append([sname, splay - remain])
                    break
        else:
            stack.append([name, end - next_start])
    answer.append(plans[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    return answer
