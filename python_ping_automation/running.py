import os
import sys

def run(start_ip, end_ip):
    start_num = start_ip.split(".")
    end_num = end_ip.split(".")
    start3 = start_num[0:3]
    startend3 = end_num[0:3]

    if start3 != startend3:
        print("Ip adresses must have the same starting 3 octets")
        sys.exit()
    elif int(start_num[-1]) > int(end_num[-1]):
        print("End can't be smaller than the start")
        sys.exit()

    for k in range(int(start_num[-1]), int(end_num[-1])+1):
        ip = str(start3[0]) + "." + str(start3[1]) + "." + str(start3[2]) + "." + str(k)
        ping(ip)




def ping(ip):
    print(os.popen(f"ping {ip}").read())
    print("")

