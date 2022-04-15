# sum = 0

# for x in range(1, 5_000_000):
# 	sum += x**x


import threading
import time


def worker(x):
  tid = threading.current_thread().name;
  print(f"x = {x} in {tid}")
  # I/O bound task
  time.sleep(2)
  print(f'{tid} ends')

# create the tread
def main():
	threads = []
	for x in range(1, 6):
		# worker(x)

		t = threading.Thread(target=worker, args=(x,))
		threads.append(t)
		t.start()
		t.join()


if __name__ == '__main__':
	start = time.perf_counter()
	main()
	end = time.perf_counter()
	print(f'Finished in {end - start:0.4f} seconds')