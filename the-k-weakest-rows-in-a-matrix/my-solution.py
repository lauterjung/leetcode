from typing import List


def kWeakestRows(mat: List[List[int]], number: int) -> List[int]:
    row_sum: List[int] = list(map(sum, mat))
    ordinal_order: List[int] = list(range(len(mat)))

    pairs: List[tuple[int]] = list(zip(row_sum, ordinal_order))
    sorted_pairs: List[tuple[int]] = sorted(pairs)
    weakest_indexes: tuple[int] = list(zip(*sorted_pairs))[1]

    return list(weakest_indexes[0:number])