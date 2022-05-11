class Counter:
    count:int = 1


counter:Counter = Counter()
counter2:Counter = Counter()

print(counter.count)
Counter.count = Counter.count + 1
print(counter.count)
counter2.count = 5
print(counter.count)
print(counter.__dict__)
print(counter2.__dict__)