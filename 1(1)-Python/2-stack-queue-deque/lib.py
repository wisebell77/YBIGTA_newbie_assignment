from __future__ import annotations
from collections import deque


"""
TODO:
- rotate_and_remove 구현하기 
"""


def create_circular_queue(n: int) -> deque[int]:
    """1부터 n까지의 숫자로 deque를 생성합니다."""
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> deque[int]:
    """
    큐에서 k번째 원소를 제거하고 반환합니다.
    """
    # 구현하세요!
    """
    k-1만큼의 원소를 뒤로 보내고 가장 앞에 있는 원소를 빼냄
    -> 원형 큐 구현
    """
    for _ in range(k - 1):
        queue.append(queue.popleft())
    return queue