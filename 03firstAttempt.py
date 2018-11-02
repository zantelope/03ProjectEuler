def largestPrimeFactor(n):

  ### initiate variables for largest known factor and current iteration factor
  largestFactor = 1
  currentFactor = 2
  
  ### while number is greater than one continue finding factors
  while n > 1:

    ### if currentFactor is a factor of n:
    ### change largestFactor to currentFactor
    ### divide n by currentFactor until it is not
    if n % currentFactor == 0:
      largestFactor = currentFactor
      n = n / currentFactor
      while n % currentFactor == 0:
        n = n / currentFactor
    ### increase currentFactor by 1 for next iteration
    currentFactor = currentFactor + 1

  ### return
  return largestFactor

print(largestPrimeFactor(600851475143))
