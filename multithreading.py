import threading

def PrintA():
    while True:
        print ("aa")

def PrintB():
    while True:
        print ("bb")

#create thread objects
thread1 = threading.Thread(target=PrintA)
thread2 = threading.Thread(target=PrintB)

thread1.start()
thread2.start()

