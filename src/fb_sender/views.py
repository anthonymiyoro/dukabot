from django.core.serializers import json
from django.shortcuts import render
from django.template.context_processors import csrf
from django.template.defaultfilters import pprint
from django.utils.decorators import method_decorator
from django.views import generic
from django.http.response import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from messengerbot import MessengerClient, messages, attachments, templates, elements
import json

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
                            message_text = x['message']['text']
                            # ask if they want to buy something
                            message = messages.Message(text='Hello, do you wish to buy or sell a product?')
                            request = messages.MessageRequest(recipient, message)
                            messenger.send(request)
                            postback_button = elements.PostbackButton(
                                title='Start chatting',
                                payload='USER_DEFINED_PAYLOAD'
                            )
                            postback_button1 = elements.PostbackButton(
                                title='Start chatting3',
                                payload='USER_DEFINED_PAYLOAD1'
                            )
                            template = templates.ButtonTemplate(
                                text='What do you want to do next?',
                                buttons=[
                                    postback_button, postback_button1
                                ]
                            )
                            attachment = attachments.TemplateAttachment(template=template)
                            message = messages.Message(attachment=attachment)
                            request = messages.MessageRequest(recipient, message)
                            messenger.send(request)
                        if x['message'].get('attachments'):
                            for att in x['message'].get('attachments'):
                                pass
                    elif x.get('postback').get('payload') == 'USER_DEFINED_PAYLOAD':
                        message = messages.Message(text='Hello World')
                        request = messages.MessageRequest(recipient, message)
                        messenger.send(request)
                        pass
                    elif x.get('postback').get('payload') == 'USER_DEFINED_PAYLOAD1':
                        message = messages.Message(text='New Message')
                        request = messages.MessageRequest(recipient, message)
                        messenger.send(request)
                        pass

        except Exception, e:
            print e.message
    except Exception, e:
        print e
    return HttpResponse()