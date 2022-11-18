class take_skip:
   def __init__(self, step, count):
      self.step = step
      self.count = count
      self.iteretions = 0

   def __iter__(self):
      return self


   def __next__(self):
      if self.iteretions == self.count:
         raise StopIteration
      result = self.iteretions * self.step
      self.iteretions += 1
      return result





numbers = take_skip(2, 6)
for number in numbers:
   print(number)