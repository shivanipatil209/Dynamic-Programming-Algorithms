from utility import take_input1
def ALG5A():
    m, n, h, matrix = take_input1()
    def TopLeftCorner(matrix, dpD, r, c, h):
        # Check if element is 0
        if matrix[r][c] < h:
            dpD[r][c] = 1
        elif matrix[r][c-1] < h or matrix[r-1][c] < h:
            dpD[r][c] = 1
        else:
            if dpD[r][c-1] == -1:
                    TopLeftCorner(matrix, dpD, r, c-1, h)
            if dpD[r-1][c] == -1:
                    TopLeftCorner(matrix, dpD, r-1, c, h)
            if dpD[r-1][c-1] == -1:
                    TopLeftCorner(matrix, dpD, r-1, c-1, h)
            dpD[r][c] = min(dpD[r][c-1], dpD[r-1][c], dpD[r-1][c-1])+1

    def TopRightCorner(matrix, dpR, r, c, h):
            # Check if element is 0
            if matrix[r][c] < h:
                dpR[r][c] = 1
            elif matrix[r-1][c-1] < h or matrix[r][c-1] < h:
                dpR[r][c] = 1
            else:
                if dpR[r][c-1] == -1:
                        TopLeftCorner(matrix, dpR, r, c-1, h)
                if dpR[r-1][c] == -1:
                        TopLeftCorner(matrix, dpR, r-1, c, h)
                if dpR[r-1][c-1] == -1:
                        TopLeftCorner(matrix, dpR, r-1, c-1, h)
                dpR[r][c] = min(dpR[r][c-1], dpR[r-1][c], dpR[r-1][c-1])+1

    def BottomLeftCorner(matrix, dpL, r, c, h):
            # Check if element is 0
            if matrix[r][c] < h:
                dpL[r][c] = 1
            elif matrix[r-1][c-1] < h or matrix[r-1][c] < h:
                dpL[r][c] = 1
            else:
                if dpL[r][c-1] == -1:
                        TopLeftCorner(matrix, dpL, r, c-1, h)
                if dpL[r-1][c] == -1:
                        TopLeftCorner(matrix, dpL, r-1, c, h)
                if dpL[r-1][c-1] == -1:
                        TopLeftCorner(matrix, dpL, r-1, c-1, h)
                dpL[r][c] = min(dpL[r][c-1], dpL[r-1][c], dpL[r-1][c-1])+1
    rs, cs = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
    dp = [[0]*cs for _ in range(rs)]
    dpR = [[-1]*cs for _ in range(rs)]
    dpD = [[-1]*cs for _ in range(rs)]
    dpL = [[-1]*cs for _ in range(rs)]

    for i in range(rs):
        for j in range(cs):
            if i==0 or j==0:
                dp[i][j] = 1
                dpD[i][j] = 1
                dpR[i][j] = 1
                dpL[i][j] = 1
            else:
                if dpD[i-1][j-1] == -1:
                    TopLeftCorner(matrix, dpD, i-1, j-1, h)
                if dpR[i-1][j] == -1:
                    TopRightCorner(matrix, dpR, i-1, j, h)
                if dpL[i][j-1] == -1:
                    BottomLeftCorner(matrix, dpL, i, j-1, h)
                dp[i][j] = min(dpD[i-1][j-1], dpR[i-1][j], dpL[i][j-1])+1
    
    maxSquareSize = 0
    for r in range(len(dp)):
        for c in range(len(dp[0])):
            if dp[r][c] >= maxSquareSize:
                maxSquareSize = dp[r][c]
                max_square = dp[r][c]
                result = [r-max_square + 1, c - max_square + 1,r,c]
    result  = [x + 1 for x in result]  
    return result

# Task 5B - Bottom Up DP for Problem 2 in O(mn)
def ALG5B():
  m,n,h,matrix = take_input1()
  rows, cols = m,n if len(matrix) > 0 else 0

  # Pad original matrix with 0's for simplicity
  for i in range(rows):
      matrix[i].insert(0,0)
  matrix.insert(0,[0 for i in range(cols+1)])

  dp = [[0] * (cols + 1) for _ in range(rows + 1)]
  dpT = [[0] * (cols + 1) for _ in range(rows + 1)]
  dpL = [[0] * (cols + 1) for _ in range(rows + 1)]
  dpD = [[0] * (cols + 1) for _ in range(rows + 1)]

  for i in range(1, rows+1):
      for j in range(1, cols+1):
          if i == 1 or j == 1:
              dpT[i][j] = 1
          else:
              if matrix[i][j] < h:
                  dpT[i][j] = 1
              elif matrix[i-1][j-1] < h or matrix[i][j-1] < h:
                  dpT[i][j] = 1
              else:
                  dpT[i][j] = min(dpT[i][j-1], dpT[i-1][j], dpT[i-1][j-1])+1
  
  for i in range(1, rows+1):
      for j in range(1, cols+1):
          if i == 1 or j == 1:
              dpL[i][j] = 1
          else:
              if matrix[i][j] < h:
                  dpL[i][j] = 1
              elif matrix[i-1][j-1] < h or matrix[i-1][j] < h:
                  dpL[i][j] = 1
              else:
                  dpL[i][j] = min(dpL[i][j-1], dpL[i-1][j], dpL[i-1][j-1])+1

  for i in range(1, rows+1):
      for j in range(1, cols+1):
          if i == 1 or j == 1:
              dpD[i][j] = 1
          else:
              if matrix[i][j] < h:
                  dpD[i][j] = 1
              elif matrix[i][j-1] < h or matrix[i-1][j] < h:
                  dpD[i][j] = 1
              else:
                  dpD[i][j] = min(dpD[i][j-1], dpD[i-1][j], dpD[i-1][j-1])+1
  
  maxSquareSize = 0
  result = [0,0,0,0]
  for r in range(1, rows+1):
      for c in range(1, cols+1):
          if r == 1 or c == 1:
              dp[r][c] = 1
          else:
              dp[r][c] = min(dpD[r-1][ c-1], dpT[r-1][c], dpL[r][c-1])+1
          if dp[r][c] >= maxSquareSize:
              maxSquareSize = dp[r][c]
              max_square = dp[r][c]
              result = [r-max_square + 1, c - max_square + 1,r,c]
  return result
