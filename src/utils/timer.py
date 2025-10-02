"""
알고리즘 성능 측정을 위한 타이머 유틸리티
"""
import time
from functools import wraps
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """
    함수 실행 시간을 측정하는 데코레이터
    
    Args:
        func: 측정할 함수
        
    Returns:
        래핑된 함수
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print(f"{func.__name__} 실행 시간: {end_time - start_time:.6f}초")
        return result
    
    return wrapper


class PerformanceTimer:
    """성능 측정을 위한 컨텍스트 매니저"""
    
    def __init__(self, name: str = "작업"):
        self.name = name
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        print(f"{self.name} 실행 시간: {duration:.6f}초")
    
    @property
    def elapsed_time(self) -> float:
        """경과 시간 반환"""
        if self.start_time is None:
            return 0.0
        end = self.end_time or time.time()
        return end - self.start_time
