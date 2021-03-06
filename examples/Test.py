#!/usr/bin/env python

# ----------
# Strings.py
# ----------

print "Strings.py"

assert type('abc') is str
assert len('abc')  == 3

assert type("abc") is str
assert len("abc")  == 3

assert type(r'abc') is str
assert len(r'abc')  == 3

assert type(r"abc") is str
assert len(r"abc")  == 3

assert type('''abc''') is str
assert len('''abc''')  == 3

assert type("""abc""") is str
assert len("""abc""")  == 3

assert len('a\nb') == 3
assert len("a\nb") == 3

assert len(r'a\nb') == 4
assert len(r"a\nb") == 4

assert len('''a\nb''') == 3
assert len("""a\nb""") == 3

assert len('a\
b') == 2
assert len("a\
b") == 2

assert len(r'a\
b') == 4
assert len(r"a\
b") == 4

assert len('''a
b''') == 3
assert len("""a
b""") == 3

assert "abc"      is     "abc"
assert str("abc") is     str("abc") is "abc"
assert "ab" + "c" is     "ab" + "c" is "abc"
assert str(True)  is     str(True)
assert str(9)     is     str(9)
assert str(10)    is not str(10)
assert str(10)    ==     str(10)
assert str(2L)    is not str(2L)
assert str(2L)    ==     str(2L)
assert str(2.34)  is not str(2.34)
assert str(2.34)  ==     str(2.34)

assert "bcd"     in "abcde"
assert "xyz" not in "abcde"

assert "" is ""

s = "abc"
t = str(s)
assert s is t

s = "abcde"
t = s[:]
assert s is t

s = "abc"
t = s
assert s is t
s += "d"
assert s == "abcd"
assert t == "abc"

s = "abCbA"
t = s.upper()
assert s == "abCbA"
assert t == "ABCBA"

s = "ABCBA"
t = s.upper()
assert s is not t
assert s ==     t

s = "abCbACb"
n = s.find("Cb")
assert s == "abCbACb"
assert n == 2

s = "abCbACb"
n = s.find("Cx")
assert s == "abCbACb"
assert n == -1

s = "abCbACb"
n = s.rfind("Cb")
assert s == "abCbACb"
assert n == 5

s = "abCbACb"
t = s.replace("Cb", "Xy")
assert s == "abCbACb"
assert t == "abXyAXy"

s = "abCbACb"
t = s.replace("Cx", "Xy")
assert s is t

s = "abCbACb"
t = s.replace("Cb", "Xy", 1)
assert s == "abCbACb"
assert t == "abXyACb"

print "Done."
