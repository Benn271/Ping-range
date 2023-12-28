import sys
from cli_args_system import Args
import h
import checkip
import running

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

    print(f'start: {Start_Ip}')
    print(f'end: {End_Ip}')
    print("starting.....")
    print("")

    if checkip.check(Start_Ip) and checkip.check(End_Ip):
        running.run(Start_Ip, End_Ip)
   
    sys.exit()
    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interupt")
        sys.exit()



