import random
import asyncio
from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        # Set the token and channel you want the bot to join
        super().__init__(token='AUTH_KEY', prefix='!', initial_channels=['oMeiaUm', 'VictorHugor'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    # Define the !pickme command
    @commands.command(name='pickme')
    async def pickme(self, ctx):
        message = ctx.message.content
        sender = ctx.author.name

        # Check if the command contains a mentioned user
        if "@" in message:
            # Extract the mentioned user from the message
            target_user = message.split('@')[1].strip()
            
            # Special case: if sender or target user is GeorgeLucas95
            if sender == "GeorgeLucas95" or target_user == "GeorgeLucas95":
                pickme_percentage = 1052
            else:
                pickme_percentage = random.randint(0, 100)
                
            await ctx.send(f'@{target_user}, sua porcentagem de pick me é: {pickme_percentage}%')
        else:
            # Special case: if sender is GeorgeLucas95
            if sender == "GeorgeLucas95":
                pickme_percentage = 1052
            else:
                pickme_percentage = random.randint(0, 100)
                
            await ctx.send(f'@{sender}, sua porcentagem de pick me é: {pickme_percentage}%')

# Define a function to start the bot with asyncio.run()
async def main():
    bot = Bot()
    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
