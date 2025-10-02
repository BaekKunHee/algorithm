# 알고리즘 문제 풀이 프로젝트

Python을 사용한 알고리즘 문제 풀이를 위한 개발 환경입니다.

## 🚀 시작하기

### 1. 가상환경 활성화

```bash
# 가상환경 활성화
source venv/bin/activate

# 가상환경 비활성화 (작업 완료 후)
deactivate
```

### 2. 패키지 설치

```bash
# 필수 패키지 설치
pip install -r requirements.txt
```

### 3. 프로젝트 구조

```
algorithm/
├── venv/                    # 가상환경
├── src/                     # 소스 코드
│   ├── data_structures/     # 데이터 구조 구현
│   │   ├── linked_list.py   # 연결 리스트
│   │   └── binary_tree.py   # 이진 트리
│   ├── algorithms/          # 알고리즘 구현
│   ├── problems/            # 문제 풀이
│   │   ├── leetcode/        # LeetCode 문제
│   │   ├── programmers/     # 프로그래머스 문제
│   │   └── baekjoon/        # 백준 문제
│   ├── utils/               # 유틸리티 함수
│   │   ├── timer.py         # 성능 측정
│   │   └── input_parser.py  # 입력 파싱
│   └── tests/               # 테스트 코드
├── requirements.txt         # 패키지 의존성
└── README.md               # 프로젝트 설명
```

## 🛠️ 사용법

### 성능 측정

```python
from src.utils.timer import timer, PerformanceTimer

# 데코레이터 사용
@timer
def my_algorithm():
    # 알고리즘 코드
    pass

# 컨텍스트 매니저 사용
with PerformanceTimer("알고리즘 실행"):
    # 알고리즘 코드
    pass
```

### 입력 파싱

```python
from src.utils.input_parser import read_int, read_ints, read_string

# 정수 하나 읽기
n = read_int()

# 정수 배열 읽기
arr = read_ints()

# 문자열 읽기
s = read_string()
```

### 데이터 구조 사용

```python
from src.data_structures.linked_list import LinkedList, create_linked_list
from src.data_structures.binary_tree import BinaryTree, create_binary_tree

# 연결 리스트
ll = LinkedList()
ll.append(1)
ll.append(2)

# 이진 트리
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
```

## 🧪 테스트 실행

```bash
# 모든 테스트 실행
pytest

# 특정 파일 테스트
pytest tests/test_linked_list.py

# 커버리지와 함께 실행
pytest --cov=src
```

## 📝 코드 포맷팅

```bash
# 코드 포맷팅
black src/

# import 정렬
isort src/

# 린팅
flake8 src/
```

## 📚 문제 풀이 가이드

### 1. 문제 분석
- 문제를 정확히 이해하고 요구사항 파악
- 입력/출력 형식 확인
- 시간/공간 복잡도 제약 확인

### 2. 접근 방법 설계
- 여러 접근 방법 고려
- 최적의 알고리즘 선택
- 예외 케이스 처리

### 3. 구현
- 깔끔하고 읽기 쉬운 코드 작성
- 변수명은 의미를 명확히 표현
- 주석으로 복잡한 로직 설명

### 4. 테스트
- 다양한 테스트 케이스 작성
- 엣지 케이스 확인
- 성능 측정

## 🔧 개발 도구

- **Python 3.13.2**: 최신 Python 버전
- **pytest**: 테스트 프레임워크
- **black**: 코드 포맷터
- **flake8**: 린터
- **mypy**: 타입 체커
- **memory-profiler**: 메모리 사용량 측정
- **line-profiler**: 라인별 성능 측정

## 📖 참고 자료

- [Python 공식 문서](https://docs.python.org/3/)
- [LeetCode](https://leetcode.com/)
- [프로그래머스](https://programmers.co.kr/)
- [백준 온라인 저지](https://www.acmicpc.net/)

## 🤝 기여하기

1. 새로운 문제 풀이 추가
2. 데이터 구조나 알고리즘 구현 개선
3. 유틸리티 함수 추가
4. 테스트 케이스 보완

---

Happy Coding! 🎉
