import pydle
import random
import asyncio

class TwitchBot(pydle.Client):
    async def on_connect(self):
        # Join the channel
        await self.join('oMeiaUm')
        print('Connected to the channel!')

    async def on_message(self, target, source, message):
        print(f'Received message from {source}: {message}')
        
        if message.startswith('!pickme'):
            if "@" in message:
                target_user = message.split('@')[1].strip()
                pickme_percentage = 1052 if source == "GeorgeLucas95" or target_user == "GeorgeLucas95" else random.randint(0, 100)
                await self.message(target, f'@{target_user}, sua porcentagem de pick me é: {pickme_percentage}%')
            else:
                pickme_percentage = 1052 if source == "GeorgeLucas95" else random.randint(0, 100)
                await self.message(target, f'@{source}, sua porcentagem de pick me é: {pickme_percentage}%')

async def main():
    # Replace with your bot token
    bot = TwitchBot(nickname='PickMeCalculator', realname='Pick Me Calculator', username='ddch1kfwybbh11ogadd0n88o3xsytk')
    await bot.connect('irc.chat.twitch.tv', 6667)
    await bot.handle_forever()

if __name__ == "__main__":
    asyncio.run(main())
