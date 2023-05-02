import scapy.all as scapy
# import regular expressions for correct format of input checking
import re
# title thing -
print("##############################    -  Starting Manual WiFi Device Scanner  -   ##############################")
print("!!!- This program is only to be used for Education and NOT any form of malicious activity by any means. -!!!")
print("######### - Scanner requires scapy install. - #########")

# regular expression pattern to know what an IPv4 is
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

#Get the address range to ARP

while True:
        ip_add_range_entered = input("Please enter the ip address and range you want to hit (xxx.xxx.xxx.0/xx): ")
        if ip_add_range_pattern.search(ip_add_range_entered):
                print(f"{ip_add_range_entered} is a valid range.")
        break

arp_result = scapy.arping(ip_add_range_entered)
# Above checks devices for us using ARP.import scapy
import scapy.all as scapy
# import regular expressions for correct format of input checking
