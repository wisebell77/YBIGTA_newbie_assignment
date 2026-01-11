# lib.py의 Matrix 클래스를 참조하지 않음
import sys


"""
TODO:
- fast_power 구현하기 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    빠른 거듭제곱 알고리즘 구현
    분할 정복을 이용, 시간복잡도 고민!
    """
    # 구현하세요!
    """
    지수가 0이 입력되는 경우 1 반환
    """
    if exp == 0:
        return 1
    
    """
    재귀함수 정지 조건
    """
    if exp == 1:
        return base % mod
    
    """
    분할 정복 구현
    """
    val = fast_power(base, exp // 2, mod)
    val = (val * val) % mod

    """
    지수가 짝수, 홀수인 경우 나눔
    mod 연산은 다음을 만족함: (A * B) % C = ((A % C) * B) % C = (A * (B % C)) % C = ((A % C) * (B % C)) % C
    """
    if exp % 2 == 0:
        return val
    
    else:
        return (val * base) % mod

def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # 입력 고정
    
    result: int = fast_power(A, B, C) # 출력 형식
    print(result) 

if __name__ == "__main__":
    main()