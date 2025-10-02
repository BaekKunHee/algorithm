# 알고리즘 복잡도 분석 (Big O)

## 📚 목차
1. [시간복잡도란?](#시간복잡도란)
2. [공간복잡도란?](#공간복잡도란)
3. [Big O 표기법](#big-o-표기법)
4. [시간복잡도 종류와 예시](#시간복잡도-종류와-예시)
5. [공간복잡도 종류와 예시](#공간복잡도-종류와-예시)
6. [실제 코드로 이해하기](#실제-코드로-이해하기)
7. [복잡도 비교표](#복잡도-비교표)

---

## 시간복잡도란?

**시간복잡도**는 알고리즘이 문제를 해결하는데 걸리는 시간이 입력 크기에 따라 어떻게 변하는지를 나타냅니다.

### 🍕 쉬운 비유
- **피자 주문**: 피자 1개 주문 vs 100개 주문
- 1개 주문: 5분
- 100개 주문: 500분 (5분 × 100)
- 이 경우 시간복잡도는 **O(n)** (입력 크기에 비례)

### 📊 왜 중요한가?
- **효율성 비교**: 같은 문제를 해결하는 여러 방법 중 어느 것이 더 빠른지
- **확장성 예측**: 데이터가 10배 늘어나면 시간이 얼마나 늘어날지
- **최적화 방향**: 어느 부분을 개선해야 할지

---

## 공간복잡도란?

**공간복잡도**는 알고리즘이 실행되는 동안 사용하는 메모리(저장공간)가 입력 크기에 따라 어떻게 변하는지를 나타냅니다.

### 🏠 쉬운 비유
- **책장 정리**: 책 10권 vs 1000권
- 10권: 작은 책장 1개
- 1000권: 큰 책장 10개
- 이 경우 공간복잡도는 **O(n)** (책의 개수에 비례)

### 💾 메모리 사용 예시
- **변수**: int, string 등 기본 변수들
- **배열/리스트**: 데이터를 저장하는 컨테이너
- **재귀 호출**: 함수가 자기 자신을 호출할 때 사용하는 스택 공간

---

## Big O 표기법

Big O는 알고리즘의 **최악의 경우**를 나타내는 표기법입니다.

### 📈 그래프로 보는 복잡도
```
시간/공간 사용량
    ↑
    |     O(n²) - 매우 느림
    |    ╱
    |   ╱
    |  ╱
    | ╱
    |╱
    |╲
    | ╲  O(n) - 보통
    |  ╲
    |   ╲
    |    ╲
    |     ╲ O(log n) - 빠름
    |      ╲
    |       ╲ O(1) - 매우 빠름
    |        ╲
    └──────────────→ 입력 크기
```

### 🎯 핵심 원칙
1. **상수 무시**: O(2n) → O(n)
2. **낮은 차수 무시**: O(n² + n) → O(n²)
3. **최고 차수만**: O(n³ + n² + n) → O(n³)

---

## 시간복잡도 종류와 예시

### 1. O(1) - 상수 시간 (Constant Time)
**특징**: 입력 크기와 관계없이 항상 같은 시간

```python
# 배열의 첫 번째 원소 접근
def get_first_element(arr):
    return arr[0]  # 항상 1번의 연산

# 해시 테이블에서 값 찾기
def find_in_hash_table(key):
    return hash_table[key]  # 해시 계산으로 바로 접근
```

### 2. O(log n) - 로그 시간 (Logarithmic Time)
**특징**: 입력이 2배 늘어나도 연산은 1번만 늘어남

```python
# 이진 탐색
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 예시: 1000개 데이터 → 최대 10번 비교
# 2000개 데이터 → 최대 11번 비교
```

### 3. O(n) - 선형 시간 (Linear Time)
**특징**: 입력 크기에 비례해서 시간이 늘어남

```python
# 배열 전체 순회
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # n번 반복
        if num > max_val:
            max_val = num
    return max_val

# 리스트에서 특정 값 찾기
def linear_search(arr, target):
    for i, num in enumerate(arr):  # n번 반복
        if num == target:
            return i
    return -1
```

### 4. O(n log n) - 선형 로그 시간 (Linearithmic Time)
**특징**: 효율적인 정렬 알고리즘의 복잡도

```python
# 병합 정렬 (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # O(log n) 레벨
    right = merge_sort(arr[mid:])   # O(log n) 레벨
    
    return merge(left, right)       # O(n) 병합

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):  # O(n)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### 5. O(n²) - 이차 시간 (Quadratic Time)
**특징**: 입력이 2배 늘어나면 시간이 4배 늘어남

```python
# 버블 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # n번 반복
        for j in range(n - 1):   # n번 반복
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 중첩 반복문으로 모든 쌍 비교
def find_all_pairs(arr):
    pairs = []
    for i in range(len(arr)):      # n번 반복
        for j in range(i + 1, len(arr)):  # n번 반복
            pairs.append((arr[i], arr[j]))
    return pairs
```

### 6. O(2ⁿ) - 지수 시간 (Exponential Time)
**특징**: 입력이 1 늘어나면 시간이 2배 늘어남

```python
# 피보나치 수열 (비효율적 구현)
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# 예시: fibonacci_naive(40)은 수십억 번의 연산 필요!
```

---

## 공간복잡도 종류와 예시

### 1. O(1) - 상수 공간 (Constant Space)
**특징**: 입력 크기와 관계없이 고정된 메모리 사용

```python
# 두 변수만 사용
def swap_variables(a, b):
    temp = a  # 추가 메모리: 1개 변수
    a = b
    b = temp
    return a, b

# 반복문으로 최댓값 찾기
def find_max_constant_space(arr):
    max_val = arr[0]  # 추가 메모리: 1개 변수
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```

### 2. O(n) - 선형 공간 (Linear Space)
**특징**: 입력 크기에 비례해서 메모리 사용

```python
# 새 배열 생성
def create_new_array(arr):
    new_arr = []  # 추가 메모리: n개 원소
    for num in arr:
        new_arr.append(num * 2)
    return new_arr

# 해시 테이블 사용
def count_frequency(arr):
    freq = {}  # 추가 메모리: 최대 n개 키-값 쌍
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq
```

### 3. O(log n) - 로그 공간 (Logarithmic Space)
**특징**: 주로 재귀 호출에서 사용

```python
# 이진 탐색 (재귀)
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# 스택 깊이: log n (재귀 호출 깊이)
```

### 4. O(n²) - 이차 공간 (Quadratic Space)
**특징**: 2차원 배열이나 모든 쌍을 저장할 때

```python
# 2차원 배열 생성
def create_matrix(n):
    matrix = []
    for i in range(n):      # n번 반복
        row = []
        for j in range(n):  # n번 반복
            row.append(i * j)
        matrix.append(row)
    return matrix  # 추가 메모리: n²개 원소

# 모든 쌍 저장
def store_all_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs  # 추가 메모리: n²개 쌍
```

---

## 실제 코드로 이해하기

### 🎯 문제: 배열에서 중복된 숫자 찾기

#### 방법 1: O(n²) 시간, O(1) 공간
```python
def find_duplicate_brute_force(arr):
    for i in range(len(arr)):           # O(n)
        for j in range(i + 1, len(arr)): # O(n)
            if arr[i] == arr[j]:
                return arr[i]
    return None

# 시간복잡도: O(n²) - 느림
# 공간복잡도: O(1) - 메모리 절약
```

#### 방법 2: O(n) 시간, O(n) 공간
```python
def find_duplicate_hash_set(arr):
    seen = set()  # 추가 메모리: O(n)
    for num in arr:  # O(n)
        if num in seen:
            return num
        seen.add(num)
    return None

# 시간복잡도: O(n) - 빠름
# 공간복잡도: O(n) - 메모리 사용
```

### 🤔 어떤 방법을 선택할까?

| 상황 | 추천 방법 | 이유 |
|------|-----------|------|
| 메모리가 부족한 환경 | 방법 1 | 공간복잡도 O(1) |
| 빠른 실행이 중요한 경우 | 방법 2 | 시간복잡도 O(n) |
| 데이터가 작은 경우 (n < 100) | 방법 1 | 차이가 미미함 |
| 데이터가 큰 경우 (n > 1000) | 방법 2 | 시간 차이가 큼 |

---

## 복잡도 비교표

### 📊 시간복잡도 성능 비교 (n = 1000 기준)

| 복잡도 | 연산 횟수 | 실제 시간 (추정) | 설명 |
|--------|-----------|------------------|------|
| O(1) | 1 | 0.001ms | 즉시 |
| O(log n) | 10 | 0.01ms | 매우 빠름 |
| O(n) | 1,000 | 1ms | 빠름 |
| O(n log n) | 10,000 | 10ms | 보통 |
| O(n²) | 1,000,000 | 1초 | 느림 |
| O(2ⁿ) | 2¹⁰⁰⁰ | 수십억 년 | 매우 느림 |

### 💾 공간복잡도 메모리 사용량 (n = 1000 기준)

| 복잡도 | 메모리 사용량 | 설명 |
|--------|---------------|------|
| O(1) | 8 bytes | 변수 몇 개 |
| O(log n) | 80 bytes | 재귀 스택 |
| O(n) | 8 KB | 배열 하나 |
| O(n²) | 8 MB | 2차원 배열 |

### 🎯 실무에서의 기준

#### 좋은 복잡도 (✅ 추천)
- **O(1)**: 해시 테이블 조회
- **O(log n)**: 이진 탐색, 균형 이진 트리
- **O(n)**: 배열 순회, 선형 탐색
- **O(n log n)**: 효율적인 정렬

#### 주의해야 할 복잡도 (⚠️ 신중히 사용)
- **O(n²)**: 작은 데이터에만 사용
- **O(n³)**: 매우 작은 데이터에만 사용

#### 피해야 할 복잡도 (❌ 피하기)
- **O(2ⁿ)**: 지수 시간 - 실용적이지 않음
- **O(n!)**: 팩토리얼 시간 - 더욱 비효율적

---

## 💡 마무리

### 핵심 포인트
1. **시간복잡도**: 알고리즘이 얼마나 빠른가?
2. **공간복잡도**: 알고리즘이 얼마나 메모리를 적게 쓰는가?
3. **트레이드오프**: 보통 시간과 공간 사이의 균형을 맞춰야 함
4. **실용성**: 이론보다는 실제 상황에 맞는 선택이 중요

### 다음 단계
- 실제 알고리즘 문제를 풀면서 복잡도 분석 연습
- 다양한 자료구조의 복잡도 이해
- 최적화 기법 학습

**기억하세요**: 완벽한 알고리즘보다는 문제 상황에 맞는 적절한 알고리즘을 선택하는 것이 더 중요합니다! 🚀
