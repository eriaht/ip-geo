# ip-geo
This script uses the traceroute or tracert tool (depending on your system OS) and outputs the city name and country of each router along the way.

### Troubleshooting
If the script seems to be "hung up" check the tracerouteout.txt file look for * in the output. The * indicates that a response was not received at that hop, the request will time out for 5 seconds before sending another request. Wait for tracert to finish or press control + C to end the program.

```
pip3 install requests
python ip_geo.py --ip=150.31.249.103
```

## Output
```
IP: 192.168.1.1, Location: , 
IP: Redacted, Location: Redacted
IP: Redacted, Location: Redacted
IP: Redacted, Location: Redacted
IP: Redacted, Location: Redacted
IP: Redacted, Location: Redacted
IP: Redacted, Location: Redacted
IP: 66.109.5.131, Location: Miami, United States
IP: 66.109.0.247, Location: Miami, United States
IP: 204.148.176.65, Location: Cranbury, United States
IP: 204.148.156.58, Location: St Louis, United States
IP: 58.138.81.81, Location: Chiyoda, Japan
IP: 58.138.88.129, Location: Chiyoda, Japan
IP: 210.138.115.210, Location: Osaka, Japan
IP: 160.13.162.2, Location: Chiyoda, Japan
IP: 210.149.34.130, Location: Chiyoda, Japan
IP: 103.249.31.150, Location: Gasan-dong, South Korea
IP: 150.31.249.103, Location: Tokyo, Japan
```

I am getting the geolocation data from https://ip-api.com/

<img width="1103" alt="ip-api.com response json with a map of the geolocation" src="https://github.com/eriaht/ip-geo/assets/44909814/5e590683-1bee-47c0-a6c2-a604fa82c3f7">

Follow the hops! Test the script with some public DNS servers at https://public-dns.info/


