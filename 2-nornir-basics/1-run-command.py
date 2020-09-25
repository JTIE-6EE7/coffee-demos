#!/usr/local/bin/python3

"""
This script is used to run a command on network devices with Nornir
"""

from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


def run_command(task):
    # command to be run
    cmd = "show ip interface brief"
    # send command to device
    output = task.run(
        task=netmiko_send_command, 
        command_string=cmd
    )
    # print command output
    print_result(output)


def main():
    # initialize The Norn
    nr = InitNornir("config.yaml")
    # run The Norn to run command
    nr.run(task=run_command)


if __name__ == "__main__":
    main()
