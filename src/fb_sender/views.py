# from django.core.serializers import json
# from django.shortcuts import render
# from django.template.context_processors import csrf
# from django.template.defaultfilters import pprint
# from django.utils.decorators import method_decorator
# from django.views import generic
# from django.utils.datetime_safe import time
# from django.http.response import HttpResponse
# from datetime import datetime
#  #from fb_sender.tests import buy

# # Create your views here.
# from django.views.decorators.csrf import csrf_exempt
# from messengerbot import MessengerClient, messages, attachments, templates, elements, quick_replies
# import json
# import requests
# import uuid


# from messengerbot.elements import Element

# nowtime = str(datetime.now())

# def buy(sender_msisdn, recipient_msisdn):
#     url = "https://vitelco-demo.jumo.world/transactions/"
#     headers={"Authorization":"8e974ff7fd1428fc8ba5ac912002ff8c", "DATE":nowtime, "Content-Type":"application/json", "X-CorrelationID":str(uuid.uuid4())}

#     payload = {
#         "amount": "2000",
#         "currency": "KSH",
#         "type": "merchantPayment",
#         "requestDate": nowtime,
#         "requestingOrganisationTransactionReference": "MWCAPIWorkshop001",
#         "debitParty": [
#         {
#         "key": "msisdn",
#         "value": sender_msisdn
#         }
#         ],
#         "creditParty": [
#         {
#         "key": "msisdn",
#         "value": recipient_msisdn
#         }
#     ]
# }

#     response = requests.post(url=url, headers=headers, data=json.dumps(payload))
#     return response

# ACCESS_TOKEN = "EAADWobK94kQBAOzjAWQc1UtFiy2vqZA1J3hRvLgp9auwM3EEhBC9l8F3YC14hK8R8sZCSdYAOTxRkSn52A4LlYoYZAZBF1bAygqb9ZCgpTAZC0EfK9Uxpo9K4GjKF0tE8t39Lds2zq7R8ypqfvLhSBHNVwp0ZCWgyKgZCsLMZAgHCTgZDZD"
# messenger = MessengerClient(access_token=ACCESS_TOKEN)

# # Send button template
# web_button = elements.WebUrlButton(
#     title='Show website',
#     url='https://petersapparel.parseapp.com'
# )
# postback_button = elements.PostbackButton(
#     title='Start chatting',
#     payload='USER_DEFINED_PAYLOAD'
# )
# template = templates.ButtonTemplate(
#     text='What do you want to do next?',
#     buttons=[
#         web_button, postback_button
#     ]
# )

# attachment = attachments.TemplateAttachment(template=template)


# # # Send button template 2
# # web_button2 = elements.WebUrlButton(
# #   title="I'm a buyer",
# #   url='https://petersapparel.parseapp.com'
# # )
# # postback_button2 = elements.PostbackButton(
# #   title='I have something to sell',
# #   payload='USER_DEFINED_PAYLOAD'
# # )

# # template2 = templates.ButtonTemplate(
# #   text='Which are you?',
# #   buttons=[
# #       web_button2, postback_button2
# #   ]
# # )
# # # attachment2 = attachments.TemplateAttachment(template=template2)


