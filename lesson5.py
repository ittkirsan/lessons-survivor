def SynchronizingTables(N, ids, salary):
    ids_new = []
    reordered_salary_array = []
    for i in range(N):
        ids_new.append(ids[i])

    for i in range(N):
        reordered_salary_array.append(salary[i])

    ids_new.sort()
    reordered_salary_array.sort()

    for i in ids_new:
        index = ids.index(i)
        for j in reordered_salary_array:
            for k in range(N):
                if salary[k] == j:
                    salary[k], salary[index] = salary[index], salary[k]

    return reordered_salary_array
