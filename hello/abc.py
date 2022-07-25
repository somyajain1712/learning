def add_sum(func):
    def wrapper(*args,**kwargs):
        l=[]
        for i in args:
            l.append(i)
        for k,v in kwargs.items():
            l.append(v)
        sum1 = sum(l)
        with open('abc.txt','a') as file:
            file.write(func(*args)+' '+str(sum1)+'\n')
        return (sum1)
    return wrapper


@add_sum
def add(q,z):
    return f"sum: {q+z}"


print(add(5,1,x=10,y=10))
print(add(1,3))
