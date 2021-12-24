
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
    
    def setNewStopKey(self, userid:str, keyValue:str)->str:
        key = userid + "_" + keyValue
        if not userid in self.dUsersReaction.keys():
            self.dUsersReaction[str(userid)] = []
        if key in self.dUsersReaction[userid]:
            return ""
        if "§a" in self.dUsersReaction[userid] or "t" in self.dUsersReaction[userid]:
            return ""
        self.dUsersReaction[userid].append(key)
        return key
    
    def aktivateKey(self, userid:str):
        print("acktivate Key")
        self.l_locktTemporary.append(userid)
        #if "§a" in self.dUsersReaction[userid]:
            #self.dUsersReaction[userid] = ["§a", "§t"]
            #return True
        self.dUsersReaction[userid] = ["t"]
        self.l_locktTemporary.append(userid)
        print("useractions = " + str(self.dUsersReaction[userid]))
        return True
    
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
    
    def deleteKey(user, key):
        return
        


if __name__ == "__main__":
    c = UserManagement()
    key = c.setNewStopKey("niklas", "test")
    print(key)
    print(c.checkForStop("niklas", key))
    print(c.aktivateKey("niklas"))
    print(c.checkForStop("niklas", key))
    print(c.checkForTempLock("niklas"))
    key = c.setNewStopKey("niklas", "test")
    print(key)
    print(c.checkForStop("niklas", key))