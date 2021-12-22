import conf

if conf.database == "replit":
  from replit import db

consSpamMessages = ("sp_messages")

class DataManagement():
  def __init__(self):
    if conf.database == "replit":
      if not consSpamMessages in db.keys():
        self.fillDatabaseFromCSV()
      
  
  def getMessagesFromCSV(self):
    dMessages = {}
    with open("messages.csv", "r") as file:
                for zeile in file:
                    
                    l_zeile = zeile.split(";")
                    dMessages[l_zeile[0]] = l_zeile[1]
                file.close()
    return dMessages
  
  def appendMessageToCSV(self, message, disappear=5):
        message = message.replace("ä", "ae")
        message = message.replace("Ä", "Ae")
        message = message.replace("ö", "oe")
        message = message.replace("Ö", "OE")
        message = message.replace("ü", "ue")
        message = message.replace("Ü", "Ue")
        self.dMessages[message] = str(disappear)
        with open("messages.csv", "a") as file:
            file.write(f"{message};{disappear};\n")
            file.close()
 
  def getMessagesDict(self)->dict:
    if conf.database == "csv":
      return self.getMessagesFromCSV()
    if conf.database == "replit":
      if consSpamMessages in db.keys():
        return dict(db[consSpamMessages])
      

  def setMessage(self, message:str, disappear = 5):
    if conf.database == "csv":
        return  self.appendMessageToCSV(message, disappear)
    if conf.database == "replit":
      if consSpamMessages in db.keys():
        db[consSpamMessages][message] = disappear
    return
  
  def fillDatabaseFromCSV(self):
    print("fill Database")
    if conf.database =="replit":
      try:
          db[consSpamMessages] = {}
          db[consSpamMessages] = self.getMessagesFromCSV()
          return "fill Database"
      except Exception as e:
          return e
    return f"conf.database = {conf.database}"
  
  