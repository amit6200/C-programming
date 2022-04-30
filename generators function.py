


def fibo():
    first_num=0
    second_num=1
    while(True):
        next_val=first_num+second_num
        yield next_val
        first_num,second_num=second_num,next_val
        
        
        
g=fibo()
for value in range(10):
    print(next(g))