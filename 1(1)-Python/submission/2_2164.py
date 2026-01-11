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
- simulate_card_game 구현하기
    # 카드 게임 시뮬레이션 구현
        # 1. 큐 생성
        # 2. 카드가 1장 남을 때까지 반복
        # 3. 마지막 남은 카드 반환
"""


def simulate_card_game(n: int) -> int:
    """
    카드2 문제의 시뮬레이션
    맨 위 카드를 버리고, 그 다음 카드를 맨 아래로 이동
    """
    # 구현하세요!
    """
    # create_circular_queue(n)으로 생성된 큐를 변수에 지정
    # 큐 내부 원소가 하나만 남을때까지
        #1. 왼쪽 원소 하나 pop
        #2. rotate(-1)을 통해 맨 위 카드를 맨 아래로 이동 구현
    # 마지막 남은 원소 반환
    """
    from collections import deque
    queue: deque[int] = create_circular_queue(n)
    while len(queue) > 1:
        queue.popleft()
        queue.rotate(-1)
    return queue[0]

def solve_card2() -> None:
    """입, 출력 format"""
    n: int = int(input())
    result: int = simulate_card_game(n)
    print(result)

if __name__ == "__main__":
    solve_card2()