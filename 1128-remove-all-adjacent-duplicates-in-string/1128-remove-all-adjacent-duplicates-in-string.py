class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if item not in stack:
                stack.append(item)
            else:
                if item == stack[-1]:
                    stack.pop()
                else:
                    stack.append(item)
                    
        return "".join(stack)