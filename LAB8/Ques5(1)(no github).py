'''Use list comprehensions for the following.
1. Take a list of strings as input along with a sample string. Count the number of strings that 
contains the sample string as a substring. 
2. Take a list of integers as input. Find the square of only the +ve integers in the list, the rest 
are converted to 0s. 
3. Take a list of integers as input. Find the square of numbers that are in the range of 10-20, 
leave the rest as they are in the resultant list.
4. Take a list of strings as input, convert all the strings into upper case, if they have the first 
character as lower case, leave the rest as they are.'''

#part1 
inp_str = list(map(str, input().split()))
sample_str = "a"
count=0
aa = ["a" in x  for x in inp_str]
print(sum(aa))

#part 2 
inp_str = list(map(int, input().split()))
aa = [x**2 if x>0 else 0 for x in inp_str]
print(aa)

#part3
inp_str = list(map(int, input().split()))
aa = [x**2 if x>10 and x<20 else x for x in inp_str]
print(aa)

#part4
inp_str = list(map(str, input().split()))
aa = [x.upper() if x == x.lower() else x for x in inp_str]
print(aa)