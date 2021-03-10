import time
# num = int(input("Please enter a positive integer: "))
num = 20
snum = str(num) #num as a string


t0 = time.perf_counter()
t1 = time.perf_counter()
print("Running time: ", t1-t0, "sec")



#1st solution
m = num
cnt = 0
while m > 0:
	if m % 10 == 0:
		cnt = cnt + 1
	m = m // 10

#2nd solution
cnt = 0
snum = str(num) #num as a string
for digit in snum:
	if digit == "0":
		cnt = cnt + 1

#4th
cnt=0
for i in range(num):
	cnt = cnt + 1

