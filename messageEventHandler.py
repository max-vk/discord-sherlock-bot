class MessageEventHandler:

    # Evaluation method which checks for command keywords and executes appropriate modules
    @staticmethod
    async def EvaluateMessage(message):
        if(message.content == "hello Sherlock"):
            await message.channel.send("Hello")
