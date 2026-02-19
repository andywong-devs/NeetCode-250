class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in my_map:
                my_map[key] = []
            my_map[key].append(s)
        return list(my_map.values())

