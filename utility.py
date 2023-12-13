def take_input1():
  m,n,h = [int(x) for x in input().split(' ')]
  
  matrix = []
  for i in range(m):
    temp = [int(x) for x in input().split(' ')]
    matrix.append(temp)

  return m,n,h,matrix


def take_input2():
  m,n,h,k = [int(x) for x in input().split(' ')]
  
  matrix = []
  for i in range(m):
    temp = [int(x) for x in input().split(' ')]
    matrix.append(temp)

  return m,n,h,k,matrix