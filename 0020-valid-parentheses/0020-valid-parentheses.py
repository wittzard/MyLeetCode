class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char in mapping:
                # if it close bracket check if stack is empty, check its couple
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)

        return not stack # check case open bracket only '(((('                  

        