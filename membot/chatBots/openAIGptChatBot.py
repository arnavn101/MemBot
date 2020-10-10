import gpt_2_simple as gpt2


class ChatBot:
    def __init__(self, textFilePath='', savedModelPath='', GPT2_model_name='124M', n_epochs=100):
        self.textFilePath = textFilePath
        self.savedModelPath = savedModelPath
        self.GPT2_model_name = GPT2_model_name
        self.n_epochs = n_epochs

    def downloadModel(self):
        gpt2.download_gpt2(model_name=self.GPT2_model_name)

    def initiateTraining(self):
        sessionTf = gpt2.start_tf_sess()
        gpt2.finetune(sessionTf, self.textFilePath, model_name=self.GPT2_model_name, steps=self.n_epochs)
        gpt2.generate(sessionTf)

    def returnGeneratedText(self, length=25, temperature=1.0, prefix='I'):
        sessionTf = gpt2.start_tf_sess()
        gpt2.load_gpt2(sessionTf, checkpoint_dir=self.savedModelPath)
        outputText = gpt2.generate(sessionTf, checkpoint_dir=self.savedModelPath, length=length,
                                   temperature=temperature, prefix=prefix)
        return outputText
