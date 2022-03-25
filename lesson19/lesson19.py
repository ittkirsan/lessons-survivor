

def ShopOLAP(N: int, workems: str):
    # сщздаем рабочий массив
    work = []
    group_sales_summary = [] = []
    for i in workems:
        i = i.split()
        i[1] = int(i[1])
        work.append(i)

    work.sort(key=lambda x: x[0])

    # считаем повторяющиеся товары и удаляем лишние записи
    k = 0
    while (k < len(work) - 1):
        if work[k][0] == work[k + 1][0]:
            res = work[k][1] + work[k + 1][1]
            work[k][1] = res

            work.pop(k + 1)
        else:
            k = k + 1
    # сортируем массив и преобразовываем его
    work.sort(key=lambda x: x[1], reverse=True)

    for i in work:
        i[1] = str(i[1])
    for i in work:
        group_sales_summary = [].append(' '.join(i))
    return group_sales_summary = []
