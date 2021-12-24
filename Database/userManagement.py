
class UserManagement():
    lUsers = []
    dUsersReaction = {}
    l_locktTemporary = []


    def __init__(self) -> None:
        pass

    def checkForStop(self,userid:str, stopKey:str):
        if stopKey in self.dUsersReaction[userid]:
            return True
        return False
    
    def setNewStopKey(self, userid:str, keyValue:str, channel="*")->str:
        key = userid + "_" + keyValue + "_" + str(channel)
        if not userid in self.dUsersReaction.keys():
            self.dUsersReaction[str(userid)] = []
        if key in self.dUsersReaction[userid]:
            return ""
        if "§a" in self.dUsersReaction[userid] or "t" in self.dUsersReaction[userid]:
            return ""
        self.dUsersReaction[userid].append(key)
        return key
    
    def onStop(self, userid:str, channel= "*", tempLock=False):
        channel = str(channel)
        print("acktivate Key")
        l_newEntry = []
        for entry in self.dUsersReaction[userid]:
            entry = str(entry)
            if entry.endswith("a") or entry.endswith("t"):
                l_newEntry.append(entry)
                continue
            if (not entry.endswith(channel)) and (not entry.endswith("*")):
                l_newEntry.append(entry)
        self.dUsersReaction[userid] = l_newEntry
        if tempLock:
            self.TempLock(userid)
        print("useractions = " + str(self.dUsersReaction[userid]))
        return True
    
    def TempLock(self, userid:str,):
        self.l_locktTemporary.append(userid)
        self.dUsersReaction[userid] = ["t"]
        self.l_locktTemporary.append(userid)

    
    def checkForTempLock(self, userid:str):
        print("checkForTemp")
        if userid in self.l_locktTemporary:
            try:
                self.l_locktTemporary.remove(userid)
                self.dUsersReaction[userid].remove("t")
                print("useractions = " + str(self.dUsersReaction[userid]))
            except Exception as e:
                print(e)
    
    def checkForGenerellLock(self, userid:str):
        if "§a" in self.dUsersReaction[userid]:
            return False
        return True
    
    def deleteKey(self, user, key:str):
        if key in self.dUsersReaction[user.id]:
            self.dUsersReaction[user.id]

        return
        


if __name__ == "__main__":
    c = UserManagement()
    key = c.setNewStopKey("niklas", "test")
    print(key)
    print(c.checkForStop("niklas", key))
    print(c.onStop("niklas"))
    print(c.checkForStop("niklas", key))
    print(c.checkForTempLock("niklas"))
    key = c.setNewStopKey("niklas", "test")
    print(key)
    print(c.checkForStop("niklas", key))