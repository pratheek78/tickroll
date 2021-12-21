import time
import webbrowser
import threading



def rickroll():
    x = 1
    while True:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        time.sleep(5)



threads = []


for i in range(50):
    t = threading.Thread(target=rickroll)
    t.daemon = True

    threads.append(t)


for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()