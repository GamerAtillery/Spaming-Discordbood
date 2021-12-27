from conf import database
import os
if database == "replit":
  from replit import db

consSpamMessages = ("sp_messages")
consPathCSV = "messages.csv"

class DataManagement(dict):
  l_CSVFiles = []
  dict_DatabaseCSV = {}
  csvFileSingleVariables = "Variables.csv"

  def __init__(self):
      self.sFolderPath = self.getFolderPathCSV()
      if database == "csv":
          self._initCSVDict
      if database == "replit":
          if not consSpamMessages in db.keys():
            self.fillDatabaseFromCSV()

  def getListOfCSVFiles(self):
     lFiles = os.listdir(self.sFolderPath)
     for file in lFiles:
         if not ".csv" in file.lower():
             continue
         sFile = str(file).replace(".csv", "")
         self.l_CSVFiles.append(sFile)




      
  
  def getFromCSV(self, dataField:str):
    dMessages = {}
    with open(consPathCSV, "r") as file:
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
        
        with open(consPathCSV, "a") as file:
            file.write(f"{message};{disappear};\n")
            file.close()
 
  def getMessagesDict(self)->dict:
    if database == "csv":
      return self.getMessagesFromCSV()
    if database == "replit":
      if consSpamMessages in db.keys():
        return dict(db[consSpamMessages])
      

  def setMessage(self, message:str, disappear = 5):
    if database == "csv":
        return  self.appendMessageToCSV(message, disappear)
    if database == "replit":
      if consSpamMessages in db.keys():
        db[consSpamMessages][message] = disappear
    return

  def getFolderPathCSV(self):
      sPath = str(__file__).replace("dataManagement.py","")
      return  sPath + "filescsv\\"
  
  def fillDatabaseFromCSV(self, dataField:str):
    print("fill Database")
    if database =="replit":
      try:
          db[consSpamMessages] = {}
          db[consSpamMessages] = self.getMessagesFromCSV()
          return "fill Database"
      except Exception as e:
          return e
    return f"database = {database}"



  def __getitem__(self, key:str):
        return self.get(key)

  def get(self, key):
      try:
          if database == "csv":
            return self.dict_DatabaseCSV[key]
          if database == "replit":
            return db[key]
      except Exception as e:
          print(f"error in database: key={key} " + str(e))

  def __setitem__(self, key:str, value):
      if database == "csv":
          self.dict_DatabaseCSV[key] = value
      if database == "replit":
          db[key] = value

  def __str__(self):
      if database == "csv":
        return str(self.dict_DatabaseCSV)
      if database == "replit":
        return str(dict(db))


  def __len__(self):
      if database == "csv":
          return len(self.dict_DatabaseCSV)
      if database == "replit":
        return len(self.db.keys())

  def __iter__(self):
      if database == "csv":
        return iter(self.dict_DatabaseCSV)
      if database == "replit":
        return iter(db)

  def keys(self):
      if database == "csv":
        return self.dict_DatabaseCSV.keys()
      if database == "replit":
        return db.keys()

  def items(self):
      if database == "csv":
          return self.dict_DatabaseCSV.items()
      if database == "replit":
          return db.items()

  def values(self):
      if database == "csv":
          return self.dict_DatabaseCSV.values()
      if database == "replit":
          return db.values()
  
if __name__ == '__main__':
    d =DataManagement()
    print(d.getFolderPathCSV())