class Host(object):
    def __init__ (self):
        self.playerNumber = 0
        self.ip = "127.0.0.1"
        self.port = 5665

    def __init__ (self, row):
        self.setPlayerNumber(row[0])
        self.setIp(row[1])
        self.setPort(row[2])

    def getPlayerNumber(self):
        return self.playerNumber

    def setPlayerNumber(self, playerNumber):
        self.playerNumber = int(playerNumber)

    def getIp(self):
        return self.ip

    def setIp(self, ip):
        self.ip = ip

    def getPort(self):
        return self.port

    def setPort(self, port):
        self.port = int(port)