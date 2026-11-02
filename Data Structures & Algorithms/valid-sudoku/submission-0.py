class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np
        def valid(lst):
            valid = True
            prev = []
            for i in lst:
                if i != ".":
                    if int(i) < 10:
                        if i in prev:
                            print("Duplicate")
                            valid = False
                            return valid
                        prev.append(i)

            return valid


        rows = False
        cols = False
        boxs = False
        transposed = np.array(board).T.tolist()
        boxes = []
        for i in range(9):
            boxes.append([])
        
        a = 0
        b = 3
        c= 0
        d= 3
        for z in range(0,3):
            a = 0
            b = 3    
            for i in range(3):
                for j in range(a,b):
                    for k in range(c,d):
                        boxes[(i+3*z)].append(board[j][k])
            
                a += 3
                b += 3
            c +=3
            d += 3

        # print(boxes)

        for row_i in range(len(board)):
            rows = valid(board[row_i])
            cols = valid(transposed[row_i])
            boxs = valid(boxes[row_i])
            print(rows,cols,boxs)
            if (rows and cols and boxs) != True:
                return False
        
        return True

        
        
        
