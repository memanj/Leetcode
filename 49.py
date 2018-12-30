class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            print(key)
            print(d)
            print(d.get(key, []))
            d[key] = d.get(key, []) + [w]
        return d.values()

def main():
    obj = Solution()
    print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    main()