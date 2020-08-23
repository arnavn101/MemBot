from pytorch_pretrained_bert import OpenAIGPTDoubleHeadsModel, OpenAIGPTTokenizer


class ChatBot:
    def __init__(self):
        self.this_model = OpenAIGPTDoubleHeadsModel.from_pretrained('openai-gpt')
        self.this_tokenizer = OpenAIGPTTokenizer.from_pretrained('openai-gpt')
        raise NotImplementedError