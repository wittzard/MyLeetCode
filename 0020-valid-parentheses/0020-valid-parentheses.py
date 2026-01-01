class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = ['()','{}','[]']

        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                if not stack: # check if close bracket and stack is empty
                    return False
                else:
                    if stack.pop() + char not in valid:
                        return False
        
        return not stack # check if stack is empty if it have remaining like '((('
                    

        