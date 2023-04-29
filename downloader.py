import paramiko
import sys, os
from time import sleep




def get_screen_programs():

    # # Load the SSH configuration
    # with open("/home/abdullah/.ssh/config") as f:
    #     config = paramiko.SSHConfig()
    #     config.parse(f)



    # prit

    # # Get the hostname and identity file from the configuration
    # hostname = config.get("default", {}).get("hostname")
    # identity_file = config.get("default", {}).get("identity_file")

    # print(hostname)

    # sys.exit(1)


    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('c220g5-110903.wisc.cloudlab.us', username="abdffsm", key_filename="/home/abdullah/.ssh/y")

    # Execute the screen command
    stdin, stdout, stderr = client.exec_command("screen -ls")

    # Get the output of the command
    screen_programs = stdout.readlines()

    # Close the SSH client
    client.close()

    return screen_programs

if __name__ == "__main__":

    while True:
        
        # Get the list of screen programs
        screen_programs = get_screen_programs()

        # Print the list of screen programs
        if "1 Socket in" in " ".join(screen_programs):
            print(" ".join(screen_programs))
            sleep(20*60)
        else:
            break        

    print("ready to download")
    os.system("scp n1-gpu:job_simulator/experiment_10.pkl .")