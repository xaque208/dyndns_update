#! /usr/bin/env python
import yaml, requests, sys

def get_ip():
    try:
        url = 'http://checkip.dyndns.com'
        r = requests.get(url)
        return(r.text.split(' ')[5].split('<')[0])
    except:
        print("unable to check current public address")
        sys.exit(1)

def update_ip(ip):
    try:
        config = yaml.load(open("etc/config.yaml").read())
        username = config["username"]
        password = config["password"]
        hostname = config["hostname"]
    except:
        print("Error parsing config.yaml file.")
        sys.exit(1)

    try:
        url = 'https://members.dyndns.org/nic/update'
        payload = {'hostname': hostname, 'myip': ip}
        r = requests.get(url, params=payload, auth=(username,password))
    except:
        print("Failed to update the ip.")

def main():
    pubip = get_ip()
    update_ip(pubip)

main()
