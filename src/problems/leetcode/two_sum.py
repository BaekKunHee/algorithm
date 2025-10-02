"""
LeetCode 1. Two Sum

문제:
정수 배열 nums와 정수 target이 주어졌을 때, 
두 숫자의 합이 target이 되는 인덱스를 반환하라.

각 입력에는 정확히 하나의 해가 있다고 가정하며, 
같은 요소를 두 번 사용할 수 없다.

예시:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

제약사항:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- 정확히 하나의 해만 존재
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from typing import List
from utils.timer import timer


class TwoSum:
    """Two Sum 문제 해결 클래스"""
    
    @staticmethod
    @timer
    def brute_force(nums: List[int], target: int) -> List[int]:
        """
        브루트 포스 방법
        시간복잡도: O(n²)
        공간복잡도: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    @staticmethod
    @timer
    def hash_map(nums: List[int], target: int) -> List[int]:
        """
        해시맵을 사용한 방법
        시간복잡도: O(n)
        공간복잡도: O(n)
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
    @staticmethod
    @timer
    def two_pointers(nums: List[int], target: int) -> List[int]:
        """
        투 포인터 방법 (정렬된 배열에서만 작동)
        시간복잡도: O(n log n) - 정렬 때문에
        공간복잡도: O(n) - 인덱스 저장 때문에
        """
        # 원본 인덱스를 저장하면서 정렬
        indexed_nums = [(nums[i], i) for i in range(len(nums))]
        indexed_nums.sort()
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []


def main():
    """메인 함수 - 문제 해결 및 테스트"""
    solution = TwoSum()
    
    # 테스트 케이스들
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 8, [2, 4]),
    ]
    
    print("=== Two Sum 문제 해결 ===\n")
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        print(f"테스트 케이스 {i}:")
        print(f"입력: nums = {nums}, target = {target}")
        print(f"예상 결과: {expected}")
        
        # 각 방법으로 해결
        result1 = solution.brute_force(nums.copy(), target)
        result2 = solution.hash_map(nums.copy(), target)
        result3 = solution.two_pointers(nums.copy(), target)
        
        print(f"브루트 포스 결과: {result1}")
        print(f"해시맵 결과: {result2}")
        print(f"투 포인터 결과: {result3}")
        
        # 결과 검증
        all_correct = all(
            sorted(result) == sorted(expected) 
            for result in [result1, result2, result3]
        )
        print(f"✅ 모든 방법 정답: {all_correct}")
        print("-" * 50)


if __name__ == "__main__":
    main()
