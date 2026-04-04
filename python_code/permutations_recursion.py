from typing import TypeVar

T = TypeVar('Any') 


def get_arr_rest(arr: list[T], index: T) -> T:
    t_arr = arr.copy()
    t_arr.pop(index)
    return t_arr

def permutation(arr: list[T]) -> list[list[T]]:
    res_perm = []
    if len(arr) > 2:
        for i in range(len(arr)):
            t_arr = get_arr_rest(arr, i)
            t_perm = permutation(t_arr)
            for x in range(len(t_perm)):
                t_perm[x].append(arr[i])
            for m in range(len(t_perm)):
                res_perm.append(t_perm[m])
        return res_perm
    else:
        return [[arr[0], arr[1]], [arr[1], arr[0]]]


arr = [1, 2, 3, 4]
#arr = ['a', 'b', 'c']
res = permutation(arr)
print('Permitations number: ', len(res))
print('Permitations list:')
for i in range(len(res)):
    print(res[i])
