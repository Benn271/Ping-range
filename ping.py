import sys
from cli_args_system import Args
import Backend_Code.h as h
import Backend_Code.checkip as checkip
import Backend_Code.running as running
import pyfiglet
import os

os.popen(f"clear").read()
# art
T = "Ping Range"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)

def main():
    if len(sys.argv) < 2:
        print("must have a arg")
        sys.exit()
    elif "-h" in sys.argv or "--help" in sys.argv:
        h.help()
        sys.exit()

    args = Args(convert_numbers=False)

    Start_Ip = args.flag_str('si','start_ip','start')
    End_Ip = args.flag_str('ei','end_ip', 'end')

    if Start_Ip == None or End_Ip == None:
        print("Must have both start and end ip addresses")
        sys.exit()

    print(f'start: {Start_Ip}')
    print(f'end: {End_Ip}')
    print("starting.....")
    print("")

    if checkip.check(Start_Ip) and checkip.check(End_Ip):
        running.run(Start_Ip, End_Ip)
    else:
        sys.exit()
    
    print("Finished")
    print("Results are in ping_output.txt")
    print("")
    sys.exit()
    


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interupt")
        sys.exit()
