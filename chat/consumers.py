# # myapp/consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from django.contrib.auth.models import User
# from .models import Message
# from django.db.models import Q
# from asgiref.sync import sync_to_async


# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         print(self.scope['user'])
#         if self.scope['user'].is_anonymous:
#             await self.close()
#         else:
#             await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     # async def receive(self, text_data):
#     #     data = json.loads(text_data)
#     #     message = data.get('message')
#     #     recipient_username = data.get('recipient')

#     #     if message and recipient_username:
#     #         sender = self.scope['user']
#     #         recipient = await self.get_user(recipient_username)

#     #         if recipient:
#     #             await self.save_message(sender, recipient, message)
#     #             await self.send_chat_message(sender.username, message)
#     async def receive(self, text_data):
#         print(text_data)
#         data = json.loads(text_data)
#         command = data.get('command')

#         # if command == 'fetch_messages':
#         #     await self.fetch_messages(data['sender'], data['recipient'])
#         # else:
#         message = data.get('message')
#         recipient_username = data.get('recipient')

#         if message and recipient_username:
#             sender = self.scope['user']
#             recipient = await self.get_user(recipient_username)

#             if recipient:
#                 await self.save_message(sender, recipient, message)
#                 await self.send_chat_message(sender.username, message)

#     @sync_to_async
#     def get_user(self, username):
#         try:
#             return User.objects.get(username=username)
#         except User.DoesNotExist:
#             return None

#     @sync_to_async
#     def save_message(self, sender, recipient, message):
#         Message.objects.create(sender=sender, recipient=recipient, content=message)

#     async def send_chat_message(self, sender_username, message):
#         await self.send(text_data=json.dumps({
#             'type': 'chat_message',
#             'message': message,
#             'sender': sender_username,
#         }))
    
#     # @sync_to_async
#     # def get_messages(self, sender, recipient):
#     #     try:
#     #         print("-------------------", sender, recipient)
#     #         return Message.objects.filter(
#     #                 (Q(sender_id=sender.pk) & Q(recipient_id=recipient.pk)) |
#     #                 (Q(sender_id=recipient.pk) & Q(recipient_id=sender.pk))
#     #             )
#     #     except Message.DoesNotExist:
#     #         return None
    
#     # async def fetch_messages(self, sender_username, recipient_username):
#     #     print(sender_username, recipient_username)
#     #     # messages = await self.get_messages(sender_username, recipient_username)
#     #     # print("new mes-----------",messages)
#     #     # sender = User.objects.get(username=sender_username)
#     #     # print(sender)
#     #     # recipient = User.objects.get(username=recipient_username)
#     #     # print(sender, recipient)
#     #     sender = await self.get_user(sender_username)
#     #     recipient = await self.get_user(recipient_username)
#     #     print(sender, recipient)
#     #     messages = await self.get_messages(sender, recipient)
#     #     print(messages)
#     #     # messages = Message.objects.filter(
#     #     #     (Q(sender=sender) & Q(recipient=recipient)) |
#     #     #     (Q(sender=recipient) & Q(recipient=sender))
#     #     # )  # Limit to 50 latest messages
#     #     # print(messages)
#     #     content = {
#     #         'command': 'fetch_messages',
#     #         'messages': messages
#     #     }
#     #     print(content)
#     #     await self.send(text_data=json.dumps(content))

#     # @database_sync_to_async
#     # def get_messages(self, sender_username, recipient_username):
#     #     sender = User.objects.get(username=sender_username)
#     #     recipient = User.objects.get(username=recipient_username)
#     #     print(sender, recipient)
#     #     messages = Message.objects.filter(
#     #         (Q(sender=sender) & Q(recipient=recipient)) |
#     #         (Q(sender=recipient) & Q(recipient=sender))
#     #     ).order_by('timestamp')[:50]  # Limit to 50 latest messages
#     #     print(messages)
#     #     return messages

#     # @database_sync_to_async
#     # def messages_to_json(self, messages):
#     #     result = []
#     #     for message in messages:
#     #         print(message)
#     #         result.append({
#     #             'sender': message.sender.username,
#     #             'recipient': message.recipient.username,
#     #             'content': message.content,
#     #             'timestamp': str(message.timestamp),
#     #         })
#     #     print(result)
#     #     return result
