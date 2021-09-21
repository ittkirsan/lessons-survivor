def SynchronizingTables(N, ids, salary):
    ids_new = []
    salary_new = []
    for i in range(N):
        ids_new.append(ids[i])

    for i in range(N):
        salary_new.append(salary[i])

    ids_new.sort()
    salary_new.sort()

    for i in ids_new:
        index = ids.index(i)
        for j in salary_new:
            for k in range(N):
                if salary[k] == j:
                    salary[k], salary[index] = salary[index], salary[k]

    return salary
