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
            thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/logo.jpg',
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

    #習題第二章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "求極限值":
        message = TextSendMessage(text="正確！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/continuous-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/continuous-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "將三式相等解a和b":
        message = TextSendMessage(text="錯誤！題目說明要使此函數為連續函數，應該使用下面方法解題：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/continuous-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/continuous-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
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
    
    #習題第三章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "先做Chain-Rule":
        message = TextSendMessage(text="第一步正確！")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/differential-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/differential-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "將數字直接代入":
        message = TextSendMessage(text="錯誤！14代入函數g求出2，再將2代入函數f，但題目沒有定義此值，所以無法求出答案")
        replay_message(event,message)
        return 0

    #習題第三章第三題------------------------------------------------------------------------------------------------
    if event.message.text == "ch3-3-(1)":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0003000301.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0003000301.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='忘記Chain Rule是什麼嗎？',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我了解Chain Rule',
                            text='了解Chain Rule'
                        )
                    ]
                )
            )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "ch3-3-(2)":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0003000302.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0003000302.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='忘記Chain Rule是什麼嗎？',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我了解Chain Rule',
                            text='了解Chain Rule'
                        )
                    ]
                )
            )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "了解Chain Rule":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00030003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00030003.jpg')
        replay_message(event,Image_Message)
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

    #習題第四章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "一次微分=0":
        message = TextSendMessage(text="錯誤！反曲點應該要求二次微分等於0")
        replay_message(event,message)
        return 0

    if event.message.text == "二次微分=0":
        message = TextSendMessage(text="正確！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/diff-application-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/diff-application-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0
    
    #習題第四章第三題------------------------------------------------------------------------------------------------
    if event.message.text == "因式分解":
        message = TextSendMessage(text="不對呦！應該先做一次微分再因式分解")
        message2 = TextSendMessage(text="讓我們來看一下正確解題過程")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00040003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00040003.jpg')
        replay_message(event,message)
        push_message(event,message2)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "一次微分":
        message = TextSendMessage(text="正確！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00040003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00040003.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='認識相關定理',
                            text='了解ch4-3相關定理'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    #習題第四章第四題------------------------------------------------------------------------------------------------
    if event.message.text == "關於asymptote":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/def00040004.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/def00040004.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='想要繼續了解題目的解題過程？',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我看解題過程',
                            text='ch4-4解題過程'
                        )
                    ]
                )
            )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "ch4-4解題過程":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00040004.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00040004.jpg')
        replay_message(event,Image_Message)
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

    #習題第五章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "分兩範圍積分":
        message = TextSendMessage(text="正確！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/integral-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/integral-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "直接積分":
        message = TextSendMessage(text="錯誤！x大於1/2及x小於1/2的函數數不同，需要分成兩個範圍積分")
        replay_message(event,message)
        return 0

    #習題第五章第三題------------------------------------------------------------------------------------------------
    if event.message.text == "ch5-3解題過程":
        message = TextSendMessage(text="讓我們來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00050003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00050003.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "ch5-3相關定理":
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='想了解哪個定理?',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='認識FTC1',
                            text='了解Fundamental Theorem of Calculus,Part1'
                        ),
                        MessageTemplateAction(
                            label='認識FTC2',
                            text='了解Fundamental Theorem of Calculus,Part2'
                        ),
                        MessageTemplateAction(
                            label='認識Chain Rule',
                            text='了解Chain Rule'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0

    if event.message.text == "了解Fundamental Theorem of Calculus,Part1":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0005000301.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0005000301.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "了解Fundamental Theorem of Calculus,Part2":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0005000302.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0005000302.jpg')
        replay_message(event,Image_Message)
        return 0

    #習題第五章第四題------------------------------------------------------------------------------------------------
    if event.message.text == "ch5-4的定理證明":
        message = TextSendMessage(text="好的，我們來看一下上面這個定理的證明：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/pf00050004.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/pf00050004.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='繼續來看題目~',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我看題目',
                            text='ch5-4題目'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "ch5-4題目":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ex0005000402.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ex0005000402.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你可能會需要：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='看解題過程',
                            text='ch5-4解題過程'
                        )
                    ]
                )
            )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "ch5-4解題過程":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00050004.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00050004.jpg')
        replay_message(event,Image_Message)
        return 0

    #習題第五章第五題------------------------------------------------------------------------------------------------
    if event.message.text == "了解中點法":
        message = TextSendMessage(text="好的，我們來看一下Midpoint Rule：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00050005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00050005.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='想要繼續了解題目的解題過程？',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我看解題過程',
                            text='ch5-5解題過程'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "ch5-5解題過程":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00050005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00050005.jpg')
        replay_message(event,Image_Message)
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

    #習題第六章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "取極限值":
        message = TextSendMessage(text="錯誤！應該求積分，來看一下正確解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/int-application-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/int-application-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "求積分":
        message = TextSendMessage(text="正確！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/int-application-answer.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/int-application-answer.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0
    
    #習題第六章第三題------------------------------------------------------------------------------------------------
    if event.message.text == "ch6-3積分":
        message = TextSendMessage(text="正確！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060003.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "ch6-3取極限值":
        message = TextSendMessage(text="錯誤！應該求積分，來看一下正確解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060003.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    #習題第六章第四題------------------------------------------------------------------------------------------------
    if event.message.text == "了解弧長定義":
        message = TextSendMessage(text="好的，我們來看一下弧長的定義：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00060004.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00060004.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "ch6-4解答":
        message = TextSendMessage(text="好的，我們來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060004.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060004.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    #習題第六章第五題------------------------------------------------------------------------------------------------
    if event.message.text == "查看ch6-5圖形":
        message = TextSendMessage(text="好的，我們來看一下ch6-5圖形：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/picture00060005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/picture00060005.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "查看ch6-5解題過程":
        message = TextSendMessage(text="好的，我們來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060005.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    #習題第六章第六題------------------------------------------------------------------------------------------------
    if event.message.text == "ch6-6答案":
        message = TextSendMessage(text="這題的答案為18")
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你可能會需要：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='看解題過程',
                            text='ch6-6解題過程'
                        )
                    ]
                )
            )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "ch6-6小提示":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/hint00060006.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/hint00060006.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你可能會需要：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='看解題過程',
                            text='ch6-6解題過程'
                        )
                    ]
                )
            )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0 

    if event.message.text == "ch6-6解題過程":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060006.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00060006.jpg')
        replay_message(event,Image_Message)
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
    
    #習題第七章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "方法一":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0007000201.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0007000201.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "方法二":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0007000202.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0007000202.jpg')
        replay_message(event,Image_Message)
        return 0 
    
    #習題第七章第三題------------------------------------------------------------------------------------------------
    if event.message.text == "ch7-3解題小技巧":
        message = TextSendMessage(text="先來看看這題的積分技巧：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00070003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00070003.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='想要了解題目完整解題過程？',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我看解題過程',
                            text='ch7-3解題過程'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0
 
    if event.message.text == "ch7-3解題過程":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00070003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00070003.jpg')
        replay_message(event,Image_Message)
        return 0

    #習題第七章第四題------------------------------------------------------------------------------------------------
    if event.message.text == "點我看簡答":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0007000401.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0007000401.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你可能會需要：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='看解題過程',
                            text='ch7-4解題過程'
                        )
                    ]
                )
            )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "第一步小提示":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/hint00070004.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/hint00070004.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你可能會需要：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='看解題過程',
                            text='ch7-4解題過程'
                        )
                    ]
                )
            )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0 

    if event.message.text == "ch7-4解題過程":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0007000402.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0007000402.jpg')
        replay_message(event,Image_Message)
        return 0

    #習題第七章第五題------------------------------------------------------------------------------------------------
    if event.message.text == "定積分代換":
        message = TextSendMessage(text="好像不對呦！來了解一下定積分代換定理和分部積分法吧~")
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='選擇想了解的選項：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='定積分代換定理',
                            text='我想了解定積分代換定理'
                        ),
                        MessageTemplateAction(
                            label='分部積分法',
                            text='我想了解分部積分法'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "分部積分法":
        message = TextSendMessage(text="正確的選擇！")
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你可能會需要：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我看解答',
                            text='ch7-5解答'
                        ),
                        MessageTemplateAction(
                            label='複習部分積分法',
                            text='我想了解分部積分法'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Buttons_Template)
        return 0 

    if event.message.text == "我想了解定積分代換定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0007000501.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0007000501.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "我想了解分部積分法":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0007000502.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0007000502.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "ch7-5解答":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00070005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00070005.jpg')
        replay_message(event,Image_Message)
        return 0

    #習題第七章第六題------------------------------------------------------------------------------------------------
    if event.message.text == "運用部分積分法":
        message = TextSendMessage(text="好像不對呦！來了解一下這兩個方法吧~")
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='選擇想了解的選項：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='瑕積分',
                            text='我想了解瑕積分'
                        ),
                        MessageTemplateAction(
                            label='分部積分法',
                            text='我想了解分部積分法'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "運用瑕積分":
        message = TextSendMessage(text="選擇正確！")
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你可能會需要：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我看解答',
                            text='ch7-6解答'
                        ),
                        MessageTemplateAction(
                            label='複習瑕積分',
                            text='我想了解瑕積分'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Buttons_Template)
        return 0 

    if event.message.text == "我想了解瑕積分":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00070006.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00070006.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "ch7-6解答":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00070006.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00070006.jpg')
        replay_message(event,Image_Message)
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

    #習題第八章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "第(1)題":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0008000201.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0008000201.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "第(2)題":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0008000202.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0008000202.jpg')
        replay_message(event,Image_Message)
        return 0
    #習題第八章第三題------------------------------------------------------------------------------------------------
    if event.message.text == "ch8-3解題過程":
        message = TextSendMessage(text="來看看這題的解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080003.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "ch8-3相關定理":
        message = TextSendMessage(text="來了解一下這題相關定理：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00080003.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00080003.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0 

    #習題第八章第四題------------------------------------------------------------------------------------------------
    if event.message.text == "圖形":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080004-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080004-1.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "解答":
        Buttons_Template = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='這是ButtonsTemplate',
                text='ButtonsTemplate可以傳送text,uri',
                thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/12.jpg',
                actions=[
                MessageTemplateAction(
                    label='ch8-4定理',
                    text='ch8-4定理'
                ),
                MessageTemplateAction(
                    label='答案',
                    text='答案'
                )
            ]
        )
    )
        replay_message(event,Buttons_Template)
        return 0
    if event.message.text == "ch8-4定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080004-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080004-2.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "答案":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080004-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080004-3.png')
        replay_message(event,Image_Message)
        return 0

    #習題第八章第五題------------------------------------------------------------------------------------------------
    if event.message.text == "8r":
        message = TextSendMessage(text="正確！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080005.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "8r*pi":
        message = TextSendMessage(text="錯誤！答案應為8r,來看一下正確的解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080005.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0 

    #習題第八章第六題------------------------------------------------------------------------------------------------
    if event.message.text == "心臟線圖形":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-1.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "解題方法":
        Carousel_Template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/12.jpg',
                        title='解答',
                        text=' ',
                        actions=[
                            MessageTemplateAction(
                                label='步驟一',
                                text='步驟一'
                            ),
                            MessageTemplateAction(
                                label='提示',
                                text='提示'
                            ),
                            MessageTemplateAction(
                                label='步驟二',
                                text='步驟二'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/12.jpg',
                        title='定理',
                        text=' ',
                        actions=[
                            MessageTemplateAction(
                                label='ch8-6定理',
                                text='ch8-6定理'
                            ),
                            MessageTemplateAction(
                                label='定理證明',
                                text='定理證明'
                            ),
                            MessageTemplateAction(
                                label='證明中引用的定理',
                                text='證明中引用的定理'
                            )
                        ]
                    )
                ]
            )
        )
        replay_message(event,Carousel_Template)
        return 0
    if event.message.text == "步驟一":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-2.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "提示":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-3.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "步驟二":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-4.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-4.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "ch8-6定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-5.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-5.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "定理證明":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-6.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-6.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "證明中引用的定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-7.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00080006-7.png')
        replay_message(event,Image_Message)
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
    
    #習題第九章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "看解題過程":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090002.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090002.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "先了解定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00090002.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00090002.jpg')
        replay_message(event,Image_Message)
        return 0

    #習題第九章第三題------------------------------------------------------------------------------------------------
    if event.message.text == "(1)":
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你會遇到的問題：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        URITemplateAction(
                            label='影片教學',
                            uri='https://tw.video.search.yahoo.com/search/video?fr=mcafee&p=L%E2%80%99Hopital%E2%80%99s+Rule#id=2&vid=2e18a89dfab2dcae2d0b1ecbff038754&action=click'
                        ),
                        MessageTemplateAction(
                            label='點我看答案',
                            text='ch9-3-1'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0
    if event.message.text == "(2)":   
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你會遇到的問題：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        URITemplateAction(
                            label='L’Hopital’s Rule',
                            uri='https://zh.wikipedia.org/zh-tw/%E6%B4%9B%E5%BF%85%E8%BE%BE%E6%B3%95%E5%88%99'
                        ),
                        MessageTemplateAction(
                            label='點我看答案',
                            text='ch9-3-2'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0
    if event.message.text == "ch9-3-1":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090003-1-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090003-1-1.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "ch9-3-2":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090003-2-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090003-2-1.png')
        replay_message(event,Image_Message)
        return 0

    #習題第九章第四題------------------------------------------------------------------------------------------------
    if event.message.text == "method1":
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090004-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090004-1.png')
        Image_Message2 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090004-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090004-3.png')
        replay_message(event,Image_Message1)
        push_message(event,Image_Message2)
        return 0
    if event.message.text == "method2":
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090004-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090004-2.png')
        Image_Message2 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090004-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090004-3.png')
        replay_message(event,Image_Message1)
        push_message(event,Image_Message2)
        return 0
 
    #習題第九章第五題------------------------------------------------------------------------------------------------
    if event.message.text == "converge":
        message = TextSendMessage(text="沒錯！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090005.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='想要了解更多級數審斂法？',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我了解更多',
                            text='各種級數審斂法'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "diverge":
        message = TextSendMessage(text="再想想喔！先來了解一下各種級數審斂法：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00090005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00090005.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='想好答案了嗎？',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='點我看解答',
                            text='ch9-5解題過程'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "ch9-5解題過程":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090005.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "各種級數審斂法":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00090005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00090005.jpg')
        replay_message(event,Image_Message)
        return 0

    #習題第九章第六題------------------------------------------------------------------------------------------------
    if event.message.text == "solution":
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你會遇到的問題：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='Answer',
                            text='Answer'
                        ),
                        MessageTemplateAction(
                            label='Binomial Series',
                            text='Binomial Series'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0
    if event.message.text == "Answer":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090006-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090006-1.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "Binomial Series":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090006-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00090006-2.png')
        replay_message(event,Image_Message)
        return 0    
    if event.message.text == "maclaurin series":
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你會遇到的問題：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        URITemplateAction(
                            label='定理',
                            uri='https://zh.wikipedia.org/zh-tw/%E6%B3%B0%E5%8B%92%E7%BA%A7%E6%95%B0'
                        ),
                        URITemplateAction(
                            label='maclaurin series教學影片',
                            uri='https://www.youtube.com/watch?v=kqD10INIkSo'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
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
    
    #習題第十章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "這題所需要用到的定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00100002.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00100002.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "解題的過程":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100002.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100002.jpg')
        replay_message(event,Image_Message)
        return 0

    #習題第十章第三題------------------------------------------------------------------------------------------------
    if event.message.text == "利用弧長公式":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100003-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100003-1.png')
        push_message(event,Image_Message)
        return 0
    if event.message.text == "弧長定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100003-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100003-2.png')
        Imagemap_Message = ImagemapSendMessage(
            base_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm.png?',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=450, width=1000),
            actions=[
                MessageImagemapAction(
                    text='利用弧長公式',
                    area=ImagemapArea(
                        x=500, y=0, width=1000, height=450
                    )
                )
            ]
        )
        replay_message(event,Image_Message)
        push_message(event,Imagemap_Message)
        return 0
    #習題第十章第四題------------------------------------------------------------------------------------------------
    if event.message.text == "詳解":
        message = TextSendMessage(text="記得自己要再寫一遍喔~~")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-1.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "弧長公式定理":
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='了解定理對於解題有幫助喔!!：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='定理',
                            text='ch10定理'
                        ),
                        MessageTemplateAction(
                            label='Remark1',
                            text='Remark1'
                        ),
                        MessageTemplateAction(
                            label='Remark2',
                            text='Remark2'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0

    if event.message.text == "ch10定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-2.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "Remark1":
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-3.png')
        message = TextSendMessage(text="證明：")
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-5.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-5.png')
        replay_message(event,Image_Message1)
        push_message(event,message)
        push_message(event,Image_Message2)
        return 0 
    if event.message.text == "Remark2":
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-4.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-4.png')
        message = TextSendMessage(text="證明：")
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-6.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100004-6.png')
        replay_message(event,Image_Message1)
        push_message(event,message)
        push_message(event,Image_Message2)
        return 0 

    #習題第十章第五題------------------------------------------------------------------------------------------------
    if event.message.text == "ch10-5解題過程":
        message = TextSendMessage(text="好的！來看一下解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100005.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "ch10-5相關定理":
        message = TextSendMessage(text="好的！來看一下此題相關定理：")
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0010000501.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0010000501.jpg')
        Image_Message2 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0010000502.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm0010000502.jpg')
        replay_message(event,message)
        push_message(event,Image_Message1)
        push_message(event,Image_Message2)
        return 0
    #習題第十章第六題------------------------------------------------------------------------------------------------
    if event.message.text == "點我看圖形!!":
        message = TextSendMessage(text="試著寫出參數範圍")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100006-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100006-2.png')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0
    if event.message.text == "表面積公式":
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='了解公式：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='revolution about x-axis',
                            text='revolution about x-axis'
                        ),
                        MessageTemplateAction(
                            label='revolution about y-axis',
                            text='revolution about y-axis'
                        ),
                        MessageTemplateAction(
                            label='我想看答案',
                            text='我想看答案'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0
    if event.message.text == "revolution about x-axis":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100006-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100006-3.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "revolution about y-axis":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100006-4.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100006-4.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "我想看答案":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100006-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00100006-1.png')
        replay_message(event,Image_Message)
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
    
    #習題第十一章第二題------------------------------------------------------------------------------------------------
    if event.message.text == "求f一階偏導數為零的解":
        message = TextSendMessage(text="正確~來看一下完整的解題步驟：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110002.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110002.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "直接求f的二階偏導數":
        message = TextSendMessage(text="在要用二階導數極值判別法前，我們要先透過一階導數找出f的臨界值喔！")
        replay_message(event,message)
        return 0
    #習題第十一章第三題------------------------------------------------------------------------------------------------
    if event.message.text == "第一小題":
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你會遇到的問題：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='定理',
                            text='偏微分'
                        ),
                        MessageTemplateAction(
                            label='點我看答案',
                            text='ch11-3-1'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0
    if event.message.text == "第二小題":
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='你會遇到的問題：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='定理',
                            text='偏微分'
                        ),
                        MessageTemplateAction(
                            label='點我看答案',
                            text='ch11-3-2'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0
    if event.message.text == "ch11-3-1":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110003-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110003-1.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "ch11-3-2":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110003-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110003-2.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "偏微分":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110003-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110003-3.png')
        replay_message(event,Image_Message)
        return 0 
    #習題第十一章第四題------------------------------------------------------------------------------------------------
    if event.message.text == "Proof":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110004-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110004-1.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "Theorem":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110004-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110004-2.png')
        replay_message(event,Image_Message)
        return 0

    #習題第十一章第五題------------------------------------------------------------------------------------------------
    if event.message.text == "ch11-5方法一":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0011000501.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0011000501.jpg')
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='學習更多',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='方法一運用定理',
                            text='ch11-5-1定理'
                        )
                    ]
                )
            )
        replay_message(event,Image_Message)
        push_message(event,Buttons_Template)
        return 0

    if event.message.text == "ch11-5方法二":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0011000502.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans0011000502.jpg')
        replay_message(event,Image_Message)
        return 0

    if event.message.text == "ch11-5-1定理":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00110005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm00110005.jpg')
        replay_message(event,Image_Message)
        return 0
            
    #習題第十一章第六題------------------------------------------------------------------------------------------------
    if event.message.text == "點我看證明":
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='了解更多：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/13.jpg',
                    actions=[
                        URITemplateAction(
                            label='證明',
                            uri='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110006-1.png'
                        ),
                        MessageTemplateAction(
                            label='類似題型練習',
                            text='類似題型練習'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0
    if event.message.text == "類似題型練習":
        Image_Message1 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110006-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110006-2.png')
        Image_Message2 = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110006-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00110006-3.png')
        replay_message(event,Image_Message1)
        push_message(event,Image_Message2)
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
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-4.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-4.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "ch12-3":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120002-3.png')
        replay_message(event,Image_Message)
        return 0
    #習題第十二章第三題------------------------------------------------------------------------------------------------ 
    if event.message.text == "參數變更極坐標":
        message = TextSendMessage(text="錯誤!!極座標只有兩個參數!!所以需先寫出參數範圍再化簡成兩個參數，就可以將參數更改為極座標!!!")
        Imagemap_Message = ImagemapSendMessage(
            base_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/thm.png?',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=85, width=298),
            actions=[
                MessageImagemapAction(
                    text='變換極坐標定理',
                    area=ImagemapArea(
                        x=0, y=0, width=298, height=85
                    )
                )
            ]
        )
        replay_message(event,message)
        push_message(event,Imagemap_Message)
        return 0
    if event.message.text == "寫出參數範圍": 
        message = TextSendMessage(text="正確!!")
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='我們將解題步驟分為兩個：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/12.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='步驟一',
                            text='參數範圍'
                        ),
                        MessageTemplateAction(
                            label='步驟二',
                            text='參數轉為極座標'
                        )
                    ]
                )
            )
        replay_message(event,message)
        push_message(event,Buttons_Template)
        return 0 

    if event.message.text == "步驟一":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120003-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120003-1.png')
        replay_message(event,Image_Message)
        return 0 
    if event.message.text == "步驟二":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120003-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120003-2.png')   
        replay_message(event,Image_Message)
        return 0 
 
    #習題第十二章第四題------------------------------------------------------------------------------------------------ 
    if event.message.text == "(a)小題": 
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='解題時可能會遇到的問題：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/12.jpg',
                    actions=[
                        URITemplateAction(
                            label='change of variables',
                            uri='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120004-1.png'
                        ),
                        MessageTemplateAction(
                            label='hint',
                            text='hint'
                        ),
                        MessageTemplateAction(
                            label='(a)答案',
                            text='(a)答案'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0 
    if event.message.text == "hint":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120004-4.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120004-4.png')
        replay_message(event,Image_Message)
        return 0 
    if event.message.text == "(a)答案":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120004-2.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120004-2.png')   
        replay_message(event,Image_Message)
        return 0 
    if event.message.text == "(b)小題": 
        Buttons_Template = TemplateSendMessage(
                alt_text='Buttons Template',
                template=ButtonsTemplate(
                    title=' ',
                    text='我們將解題步驟分為兩個：',
                    thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/12.jpg',
                    actions=[
                        URITemplateAction(
                            label='change of variables',
                            uri='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120004-1.png'
                        ),
                        URITemplateAction(
                            label='Jacobian',
                            uri='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120004-5.png'
                        ),
                        MessageTemplateAction(
                            label='(b)答案',
                            text='(b)答案'
                        )
                    ]
                )
            )
        replay_message(event,Buttons_Template)
        return 0
    if event.message.text == "(b)答案":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120004-3.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120004-3.png')   
        replay_message(event,Image_Message)
        return 0 
    #習題第十二章第五題------------------------------------------------------------------------------------------------
    if event.message.text == "(x,y,z)":
        message = TextSendMessage(text="對(r,theta,z)做更好喔!")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120005.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    if event.message.text == "(r,theta,z)":
        message = TextSendMessage(text="沒錯!來看一下完整的解題過程：")
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120005.jpg',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120005.jpg')
        replay_message(event,message)
        push_message(event,Image_Message)
        return 0

    #習題第十二章第六題------------------------------------------------------------------------------------------------ 
    if event.message.text == "解題步驟":
        Carousel_Template = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/12.jpg',
                        title='第一步',
                        text=' ',
                        actions=[
                            URITemplateAction(
                                label='質心相對於x軸',
                                uri='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120006-2.png'
                            ),
                            URITemplateAction(
                                label='質心相對於y軸',
                                uri='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120006-3.png'
                            ),
                            URITemplateAction(
                                label='質心相對於z軸',
                                uri='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120006-4.png'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/12.jpg',
                        title='第二步',
                        text=' ',
                        actions=[
                            MessageTemplateAction(
                                label='質量',
                                text='質量'
                            ),
                            MessageTemplateAction(
                                label='the center of mass',
                                text='the center of mass'
                            ),
                            MessageTemplateAction(
                                label='為甚麼"相對於y軸的質心"為0',
                                text='為甚麼"相對於y軸的質心"為0'
                            )
                        ]
                    )
                ]
            )
        )
        replay_message(event,Carousel_Template)
        return 0
    if event.message.text == "質量":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120006-1.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120006-1.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "the center of mass":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120006-5.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120006-5.png')
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "為甚麼相對於y軸的質心為0":
        message = TextSendMessage(text="圖形對稱x軸,所以y的中心部分會落在x軸上，因此等於0!!")
        replay_message(event,Image_Message)
        return 0
    if event.message.text == "點我看公式":
        Image_Message = ImageSendMessage(original_content_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120006-6.png',preview_image_url='https://jylin.myqnapcloud.com/Projects/year201901/wp-content/uploads/2019/10/ans00120006-6.png')
        replay_message(event,Image_Message)
        return 0
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
        sql = """SELECT "value", "Llabel", "Ltext", "Rlabel", "Rtext","lable" FROM public."temp" WHERE "number" LIKE '%""" + event.postback.data + "%'" 
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
            text7 = text7 + str(row[5])

        Image_Message = ImageSendMessage(original_content_url=text2,preview_image_url=text2)
        Confirm_Template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ConfirmTemplate(
                title='這是ConfirmTemplate',
                text=text7,
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