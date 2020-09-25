#!/usr/local/bin/python3

"""
This script is used to run a command on network devices with Nornir
"""

from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from openpyxl import Workbook


def run_command(task):
    # command to be run
    cmd = "show ip interface brief"
    # send command to device
    output = task.run(
        task=netmiko_send_command, 
        command_string=cmd,
        use_textfsm=True
    )
    # assign output to host variable
    task.host["ip_addresses"] = output.result


def print_addresses(task):
    # print inventory hostname
    print(task.host)
    # print previously assigned output
    for intf in task.host["ip_addresses"]:
        print(intf["intf"])
        print(intf["ipaddr"])
    print()


def main():
    # initialize The Norn
    nr = InitNornir("config.yaml")
    # run The Norn to run command
    nr.run(task=run_command)

    filename = "hello_world.xlsx"

    workbook = Workbook()

    sheet = workbook.active
    
    sheet["A1"] = "hello"

    sheet["B1"] = "world!"

    workbook.save(filename=filename)

    # print results for each host
    nr.run(task=print_addresses)
    

if __name__ == "__main__":
    main()
