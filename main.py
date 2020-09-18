# Author: Jasmine Sandhu jps6818@psu.edu
# Collaborator: Nick Orf nco5067@psu.edu
# Collaborator: Emma Dischner etd5123@psu.edu
# Collaborator: Hao Chen hzc5424@psu.edu
# Section: 10
# Breakout: 2

def sum_n(n):
  if n == 0:
    return 0
  else: 
    return n + sum_n(n-1)

def print_n(s, n):
  if n == 0:
    return
  else:
    print(s)
    print_n(s, n-1)

def run():
  n = input ("Enter an int: ")
  n = int(n)
  print (f"sum is {sum_n(n)}.")
  s = input ("Enter a string: ")
  print_n(s, n)

if __name__ == "__main__":
  run()