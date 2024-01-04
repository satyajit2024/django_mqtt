#Topic - Consumer

from channels.consumer import SyncConsumer , AsyncConsumer

class MySyncConsumer(SyncConsumer):
    
	def websocket_connect(self , event):
		print("Connected......",event)
	
	def websocket_receive(self , event):
		print("Received.....",event)
	
	def websocket_disconnect(self,event):
		print("Disconnected.....",event)


class MyAsyncConsumer(AsyncConsumer):
    
	async def websocket_connect(self , event):
		print("Connected......",event)
	
	async def websocket_receive(self , event):
		print("Received.....",event)
	
	async def websocket_disconnect(self,event):
		print("Disconnected.....",event)
