class PrimeChecker(object):
  def __init__(self, number):
    self.num = number
  def is_prime(self):
    a=2
    while self.num > a :
      if self.num%a==0 & a!=self.num:
        return False
        a=a+1
      else:
        return True
        a=(self.num)+1

print(PrimeChecker(5).is_prime())