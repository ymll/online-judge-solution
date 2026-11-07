class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        max_length = 0
        words.sort()
        print(words)
        dict_tree = {}
        '''
        python tree structure
        {
          m0:
          {
            m1: {},
            m2: {}
          }
        }
        '''
        for w in words:
            
            if len(w) == 1:
                d[w] = {}
            else:
                pass
                # search the tree
                # if next element not exist in the tree -> pass
                # else add the next element to the tree