# @csrf_exempt
# def webhook(request):
#     if request.GET:
#         if request.GET['hub.verify_token'] == '555777':
#             return HttpResponse(request.GET['hub.challenge'])
#         else:
#             return HttpResponse('Error, invalid token')
#     try:
#         output = json.loads(request.body.decode('utf-8'))
#         print (output)
#         try:
#             for event in output['entry']:
#                 messaging = event['messaging']
#                 for x in messaging:
#                     recipient_id = x['sender']['id']
#                     recipient = messages.Recipient(recipient_id=recipient_id)
#                     if x.get('message'):
#                         # collect text
#                         if x['message'].get('text'):
#                             if x['message'].get('text').lower() == 'hello' or x['message'].get('text').lower() == 'hi':
#                                 message_text = x['message']['text']
#                                 # ask if they want to buy something
#                                 # message = messages.Message(text='Hello, do you wish to buy or sell a product?')
#                                 # request = messages.MessageRequest(recipient, message)
#                                 # messenger.send(request)
#                                 postback_button = elements.PostbackButton(
#                                     title='Buy',
#                                     payload='BUY'
#                                 )
#                                 postback_button1 = elements.PostbackButton(
#                                     title='Sell',
#                                     payload='SELL'
#                                 )
#                                 template = templates.ButtonTemplate(
#                                     text='Hello, do you wish to buy or sell a product?',
#                                     buttons=[
#                                         postback_button, postback_button1
#                                     ]
#                                 )
#                                 attachment = attachments.TemplateAttachment(template=template)
#                                 message = messages.Message(attachment=attachment)
#                                 request = messages.MessageRequest(recipient, message)
#                                 messenger.send(request)
#                             # elif x['message'].get('text').lower() == 'Page 1':
#                             else:
#                                 my_elements = []
#                                 postback_button2 = elements.PostbackButton(
#                                     title="Buy",
#                                     payload='BUY_1'
#                                 )
#                                 # my_elements.append(Element(title="prod title", subtitle="prod substitle",
#                                 #                           image_url="https://cdn.shopify.com/s/files/1/0739/4315/products/laguna_profile_mayfair_fullres_4815ea8f-83a8-4e29-841f-c099841987de.png?v=1480399889",
#                                 #                           buttons=[postback_button2]))
#                                 # my_elements.append(Element(title="prod title", subtitle="prod substitle",
#                                 #                           image_url="https://cdn.shopify.com/s/files/1/0739/4315/products/laguna_profile_mayfair_fullres_4815ea8f-83a8-4e29-841f-c099841987de.png?v=1480399889",
#                                 #                           buttons=[postback_button2]))
#                                 # my_elements.append(Element(title="prod title", subtitle="prod substitle",
#                                 #                           image_url="https://cdn.shopify.com/s/files/1/0739/4315/products/laguna_profile_mayfair_fullres_4815ea8f-83a8-4e29-841f-c099841987de.png?v=1480399889",
#                                 #                           buttons=[postback_button2]))
#                                 # my_elements.append(Element(title="prod title", subtitle="prod substitle",
#                                 #                           image_url="https://cdn.shopify.com/s/files/1/0739/4315/products/laguna_profile_mayfair_fullres_4815ea8f-83a8-4e29-841f-c099841987de.png?v=1480399889",
#                                 #                           buttons=[postback_button2]))
#                                 my_elements.append(Element(title="HP Pavilion 420", subtitle="KES 24000",
#                                                 image_url="http://www.browsingphones.com/wp-content/uploads/2015/11/HP-Laptop-Price-In-Kenya-Specs-Jumia-300x225.jpg",
#                                                 buttons=[postback_button2]))
#                                 my_elements.append(Element(title="Lenovo workbook 14 inch", subtitle="KES 30000",
#                                                 image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThIxirSJSLuv9qpZCeyhp30itUZ-IrndcTyloWPSHEij2e3zjo2Q",
#                                                 buttons=[postback_button2]))
#                                 my_elements.append(Element(title="HP Workbook 8200", subtitle="KED 27000",
#                                                 image_url="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQaz0E0LRQEwsNq1H24VKTn4Idxy0nnFDvHcyIuOzH9cQFJaG5E",
#                                                 buttons=[postback_button2]))
#                                 my_elements.append(Element(title="HP Pavilion 328", subtitle="KES 45000",
#                                                 image_url="https://i5.walmartimages.com/dfw/4ff9c6c9-2ac9/k2-_ed8b8f8d-e696-4a96-8ce9-d78246f10ed1.v1.jpg",
#                                                 buttons=[postback_button2]))
#                                 template = templates.GenericTemplate(elements=my_elements)
#                                 attachment = attachments.TemplateAttachment(template=template)
#                                 message = messages.Message(attachment=attachment)
#                                 request = messages.MessageRequest(recipient, message)
#                                 messenger.send(request)

#                         if x['message'].get('attachments'):
#                             for att in x['message'].get('attachments'):
#                                 pass
#                     elif x.get('postback').get('payload') == 'BUY':
#                         quick_reply = quick_replies.QuickReplyItem(
#                             content_type='text',
#                             title='LaptopMart',
#                             payload='page_1'
#                         )
#                         quick_reply2 = quick_replies.QuickReplyItem(
#                             content_type='text',
#                             title='BikeMart',
#                             payload='page_2'
#                         )
#                         replies = quick_replies.QuickReplies(quick_replies=[quick_reply, quick_reply2])
#                         message = messages.Message(text='Where would you like to shop?', quick_replies=replies)
#                         request = messages.MessageRequest(recipient, message)
#                         messenger.send(request)
#                         pass
#                     elif x.get('postback').get('payload') == 'USER_DEFINED_PAYLOAD1':
#                         message = messages.Message(text='New Message')
#                         request = messages.MessageRequest(recipient, message)
#                         messenger.send(request)
#                         pass
#                     elif x.get('postback').get('payload') == 'BUY_1':
#                         my_elements = []
#                         id = str(uuid.uuid4())
#                         buy_response =  buy('+254720000801', '+254720000800', id)
#                         if buy_response.status_code == 202:
#                             message = messages.Message(text='Transaction complete')
#                             request = messages.MessageRequest(recipient, message)
#                             messenger.send(request)
#                             template = templates.GenericTemplate(elements=my_elements)
#                             attachment = attachments.TemplateAttachment(template=template)
#                             message = messages.Message(attachment=attachment)
#                             request = messages.MessageRequest(recipient, message)
#                             messenger.send(request)
#                     else:
#                         print buy_response.status_code
#                         buy_response =  buy('+254720000802', '+254720000800', id)
#                         quick_reply3 = quick_replies.QuickReplyItem(
#                         content_type='text',
#                         title=buy_response.status_code,
#                         payload='page_2'
#                     )

