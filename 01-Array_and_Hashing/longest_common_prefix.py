class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0];

        my_map = {}
        for s in strs:       # for string in strings
            temp = ""
            for c in s:     # for character in string
                temp += c
                if temp is not map:
                    my_map[temp] = my_map.get(temp, 0) + 1
        print(my_map)

        res = ""
        max_val = len(strs)
        for k, v in my_map.items():
            if v == max_val and len(k) > len(res):
                res = k
        return res

        
        
