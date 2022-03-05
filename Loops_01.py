word= "operators"
prog_lst=["python", "java", "C", "C#", "C++", "prolog", "Haskell"]
prog_tup=("python", "java", "C", "C#", "C++", "prolog", "Haskell")

print(">>> Iterate a String.")
for letter in word:
    print(letter)

print(">>> Iterate a list.")
for languages in prog_lst:
    print( languages)

print(">>> Iterate a tuple.")
for progs in prog_tup:
    print(progs)

print(">>> Iterate a number range")
for value in range(1, 10):
    print(value)

print(">>> Iterate a Enumerated list")
for idx, lng in enumerate(prog_lst):
    print(f"{idx}.{lng}")
