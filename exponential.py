import time
start=time.time()

num=1e9

num1=100.001e1

num2=100.001e-5

print(num) # 1000000000.0
print(num1) # 1000.01
print(num2) # 0.00100001
print(round(num2,5)) # 0.001
end=time.time()
print('time:', end-start) # time: 7.200241088867188e-05


    