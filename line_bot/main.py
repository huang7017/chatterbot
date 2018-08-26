# -*- coding: utf8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from chatterbot import ChatBot
class bot:
    def __init__(self):
        self.chatbot = ChatBot(
            'Ron Obvious',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
        )
    def read(self):
        for i in range(len(sys.argv)):
            str_1 = sys.argv[i]
        return str_1
    def train(self):
        s = self.read()
        # self.chatbot.train("chatterbot.corpus.chinese")
        # print(s)
        print(self.chatbot.get_response(s))
if __name__ == '__main__':
    obj = bot()
    obj.train()