import os, time, signal

def uselessFunction():
    print("Useless function is completed it's useless task successfully with the help of the child process! YAY!! ")

print("Parent pid: ", os.getpid() , "\n")

for i in range(1, 10):
    cpid = os.fork()
    if cpid == 0: # This block will work
        uselessFunction() # Child process does some useless work
        print("Child",i ,"pid: ", os.getpid())
        os.kill(os.getpid(), signal.SIGKILL) # Kill the current process which is the child
        print("I'm dead inside!!!") # This won't print because child process is dead now
    else:
        time.sleep(1)

os.kill(os.getpid(), signal.SIGKILL) # Kill the main process
