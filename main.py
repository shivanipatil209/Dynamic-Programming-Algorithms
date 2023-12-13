
import sys
import ALG1, ALG2, ALG3, ALG4,ALG5,ALG6

if __name__ == "__main__":
  # Invoking tasks

  if sys.argv[1] == "ALG1":
      output = ALG1.ALG1()
  elif sys.argv[1] == "ALG2":
      output = ALG2.ALG2()
  elif sys.argv[1] == "ALG3":
      output = ALG3.ALG3()
  elif sys.argv[1] == "ALG4":
      output = ALG4.ALG4()
  elif sys.argv[1] == "ALG5A":
      output = ALG5.ALG5A()
  elif sys.argv[1] == "ALG5B":
      output = ALG5.ALG5B()
  elif sys.argv[1] == "ALG6":
      output = ALG6.ALG6()
  
  print(" ".join(str(element) for element in output))