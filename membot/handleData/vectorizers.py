# import os
# from utilsFuncs.utils import UtilFunctions
# import numpy as np
# import zipfile


class VocabularyHandler:
    def __init__(self, uniqueName):
        self.__NAME__ = uniqueName
        print(f"Vocab handler {self.__NAME__} Initialized!")

        self.wordIndices = {}
        self.wordCount = {}
        self.number_words = 0

    def appendSentence(self, sentence_input):
        for individual_word in sentence_input.split():
            self.appendWord(individual_word)

    def appendWord(self, word_input):
        if word_input not in self.wordIndices.keys():
            self.wordIndices[word_input] = self.number_words
            self.wordCount[word_input] = 1
        else:
            self.wordCount += 1

    # Remove words below the Occurrence_count
    def removeLowOccurrence(self, occurrence_count):
        # Retain copies of previous dictionaries
        retainedWords = []
        for word_index in self.wordIndices.keys():
            if self.wordIndices[word_index] >= occurrence_count:
                retainedWords.append([word_index, self.wordIndices[word_index]])
        self.wordIndices = {}
        self.wordCount = {}
        for individual_word in retainedWords:
            self.appendWord(individual_word[0])
            self.wordCount[individual_word[0]] = individual_word[1]


class VectorizerGloVE:
    def __init__(self, download_directory="/tmp", gloveFile='glove.6B.100d.txt', **kwargs):
        raise NotImplementedError
    #     self.download_directory = download_directory
    #     self.gloveFile = gloveFile
    #     for k, v in kwargs.items():
    #         if k == 'download_directory':
    #             self.download_directory = v
    #         if k == 'gloveFile':
    #             self.gloveFile = v
    #     self.DownloadUrlGloVE = "http://nlp.stanford.edu/data/glove.6B.zip"
    #
    # def downloadWordVectors(self):
    #     zipFileName = UtilFunctions.retrieveFileFromUrl(self.DownloadUrlGloVE)
    #     zipFilePath = os.path.join(self.download_directory, zipFileName)
    #     gloveFilePath = os.path.join(self.download_directory, self.gloveFile)
    #
    #     if not os.path.exists(gloveFilePath):
    #         if not os.path.exists(zipFilePath):
    #             UtilFunctions.download_file(self.DownloadUrlGloVE, self.download_directory)
    #         if os.path.exists(gloveFilePath):
    #             with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
    #                 zip_ref.extractall(self.download_directory)
    #         else:
    #             raise Exception("Zip File Does not Exist. Check the Validity of DownloadUrlGloVE.")
    #
    #     with open(gloveFilePath, 'r') as file_object:
    #         word_vectors = {}
    #         for individual_word in file_object:
    #             word_vectors[individual_word.split()[0]] = np.array(list(map(float, individual_word.split()[1:])))
    #     return word_vectors
