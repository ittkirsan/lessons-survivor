

def MassVote(N, Votes):

    sum_votes = 0
    # подсчитываем колличество голосов
    for i in Votes:
        sum_votes += i

    max_votes = max(Votes)
    pr = round((max_votes*100 / sum_votes), 3)

    # определяем есть ли одинаковое колличество голосов
    l = 0
    for i in Votes:
        if i == max_votes:
            l += 1

    # оглашаем результаты
    if l > 1:
        return "no winner"
    elif pr > 50:
        for i in range(N):
            if Votes[i] == max_votes:
                result = 'majority winner' + ' ' + str(i+1)
                return result
    elif pr <= 50:
        for i in range(N):
            if Votes[i] == max_votes:
                result = 'minority winner' + ' ' + str(i+1)
                return result
