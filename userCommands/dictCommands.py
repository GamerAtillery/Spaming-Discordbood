from userCommands.methodsCommands import MethodsCommands


class DictCommands(MethodsCommands):
    def __init__(self, mainclass):
        self.mainclass = mainclass
        self.dCommandList = {
            "!id":(self.sendID,"gibt die eigene UserID zurück"),
            "!help":(self.getHelp, "zeigt die Hilfe an"),
            "!filldb":(self.fillDB, "Macht einen Eintrag in die Datenbank!"),
            "!nyancat":(self.NyanCat, "Nyan Caaaat"),
            "!spam":(self.Spam, "Spamt einen beliebigen Nutzer voll"),
            "!addmessage":(self.AddMessage, "Fügt eine neue Spamnachricht hinzu"),
            "!addlink":(self.AddLink, "Fügt einen neuen Link hinzu"),
            "!penis-growing":(self.onPenisGrowing, "you don't need a description here"),
            "!penis":(self.onPenis, "you don't need a description here")

        }