import discord
from discord.ext import commands
from chatterbot import ChatBot  # pip install chatterbot==1.0.4
from chatterbot.trainers import ChatterBotCorpusTrainer

# Prepare and train the chatbot
chatbot = ChatBot("Eve")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("eve-bot/cogs/miscellaneous.yml", "eve-bot/cogs/ai.yml")


class Chatbot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["chat", "chatbot", "ask"])
    async def q(self, ctx, *, question):
        response = chatbot.get_response(question)
        print(
            f"Response: {response} \nResponse Confidence: {response.confidence}")
        if response.confidence >= 0.60:
            await ctx.send(response)
        else:
            await ctx.send("I'm sorry, I don't understand the question.")


def setup(client):
    client.add_cog(Chatbot(client))
