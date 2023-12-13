from utility import take_input1
def ALG1():
  m,n,h,matrix = take_input1()
  result = [0 ,0, 0, 0]
  
  #Traversing through matrix
  for start_r in range(m):
    for start_col in range(n):

      # If no of trees in plot>=h, traverse through all squares starting from that plot
      if(matrix[start_r][start_col]>=h):
        end_r,end_col = start_r,start_col
        while (end_r< m and end_col<n):      
            flag = True

            #Traversing through square area to check whether every plot has no of trees >=h
            for i in range(start_r,end_r+1):
              for j in range(start_col, end_col+1):
                if matrix[i][j]>=h:
                  continue
                else:
                  flag = False
            
            #updating latest max square area
            if flag==True:
              temp = [start_r,start_col,end_r,end_col]
              temp_area = (end_r-start_r)*(end_col-start_col)
              max_area = (result[2]-result[0])*(result[3]- result[1])
              if max_area<temp_area:
                result= temp

            end_r+=1
            end_col+=1
  result  = [x + 1 for x in result]   
  return result