#         except Exception, e:
#             print e.message
#     except Exception, e:
#         print e
#     return HttpResponse()


from django.core.serializers import json
from django.shortcuts import render
from django.template.context_processors import csrf
from django.template.defaultfilters import pprint
from django.utils.decorators import method_decorator
from django.views import generic
from django.utils.datetime_safe import time
from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from messengerbot import MessengerClient, messages, attachments, templates, elements, quick_replies
import json
import requests
import uuid


from messengerbot.elements import Element

nowtime = str(datetime.now())

def buy(sender_msisdn, recipient_msisdn):
    url = "https://vitelco-demo.jumo.world/transactions/"
    headers={"Authorization":"8e974ff7fd1428fc8ba5ac912002ff8c", "DATE":nowtime, "Content-Type":"application/json", "X-CorrelationID":"hhsgyehjvjsdjg12344"}

    payload = {
        "amount": "2000",
        "currency": "KSH",
        "type": "merchantPayment",
        "requestDate": nowtime,
        "requestingOrganisationTransactionReference": "MWCAPIWorkshop001",
        "debitParty": [
        {
        "key": "msisdn",
        "value": sender_msisdn
        }
        ],
        "creditParty": [
        {
        "key": "msisdn",
        "value": recipient_msisdn
        }
    ]
}

    response = requests.post(url=url, headers=headers, data=json.dumps(payload))
    return response

ACCESS_TOKEN = "EAADWobK94kQBAOzjAWQc1UtFiy2vqZA1J3hRvLgp9auwM3EEhBC9l8F3YC14hK8R8sZCSdYAOTxRkSn52A4LlYoYZAZBF1bAygqb9ZCgpTAZC0EfK9Uxpo9K4GjKF0tE8t39Lds2zq7R8ypqfvLhSBHNVwp0ZCWgyKgZCsLMZAgHCTgZDZD"
messenger = MessengerClient(access_token=ACCESS_TOKEN)

# Send button template
web_button = elements.WebUrlButton(
    title='Show website',
    url='https://petersapparel.parseapp.com'
)
postback_button = elements.PostbackButton(
    title='Start chatting',
    payload='USER_DEFINED_PAYLOAD'
)
template = templates.ButtonTemplate(
    text='What do you want to do next?',
    buttons=[
        web_button, postback_button
    ]
)

attachment = attachments.TemplateAttachment(template=template)


# # Send button template 2
# web_button2 = elements.WebUrlButton(
#   title="I'm a buyer",
#   url='https://petersapparel.parseapp.com'
# )
# postback_button2 = elements.PostbackButton(
#   title='I have something to sell',
#   payload='USER_DEFINED_PAYLOAD'
# )

# template2 = templates.ButtonTemplate(
#   text='Which are you?',
#   buttons=[
#       web_button2, postback_button2
#   ]
# )
# # attachment2 = attachments.TemplateAttachment(template=template2)


