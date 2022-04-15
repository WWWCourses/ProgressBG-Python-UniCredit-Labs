import threading
import multiprocessing
import time

counter = 0

def worker():
	global counter
	print("Before:",counter)
	counter += 1

	sum = 0
	for x in range(1, 5_000_000):
		sum += x**x

	print("After:",counter)


if __name__ == '__main__':
	processes = []
	for x in range(1,6):
		pr = multiprocessing.Process(target=worker)
		processes.append(pr)
		pr.start()


	for tr in processes:
		tr.join()

	print(f'counter: {counter}')

	print('End')