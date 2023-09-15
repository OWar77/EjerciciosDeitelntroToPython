"""
4.6 (Modified average Function) The average function we defined in Section 4.11
can receive any number of arguments. If you call it with no arguments, however, the func-
tion causes a ZeroDivisionError. Reimplement average to receive one required argu-
ment and the arbitrary argument list argument *args, and update its calculation
accordingly. Test your function. The function will always require at least one argument,
so you’ll no longer be able to get a ZeroDivisionError. When you call average with no
arguments, Python should issue a TypeError indicating "average() missing 1 required
positional argument."
"""

def average(arg1, *args):
    return (arg1 + sum(args)) / (1 + len(args))

