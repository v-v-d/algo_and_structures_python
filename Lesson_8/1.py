"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque


def get_haffman_tree(s):
    unique_symbols = Counter(s)
    sorted_symbols = deque(sorted(unique_symbols.items(), key=lambda item: item[1]))

    if len(sorted_symbols) > 1:
        while len(sorted_symbols) > 1:
            combined_weight = sorted_symbols[0][1] + sorted_symbols[1][1]
            combined_node = {0: sorted_symbols.popleft()[0],
                             1: sorted_symbols.popleft()[0]}

            for i, symbol in enumerate(sorted_symbols):
                if combined_weight > symbol[1]:
                    continue
                else:
                    sorted_symbols.insert(i, (combined_node, combined_weight))
                    break
            else:
                sorted_symbols.append((combined_node, combined_weight))

    else:
        combined_weight = sorted_symbols[0][1]
        combined_node = {0: sorted_symbols.popleft()[0], 1: None}
        sorted_symbols.append((combined_node, combined_weight))

    return sorted_symbols[0][0]


code_table = dict()


def get_haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        get_haffman_code(tree[0], path=f'{path}0')
        get_haffman_code(tree[1], path=f'{path}1')


s = "на доме чемодан"

haffman_tree = get_haffman_tree(s)
get_haffman_code(haffman_tree)

print(code_table)

for i in s:
    print(code_table[i], end=' ')
