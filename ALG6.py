from utility import take_input2
def ALG6():
  m,n,h,k,matrix = take_input2()
  result = [0,0,0,0]
  #Traversing through matrix
  for start_r in range(m):
    for start_col in range(n):

      #traverse through all squares starting from the plot
      increament = 1
      end_r,end_col = start_r,start_col
      
      while (end_r< m and end_col<n):      
          count = 0

          #Traversing through square area and keeping count of plot where no of trees<h
          for i in range(start_r,end_r+1):
            for j in range(start_col, end_col+1):
              if matrix[i][j]>=h:
                continue
              
              else:
                count+=1
                
          
          #updating latest max square area
          if count<=k:
            temp = [start_r,start_col,end_r,end_col]
            temp_area = (end_r-start_r)*(end_col-start_col)
            max_area = (result[2]-result[0])*(result[3]- result[1])
            if max_area<temp_area:
              result= temp
          end_r+=increament
          end_col+=increament
  result  = [x + 1 for x in result] 
  return result