# Leap year 

"""
year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0

"""
def isLeapyear(year):
 if (year % 4 == 0 and year % 100!= 0) or year % 400 == 0:
   return True 
 else:
   return False 
year=2000

if isLeapyear(year):
  print('{} is a Leap Year.'.format(year))
else:
  print('{} is not a Leap Lear.'.format(year))
   
  