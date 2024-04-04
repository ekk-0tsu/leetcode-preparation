# First solution to use a queue to traverse the tree level by level
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root.children])
        ans = [[root.val]]
        created = set()
        
        while q:
            arr = []
            for _ in range(len(q)):
                for item in q.popleft():
                    arr.append(item.val)
                    q.append(item.children)

            if arr:
                ans.append(arr)
            
        return ans

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q = deque([(root, 0)])
        ans = [[]]
        
        while q:
            node, level = q.popleft()
            # If the level is greater than the length of the answer array
            # then we need to add a new array to the answer array, because
            # we are now at a new level
            if len(ans) == level:
                ans.append([])

            ans[level].append(node.val)
            for child in node.children:
                q.append((child, level + 1))

        return ans

