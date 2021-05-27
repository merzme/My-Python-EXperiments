# Display the powers of 2 using anonymous function

terms = 20

# Uncomment code below to take input from the user
# terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(20)))

print("The total terms are:",20)
for i in range(20):
   print("2 raised to power",i,"is",result[i])
