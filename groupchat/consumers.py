import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from users.models import Token

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # print(self.scope)
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        # token = self.scope.get('headers', {}).get(b'authorization', b'').decode('utf-8').split()[1]
        print(self.scope)
        print(self.scope.get('headers', [])[0])
        # print("Token Data",token)
        self.group_name = f"group_{self.group_id}"
        # print(self.group_id, self.group_name)

        # Authenticate the user using the provided auth_token
        await self.authenticate_user()
        
        # Add the user to the group
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        # print(self.scope)
        user = self.scope["user"]

        # Send the message to the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat.message',
                'message': message,
                'username': user.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))
    
    @database_sync_to_async
    def authenticate_user(self):
        try:
            token_key = self.scope['query_string'].decode("utf-8")
            token = Token.objects.get(key=token_key)
            self.user = token.user
        except Token.DoesNotExist:
            self.close()


# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_id = self.scope['url_route']['kwargs']['group_id']
#         self.room_group_name = f'chat_{self.room_name}'

#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']

#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat.message',
#                 'message': message,
#             }
#         )

#     async def chat_message(self, event):
#         message = event['message']

#         await self.send(text_data=json.dumps({
#             'message': message,
#         }))



# consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class GroupChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Authenticate user
#         if self.scope['user'].is_anonymous:
#             await self.close()
#         else:
#             group_name = self.scope['url_route']['kwargs']['group_name']
#             self.group_name = f"group_{group_name}"
            
#             await self.channel_layer.group_add(
#                 self.group_name,
#                 self.channel_name
#             )

#             await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']

#         await self.channel_layer.group_send(
#             self.group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'sender': self.scope['user'].username
#             }
#         )

#     async def chat_message(self, event):
#         message = event['message']
#         sender = event['sender']

#         await self.send(text_data=json.dumps({
#             'message': message,
#             'sender': sender
#         }))

