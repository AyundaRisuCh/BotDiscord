import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Bot berhasil login sebagai {bot.user}')


@bot.command()
async def announce(ctx, *, pesan):
    channel_id = 1388049036560302134  # Ganti dengan ID channel tujuan kamu
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send(f"📢 **Announcement** \n{pesan}")
        await ctx.send("✅ Pengumuman berhasil dikirim.")
    else:
        await ctx.send("❌ Channel tidak ditemukan.")


from keep_alive import keep_alive

keep_alive()
bot.run(os.environ["TOKEN"])
