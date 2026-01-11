from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    """
    모든 원소를 n으로 가지는 행렬 생성
    """
    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    """
    모든 원소를 0으로 가지는 행렬 생성
    """
    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    """
    모든 원소를 1로 가지는 행렬 생성
    """
    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    """
    n * n 단위 행렬 생성
    """
    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    """
    A.shape()로 A의 행과 열의 개수 출력
    """
    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    """
    행렬 복사(깊은 복사)
    """
    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    """
    A[a, b]가 A.matrix[a][b]와 같은 역할
    """
    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    """
    A[a, b] = k로 A의 (a, b) 원소를 k로 지정
    """
    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        # 구현하세요!
        self.matrix[key[0]][key[1]] = value

    """
    A @ B가 행렬 곱의 역할
    """
    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        """
        행렬 연산 결과를 저장할 영행렬 생성
        """
        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]

        return result
    """
    A ** n 연산 구현
    """
    def __pow__(self, n: int) -> Matrix:
        # 구현하세요!
        x, y = self.shape
        assert x == y

        temp = self
        result = Matrix.eye(x)

        """
        @ 연산 진행할 때마다 MOD값으로 모듈러 연산을 해서
        숫자 크기가 커지는 것을 방지
        """
        while n > 0:
            if n % 2 == 1:
                result @= temp
                for i in range(x):
                    for j in range(y):
                        result[i, j] %= self.MOD
                n -= 1
            temp @= temp
            for i in range(x):
                for j in range(y):
                    temp[i, j] %= self.MOD
            n //= 2

        return result

    """
    A ** n 연산으로 출력된 리스트를 행렬 형태의 str 문자열로 변환
    """
    def __repr__(self) -> str:
        lines = []
        
        for row in self.matrix:
            line_str = " ".join(map(str, row))
            lines.append(line_str)
            
        return "\n".join(lines)


from typing import Callable
import sys


"""
-아무것도 수정하지 마세요!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, B = intify(lines[0])
    matrix: list[list[int]] = [*map(intify, lines[1:])]

    Matrix.MOD = 1000
    modmat = Matrix(matrix)

    print(modmat ** B)


if __name__ == "__main__":
    main()