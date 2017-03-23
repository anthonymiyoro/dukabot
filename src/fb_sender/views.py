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
@csrf_exempt
def verify(request, self=None):
	if self.request.GET['hub.verify_token'] == '555777':
		    return HttpResponse(self.request.GET['hub.challenge'])
	else:
            return HttpResponse('Error, invalid token')

@csrf_exempt
def webhook(request):

    output = json.loads(request.body)
    print output
    try:
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                recipient_id = x['sender']['id']
                recipient = messages.Recipient(recipient_id=recipient_id)
                if x.get('message'):

                    if x['message'].get('text'):
                        message_text = x['message']['text']
                        if message_text == 'hi':
                            message = messages.Message(attachment=attachment)
                            # bot.send_text_message(recipient_id, message)
                            request = messages.MessageRequest(recipient, message)
                            messenger.send(request)
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            pass
                            # bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                elif x.get('postback').get('payload')=='USER_DEFINED_PAYLOAD':
                    message = messages.Message(text='Hello World')
                    request = messages.MessageRequest(recipient, message)
                    messenger.send(request)
                    pass
    except Exception, e:
        print e.message
    return HttpResponse()


# class fb_senderView(generic.View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return generic.View.dispatch(self, request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         if self.request.GET['hub.verify_token'] == '555777':
#             return HttpResponse(self.request.GET['hub.challenge'])
#         else:
#             return HttpResponse('Error, invalid token')
#
#         def post(self, request, *args, **kwargs):
#             #Convert incoming text into a python dictionary
#             incoming_message = json.loads(self.request.body.decode('utf-8'))
#             #Goes through multiple messages if received at once
#             for entry in incoming_message['entry']:
#                 for message in entry['message']:
#                 if 'message' in message:
#                     pprint(message)
#             return HttpResponse()