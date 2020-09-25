# Coffee and Network Automation (session 2): Nornir Basics

Simple examples demonstrating Nornir basics

## Config

config.yaml sets the number of workers to 1 to keep output formatted consistently

## Inventory

hosts.yaml contains all the devices Nornir will run against

defaults.yaml contains the username, password and platform to be used by Netmiko

## 1-run-command.py

1-run-command.py imports only the needed modules, defines a task to execute the command
found in "command_string", runs that task against all devices found in inventory and
prints the output from the command.

## 2-host-data.py

2-host-data.py builds on the first example by demonstrating how to assign and access
data within Nornir host variables 

## 3-textfsm.py

3-textfsm.py builds on the previous example by demonstrating how to format the output
data in a way that it can be programmatically accessed

## 4-pprint.py

4-pprint.py perfoms the same function as #3 but using pprint for better readability

## 5-formatting-data.py

5-formatting-data.py demonstrates how to interact with the collected data to extract
the specific items needed

##  6-exporting-data.py 

 6-exporting-data.py demonstrates exporting the extracted data to a CSV file
 
 
