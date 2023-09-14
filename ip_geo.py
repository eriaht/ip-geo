# Written by Eriaht 09/12/23
# I want to see where I am hopping to
import re
import os
import argparse
import platform
import requests

# Create parser
parser = argparse.ArgumentParser(
						prog='ip_geo.py',
						usage='python ip_geo.py --ip=210.213.125.186',
						description='Follow the location of each router!')

# Create arguments
parser.add_argument("--ip", dest="ip", help="Set the ip address.")
parser.add_argument("-w", dest="timeout", help="Set the time (in seconds) to wait for a response to a probe.")
parser.add_argument("-m", dest="max_ttl", help="Set the max_ttl (max number of hops) used in outgoing probe packets.")

# Get arguments
args = parser.parse_args()

if args.ip == None:
    parser.print_help()
    exit()

print("Tracing the route this may take a while...")

# Execute traceroute then send the output to tracerouteout.txt
if platform.system() == "Windows":
    # Set system defaults
    if args.max_ttl == None:
        args.max_ttl = 30
    if args.timeout == None:
        args.timeout = 4
    os.system(f"tracert /w {args.timeout} /h {args.max_ttl} {args.ip} > tracerouteout.txt")
else:
    # Set system defaults
    if args.max_ttl == None:
        args.max_ttl = 64
    if args.timeout == None:
        args.timeout = 5
    os.system(f"traceroute -w {args.timeout} -m {args.max_ttl} {args.ip} > tracerouteout.txt")

try:
    # Read from tracerouteout.txt
    with open("tracerouteout.txt", "r") as tro:
        while True:
            line = tro.readline()

            if not line:
                break

            # Get IP addresses from each line
            ips = set(re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line))

            # Loop through each ip 
            for i, ip in enumerate(ips):
                ip_geo = {}
                ip_geo[f"ip_{i}"] = ip
                
                # Search for Geolocation of IP
                req = requests.get(f"http://ip-api.com/json/{ip}")
                
                if req.status_code == 200:
                    res = req.json()
                    # Get the city and country 
                    city = ''
                    region_name = ''
                    country = ''
                    for key, value in res.items():
                        if key == "city":
                            city = value
                        if key == "regionName":
                            region_name = value
                        if key == "country":
                            country = value

                    ip_geo["location"] = f"{city}, {region_name}, {country}"

                    print(f"IP: {ip}, Location: {ip_geo['location']}")
                else:
                    raise Exception             
except Exception as e:
    print(e)

