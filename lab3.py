# 13. Написать функцию для рекурсивного обхода графа (например, поиск в глубину)
def dfs(graph, top, n=None):
    if n is None:
        n = set()

    print(f"вершина {top} посещена")
    n.add(top)

    list(map(lambda x: dfs(graph, x, n), graph[top] - n))


graph1 = {
    0: {1, 2},
    1: {0, 3, 4},
    2: {0, 4},
    3: {1, 4},
    4: {1, 2, 3}
}

dfs(graph1, 0)

# ----------------------------------------------------------------------------------------------------

# Написать рекурсивную функцию, которая выводит последовательность шагов для решения задачи о Ханойских башнях для n дисков
# def hanoi_towers(n, source, target, auxiliary):
#     """
#     Решение задачи о Ханойских башнях.
#     n - количество дисков
#     source - начальный стержень
#     target - целевой стержень
#     auxiliary - вспомогательный стержень
#     """
#     if n > 0:
#      hanoi_towers(n - 1, source, auxiliary, target)
#      print(f"Переместить диск с {source} на {target}")
#      hanoi_towers(n - 1, auxiliary, target, source)
#
# hanoi_towers(3, 'A', 'C', 'B')
