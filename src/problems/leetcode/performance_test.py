"""
Two Sum 알고리즘들의 성능 비교 테스트
"""
import sys
import os
import time
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from utils.timer import PerformanceTimer
from problems.leetcode.two_sum import TwoSum


def generate_test_data(size: int) -> tuple:
    """테스트 데이터 생성"""
    nums = [random.randint(-1000, 1000) for _ in range(size)]
    # 해가 존재하도록 target 설정
    idx1, idx2 = random.sample(range(size), 2)
    target = nums[idx1] + nums[idx2]
    return nums, target


def performance_comparison():
    """성능 비교 테스트"""
    print("=== Two Sum 알고리즘 성능 비교 ===\n")
    
    test_sizes = [100, 500, 1000, 2000]
    
    for size in test_sizes:
        print(f"배열 크기: {size}")
        nums, target = generate_test_data(size)
        
        # 브루트 포스 (작은 크기에서만)
        if size <= 1000:
            with PerformanceTimer(f"브루트 포스 (크기 {size})"):
                result1 = TwoSum.brute_force(nums.copy(), target)
        
        # 해시맵
        with PerformanceTimer(f"해시맵 (크기 {size})"):
            result2 = TwoSum.hash_map(nums.copy(), target)
        
        # 투 포인터
        with PerformanceTimer(f"투 포인터 (크기 {size})"):
            result3 = TwoSum.two_pointers(nums.copy(), target)
        
        # 결과 검증
        if size <= 1000:
            print(f"브루트 포스 결과: {sorted(result1)}")
        print(f"해시맵 결과: {sorted(result2)}")
        print(f"투 포인터 결과: {sorted(result3)}")
        
        # 결과가 올바른지 확인 (합이 target과 같은지)
        if size <= 1000 and result1:
            assert nums[result1[0]] + nums[result1[1]] == target
        if result2:
            assert nums[result2[0]] + nums[result2[1]] == target
        if result3:
            assert nums[result3[0]] + nums[result3[1]] == target
        
        print(f"결과: {sorted(result2)}")
        print("-" * 60)


def memory_usage_test():
    """메모리 사용량 테스트 (간단한 버전)"""
    print("\n=== 메모리 사용량 비교 ===\n")
    
    import tracemalloc
    
    nums, target = generate_test_data(1000)
    
    # 해시맵 방법
    tracemalloc.start()
    result1 = TwoSum.hash_map(nums.copy(), target)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"해시맵 메모리 사용량: {peak / 1024 / 1024:.2f} MB")
    
    # 투 포인터 방법
    tracemalloc.start()
    result2 = TwoSum.two_pointers(nums.copy(), target)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"투 포인터 메모리 사용량: {peak / 1024 / 1024:.2f} MB")


def complexity_analysis():
    """복잡도 분석 설명"""
    print("\n=== 알고리즘 복잡도 분석 ===\n")
    
    analysis = {
        "브루트 포스": {
            "시간복잡도": "O(n²)",
            "공간복잡도": "O(1)",
            "장점": "구현이 간단, 추가 메모리 불필요",
            "단점": "큰 입력에서 매우 느림"
        },
        "해시맵": {
            "시간복잡도": "O(n)",
            "공간복잡도": "O(n)",
            "장점": "가장 빠른 시간복잡도",
            "단점": "추가 메모리 필요"
        },
        "투 포인터": {
            "시간복잡도": "O(n log n)",
            "공간복잡도": "O(n)",
            "장점": "정렬된 배열에서 효율적",
            "단점": "정렬 과정에서 시간 소요"
        }
    }
    
    for method, details in analysis.items():
        print(f"📊 {method}:")
        for key, value in details.items():
            print(f"  {key}: {value}")
        print()


if __name__ == "__main__":
    performance_comparison()
    memory_usage_test()
    complexity_analysis()
