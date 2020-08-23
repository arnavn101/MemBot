from urllib.parse import urlparse
import os
import re
import progressbar
from configparser import ConfigParser
import contextlib
import unicodedata
import urllib.request


class UtilFunctions:
    def __init__(self):
        UtilFunctions.printClassMethods(self)

    @staticmethod
    def writeConversationDataToFile(file_name, listConversations):
        with open(file_name, "w+") as file_object:
            for index_array in range(len(listConversations)):
                file_object.write(f"{listConversations[index_array][0]}\n")
                file_object.write(f"{listConversations[index_array][1]}\n")
                file_object.write("\n\n")

    @staticmethod
    def retrieveFileFromUrl(input_url):
        parsed_url = urlparse(input_url)
        return os.path.basename(parsed_url.path)

    @staticmethod
    def download_file(download_URL, file_path):
        urllib.request.urlretrieve(download_URL,
                                   os.path.join(file_path,
                                                UtilFunctions.retrieveFileFromUrl(download_URL)),
                                   DownloadProgressBar())

    @staticmethod
    def retrieveLinesFile(file_name):
        return [line.rstrip() for line in open(file_name)]

    @staticmethod
    def formatString(input_string):
        input_string = UtilFunctions.stripAccents(input_string)
        input_string = re.sub(r"([.!?])", r" \1", input_string)
        input_string = re.sub(r"[^a-zA-Z.!?]+", r" ", input_string)
        input_string = re.sub(r"\s+", r" ", input_string).strip()
        return input_string

    @staticmethod
    def clean_tweet(tweet_text):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet_text).split())

    @staticmethod
    def returnClassMethods(class_object):
        return [method for method in dir(class_object) if "____" not in method[0:2] + method[-2:]]

    @staticmethod
    def printList(input_list):
        print(*input_list, sep=", ")

    @staticmethod
    def printClassMethods(class_object):
        print("List of Functions --> ", end='')
        UtilFunctions.printList(UtilFunctions.returnClassMethods(class_object))

    @staticmethod
    @contextlib.contextmanager
    def suppressStdout():
        with open(os.devnull, 'w') as fnull:
            with contextlib.redirect_stderr(fnull) as err, contextlib.redirect_stdout(fnull) as out:
                yield err, out

    @staticmethod
    def stripAccents(string_input):
        return ''.join(
            char for char in unicodedata.normalize('NFD', string_input)
            if unicodedata.category(char) != 'Mn'
        )


class DownloadProgressBar:
    def __init__(self):
        self.progress_bar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.progress_bar:
            self.progress_bar = progressbar.ProgressBar(maxval=total_size)
            self.progress_bar.start()
        downloaded = block_num * block_size
        if downloaded < total_size:
            self.progress_bar.update(downloaded)
        else:
            self.progress_bar.finish()


class EditConfiguration:
    def __init__(self, configFileName):
        self.configFileName = configFileName
        self.config = ConfigParser()
        self.config.read(configFileName)
        UtilFunctions.printClassMethods(self)

    def listSections(self):
        UtilFunctions.printList(self.config.sections())
        return self.config.sections()

    def listOptions(self, section_name):
        if not self.existsSection(section_name):
            return "No such Section"
        UtilFunctions.printList(self.config.options(section_name))
        return self.config.options(section_name)

    def listValue(self, section_name, option_name):
        if not self.existsSection(section_name) or self.existsOption(section_name, option_name):
            return "No such Section or Option"
        print(self.config.get(section_name, option_name))
        return self.config.get(section_name, option_name)

    def existsOption(self, option_name, section_name):
        return self.config.has_option(section_name, option_name)

    def existsSection(self, section_name):
        return self.config.has_section(section_name)

    def editOption(self, section_name, option_name, option_value):
        if not self.existsSection(section_name) or self.existsOption(section_name, option_name):
            return "No such Section or Option"
        self.config.set(section_name, option_name, option_value)

    def saveConfigFile(self):
        with open(self.configFileName, "w+") as configfile:
            self.config.write(configfile)
