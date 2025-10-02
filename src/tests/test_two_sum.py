"""
Two Sum 문제에 대한 단위 테스트
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from problems.leetcode.two_sum import TwoSum


class TestTwoSum:
    """Two Sum 테스트 클래스"""
    
    def test_brute_force_basic(self):
        """브루트 포스 기본 테스트"""
        nums = [2, 7, 11, 15]
        target = 9
        result = TwoSum.brute_force(nums, target)
        assert sorted(result) == [0, 1]
    
    def test_brute_force_multiple_cases(self):
        """브루트 포스 여러 케이스 테스트"""
        test_cases = [
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([1, 2, 3, 4, 5], 8, [2, 4]),
        ]
        
        for nums, target, expected in test_cases:
            result = TwoSum.brute_force(nums, target)
            assert sorted(result) == sorted(expected)
    
    def test_hash_map_basic(self):
        """해시맵 방법 기본 테스트"""
        nums = [2, 7, 11, 15]
        target = 9
        result = TwoSum.hash_map(nums, target)
        assert sorted(result) == [0, 1]
    
    def test_hash_map_multiple_cases(self):
        """해시맵 방법 여러 케이스 테스트"""
        test_cases = [
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([1, 2, 3, 4, 5], 8, [2, 4]),
        ]
        
        for nums, target, expected in test_cases:
            result = TwoSum.hash_map(nums, target)
            assert sorted(result) == sorted(expected)
    
    def test_two_pointers_basic(self):
        """투 포인터 방법 기본 테스트"""
        nums = [2, 7, 11, 15]
        target = 9
        result = TwoSum.two_pointers(nums, target)
        assert sorted(result) == [0, 1]
    
    def test_two_pointers_multiple_cases(self):
        """투 포인터 방법 여러 케이스 테스트"""
        test_cases = [
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([1, 2, 3, 4, 5], 8, [2, 4]),
        ]
        
        for nums, target, expected in test_cases:
            result = TwoSum.two_pointers(nums, target)
            assert sorted(result) == sorted(expected)
    
    def test_edge_cases(self):
        """엣지 케이스 테스트"""
        # 최소 길이 배열
        nums = [1, 2]
        target = 3
        result = TwoSum.hash_map(nums, target)
        assert sorted(result) == [0, 1]
        
        # 음수 포함
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = TwoSum.hash_map(nums, target)
        assert sorted(result) == [2, 4]
    
    def test_all_methods_consistency(self):
        """모든 방법이 같은 결과를 반환하는지 테스트"""
        test_cases = [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
            ([1, 2, 3, 4, 5], 8),
        ]
        
        for nums, target in test_cases:
            result1 = TwoSum.brute_force(nums.copy(), target)
            result2 = TwoSum.hash_map(nums.copy(), target)
            result3 = TwoSum.two_pointers(nums.copy(), target)
            
            assert sorted(result1) == sorted(result2) == sorted(result3)
    
    def test_no_solution(self):
        """해가 없는 경우 테스트 (문제 조건상 발생하지 않지만 안전장치)"""
        nums = [1, 2, 3]
        target = 7  # 해가 없는 경우
        
        # 모든 방법이 빈 리스트를 반환해야 함
        result1 = TwoSum.brute_force(nums, target)
        result2 = TwoSum.hash_map(nums, target)
        result3 = TwoSum.two_pointers(nums, target)
        
        assert result1 == result2 == result3 == []
