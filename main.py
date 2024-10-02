import discord
from discord.ext import commands
import requests
from discord import option
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


java_url = "https://api.mcstatus.io/v2/status/java/"
bedrock_url = "https://api.mcstatus.io/v2/status/bedrock/"

@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.slash_command(name="status", description="Get the status of the Minecraft server (Java or Bedrock)")
@option("server_type", description="Choose the type of Minecraft server", choices=["Java", "Bedrock"])
@option("server_ip", description="Enter the server IP")
async def status(ctx, server_type: str, server_ip: str):
    
    await ctx.defer()

   
    if server_type.lower() == "java":
        url = f"{java_url}{server_ip}"
    else:
        url = f"{bedrock_url}{server_ip}"

   
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data:
            
            embed = discord.Embed(title=f"Minecraft {server_type} Server Status", color=discord.Color.green())
            embed.add_field(name="Server IP", value=server_ip, inline=False)
            
            if data.get("online"):
                embed.add_field(name="Status", value="🟢 Online", inline=True)
                embed.add_field(name="Players Online", value=f"{data['players']['online']} / {data['players']['max']}", inline=True)

                
                version = data.get('version', {})
                version_name = version.get('name_clean', "Unknown Version")
                embed.add_field(name="Version", value=version_name, inline=True)
            else:
                embed.add_field(name="Status", value="🔴 Offline", inline=True)


            embed.set_footer(text="Server status provided by mcstatus.io")
           
            await ctx.followup.send(embed=embed)
        else:
            await ctx.followup.send("⚠️ Could not retrieve the server status. Please check the IP and try again.")
    except Exception as e:
        await ctx.followup.send(f"Error fetching server status: {e}")

bot.run(TOKEN)
