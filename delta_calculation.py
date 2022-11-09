import math

def function_quadratic_roots(a,b,c):
  delta = b*b - 4*a*c
  if delta > 0:
    x1 = round((- b - (math.sqrt(delta)))/2/a,5)
    x2 = round((- b + (math.sqrt(delta)))/2/a,5)
    print(f'wartość x1 to: {x1}, wartość x2 to: {x2}')
  elif delta == 0:
    x1 = round(-b/2/a,5)
    print(f'wartość x to: {x1}')
  else:
    print('brak rozwiązań')

function_quadratic_roots(4,8,4)









