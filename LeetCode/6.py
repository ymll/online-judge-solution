class Solution:        
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        output = ""
        if (len(s) == 1) or (numRows == 1):
            return s
        '''
        P     I     N
        A   L S   I G
        Y A   H R
        P     I
        
        0  6  2 # row0: 0 + 2*3 or 2*0
        1 57 13 # row1: 1 + 2*2 or 2*1
        24 80 4 # row2: 2 + 2*1 or 2*2
        3  9  5 # row3: 3 + 2*0 or 2*3
        '''
        for row in range(numRows):
            # print('row:{}, numRows: {}'.format(row, numRows))
            idx = row
            turn_flag = True
            skip_output = False
            while True:
                try:
                    if not skip_output:
                        output += s[idx]
                    # print('output:{}, idx:{}'.format(output, idx))
                    if turn_flag:
                        next_idx = 2 * (numRows-1-row)
                    else:
                        next_idx = 2 * row
                    if next_idx > 0:
                        idx += next_idx
                        skip_output = False
                    else:
                        skip_output = True
                    turn_flag = not turn_flag
                except IndexError:
                    break
        return output
