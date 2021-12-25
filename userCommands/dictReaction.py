
from .methodsReaction import MethodsReaction


class DictReaction(MethodsReaction):
    def __init__(self, mainclass):
        super().__init__(mainclass)
        # "key":(self.method, description, authorisation )
        self.dCommandList = {

        }
        self.dCommandListObserver = {
            "!r":(self.reactionSquidGame, "rechts squidGameTower", 2, self.oSquidGame.checkIsRunning),
            "!l":(self.reactionSquidGame, "rechts squidGameTower", 2, self.oSquidGame.checkIsRunning)
        }

    def get(self, key:str, channelID="*"):
        print(f"{self.lObservedChannels} {channelID=} {key=} {self.dCommandListObserver}")
        if channelID == "*":
            return super().get(key)
        if channelID in self.lObservedChannels:
            print(f"{self.lObservedChannels} {channelID=} {key=} {self.dCommandListObserver}")
            for value, item in self.dCommandListObserver.items():
                if key.startswith(value) and item[3](channelID):
                    return item
        return super().get(key)

