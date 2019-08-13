"""
1. We want a fuction that takes a parameter called degrees
2. sutract 32 from the number in degrees
3. Then multiply by five from the number in degrees
4. After divide by nine from the number in degrees
5. Print final answer
"""

def convert_f_to_c(f):
  f = f - 32
  f = f * 5
  c = f / 9
  print(c)
  
convert_f_to_c(84)
