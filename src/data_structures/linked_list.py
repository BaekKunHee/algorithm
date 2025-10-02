"""
연결 리스트 구현
"""
from typing import Optional, Any


class ListNode:
    """연결 리스트 노드"""
    
    def __init__(self, val: Any = 0, next_node: Optional['ListNode'] = None):
        self.val = val
        self.next = next_node
    
    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class LinkedList:
    """연결 리스트"""
    
    def __init__(self):
        self.head: Optional[ListNode] = None
        self.size = 0
    
    def append(self, val: Any) -> None:
        """리스트 끝에 요소 추가"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, val: Any) -> None:
        """리스트 앞에 요소 추가"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, val: Any) -> bool:
        """값이 val인 첫 번째 노드 삭제"""
        if not self.head:
            return False
        
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def find(self, val: Any) -> bool:
        """값이 val인 노드가 있는지 확인"""
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
    
    def to_list(self) -> list:
        """리스트를 Python 리스트로 변환"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return f"LinkedList({self.to_list()})"


def create_linked_list(values: list) -> Optional[ListNode]:
    """리스트 값들로부터 연결 리스트 생성"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list:
    """연결 리스트를 Python 리스트로 변환"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
