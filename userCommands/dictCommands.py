from userCommands.methodsCommands import MethodsCommands
from userCommands.methodsCommandsDev import MethodsCommandsDev


class DictCommands(MethodsCommands, MethodsCommandsDev):
    def __init__(self, mainclass):
        self.mainclass = mainclass
        # "key":(self.method, description, authorisation )
        self.dCommandList = {
            "!id":(self.sendID,"->gibt die eigene UserID zurück",3),
            "!help":(self.getHelp, "->zeigt die Hilfe an",3),
            "!nyancat":(self.NyanCat, "->Nyan Caaaat",2),
            "!spam":(self.Spam, "->Spamt einen beliebigen Nutzer voll",2),
            "!addmessage":(self.AddMessage, "Fügt eine neue Spamnachricht hinzu",2),
            "!addlink":(self.AddLink, "Fügt einen neuen Link hinzu",2),
            "!penis":(self.onPenis, "Shows you penis, !penis-growing --> lässt den Schwengel wachsen",2),
            "!showspammessages":(self.showAllSpamMessages,"->show all speammessages from csv/database",0),
            "!showspamlinks":(self.showSpamMessagesLink,"show all speammessages from csv/database",2),
            "!showspamtexts":(self.showSpamMessagesText,"show all speammessages from csv/database",2),
            "!clear":(self.mainclass.clearChannel,"->clear the messages from the bot", 0),
            "!dev":(self.onDev, "development commands for more info: !dev-help",0)

        }