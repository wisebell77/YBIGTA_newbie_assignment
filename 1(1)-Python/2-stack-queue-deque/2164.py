from lib import create_circular_queue


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