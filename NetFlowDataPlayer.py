import json
import os

#Take Input for Filename, GlobalID, Protocol, Protocol Description, Server Port, Source Address Range, Destination Address, Destination Host, Bytes In/Out Range

output = []

filename = input("Name of json file : ")
globalID = input("Global ID Please : ")
protocol = input("Protocol : ")
protocol_descr = input("Protocol Description : ")
server_port = input("Server Port : ")
sourceAddress_Range = input("Source address range eg:10.10.10.11-50 : ")
destination_Address = input("Destination Address : ")
destination_Address_Hostname = input("Destination Address Hostname : ")
outbytesrange = input("Outbytes Range eg: 1000,15000 : ")
inbytesrange = input("Inbytes range eg: 2000,2500 : ")

# Now get the Source Address Range and iterate
srcAddressSplit = sourceAddress_Range.split('-')
srcAddressStart = srcAddressSplit[0].split('.')

startRange = int(srcAddressStart[3])
endRange = int(srcAddressSplit[1])

srcAddressFirst3Octet = srcAddressStart[0]+"."+srcAddressStart[1]+"."+srcAddressStart[2]

# Append .json if user did not provide any extension
if not os.path.splitext(filename)[1]:
    filename += ".json"

with open(filename, 'w') as f:
    for srcAddressVal in range(startRange,endRange):
        json.dump({
            "globalID": [""+globalID+ ""],
            "metrics_metadata":
                {
                    "archive_type": "conversation",
                    "Protocol": protocol,
                    "protocol_description": protocol_descr,
                    "serverPort": server_port,
                    "srcAddr": srcAddressFirst3Octet+"."+str(srcAddressVal),
                    "srcAddr_hostname": "Client-"+srcAddressStart[2]+"."+str(srcAddressVal),
                    "dstAddr": destination_Address,
                    "dstAddr_hostname": destination_Address_Hostname
                },
            "metrics":
                {
                    "outbytes": "rand[" + outbytesrange.split(',')[0] + "," + outbytesrange.split(',')[1] + "]",
                    "inbytes": "rand[" + inbytesrange.split(',')[0] + "," + inbytesrange.split(',')[1] + "]",
                    "totalbytes": "${inbytes}+${outbytes}"

                }
        }, f, indent=4)
        f.write(',')

with open(filename, 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()