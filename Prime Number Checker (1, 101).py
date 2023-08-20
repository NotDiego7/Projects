# #Primes are only divisible by 1 and itself

# number = int(input("Enter the number you want to check. "))
# end_of_check = False
# check = 0

# while not end_of_check:
#   for iterance in range(1, number + 1):
#       if number % iterance == 0:
#         check += 1
#   if check > 2 or number == 1:
#     end_of_check = True
#     print("It is not a prime.")
#   else:
#       end_of_check = True
#       print("It is a prime.")

#Write your code below this line 👇

def prime_checker(number):
  end_of_check = False
  check = 0

  while not end_of_check:
    for iterance in range(1, number + 1):
        if number % iterance == 0:
          check += 1
    if check > 2 or number == 1:
      end_of_check = True
      print("It's not a prime number.")
    else:
        end_of_check = True
        print("It's a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
