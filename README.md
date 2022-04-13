# MayorbotC2


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

## This is my Discord C2 bot. There are many like it, but this one is mine.

<p align="center">
  <img src="https://github.com/dievus/MayorbotC2/blob/main/images/mayorbotc2.png" />
</p>

MayorbotC2 is a project I absolutely forgot about until I was pilfering through my OneDrive the other day and realized that I had started writing this thing an eon ago. It provides an interesting avenue for command and control, utilizing a PRIVATE Discord server as the team server, and the Discord bot itself as the beacon or client.

This is set up to work on Windows only currently. Linux will come after I lose this thing for a while and find it again down the road.

## Usage
##### Installing MayorbotC2
```git clone https://github.com/dievus/MayorbotC2.git```

##### Create a PRIVATE Discord Server
You can Google this one

##### Creating the Discord Bot
This article and the included videos is great - https://www.freecodecamp.org/news/create-a-discord-bot-with-python/. Once done, make sure to replace the token in the Python file with the token for your bot.

##### Convert MayorbotC2.py to an Executable
There are different ways to do this, either with Pyinstaller, or Auto Py to EXE. Google again.

##### Current Commands
```$custom_command <command here>``` - You can run just about any command you want, however if it is greater than 2000 characters it may not print. (Fix coming soon that will address this)

```$cd <directory>``` - Change directory is working as intended. Mind that you must specify the actual directory. .. changes likely won't work.

```$screenshot``` - Will take a screenshot, upload it to the Discord Server, and delete from the file system.

```$ip``` - This has a tendency to print greater than 2000 characters, and if it does, it will generate a text file, upload it to the server, and delete it. Otherwise, if less than 2000 characters it will output to the server.

```$sysinfo``` - Does what it says, and is the same as $ip above.

```$filegrab``` - Grabs a file from the host machine and uploads it to the Discord server.

```$fodhelper``` - None of my tools would be mine if I didn't include this. Make sure to modify the IP address in the command to your hosting server. You can change custom commands behind the -custom flag in the command.

```$shutdown, $restart, $exit``` - These are exactly as they sound.

##### Mandatory Don't Do Dumb Shit Statement
This is meant for research purposes only. Please do not do anything stupid with this. Anything you do is your responsibility, and I cannot be held accountable for your stupidity should you screw up. 

