__author__ = 'MACvati'

"""
Notes:
Make sure to consider count for the first digit (self.findDiff(N-1, K, i, current_number_list)
Submission failed due to duplicate elements list(set(current_number_list))
Need to read about DFS
"""

class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """

        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        current_number_list = []
        for i in range(1,10):
            self.findDiff(N-1, K, i, current_number_list)
        return list(set(current_number_list))

    def findDiff(self, N, K, current_number, current_number_list):
        if not N:
            current_number_list.append(current_number)
            return
        last_digit = current_number % 10
        if last_digit-K >= 0:
            self.findDiff(N-1, K, current_number*10 + last_digit-K, current_number_list)
        if last_digit+K <= 9:
            self.findDiff(N-1, K, current_number*10 + last_digit+K, current_number_list)

def main():
    obj = Solution()
    print(obj.numsSameConsecDiff(2, 3))


if __name__ == '__main__':
    main()
