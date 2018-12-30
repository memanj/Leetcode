__author__ = 'MACvati'

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        result_dict = {}
        for i, line_list in enumerate(board):
            for j, element in enumerate(line_list):
                if element == ".":
                    continue

                if element in result_dict:
                    for result_list in result_dict[element]:
                        if result_list[0] == i or result_list[1] == j or  result_list[2] == (i//3, j//3):
                            print(element)
                            return False
                    result_dict[element].append([i, j, (i//3, j//3)])
                else:
                    result_dict[element] = [[i, j, (i//3, j//3)]]
        return True


def main():
    obj = Solution()
    board = [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    print(obj.isValidSudoku(board=board))


if __name__ == '__main__':
    main()