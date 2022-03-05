## Tuples ##
# ''' A tuple is an immutable sequence, which means that its contents cannot
# be changed. Each item that is stored in a tuple is called
# an element.
# 0. Tuples are not mutable, which means their elements cannot be changed.
# 1. Tuples do not support methods such as append, remove, insert, reverse, and sort.
# custom_tuple=( <object_01>, <object_02>, <object_03> ... <object_n> )


prog_tup=["python", "java", "C", "C#", "C++", "prolog", "Haskell"]
print(prog_tup[1])
print(prog_tup[-1])

prog_tup.append("perl")     # adds a new object at the end of the tuple.
print(prog_tup)
print(prog_tup[-1])

print(len(prog_tup))        # prints the number of elements on the tuple.

# tuples() are iterable objects.
for idx, value in enumerate(prog_tup):
    print(f"{idx}:{value}")
