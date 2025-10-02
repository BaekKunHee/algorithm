"""
알고리즘 문제 입력 파싱을 위한 유틸리티
"""
import sys
from typing import List, Tuple, Any


def read_int() -> int:
    """정수 하나를 읽어서 반환"""
    return int(sys.stdin.readline().strip())


def read_ints() -> List[int]:
    """공백으로 구분된 정수들을 읽어서 리스트로 반환"""
    return list(map(int, sys.stdin.readline().strip().split()))


def read_string() -> str:
    """문자열 하나를 읽어서 반환"""
    return sys.stdin.readline().strip()


def read_strings() -> List[str]:
    """공백으로 구분된 문자열들을 읽어서 리스트로 반환"""
    return sys.stdin.readline().strip().split()


def read_matrix(rows: int, cols: int) -> List[List[int]]:
    """rows x cols 크기의 행렬을 읽어서 반환"""
    matrix = []
    for _ in range(rows):
        row = list(map(int, sys.stdin.readline().strip().split()))
        matrix.append(row)
    return matrix


def read_graph_edges(edges_count: int) -> List[Tuple[int, int]]:
    """그래프의 간선들을 읽어서 반환"""
    edges = []
    for _ in range(edges_count):
        u, v = map(int, sys.stdin.readline().strip().split())
        edges.append((u, v))
    return edges


def read_test_cases(test_count: int) -> List[Any]:
    """테스트 케이스들을 읽어서 반환"""
    test_cases = []
    for _ in range(test_count):
        # 각 테스트 케이스의 형태에 따라 수정 필요
        n = read_int()
        arr = read_ints()
        test_cases.append((n, arr))
    return test_cases
