from flask import Flask, request, abort

import psycopg2

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
   MessageEvent,TextMessage,TextSendMessage,StickerSendMessage, PostbackTemplateAction, PostbackEvent,ImageSendMessage,TemplateSendMessage,ButtonsTemplate,PostbackTemplateAction
)

from linebot.models import *

import os
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(os.environ['lineToken'])
# Channel Secret
handler = WebhookHandler(os.environ['lineSecret'])

import requests
#import test1

headers = {"Authorization":"Bearer " + os.environ['lineToken'] + "\"","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-1bbc439c8565a487708dec4f59871f76', 
                       headers=headers)

print(req.text)

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


@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    print(event)

    message = TextSendMessage(text="收到圖片")  
    replay_message(event,message)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
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

    # {
    #   "richmenus": [
    #     {
    #       "richMenuId": "richmenu-4a2a6a2391bf4eaafba936d4bd9a950b",
    #       "size": {
    #         "width": 2500,
    #         "height": 1686
    #       },
    #       "selected": false,
    #       "areas": [
    #         {
    #           "bounds": {
    #             "x": 0,
    #             "y": 0,
    #             "width": 2500,
    #             "height": 1686
    #           },
    #           "action": {
    #             "type": "postback",
    #             "data": "action=buy&itemid=123"
    #           }
    #         }
    #       ]
    #     }
    #   ]
    # }

    #連接資料庫---------------------------------------------------------------------------------------------------------
    conn=psycopg2.connect("host=120.113.174.17 port=5432 dbname=project201901 user=project201901 password=postgresqllinebotA16829") #user=os.environ['改']
    cur = conn.cursor()


    #微微---------------------------------------------------------------------------------------------------------------
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

    #點RichMenu的"我要找微微"--------------------------------------------------------------------------------------------
    if event.message.text == "Hello, WeiWei~":
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
        replay_message(event,Buttons_Template)

    #海報---------------------------------------------------------------------------------------------------------------
    if event.message.text == "海報(<-解答點我)":
        Carousel_Template1 = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://www.how-to-study.com/images/study-skills-assessments.jpg',
                        title='第一題',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='poster01'
                            ),
                            PostbackTemplateAction(
                                label='解答',
                                data='posterA01'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.how-to-study.com/images/study-skills-assessments.jpg',
                        title='第二題',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='poster02'
                            ),
                            PostbackTemplateAction(
                                label='解答',
                                data='posterA02'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.how-to-study.com/images/study-skills-assessments.jpg',
                        title='第三題',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='poster03'
                            ),
                            PostbackTemplateAction(
                                label='解答',
                                data='posterA03'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.how-to-study.com/images/study-skills-assessments.jpg',
                        title='第四題',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='poster04'
                            ),
                            PostbackTemplateAction(
                                label='解答',
                                data='posterA04'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.how-to-study.com/images/study-skills-assessments.jpg',
                        title='第五題',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='poster05'
                            ),
                            PostbackTemplateAction(
                                label='解答',
                                data='posterA05'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.how-to-study.com/images/study-skills-assessments.jpg',
                        title='第六題',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='poster06'
                            ),
                            PostbackTemplateAction(
                                label='解答',
                                data='posterA06'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.how-to-study.com/images/study-skills-assessments.jpg',
                        title='第七題',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='poster07'
                            ),
                            PostbackTemplateAction(
                                label='解答',
                                data='posterA07'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.how-to-study.com/images/study-skills-assessments.jpg',
                        title='第八題',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='poster08'
                            ),
                            PostbackTemplateAction(
                                label='解答',
                                data='posterA08'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.how-to-study.com/images/study-skills-assessments.jpg',
                        title='第九題',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='poster09'
                            ),
                            PostbackTemplateAction(
                                label='解答',
                                data='posterA09'
                            )
                        ]
                    )
                ]
            )
        )
        replay_message(event,Carousel_Template1)
        return 0

    #海報第一題----------------------------------------------------------------------------------------------------------
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

    #習題---------------------------------------------------------------------------------------------------------------
    if event.message.text == "微積分習題":
        Carousel_Template1 = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0011.jpg',
                        title='函數極限',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0001'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0008.jpg',
                        title='連續',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0002'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0007.jpg',
                        title='微分',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0003'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0006.jpg',
                        title='微分應用',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0004'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0003.jpg',
                        title='積分',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0005'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0001.jpg',
                        title='積分應用',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0006'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0002.jpg',
                        title='積分技巧',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0007'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0005.jpg',
                        title='極座標',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0008'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0004.jpg',
                        title='數列與級數',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0009'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0010.jpg',
                        title='弧長 表面積',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0010'
                            )
                        ]
                    )
                ]
            )
        )

        Carousel_Template2 = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0012.jpg',
                        title='多變量微分與應用',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0011'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/微積分習題_190526_0009.jpg',
                        title='重積分',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='題目',
                                data='ex0012'
                            )
                        ]
                    )
                ]
            )
        )
        
        replay_message(event,Carousel_Template1)
        push_message(event,Carousel_Template2)
        return 0

    #習題第一章第一題-----------------------------------------------------------------------------------------------
    if event.message.text == "取ln正確!!!":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/ans-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/ans-1.png')
        Imagemap_Message = ImagemapSendMessage(
            base_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/06/chose.png?',
            alt_text='this is an imagemap',
            base_size=BaseSize(width=1040,height=424),
            actions=[
                MessageImagemapAction(
                    text='左邊分數型態',
                    area=ImagemapArea(
                        x=0, y=172, width=530, height=252
                    )
                ), 
                MessageImagemapAction(
                    text='右邊分數型態',
                    area=ImagemapArea(
                        x=530, y=172, width=510, height=252
                    )
                ) 
            ]
        )
        replay_message(event,Image_Message)
        push_message(event,Imagemap_Message)
        return 0
    
    if event.message.text == "左邊分數型態":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/left-ans.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/left-ans.png')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "右邊分數型態":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/right-ans.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/05/right-ans.png')
        replay_message(event,Image_Message)
        return 0   

    if event.message.text == "x=0帶入錯誤!!!":
        message = TextSendMessage(text="因為0的0次方是無意義!!!")
        replay_message(event,message)
        return 0
    
    #習題第二章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "計算極限值":
        message = TextSendMessage(text="正確的第一步！")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/1562069251935.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/1562069251935.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "解方程式":
        message = TextSendMessage(text="好像不對呦！讓我們先來了解一下判斷函數是否連續需要注意的事情：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/1562070062061.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/1562070062061.jpg')
        message2 = TextSendMessage(text="此題的極限值不等於函數值，所以不是連續函數")
        replay_message(event,message)
        push_message(event,Image_Message)
        push_message(event,message2)
        return 0

    #習題第三章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "上下各別微分":
        message = TextSendMessage(text="對於除法模式的微分是有公式的呦，分子分母各別微分是不對的！")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/04/1562424192384.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/04/1562424192384.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "利用除法微分公式":
        message = TextSendMessage(text="沒錯！利用除法微分公式對函數進行微分，且過程中需特別注意鏈鎖律(Chain-Rule)！！！解題過程如下：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/04/1562423294456.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/04/1562423294456.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    #習題第四章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "利用中間值定理":
        message = TextSendMessage(text="沒錯！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/1562568755853.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/1562568755853.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "化簡平方根":
        message = TextSendMessage(text="利用中間值定理(Mean Value Theorem)會更棒喔！")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/1562570556071.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/1562570556071.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    #習題第五章第一題-----------------------------------------------------------------------------------------------
    if event.message.text == "第一步":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans000500001-1.gif',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans000500001-1.gif')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "第二步":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00050001-2.gif',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00050001-2.gif')
        Buttons_Template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='了解更多',
                text=' ',
                thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/11.jpg',
                actions=[
                    URITemplateAction(
                        label='何謂"代換積分法"',
                        uri='https://learningcalculus.hol.es/cswei/%EF%BC%83%E4%BB%A3%E6%8F%9B%E7%A9%8D%E5%88%86%E6%B3%95/'
                    ),
                    URITemplateAction(
                        label='三角積分公式表',
                        uri='https://zh.wikipedia.org/zh-tw/%E4%B8%89%E8%A7%92%E5%87%BD%E6%95%B0%E7%A7%AF%E5%88%86%E8%A1%A8'
                    )
                ]
            )
        )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    #習題第六章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "a":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00060001-a.gif',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00060001-a.gif')
        Buttons_Template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='了解更多旋轉體體積運算!!!',
                text=' ',
                thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/10.jpg',
                actions=[
                    URITemplateAction(
                        label='旋轉體公式',
                        uri='https://zh.wikipedia.org/zh-tw/%E6%97%8B%E8%BD%AC%E4%BD%93'
                    ),
                    URITemplateAction(
                        label='教學影片1',
                        uri='https://www.youtube.com/watch?v=cbmGB3MI96w'
                    ),
                    URITemplateAction(
                        label='教學影片2',
                        uri='https://www.youtube.com/watch?v=Y4A1k7FNIus'
                    ),
                ]
            )
        )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0
    if event.message.text == "b":
        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text='此題有兩種解，請選擇',
                actions=[                              
                    MessageTemplateAction(
                        label='solution1',
                        text='solution1'
                    ),
                    MessageTemplateAction(
                        label='solution2',
                        text='solution2'
                    )
                ]
            )
        )
        replay_message(event,Confirm_Template)
        return 0
    if event.message.text == "solution1":
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00060001-b1.gif',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00060001-b1.gif')
        replay_message(event,Image_Message1)
        return 0
    if event.message.text == "solution2":
        Image_Message2 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00060001-b2.gif',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00060001-b2.gif')
        replay_message(event,Image_Message2)
        return 0
    #習題第七章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "積分代換法":
        message = TextSendMessage(text="因為無法消去x")
        replay_message(event,message)
        return 0
    if event.message.text == "瑕積分":
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00070001-1.gif',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00070001-1.gif')
        Image_Message2 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00070001-2.gif',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/ans00070001-2.gif')
        replay_message(event,Image_Message1)
        push_message(event,Image_Message2)
        return 0

    #習題第八章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "sqrt(r1平方+r2平方)":
        message = TextSendMessage(text="錯誤！未考慮兩個半徑的夾角")
        replay_message(event,message)
        return 0

    if event.message.text == "sqrt(r1平方+r2平方-2r1r2cos(theta1-theta2))":
        message = TextSendMessage(text="沒錯！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/polar-coordinate-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/polar-coordinate-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0   

    #習題第九章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "使用Root Test":
        message = TextSendMessage(text="錯誤！因為(2n)!無法開根號")
        replay_message(event,message)
        return 0

    if event.message.text == "使用Ratio Test":
        message = TextSendMessage(text="沒錯！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/series-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/series-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0 

    #習題第十章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "r微分一次的平方+r微分二次的平方":
        message = TextSendMessage(text="錯誤！正確解答如下")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/surface-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/surface-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "r平方+r微分一次的平方":
        message = TextSendMessage(text="沒錯！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/surface-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/surface-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0 

    #習題第十一章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "做偏微分":
        message = TextSendMessage(text="沒錯！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/several-variables-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/several-variables-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "直接將點帶入":
        message = TextSendMessage(text="直接將點帶入無法求出切平面喔")
        replay_message(event,message)
        return 0

    #習題第十二章第一題------------------------------------------------------------------------------------------------
    if event.message.text == "先做dy再dx":
        message = TextSendMessage(text="沒錯！來看一下解題過程：")
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/iterated-integral-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/iterated-integral-answer.png')
        Image_Message2 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/iterated-integral-answer-plot.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/iterated-integral-answer-plot.png')
        replay_message(event,message)
        push_message(event,Image_Message1)
        push_message(event,Image_Message2)
        return 0

    if event.message.text == "先做dx再dy":
        message = TextSendMessage(text="先對x積分需對根號x及sin(x)積分，如果做iterated integral，可以先將根號x及sin(x)當成常數對y積分，然後再對x積分")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/iterated-integral-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/07/iterated-integral-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0
    
    #習題第十二章第二題------------------------------------------------------------------------------------------------ 
    if event.message.text == "將參數更改為極坐標":
        message = TextSendMessage(text="沒錯！你可能會遇到的問題：")
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='如何將參數更改為極坐標：',
                    thumbnail_image_url='https://sites.google.com/a/lsps.ptc.edu.tw/lsps/_/rsrc/1470837072195/home/shu-xue-ke/math.png',
                    actions=[
                        MessageTemplateAction(
                            label='定理',
                            text='變換極坐標定理'
                        ),
                        MessageTemplateAction(
                            label='證明',
                            text='變換極坐標定理證明'
                        ),
                        MessageTemplateAction(
                            label='點我看答案',
                            text='ch12-2'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Buttons_Template)
        return 0
    
    if event.message.text == "變換極坐標定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-1.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "變換極坐標定理證明":
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-1-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-1-1.png')
        Image_Message2 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-1-11.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-1-11.png')        
        replay_message(event,Image_Message1)
        push_message(event,Image_Message2)
        return 0
    if event.message.text == "ch12-2":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-2.png')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "利用旋轉體體積":
        message = TextSendMessage(text="沒錯！旋轉體體積也是一種方法")
        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text='了解定理，運算方面能更加清楚喔!!',
                actions=[                              
                    MessageTemplateAction(
                        label='旋轉體體積定理',
                        text='旋轉體體積定理'
                    ),
                    MessageTemplateAction(
                        label='點我看答案',
                        text='ch12-3'
                    )
                ]
            )
        )
        replay_message(event,message)
        push_message(event,Confirm_Template)
        return 0

    if event.message.text == "旋轉體體積定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-1.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "ch12-3":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-2.png')
        replay_message(event,Image_Message)
        return 0
    #習題第十二章第三題------------------------------------------------------------------------------------------------ 

    #講義-----------------------------------------------------------------------------------------------------------
    if event.message.text == "講義":
        Carousel_Template1 = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://applealmond.com/wp-content/uploads/2018/11/1541078537-090bd6987af814bfa1d1a0bfd919f47d.png',
                        title='Preparation for Calculus',
                        text=' ',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch00'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.itaste168.com/Uploads/Document/33/636667442060636366.jpg',
                        title='Chapter1',
                        text='Limits and Their Properties',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch01'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/pooh-800x800-4-1547120194.jpg?crop=1.00xw:0.746xh;0,0&resize=480:*',
                        title='Chapter2',
                        text='Differentiation',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch02'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/pooh-800x800-2-1547120140.jpg?crop=1.00xw:0.751xh;0,0&resize=480:*',
                        title='Chapter3',
                        text='Applications of Differentiation',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch03'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://icrvb3jy.xinmedia.com/solomo/article/160769/A630FC9A-B215-6038-DA34-52280F785AB1.jpeg',
                        title='chapter4',
                        text='Integration',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch04'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://pic.pimg.tw/yannshiuan/114111989450.bmp_n.jpg',
                        title='chapter5',
                        text='Logarithmic,Exponential,and Other Transcendental Functions',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch05'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://wallpaper.gamme.com.tw/wp/514/download/1024x768',
                        title='chapter6',
                        text='Differetial Equations',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch06'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://images.chinatimes.com/newsphoto/2017-01-26/900/20170126004408.jpg',
                        title='chapter7',
                        text='Applications of Integration',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch07'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt2Jmz1oUfg38IFd_ohJao4PZfQzrQs-pidgMLRzneQmXuzPH2',
                        title='chapter8',
                        text='Integration Techniques and Improper Integrals',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch08'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12458515/ANDROID/sticker.png',
                        title='chapter9',
                        text='Infinite Series',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch09'
                            )
                        ]
                    )
                ]
            )
        )

        Carousel_Template2 = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYda8vHxZVOnqjMC9BWTjq0IhMctvHh5DhQBywzTFDvAcLTzQ6',
                        title='chapter10',
                        text='Conics,Parametric Equations,and Polar Coordinates',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch10'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://wallpapercave.com/wp/wp2491155.jpg',
                        title='chapter11',
                        text='Vectors and the Geometry of Space',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch11'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://ae01.alicdn.com/kf/HTB1Qj.JRFXXXXXwapXXq6xXFXXXb/7x5FT-Hijau-Rumput-Taman-Winnie-Tiger-Bunga-Sky-Photo-Studio-Backdrop-Latar-Belakang-Vinyl-220-Cm.jpg',
                        title='chapter12',
                        text='Vector-Valued Functions',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch12'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://stmed.net/sites/default/files/winnie-the-pooh-wallpapers-26330-478526.jpg',
                        title='chapter13',
                        text='Functions of Several Variables',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch13'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://cdn.newsapi.com.au/image/v1/e5a2fa8d705134aebee222ba8218cadb',
                        title='chapter14',
                        text='Multiple Integration',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch14'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i0.wp.com/clipart-library.com/img1/417460.png?w=600',
                        title='chapter15',
                        text='Vector Analysis',
                        actions=[
                            PostbackTemplateAction(
                                label='講義',
                                data='ch15'
                            )
                        ]
                    )
                ]
            )
        )

        replay_message(event,Carousel_Template1)
        push_message(event,Carousel_Template2)
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


