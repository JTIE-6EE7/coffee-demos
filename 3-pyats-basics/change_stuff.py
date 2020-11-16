#!/usr/local/bin/python3

"""
Change stuff
"""

import sys
from getpass import getpass
from datetime import datetime
from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks import text, files
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_config

def change_stuffs(task):

    cmd = "int loopback0"

    if task.host.name == 'CSR-2':    
        cmd = "int loopback0\nshutdown\n"
    if task.host.name == 'CSR-3':       
        cmd = "int GigabitEthernet1\nshutdown\n"

    task.run(task=netmiko_send_config, config_commands=cmd)


def main():
    # kickoff The Norn
    nr = InitNornir()
    # run The Norn
    print("~" * 80)
    print("Making network changes.".center(80," "))
    print("~" * 80)
    nr.run(task=change_stuffs)
    print("Network changes complete.".center(80," "))
    print("~" * 80)
    
if __name__ == "__main__":
    main()