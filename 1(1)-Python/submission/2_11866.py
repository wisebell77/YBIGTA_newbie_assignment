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




"""
TODO:
- josephus_problem 구현하기
    # 요세푸스 문제 구현
        # 1. 큐 생성
        # 2. 큐가 빌 때까지 반복
        # 3. 제거 순서 리스트 반환
"""


def josephus_problem(n: int, k: int) -> list[int]:
    """
    요세푸스 문제 해결
    n명 중 k번째마다 제거하는 순서를 반환
    """
    # 구현하세요!
    """
    queue 변수에 1~n의 큐 생성
    queue가 빌 때까지 rotate_and_remove 실행
    queue에서 빼낸 원소는 차례대로 result 리스트에 추가
    """
    from collections import deque
    result: list[int] = []
    queue: deque[int] = create_circular_queue(n)
    while len(queue) > 0:
        rotate_and_remove(queue, k)
        result.append(queue.popleft())
    return result

def solve_josephus() -> None:
    """입, 출력 format"""
    n: int
    k: int
    n, k = map(int, input().split())
    result: list[int] = josephus_problem(n, k)
    
    # 출력 형식: <3, 6, 2, 7, 5, 1, 4>
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    solve_josephus()