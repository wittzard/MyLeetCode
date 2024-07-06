class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for str in strs:
            sort_str = ''.join(sorted(str))
            if sort_str not in hash:
                hash[sort_str] = [str]
            else:
                hash[sort_str].append(str)

        ans = []
        for value in hash.values():
            ans.append(value)
            
        return ans