from utilsFuncs.utils import UtilFunctions


class MemBot:
    def __init__(self, chatBotModel):
        self.chatBotModel = chatBotModel
        UtilFunctions.printClassMethods(self)
        self.handleInp()

    def handleInp(self):
        return getattr(self, self.chatBotModel)

    def MRSMCorpusChatBot(self):
        raise NotImplementedError

    def OpenAIGptChatBot(self):
        raise NotImplementedError
