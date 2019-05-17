from flask import Flask, request, abort

import psycopg2

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
   MessageEvent,TextMessage,TextSendMessage,StickerSendMessage,ImageSendMessage,TemplateSendMessage,ButtonsTemplate,PostbackTemplateAction
)

from linebot.models import *

import os
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(os.environ['lineToken'])
# Channel Secret
handler = WebhookHandler(os.environ['lineSecret'])


# 監聽所有來自 /callback 的 Post Request
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
    print(event)
    
    text2 = "According to your input, my answer is " + event.message.text
    
    if event.message.text.find("bye")>=0 or event.message.text.find("Bye")>=0 or event.message.text.find("拜拜")>=0:
        text2 = "謝謝您的詢問，希望有機會能再為您服務。"
    if event.message.text.find("你好")>=0 or event.message.text.find("您好")>=0 or event.message.text.find("妳好")>=0:
        text2 = "您好!!很高興跟您傳訊息!"
    if event.message.text.find("會考")>=0:
        text2 = "請找陳昇國!"
    if event.message.text.find("喝酒")>=0:
        text2 = "請找彭振昌，他會灌到你，讓你不要不要的!"
    if event.message.text.find("ChiChi")>=0:
        text2 = "Please find ID:cliff135。"
    if event.message.text.find("助教")>=0:
        text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"
    if event.message.text.find("線性代數")>=0:
        text2 = "目前教授線性代數的老師有陳嘉文、彭振昌、陳昇國、林仁彥，但是大多數老師都可以、也有可能會教授此門課。"
    if event.message.text.find("微積分")>=0:
        text2 = "目前全體老師均有教授微積分的經驗。"
    if event.message.text.find("高等微積分")>=0:
        text2 = "今年教授高等微積分的老師為陳嘉文教授。"
    if event.message.text.find("林仁彥")>=0:
        text2 = "林仁彥老師的專長為最佳化，辦公室在理工大樓八樓A16-815，辦公室電話05-271-7880。"
    if event.message.text.find("彭振昌")>=0:
        text2 = "彭振昌老師的專長為動態系統，辦公室在理工大樓八樓A16-822，辦公室電話05-271-7878。"

    

    # message = TextSendMessage(text=text2) 
    
    
    # #傳送貼圖
    # Sticker_Message = StickerSendMessage(package_id=1,sticker_id=2) 
    
    # #傳送圖片
    # Image_Message = ImageSendMessage(original_content_url='https://ithelp.ithome.com.tw/upload/images/20180103/20107144nFRc5tsPkp.png',preview_image_url='https://ithelp.ithome.com.tw/upload/images/20180103/20107144nFRc5tsPkp.png')

    # Video_Message = VideoSendMessage(original_content_url='https://jylin.myqnapcloud.com/test.mp4', preview_image_url='https://ithelp.ithome.com.tw/upload/images/20180103/20107144nFRc5tsPkp.png')

    # Audio_Message = AudioSendMessage(original_content_url='https://jylin.myqnapcloud.com/test.m4a', duration=100000)

    # #Location_Message = LocationSendMessage(title='my location', address='Tainan', latitude=22.994821, longitude=120.196452)

    # Imagemap_Message = ImagemapSendMessage(
    #     base_url='https://www.kamigo.tw/assets/kamigo-c3b10dff4cdb60fa447496b22edad6c32fffde96de20262efba690892e4461e8.png#',
    #     alt_text='this is an imagemap',
    #     base_size=BaseSize(height=1040, width=1040),
    #     actions=[
    #         URIImagemapAction(
    #             link_uri='https://ithelp.ithome.com.tw/m/articles/10198142',
    #             area=ImagemapArea(
    #                 x=0, y=0, width=520, height=1040
    #             )
    #         ),
    #         MessageImagemapAction(
    #             text='hello',
    #             area=ImagemapArea(
    #                 x=520, y=0, width=520, height=1040
    #             )
    #         )
    #     ]
    # )


    # Buttons_Template = TemplateSendMessage(
    #     alt_text='Buttons Template',
    #     template=ButtonsTemplate(
    #         title='這是ButtonsTemplate',
    #         text='ButtonsTemplate可以傳送text,uri',
    #         thumbnail_image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #         actions=[
    #             MessageTemplateAction(
    #                 label='ButtonsTemplate',
    #                 text='ButtonsTemplate'
    #             ),
    #             URITemplateAction(
    #                 label='VIDEO1',
    #                 uri='https://www.youtube.com/watch?v=YKiMrg6rgYQ'
    #             ),
    #             PostbackTemplateAction(
    #                 label='postback',
    #                 text='postback text',
    #                 data='postback1'
    #             )
    #         ]
    #     )
    # )

      
    # Confirm_Template = TemplateSendMessage(
    #     alt_text='目錄 template',
    #     template=ConfirmTemplate(
    #         title='這是ConfirmTemplate',
    #         text='這就是ConfirmTemplate,用於兩種按鈕選擇',
    #         actions=[                              
    #             PostbackTemplateAction(
    #                 label='Y',
    #                 text='Y',
    #                 data='action=buy&itemid=1'

    #             ),
    #             MessageTemplateAction(
    #                 label='N',
    #                 text='N'
    #             )
    #         ]
    #     )
    # )

    # Carousel_Template = TemplateSendMessage(
    #     alt_text='Carousel template',
    #     template=CarouselTemplate(
    #         columns=[
    #             CarouselColumn(
    #                 thumbnail_image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #                 title='this is menu1',
    #                 text='description1',
    #                 actions=[
    #                     PostbackTemplateAction(
    #                         label='postback1',
    #                         text='postback text1',
    #                         data='action=buy&itemid=1'
    #                     ),
    #                     MessageTemplateAction(
    #                         label='message1',
    #                         text='message text1'
    #                     ),
    #                     URITemplateAction(
    #                         label='uri1',
    #                         uri='https://www.youtube.com/watch?v=YKiMrg6rgYQ'
    #                     )
    #                 ]
    #             ),
    #             CarouselColumn(
    #                 thumbnail_image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #                 title='this is menu2',
    #                 text='description2',
    #                 actions=[
    #                     PostbackTemplateAction(
    #                         label='postback2',
    #                         text='postback text2',
    #                         data='action=buy&itemid=2'
    #                     ),
    #                     MessageTemplateAction(
    #                         label='message2',
    #                         text='message text2'
    #                     ),
    #                     URITemplateAction(
    #                         label='連結2',
    #                         uri='https://www.youtube.com/watch?v=GuqY5OViunk'
    #                     )
    #                 ]
    #             ),
    #             CarouselColumn(
    #                 thumbnail_image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #                 title='this is menu3',
    #                 text='description2',
    #                 actions=[
    #                     PostbackTemplateAction(
    #                         label='postback3',
    #                         text='postback text2',
    #                         data='action=buy&itemid=2'
    #                     ),
    #                     MessageTemplateAction(
    #                         label='message3',
    #                         text='message text2'
    #                     ),
    #                     URITemplateAction(
    #                         label='連結3',
    #                         uri='https://www.youtube.com/watch?v=GuqY5OViunk'
    #                     )
    #                 ]
    #             )
    #         ]
    #     )
    # )

    # Image_Carousel = TemplateSendMessage(
    #     alt_text='目錄 template',
    #     template=ImageCarouselTemplate(
    #         columns=[
    #             ImageCarouselColumn(
    #                 image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #                 action=PostbackTemplateAction(
    #                     label='postback1',
    #                     text='postback text1',
    #                     data='action=buy&itemid=1'
    #                 )
    #             ),
    #             ImageCarouselColumn(
    #                 image_url='https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
    #                 action=PostbackTemplateAction(
    #                     label='postback2',
    #                     text='postback text2',
    #                     data='action=buy&itemid=2'
    #                 )
    #             )
    #         ]
    #     )
    # )

    # replay_message(event,Image_Carousel)




    Buttons_Template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='Hello\U0001f600~我是微微~歡迎問我各種關於微積分的問題喔~',
            text=' ',
            thumbnail_image_url='https://math-2019.000webhostapp.com/LOGO.jpg',
            actions=[
                MessageTemplateAction(
                    label='海報(<-解答點我)',
                    text='海報(<-解答點我)'
                ),
                MessageTemplateAction(
                    label='微積分習題',
                    text='微積分習題'
                ),
                MessageTemplateAction(
                    label='講義',
                    text='講義'
                )
            ]
        )
    )

    conn=psycopg2.connect("host=120.113.174.17 port=5432 dbname=project201901 user=project201901 password=postgresqllinebotA16829")
    cur = conn.cursor()


    if event.message.text == "海報(<-解答點我)":
        Imagemap_Message = ImagemapSendMessage(
            base_url='https://math-2019.000webhostapp.com/poster_.png?',
            alt_text='this is an imagemap',
            base_size=BaseSize(width=1090, height=420),
            actions=[
                MessageImagemapAction(
                    text='第一題',
                    area=ImagemapArea(
                        x=13, y=15, width=312, height=107
                    )
                ),
                MessageImagemapAction(
                    text='第二題',
                    area=ImagemapArea(
                        x=392, y=15, width=312, height=107
                    )
                ),
                MessageImagemapAction(
                    text='第三題',
                    area=ImagemapArea(
                        x=765, y=15, width=312, height=107
                    )
                ),
                MessageImagemapAction(
                    text='第四題',
                    area=ImagemapArea(
                        x=13, y=157, width=312, height=107
                    )
                ),
                MessageImagemapAction(
                    text='第五題',
                    area=ImagemapArea(
                        x=392, y=157, width=312, height=107
                    )
                ),
                MessageImagemapAction(
                    text='第六題',
                    area=ImagemapArea(
                        x=765, y=157, width=312, height=107
                    )
                ),
                MessageImagemapAction(
                    text='第七題',
                    area=ImagemapArea(
                        x=13, y=303, width=312, height=107
                    )
                ),
                MessageImagemapAction(
                    text='第八題',
                    area=ImagemapArea(
                        x=392, y=303, width=312, height=107
                    )
                ),
                MessageImagemapAction(
                    text='第九題',
                    area=ImagemapArea(
                        x=765, y=303, width=312, height=107
                    )
                )
            ]
        )
        replay_message(event,Imagemap_Message)
        return 0

    if event.message.text == "第一題":
        sql = """SELECT "ID", "messageList", "replyList", "ImagemapUrl", "basesizeWidth", "basesizeHeight" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        # text4=""

        for row in rows:
            text2 = text2 + str(row[2])
            text3 = text3 + str(row[3])
            # BSwidth = int(row[3])
            # BSheight = int(row[4])
            # text4 = text4 + str(rwo[6])
            # x1 = int(row[7])
            # y1 = int(row[8])
            # w1 = int(row[9])
            # h1 = int(row[10])

        Image_Message = ImageSendMessage(original_content_url=text2,preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/f0000-0.png')

        Imagemap_Message = ImagemapSendMessage(
            base_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/Ex001.png?',
            alt_text='this is an imagemap',
            base_size=BaseSize(width=1040, height=170),
            actions=[
                MessageImagemapAction(
                    text='海報第一題解答',
                    area=ImagemapArea(
                        x=177, y=26, width=336, height=92
                    )
                )
            ]
        )
        replay_message(event,Image_Message)
        push_message(event, Imagemap_Message)
        return 0

    if event.message.text == "海報第一題解答":
        sql = """SELECT "ID", "messageList", "replyList", "ButtonText", "ButtonImage", "ButtonLabel-1", "ButtonLabel-2" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2])
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])

        Image_Message = ImageSendMessage(original_content_url=text2,preview_image_url=text2)
        Buttons_Template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title=' ',
                text=text3,
                thumbnail_image_url=text4,
                actions=[
                    MessageTemplateAction(
                        label=text5,
                        text=text5
                    ),
                    MessageTemplateAction(
                        label=text6,
                        text=text6
                    )
                ]
            )
        )
        replay_message(event,Image_Message)
        push_message(event, Buttons_Template)
        return 0

    if event.message.text == "什麼是連續函數？":
        sql = """SELECT "ID", "messageList", "replyList", "ButtonLabel-1", "ButtonLabel-2", "ButtonUrl-1", "ButtonText" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2])
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])

        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text6,
                actions=[                              
                    URITemplateAction(
                        label=text3,
                        uri=text5
                    ),
                    MessageTemplateAction(
                        label=text4,
                        text=text4
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "下一個問題":
        sql = """SELECT "ID", "messageList", "replyList", "ButtonText", "ButtonImage", "ButtonLabel-1", "ButtonLabel-2" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2])
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])

        Buttons_Template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title=' ',
                text=text3,
                thumbnail_image_url=text4,
                actions=[
                    MessageTemplateAction(
                        label=text5,
                        text=text5
                    ),
                    MessageTemplateAction(
                        label=text6,
                        text=text6
                    )
                ]
            )
        )
        replay_message(event,Buttons_Template)
        return 0

    if event.message.text == "什麼是Fubini定理？":
        sql = """SELECT "ID", "messageList", "replyList", "ButtonText", "ButtonImage", "ButtonLabel-1", "ButtonLabel-2", "ButtonLabel-3", "ButtonText-1", "ButtonText-2", "ButtonText-3" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""
        text7=""
        text8=""
        text9=""
        text10=""

        for row in rows:
            text2 = text2 + str(row[2])
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])
            text7 = text7 + str(row[7])
            text8 = text8 + str(row[8])
            text9 = text9 + str(row[9])
            text10 = text10 + str(row[10])

        Buttons_Template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='Fubini Theorem',
                text=text3,
                thumbnail_image_url=text4,
                actions=[
                    MessageTemplateAction(
                        label=text5,
                        text=text8
                    ),
                    MessageTemplateAction(
                        label=text6,
                        text=text9
                    ),
                    MessageTemplateAction(
                        label=text7,
                        text=text10
                    )
                ]
            )
        )
        replay_message(event,Buttons_Template)
        return 0

    if event.message.text == "Fubini定理敘述":
        sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""

        for row in rows:
            text2 = text2 + str(row[2])

        Image_Message = ImageSendMessage(original_content_url=text2,preview_image_url=text2)
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "證明Fubini定理":
        sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""

        for row in rows:
            text2 = text2 + str(row[2])

        Image_Message = ImageSendMessage(original_content_url=text2,preview_image_url=text2)
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "Fubini的相關推論":
        sql = """SELECT "ID", "messageList", "replyList", "replyList-2" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""

        for row in rows:
            text2 = text2 + str(row[2])
            text3 = text3 + str(row[3])

        Image_Message1 = ImageSendMessage(original_content_url=text2,preview_image_url=text2)
        Image_Message2 = ImageSendMessage(original_content_url=text3,preview_image_url=text3)
        replay_message(event,Image_Message1)
        push_message(event, Image_Message2)
        return 0

    
    if event.message.text == "第二題":       
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/題目.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/題目.png')
        Confirm_Template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ConfirmTemplate(
            title='這是ConfirmTemplate',
            text='第一步如何做?',
            actions=[                              
                MessageTemplateAction(
                    label='取ln',
                    text='取ln',

                ),
                MessageTemplateAction(
                    label='x=0帶入',
                    text='x=0帶入'
                )
            ]
        )
    )
        replay_message(event,Image_Message)
        push_message(event,Confirm_Template)
        return 0

    if event.message.text == "x=0帶入":
        message1 = TextSendMessage(text='錯誤!!!')
        message2 = TextSendMessage(text='因為0的0次方是無意義!!!')
        replay_message(event,message1)
        push_message(event,message2)
        return 0
    
    if event.message.text == "取ln":
        message = TextSendMessage(text='正確!!!')
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/ans-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/ans-1.png')
        Confirm_Template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ConfirmTemplate(
            title='這是ConfirmTemplate',
            text='分數型態',
            actions=[                              
                URITemplateAction(
                    uri='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/left.png',
                    text='left',

                ),
                URITemplateAction(
                    uri='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/right.png',
                    text='right'
                )
            ]
        )
    )
        replay_message(event,message)
        push_message(event,Image_Message)
        push_message(event,Confirm_Template)
        return 0
    if event.message.text == "left":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/left-ans.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/left-ans.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "right":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/right-ans.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/right-ans.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "第三題":
        sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""

        for row in rows:
            text2 = text2 + str(row[2]) 
        if text2 == "":
            text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"

        message = TextSendMessage(text=text2)
        replay_message(event,message)
        return 0

    if event.message.text == "第四題":
        sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""

        for row in rows:
            text2 = text2 + str(row[2]) 
        if text2 == "":
            text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"

        message = TextSendMessage(text=text2)
        replay_message(event,message)
        return 0

    if event.message.text == "第五題":
        sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""

        for row in rows:
            text2 = text2 + str(row[2]) 
        if text2 == "":
            text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"

        message = TextSendMessage(text=text2)
        replay_message(event,message)
        return 0

    if event.message.text == "第六題":
        sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""

        for row in rows:
            text2 = text2 + str(row[2]) 
        if text2 == "":
            text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"

        message = TextSendMessage(text=text2)
        replay_message(event,message)
        return 0

    if event.message.text == "第七題":
        sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""

        for row in rows:
            text2 = text2 + str(row[2]) 
        if text2 == "":
            text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"

        message = TextSendMessage(text=text2)
        replay_message(event,message)
        return 0

    if event.message.text == "第八題":
        sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""

        for row in rows:
            text2 = text2 + str(row[2]) 
        if text2 == "":
            text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"

        message = TextSendMessage(text=text2)
        replay_message(event,message)
        return 0

    if event.message.text == "第九題":
        sql = """SELECT "ID", "messageList", "replyList" FROM public."TalkingList" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""

        for row in rows:
            text2 = text2 + str(row[2]) 
        if text2 == "":
            text2 = "嘉義大學應用數學系有一個熱心的曾采雯助教，她的辦公室電話是05-2717861"

        message = TextSendMessage(text=text2)
        replay_message(event,message)
        return 0

    if event.message.text == "講義":
        Imagemap_Message = ImagemapSendMessage(
            base_url='https://math-2019.000webhostapp.com/Teacherlist.png?',
            alt_text='this is an imagemap',
            base_size=BaseSize(width=1061, height=540),
            actions=[
                MessageImagemapAction(
                    text='彭振昌老師',
                    area=ImagemapArea(
                        x=50, y=40, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='陳嘉文老師',
                    area=ImagemapArea(
                        x=380, y=40, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='陳琴韻老師',
                    area=ImagemapArea(
                        x=708, y=40, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='潘宏裕老師',
                    area=ImagemapArea(
                        x=50, y=163, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='鄭富國老師',
                    area=ImagemapArea(
                        x=380, y=163, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='陳榮治老師',
                    area=ImagemapArea(
                        x=708, y=163, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='莊智升老師',
                    area=ImagemapArea(
                        x=50, y=286, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='吳忠武老師',
                    area=ImagemapArea(
                        x=380, y=286, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='陳昇國老師',
                    area=ImagemapArea(
                        x=708, y=286, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='嚴志弘老師',
                    area=ImagemapArea(
                        x=50, y=410, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='胡承方老師',
                    area=ImagemapArea(
                        x=380, y=410, width=288, height=95
                    )
                ),
                MessageImagemapAction(
                    text='鄭博仁老師',
                    area=ImagemapArea(
                        x=708, y=410, width=288, height=95
                    )
                )
            ]
        )
        replay_message(event,Imagemap_Message)
        return 0

    if event.message.text == "微積分習題":
        Imagemap_Message = ImagemapSendMessage(
            base_url='https://math-2019.000webhostapp.com/HandOut.png?',
            alt_text='this is an imagemap',
            base_size=BaseSize(width=1044, height=570),
            actions=[
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=_yqhI8HQlOE',
                    area=ImagemapArea(
                        x=15, y=27, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=OtEJ6LGCW-U',
                    area=ImagemapArea(
                        x=370, y=27, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=bu7nU9Mhpyo',
                    area=ImagemapArea(
                        x=720, y=27, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=BVK_Q6KZSUI',
                    area=ImagemapArea(
                        x=15, y=166, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=Dnj5Tcpev0Q&list=RDY2ge3KrdeWs&index=5',
                    area=ImagemapArea(
                        x=370, y=166, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=ma7r2HGqwXs',
                    area=ImagemapArea(
                        x=720, y=166, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=GuqY5OViunk&list=RDma7r2HGqwXs&index=13',
                    area=ImagemapArea(
                        x=15, y=307, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=5DKNU34L5DA&list=RDma7r2HGqwXs&index=32',
                    area=ImagemapArea(
                        x=370, y=307, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=lUCa4e5Mkrc',
                    area=ImagemapArea(
                        x=720, y=307, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=YKiMrg6rgYQ',
                    area=ImagemapArea(
                        x=15, y=444, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=GCgvpwLNvtY&list=RDma7r2HGqwXs&index=23',
                    area=ImagemapArea(
                        x=370, y=444, width=307, height=102
                    )
                ),
                URIImagemapAction(
                    link_uri='https://www.youtube.com/watch?v=T4SimnaiktU&list=RDma7r2HGqwXs&index=18',
                    area=ImagemapArea(
                        x=720, y=444, width=307, height=102
                    )
                )
            ]
        )
        replay_message(event,Imagemap_Message)
        push_message(event, TextSendMessage(text='請輸入題號'))
        return 0

    if event.message.text == "彭振昌老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "陳嘉文老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "陳琴韻老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "潘宏裕老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "鄭富國老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "陳榮治老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "莊智升老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "吳忠武老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "陳昇國老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "嚴志弘老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "胡承方老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0

    if event.message.text == "鄭博仁老師":
        sql = """SELECT "ID", "messageList", "replyList-1", "replyList-2", "Question", "label-1", "label-2" FROM public."Teacherlist" WHERE "messageList" LIKE '%""" + event.message.text + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[2]) 
            text3 = text3 + str(row[3])
            text4 = text4 + str(row[4])
            text5 = text5 + str(row[5])
            text6 = text6 + str(row[6])



        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text4,
                actions=[                              
                    URITemplateAction(
                        label=text5,
                        uri=text2

                    ),
                    URITemplateAction(
                        label=text6,
                        uri=text3
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0        

    replay_message(event,Buttons_Template)

def replay_message(event,text):
    #text = 'According to your input, my answer is ' + text
    line_bot_api.reply_message(
        event.reply_token,
         text)
        
def push_message(event,text):
    #text = 'According to your input, my answer is ' + text
    line_bot_api.push_message(
        event.source.user_id,
        text)        
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)