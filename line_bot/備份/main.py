from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('rqi6Ooc9nTf11tUk0ZsGl570J+0skjOCQ1vLBGy1HcR5J1I951ZxclBfYTxgM1J8Uien3Te7Dn0M5qA9egq+m5f4PnQoixMnwqRmoO2COG3hu9gUFzLhPBawoPitQvFQXCXJva4OVq5WUYi/kYWCuAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1f9fff19d613da0a7ebeab77703cdcaa')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    test = bot(event.message.text)
    print(test)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=test))

def bot(str):
    chatbot = ChatBot("Ptorch")
    chatbot.set_trainer(ChatterBotCorpusTrainer)
    chatbot.train("chatterbot.corpus.chinese")
    response = chatbot.get_response(str)
    return response
if __name__ == "__main__":
    app.run()