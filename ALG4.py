from utility import take_input1
def ALG4():

  m,n,h,matrix = take_input1()
  result = [0 ,0, 0, 0]

  dp = [[[0 for k in range(n+1)] for j in range(n+1)] for i in range(m+1)]
  max_square = 0
  
  for r in range(1,m+1):
    for c1 in range(1,n+1):
      val = 1 if matrix[r-1][c1-1] < h else 1+dp[r-1][c1][c1]
      for c2 in range(c1,n+1):
        dp[r][c1][c2] = 1 if val == 1 else 1+dp[r-1][c1][c2]
        temp_sq = dp[r-1][c1][c2] + 1 if c2-c1+1 == dp[r-1][c1][c2] + 1 else 1
        if(temp_sq > max_square):
          max_square = temp_sq
          result = [r-max_square+1,c2-max_square+1, r,c2]
        if matrix [r-1][c2-1] < h and c1!=c2:
          dp[r][c1][c2] = 1
          break
  return result