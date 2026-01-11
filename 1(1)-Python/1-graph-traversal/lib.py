from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
TODO:
- __init__ 구현하기
- add_edge 구현하기
- dfs 구현하기 (재귀 또는 스택 방식 선택)
- bfs 구현하기
"""


class Graph:
    def __init__(self, n: int) -> None:
        """
        그래프 초기화
        n: 정점의 개수 (1번부터 n번까지)
        graph 변수에 1 ~ n의 정점을 딕셔너리로 생성
        """
        self.n = n
        # 구현하세요!
        self.graph: dict = defaultdict(list)
        for i in range(1, n + 1):
            self.graph[i]

    
    def add_edge(self, u: int, v: int) -> None:
        """
        양방향 간선 추가
        각 노드에 인접한 노드들의 집합을 리스트로 저장
        """
        # 구현하세요!
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, start: int) -> list[int]:
        """
        깊이 우선 탐색 (DFS)
        
        구현 방법 선택:
        1. 재귀 방식: 함수 내부에서 재귀 함수 정의하여 구현
        2. 스택 방식: 명시적 스택을 사용하여 반복문으로 구현
        -> 스택 방식 선택
        """
        # 구현하세요!
        """
        정점 번호가 작은 것부터 방문 구현 위하여 내림차순 정렬
        """
        for i in range(1, self.n + 1):
            self.graph[i].sort(reverse = True)

        """
        리스트를 통해 방문 순서 보존
        """
        visit = list()
        stack = list()
        
        stack.append(start)

        
        while stack:
            node = stack.pop()
            """
            방문 노드 중복 방지
            """
            if node not in visit:
                visit.append(node)
                stack.extend(self.graph[node])

        return visit
    
    def bfs(self, start: int) -> list[int]:
        """
        너비 우선 탐색 (BFS)
        큐를 사용하여 구현
        """
        # 구현하세요!
        """
        정점 번호가 작은 것부터 방문 구현 위하여 오름차순 정렬
        """
        for i in range(1, self.n + 1):
            self.graph[i].sort()

        visit = list()
        queue: deque = deque()

        queue.append(start)

        while queue:
            node = queue.popleft()
            if node not in visit:
                visit.append(node)
                queue.extend(self.graph[node])

        return visit
    
    def search_and_print(self, start: int) -> None:
        """
        DFS와 BFS 결과를 출력
        """
        dfs_result = self.dfs(start)
        bfs_result = self.bfs(start)
        
        print(' '.join(map(str, dfs_result)))
        print(' '.join(map(str, bfs_result)))
