import nextcord
from nextcord.ext import commands
import random


class EightBall(commands.Cog):
    """
    Magic 8 Ball wizardry
    """

    def __init__(self, client):
        self.client = client

    @commands.command(usage="<question>", aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        """
        Make good decisions with a magic 8 ball.
        """
        responses = ["As I see it, yes.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don’t count on it.",
                     "It is certain.",
                     "It is decidedly so.",
                     "Most likely.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Outlook good.",
                     "Reply hazy, try again.",
                     "Signs point to yes.",
                     "Very doubtful.",
                     "Without a doubt."]
        await ctx.send(f"Question: {question.capitalize()}\nAnswer: {random.choice(responses)}")


def setup(client):
    client.add_cog(EightBall(client))
