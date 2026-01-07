class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }

        result = []

        def dfs(i, state):
            if i == len(digits):
                result.append(''.join(state))
                return
            
            for char in mapping[digits[i]]:
                state.append(char)
                dfs(i+1, state)
                state.pop()

        dfs(0, [])

        return result
        