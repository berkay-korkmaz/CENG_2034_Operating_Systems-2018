import os, time, signal

def uselessFunction():
    print("Useless function is completed it's useless task successfully with the help of the child process! YAY!! ")

print("Parent pid: ", os.getpid() , "\n")

cpid = os.fork()
for i in range(10):
    if cpid == 0: # This block will work
        uselessFunction()
        print("Child",i ,"pid: ", os.getpid())
        os.kill(os.getpid(), signal.SIGKILL) # Kill the current process which is the child
        print("I'm dead inside!!!") # This won't print because child process is dead now
    else: # Create a child process every iteration
        time.sleep(1)
        cpid = os.fork()

os.kill(os.getpid(), signal.SIGKILL) # Kill the main process
