from utility import take_input1
def ALG3():
  m,n,h,matrix = take_input1()
  result = [0 ,0, 0, 0]
  
  #create matrix to store sqaure_size 
  square_size = [[0 for x in range(n+1)] for x in range(m+1)]
  max_square = 0

  #Traversing through matrix
  for end_r in range(1,m+1):
    for end_col in range(1,n+1):
      if(matrix[end_r-1][end_col-1]>=h):
        square_size[end_r][end_col] = min(square_size[end_r-1][end_col],square_size[end_r-1][end_col-1],square_size[end_r][end_col-1])+1
        if(square_size[end_r][end_col]>max_square):
          max_square = square_size[end_r][end_col]
          result = [end_r-max_square+1, end_col-max_square+1,end_r,end_col]

  return result