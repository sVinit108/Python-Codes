s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s)) # 20 & 20.0 is counted as one.