import discord
import asyncio

# Replace 'YOUR_TOKEN_HERE' with your actual Discord login token
TOKEN = 'MTEyMDcxMjM0MTMzMjQzNDk5NA.GyH1hv._kUXMbDK2sOUwd5DA_ckF1gQi_NF9eSJzksvcg'

client = discord.Client()

async def send_message(channel_id, message):
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(message)
    else:
        print(f"Couldn't find channel with ID {channel_id}.")

@client.event
async def on_ready():
    print(f"We're in, mate! Logged in as {client.user.name}")

    # Your channel IDs go below (replace 'channel_id_1', 'channel_id_2', etc.)
    channels = [1112992355038023692, 11326062873692078181132606287369207818, 1132606317215887381]

    while True:
        try:
            for channel_id in channels:
                await send_message(channel_id, "Hey there! I'm a Discord selfbot, bitches!")
                await asyncio.sleep(3)  # Adding a 3-second delay between sending messages to different channels
            await asyncio.sleep(600)  # 10 minutes in seconds
        except discord.errors.HTTPException as e:
            print(f"Oops, we triggered Discord's rate limit! Waiting a bit before continuing. Error: {e}")
            # Wait for 10 minutes before trying again
            await asyncio.sleep(600)

@client.event
async def on_message(message):
    if message.author == client.user:  # Ignore messages from yourself
        return

    await message.channel.send("Hey there! I'm alive and ready to fuck shit up!")

    # Add an asyncio sleep of 3 seconds before responding to the next message
    await asyncio.sleep(3)

# Let's run this sucker!
client.run(TOKEN)
