
import os, sys, atexit, time

def main():
	pid = os.fork() 
	if pid > 0:
		sys.exit()

	os.chdir('/')
	os.setsid()
	os.umask(0)

	f = open('/dev/null', 'w')
	def close_f():
		f.close()
	
	sys.stdin = f
	sys.stdout = f
	sys.stderr = f

	atexit.register(close_f)

	while True:
		time.sleep(1)

if __name__ == '__main__':
	main()

