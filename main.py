import func1
import func2

m = func1.math_class(10,4)
print("{} + {} = {}".format(m.mem1,m.mem2,m.sum()))
print("AVG({},{}) = {}".format(m.mem1,m.mem2,m.avg()))
print("SUM: "+str(func1.sum(m.mem1,m.mem2)))
print("AVG: "+str(func1.avg(m.mem1,m.mem2)))
print(func2.sub(9,2))