"""
이진 트리 구현
"""
from typing import Optional, List, Any
from collections import deque


class TreeNode:
    """이진 트리 노드"""
    
    def __init__(self, val: Any = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class BinaryTree:
    """이진 트리"""
    
    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root
    
    def insert(self, val: Any) -> None:
        """레벨 순서로 삽입"""
        if not self.root:
            self.root = TreeNode(val)
            return
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            
            if not node.left:
                node.left = TreeNode(val)
                return
            elif not node.right:
                node.right = TreeNode(val)
                return
            else:
                queue.append(node.left)
                queue.append(node.right)
    
    def inorder_traversal(self) -> List[Any]:
        """중위 순회 (Left -> Root -> Right)"""
        result = []
        
        def _inorder(node: Optional[TreeNode]) -> None:
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        
        _inorder(self.root)
        return result
    
    def preorder_traversal(self) -> List[Any]:
        """전위 순회 (Root -> Left -> Right)"""
        result = []
        
        def _preorder(node: Optional[TreeNode]) -> None:
            if node:
                result.append(node.val)
                _preorder(node.left)
                _preorder(node.right)
        
        _preorder(self.root)
        return result
    
    def postorder_traversal(self) -> List[Any]:
        """후위 순회 (Left -> Right -> Root)"""
        result = []
        
        def _postorder(node: Optional[TreeNode]) -> None:
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.val)
        
        _postorder(self.root)
        return result
    
    def level_order_traversal(self) -> List[Any]:
        """레벨 순회 (BFS)"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def max_depth(self) -> int:
        """트리의 최대 깊이"""
        def _max_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(_max_depth(node.left), _max_depth(node.right))
        
        return _max_depth(self.root)
    
    def is_balanced(self) -> bool:
        """균형 잡힌 트리인지 확인"""
        def _check_balance(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = _check_balance(node.left)
            if left_height == -1:
                return -1
            
            right_height = _check_balance(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return _check_balance(self.root) != -1


def create_binary_tree(values: List[Any]) -> Optional[TreeNode]:
    """리스트 값들로부터 이진 트리 생성 (레벨 순서)"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def binary_tree_to_list(root: Optional[TreeNode]) -> List[Any]:
    """이진 트리를 레벨 순서 리스트로 변환"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # 끝의 None 값들 제거
    while result and result[-1] is None:
        result.pop()
    
    return result
