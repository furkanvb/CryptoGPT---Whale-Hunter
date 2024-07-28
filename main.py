from multiprocessing import Process, Queue
from time import sleep
from bot import startbot

queue = Queue()

def mp_worker(queue):

	while queue.qsize() > 0:
		record = queue.get()
		startbot(record)
	queue.close()
	print("BOT WAITING 30 SECONDS")

def mp_handler():
    processes = [Process(target=mp_worker, args=(queue,)) for _ in range(1)]

    for process in processes:
        process.start()
        print('BOT STARTED!')

    for process in processes:
        process.join()
	
    for process in processes:
        process.close()


if __name__ == '__main__':
	while True:
		with open('coinlist.csv', 'r') as f:
			id_list = f.read().splitlines()
				
			for i in id_list:
				i = i.replace('\n',	'')
				queue.put(i)
			mp_handler()
		f.close()
		sleep(30)