@handler.add(PostbackEvent)
def handle_postback(event):

    #連接資料庫--------------------------------------------------------------------------------------------------
    conn=psycopg2.connect("host=120.113.174.17 port=5432 dbname=project201901 user=project201901 password=postgresqllinebotA16829")
    cur = conn.cursor()

    #習題題目格式------------------------------------------------------------------------------------------------
    if  len(event.postback.data) == 10:
        sql = """SELECT "value", "Llabel", "Ltext", "Rlabel", "Rtext" FROM public."temp" WHERE "number" LIKE '%""" + event.postback.data + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        # #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""

        for row in rows:
            text2 = text2 + str(row[0]) 
            text3 = text3 + str(row[1])
            text4 = text4 + str(row[2])
            text5 = text5 + str(row[3])
            text6 = text6 + str(row[4])

        Image_Message = ImageSendMessage(original_content_url=text2,preview_image_url=text2)
        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text='第一步如何做?',
                actions=[                              
                    MessageTemplateAction(
                        label=text3,
                        text=text4
                    ),
                    MessageTemplateAction(
                        label=text5,
                        text=text6
                    )
                ]
            )
        )
        replay_message(event,Image_Message)
        push_message(event, Confirm_Template)
        
    #習題章節--------------------------------------------------------------------------------------------------------
    if  len(event.postback.data) == 6:
        sql = """SELECT "value", "name", "picture" FROM public."chapter" WHERE "number" LIKE '%""" + event.postback.data + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        # #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        # text5=""
        # text6=""

        for row in rows:
            text2 = text2 + str(row[0]) 
            text3 = text3 + str(row[1])
            text4 = text4 + str(row[2])
        #     text5 = text5 + str(row[5])
        #     text6 = text6 + str(row[6])


        if text2 == '1' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第一題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0001"
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '2' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第一題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0001"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第二題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0002"
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '3' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第一題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0001"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第二題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0002"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第三題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0003"
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '4' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第一題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0001"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第二題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0002"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第三題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0003"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第四題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0004"
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '5' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第一題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0001"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第二題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0002"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第三題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0003"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第四題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0004"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第五題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0005"
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '6' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第一題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0001"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第二題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0002"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第三題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0003"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第四題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0004"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第五題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0005"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第六題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0006"
                                )
                            ]
                        )
                    ]
                )
            )
        else:
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第一題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0001"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第二題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0002"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第三題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0003"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第四題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0004"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第五題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0005"
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text3,
                            text='第六題',
                            actions=[
                                PostbackTemplateAction(
                                    label='題目',
                                    data=str(event.postback.data) + "0006"
                                )
                            ]
                        )
                    ]
                )
            )

        replay_message(event,Carousel_Template)

    #海報題目-----------------------------------------------------------------------------------------------------------------------
    if  len(event.postback.data) == 8:
        sql = """SELECT "value" FROM public."poster" WHERE "number" LIKE '%""" + event.postback.data + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        # #text2 = "According to your input, my answer is "
        text2=""
        # text3=""
        # text4=""
        # text5=""
        # text6=""

        for row in rows:
            text2 = text2 + str(row[0]) 
        #     text3 = text3 + str(row[3])
        #     text4 = text4 + str(row[4])
        #     text5 = text5 + str(row[5])
        #     text6 = text6 + str(row[6])

        Image_Message = ImageSendMessage(original_content_url=text2,preview_image_url=text2)
        replay_message(event,Image_Message)  

    #海報---------------------------------------------------------------------------------------------------------------------------
    if  len(event.postback.data) == 9:
        sql = """SELECT "value", "problem", "label1", "text1", "label2", "text2" FROM public."posterAnswer" WHERE "number" LIKE '%""" + event.postback.data + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        # #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""
        text7=""

        for row in rows:
            text2 = text2 + str(row[0]) 
            text3 = text3 + str(row[1])
            text4 = text4 + str(row[2])
            text5 = text5 + str(row[3])
            text6 = text6 + str(row[4])
            text7 = text6 + str(row[5])

        Image_Message = ImageSendMessage(original_content_url=text2,preview_image_url=text2)
        
        if text3 == "Y":
            Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你可能會遇到的問題：',
                    thumbnail_image_url='https://media.istockphoto.com/vectors/collection-of-colurful-stickmen-with-question-mark-icon-vector-vector-id936398386',
                    actions=[
                        MessageTemplateAction(
                            label=text4,
                            text=text5
                        ),
                        MessageTemplateAction(
                            label=text6,
                            text=text7
                        )
                    ]
                )
            )
            replay_message(event,Image_Message)
            push_message(event, Buttons_Template)

        replay_message(event,Image_Message)
        

    #講義-------------------------------------------------------------------------------------------------------------------------------
    if  len(event.postback.data) == 4:
        sql = """SELECT "value", "name", "picture", "chapter", "part1", "part2", "part3", "part4", "part5", "part6", "part7", "part8", "part9", "part10" FROM public."handoutChapter" WHERE "number" LIKE '%""" + event.postback.data + "%'" 
        cur.execute(sql)
        rows = cur.fetchall()
        # #text2 = "According to your input, my answer is "
        text2=""
        text3=""
        text4=""
        text5=""
        text6=""
        text7=""
        text8=""
        text9=""
        text10=""
        text11=""
        text12=""
        text13=""
        text14=""
        text15=""

        for row in rows:
            text2 = text2 + str(row[0]) 
            text3 = text3 + str(row[1])
            text4 = text4 + str(row[2])
            text5 = text5 + str(row[3])
            text6 = text6 + str(row[4])
            text7 = text7 + str(row[5])
            text8 = text8 + str(row[6])
            text9 = text9 + str(row[7])
            text10 = text10 + str(row[8])
            text11 = text11 + str(row[9])
            text12 = text12 + str(row[10])
            text13 = text13 + str(row[11])
            text14 = text14 + str(row[12])
            text15 = text15 + str(row[13])


        if text2 == '1' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '2' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part2',
                                    uri=text7
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '3' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part2',
                                    uri=text7
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part3',
                                    uri=text8
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '4' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part2',
                                    uri=text7
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part3',
                                    uri=text8
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part4',
                                    uri=text9
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '5' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part2',
                                    uri=text7
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part3',
                                    uri=text8
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part4',
                                    uri=text9
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part5',
                                    uri=text10
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '6' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part2',
                                    uri=text7
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part3',
                                    uri=text8
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part4',
                                    uri=text9
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part5',
                                    uri=text10
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part6',
                                    uri=text11
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '7' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                       CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part2',
                                    uri=text7
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part3',
                                    uri=text8
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part4',
                                    uri=text9
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part5',
                                    uri=text10
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part6',
                                    uri=text11
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part7',
                                    uri=text12
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '8' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part2',
                                    uri=text7
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part3',
                                    uri=text8
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part4',
                                    uri=text9
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part5',
                                    uri=text10
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part6',
                                    uri=text11
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part7',
                                    uri=text12
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part8',
                                    uri=text13
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '9' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part2',
                                    uri=text7
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part3',
                                    uri=text8
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part4',
                                    uri=text9
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part5',
                                    uri=text10
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part6',
                                    uri=text11
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part7',
                                    uri=text12
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part8',
                                    uri=text13
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part9',
                                    uri=text14
                                )
                            ]
                        )
                    ]
                )
            )
        elif text2 == '10' :
            Carousel_Template = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part1',
                                    uri=text6
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part2',
                                    uri=text7
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part3',
                                    uri=text8
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part4',
                                    uri=text9
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part5',
                                    uri=text10
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part6',
                                    uri=text11
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part7',
                                    uri=text12
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part8',
                                    uri=text13
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part9',
                                    uri=text14
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=text4,
                            title=text5,
                            text=text3,
                            actions=[
                                URITemplateAction(
                                    label='part10',
                                    uri=text15
                                )
                            ]
                        )
                    ]
                )
            )

        replay_message(event,Carousel_Template)




        #replay_message(event,TextSendMessage(text='pong'))

        #line_bot_api.reply_message(
            #event.reply_token, TextSendMessage(text='pong'))      
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)