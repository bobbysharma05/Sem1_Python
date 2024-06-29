'''A program that takes a string as input and checks where the string is a pangram or not.
 Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
 For example : "The quick brown fox jumps over the lazy dog"'''

n = "The quick brown fox jumps over the lazy dog"
ss = ""
count=0
for i in n:
    if i not in ss:
        ss+=i

ss = ss.upper()
print(ss)
for i in  [chr(v) for v in range(65,91)]:
    count+=1
if count==26:
    print("poppy")
else:
    print("blahhh")    