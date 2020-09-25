#!/usr/local/bin/python3

"""
This script is used to run a command on network devices with Nornir
"""

from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
import csv


def run_command(task):
    # command to be run
    cmd = "show ip interface brief"
    # send command to device
    output = task.run(task=netmiko_send_command, command_string=cmd, use_textfsm=True)
    # assign output to host variable
    task.host["ip_addresses"] = output.result


def write_addresses(task):
    # initialize list with device hostname
    csv_row = [task.host.name]
    # iterate over interfaces
    for intf in task.host["ip_addresses"]:
        # append each IP address to the list
        csv_row.append(intf["ipaddr"])
    # print CSV row for debugging
    print(csv_row)

    # open or create CSV file
    with open("ip_addresses.csv", mode="a") as ipaddr_file:
        # initialize CSV writer
        ipaddr_writer = csv.writer(
            ipaddr_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        # write row of data to CSV file
        ipaddr_writer.writerow(csv_row)


def main():
    # initialize The Norn
    nr = InitNornir("config.yaml")
    # run The Norn to run command
    nr.run(task=run_command)
    # print results for each host
    nr.run(task=write_addresses)


if __name__ == "__main__":
    main()