@csrf_exempt
def webhook(request):
    if request.GET:
        if request.GET['hub.verify_token'] == '555777':
            return HttpResponse(request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
    try:
        output = json.loads(request.body.decode('utf-8'))
        print (output)
        try:
            for event in output['entry']:
                messaging = event['messaging']
                for x in messaging:
                    recipient_id = x['sender']['id']
                    recipient = messages.Recipient(recipient_id=recipient_id)
                    if x.get('message'):
                        # collect text
                        if x['message'].get('text'):
                            if x['message'].get('text').lower() == 'hello' or x['message'].get('text').lower() == 'hi':
                                message_text = x['message']['text']
                                # ask if they want to buy something
                                # message = messages.Message(text='Hello, do you wish to buy or sell a product?')
                                # request = messages.MessageRequest(recipient, message)
                                # messenger.send(request)
                                postback_button = elements.PostbackButton(
                                    title='Buy',
                                    payload='BUY'
                                )
                                postback_button1 = elements.PostbackButton(
                                    title='Sell',
                                    payload='SELL'
                                )
                                template = templates.ButtonTemplate(
                                    text='Hello, do you wish to buy or sell a product?',
                                    buttons=[
                                        postback_button, postback_button1
                                    ]
                                )
                                attachment = attachments.TemplateAttachment(template=template)
                                message = messages.Message(attachment=attachment)
                                request = messages.MessageRequest(recipient, message)
                                messenger.send(request)
                            # elif x['message'].get('text').lower() == 'Page 1':
                            else:
                                my_elements = []
                                postback_button2 = elements.PostbackButton(
                                    title="Buy",
                                    payload='BUY_1'
                                )
                                # my_elements.append(Element(title="prod title", subtitle="prod substitle",
                                #                           image_url="https://cdn.shopify.com/s/files/1/0739/4315/products/laguna_profile_mayfair_fullres_4815ea8f-83a8-4e29-841f-c099841987de.png?v=1480399889",
                                #                           buttons=[postback_button2]))
                                # my_elements.append(Element(title="prod title", subtitle="prod substitle",
                                #                           image_url="https://cdn.shopify.com/s/files/1/0739/4315/products/laguna_profile_mayfair_fullres_4815ea8f-83a8-4e29-841f-c099841987de.png?v=1480399889",
                                #                           buttons=[postback_button2]))
                                # my_elements.append(Element(title="prod title", subtitle="prod substitle",
                                #                           image_url="https://cdn.shopify.com/s/files/1/0739/4315/products/laguna_profile_mayfair_fullres_4815ea8f-83a8-4e29-841f-c099841987de.png?v=1480399889",
                                #                           buttons=[postback_button2]))
                                # my_elements.append(Element(title="prod title", subtitle="prod substitle",
                                #                           image_url="https://cdn.shopify.com/s/files/1/0739/4315/products/laguna_profile_mayfair_fullres_4815ea8f-83a8-4e29-841f-c099841987de.png?v=1480399889",
                                #                           buttons=[postback_button2]))
                                my_elements.append(Element(title="HP Pavilion 420", subtitle="KES 24000",
                                                image_url="http://www.browsingphones.com/wp-content/uploads/2015/11/HP-Laptop-Price-In-Kenya-Specs-Jumia-300x225.jpg",
                                                buttons=[postback_button2]))
                                my_elements.append(Element(title="Lenovo workbook 14 inch", subtitle="KES 30000",
                                                image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThIxirSJSLuv9qpZCeyhp30itUZ-IrndcTyloWPSHEij2e3zjo2Q",
                                                buttons=[postback_button2]))
                                my_elements.append(Element(title="HP Workbook 8200", subtitle="KED 27000",
                                                image_url="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQaz0E0LRQEwsNq1H24VKTn4Idxy0nnFDvHcyIuOzH9cQFJaG5E",
                                                buttons=[postback_button2]))
                                my_elements.append(Element(title="HP Pavilion 328", subtitle="KES 45000",
                                                image_url="https://i5.walmartimages.com/dfw/4ff9c6c9-2ac9/k2-_ed8b8f8d-e696-4a96-8ce9-d78246f10ed1.v1.jpg",
                                                buttons=[postback_button2]))
                                template = templates.GenericTemplate(elements=my_elements)
                                attachment = attachments.TemplateAttachment(template=template)
                                message = messages.Message(attachment=attachment)
                                request = messages.MessageRequest(recipient, message)
                                messenger.send(request)

                        if x['message'].get('attachments'):
                            for att in x['message'].get('attachments'):
                                pass
                    elif x.get('postback').get('payload') == 'BUY':
                        quick_reply = quick_replies.QuickReplyItem(
                            content_type='text',
                            title='LaptopMart',
                            payload='page_1'
                        )
                        quick_reply2 = quick_replies.QuickReplyItem(
                            content_type='text',
                            title='BikeMart',
                            payload='page_2'
                        )
                        replies = quick_replies.QuickReplies(quick_replies=[quick_reply, quick_reply2])
                        message = messages.Message(text='Where would you like to shop?', quick_replies=replies)
                        request = messages.MessageRequest(recipient, message)
                        messenger.send(request)
                        pass
                    elif x.get('postback').get('payload') == 'USER_DEFINED_PAYLOAD1':
                        message = messages.Message(text='New Message')
                        request = messages.MessageRequest(recipient, message)
                        messenger.send(request)
                        pass
                    elif x.get('postback').get('payload') == 'BUY_1':
                        my_elements = []
                        id = str(uuid.uuid4())
                        buy_response =  buy('+254720000802', '+254720000800', id)
                        if buy_response.status_code == 202:
                            message = messages.Message(text='Transaction complete')
                            request = messages.MessageRequest(recipient, message)
                            messenger.send(request)
                            template = templates.GenericTemplate(elements=my_elements)
                            attachment = attachments.TemplateAttachment(template=template)
                            message = messages.Message(attachment=attachment)
                            request = messages.MessageRequest(recipient, message)
                            messenger.send(request)
                    else:
                        print buy_response.status_code
                        buy_response =  buy('+254720000802', '+254720000800', id)
                        quick_reply3 = quick_replies.QuickReplyItem(
                        content_type='text',
                        title=buy_response.status_code,
                        payload='page_2'
                    )

        except Exception, e:
            print e.message
    except Exception, e:
        print e
    return HttpResponse()