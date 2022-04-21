import time
import threading

# def sum_sqrs(start,end ):
# 	for x in range(start,end+1):
# 		sum+=x**2

# sum = 0
# start = 0
# # end = 1_000_000
# step = 1_000_000

# for i in range(1,11):
# 	sum_sqrs(start,end)
# 	start = end




# 	print(f'sum = {sum}')
# 333333283333335000000

# start = time.perf_counter()
# sum_sqrs()
# end = time.perf_counter()
# print(f'Total time: {end-start}')



import threading
import time


def worker():
	global counter

	time.sleep(1)
	lock.acquire()
	tmp = counter
	print("Before:",counter)
	counter = tmp + 1
	lock.release()
	print("After:",counter)



counter = 0
# create a lock
lock = threading.Lock()

# create some treads to count together:
thread_pool = []
for i in range(10):
  tr = threading.Thread(target=worker)
  tr.start()
  thread_pool.append(tr)

# wait for tread to finish:
for tr in thread_pool:
  tr.join()

print("Workers counted:", counter)