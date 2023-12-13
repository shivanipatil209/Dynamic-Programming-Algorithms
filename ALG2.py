from utility import take_input1
def ALG2():
  m,n,h,matrix = take_input1()
  result = [0 ,0, 0, 0]

  #Traversing through matrix
  for start_r in range(m):
    for start_col in range(n):

      '''
       # If no of trees in plot>=h, increasing square plot size by one r and one column
       # and checking no of trees in only newly added r and col
       '''

      if(matrix[start_r][start_col]>=h):
        flag = True
        square_size= 0
        end_r,end_col = start_r,start_col
        while (end_r< m and end_col<n and flag):

          for j in range(start_col,end_col+1):
            if matrix[end_r][j] < h:
              flag = False
              break
            
          for i in range(start_r,end_r+1):
            if matrix[i][end_col] < h:
              flag=False
              break

          #updating latest max square area    
          if flag==True:
            temp = [start_r,start_col,end_r,end_col]
            temp_area = (end_r-start_r)*(end_col-start_col)
            max_area = (result[2]-result[0])*(result[3]- result[1])
            if max_area<temp_area:
              result= temp
            
            end_r,end_col = start_r+square_size,start_col+square_size
            square_size+=1

  result  = [x + 1 for x in result]        
  return result
