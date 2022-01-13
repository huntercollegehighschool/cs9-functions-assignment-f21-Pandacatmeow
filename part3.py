"""
******
PART 3
******
The factorial function is defined below.

Define the combination function which takes two integer arguments, n and r, which represent the number of objects and the number to choose respectively. The function RETURNS (not print) how many combinations are possible. Return it as an integer (// may help here)

You are expected to call the defined factorial function inside the combination definition

The combination formula: n! / (r! * (n-r)!)  (! is factorial)
"""

# do not change the factorial function
def factorial(number):
  product = 1
  for i in range(1, number + 1):
    product *= i
  return product


def combination(n, r):  # do not change this line
  def factorial(number):
    product = 1
    for n in range(1, number + 1):
      product *= n
    return product
    product = 1
    for r in range(1, number + 1):
      product *= r
    return product

"""
I'm a bit confused as to what I'm supposed to do with the code, I thought I would need to define the factorials for n and r so I could implement them into the return equation but the code doesn't seem to be working and I can't figure it out. I've changed it like 12 times, even rewriting it a couple times but I can't figure out how to make it operational. Also, I forgot to ask this last class but is the homework graded based on completion or being fully functional?
"""