import socket
import host
import netifaces as ni

def identifyPlayer(hosts, myIp):
    for h in hosts:
        if h.getIp() == myIp:
            return h.getPlayerNumber()
    return -1

def identififyPort(hosts):
    try:
        return hosts[0].getPort()
    except:
        return -1

def myIpAddress():
	ni.ifaddresses('enp0s8')
	ip = ni.ifaddresses('enp0s8')[2][0]['addr']
	return ip