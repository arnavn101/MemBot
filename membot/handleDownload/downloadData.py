from utilsFuncs.utils import UtilFunctions


class DataDownloader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.LinkMRSMConversationCorpus = "https://download.microsoft.com/download/4/8/D/" \
                                          "48DC89F7-0AFC-4145-9C6B-B6BED2CE7665/MSRSocialMediaConversationCorpus.zip"
        UtilFunctions.printClassMethods(self)

    # Microsoft Research Social Media Conversation Corpus Parser
    def downloadMRSMConversationCorpus(self):
        print("\nDownloading Microsoft Research Social Media Conversation Corpus\n")
        UtilFunctions.download_file(self.LinkMRSMConversationCorpus, self.file_path)
