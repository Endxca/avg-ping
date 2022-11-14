import requests
import time
import sys

pings = []
while True:
    t1 = time.time()
    try:
        r = requests.get("http://1.1.1.1")
        t2 = time.time()
        resp = t2-t1
    except KeyboardInterrupt:
    # quit
        print("[+]Exiting...",end="\n")
        sys.exit()
    except requests.exceptions.Timeout:
        print("[-]Timed out",end="\n")
        resp=10
    pings.append(resp)
    avg = round((sum(pings)/len(pings))*1000,2)
    print("[+]avg ping:",avg,end="ms\r")
    if len(pings)>100:
        print(f"max: {round(max(pings),2)}s, min: {round(min(pings)*1000,2)}ms, avg: {avg}ms",end="\n")
        pings=[]
