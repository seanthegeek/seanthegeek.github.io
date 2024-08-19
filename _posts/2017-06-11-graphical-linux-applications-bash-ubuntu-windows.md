---
layout: post
permalink: /234/graphical-linux-applications-bash-ubuntu-windows/
title: How to run graphical Linux applications on Windows 10 using the Windows Subsystem
  for Linux (WSL) 1.0
description: A step-by-step guide on installing Bash on Ubuntu on Windows, with additional
  steps for running graphical Linux applications.
date: 2017-06-11 20:01:53 -0000
last_modified_at: 2020-03-04 13:30:36 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2017/06/xeyes-bash-ubuntu-windows-10.webp
  alt: A screenshot of xeyes running on Bash on Ubuntu on Windows 10 WSL
categories:
- Guides
tags:
- Linux
- Ubuntu
- Windows
- WSL
---
**Note** : This is an old guide that only applies to WSL 1.0. WSL 2.0 supports
GUI applications out-of-the-box.

The Windows Subsystem for Linux (WSL) was introduced by Microsoft in the
Windows 10 Anniversary Update. It allows users to run a full Linux user space
in Windows. It is a much nicer approach for most applications than Cygwin, or
using a Linux VM. It is not an emulator either. Think of it as
GNU/Linux/Windows (apologies to Richard Stallman). This guide starts off with
Microsoft's instructions for installing the WSL, and then goes a few steps
further by describing how to run graphical Linux applications.

## Prerequisites

Your PC must be running (at a minimum) a 64-bit version of Windows 10 with the
Anniversary Update. The Creator's Update is recommended.

To find your PC's CPU architecture and Windows version/build number, open
Settings>System>About. Look for the System Type and Version fields
respectively, as shown in the screenshot below.

[![Acreenshot of the About section of the Windows 10 Settings
app](/assets/wp-content/uploads/2017/06/windows_about.webp)](/assets/wp-content/uploads/2017/06/windows_about.webp)

If your build is below 14393, try checking for updates.

## Enable the Windows Subsystem for Linux feature

You can enable the feature using a GUI or command-line interface.

### GUI Method

  1. From the Start Menu, search for "Turn Windows features on or off" (type 'turn')
  2. Select Windows Subsystem for Linux  
[![The Windows features dialog box in Windows
10](/assets/wp-content/uploads/2017/06/windows_features.webp)](/assets/wp-content/uploads/2017/06/windows_features.webp)

  3. Click OK

### Command-line Method

Open a PowerShell prompt as administrator and run:

    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

## After enabling Windows Subsystem for Linux

Restart your computer when prompted.

> It is important that you DO restart when prompted as some of the
> infrastructure which the Windows Subsystem for Linux requires can only be
> loaded during Windows' boot-up sequence.

### Install your Linux distribution of choice

Linux distributions can be installed [using a
script](https://docs.microsoft.com/en-us/windows/wsl/install-manual), or by
using the Microsoft Store links below:

* [Ubuntu](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6)
* [Kali Linux](https://www.microsoft.com/store/apps/9PKR34TNCV07)
* [Debian GNU/Linux](https://www.microsoft.com/store/apps/9MSVKQC78PK6)
* [Fedora Remix for WSL](https://www.microsoft.com/store/apps/9n6gdm4k2hnc)
* [Pengwin](https://www.microsoft.com/store/apps/9NV1GV1PXZ6P)
* [Pengwin Enterprise](https://www.microsoft.com/store/apps/9N8LP0X93VCP)
* [Alpine WSL](https://www.microsoft.com/store/apps/9p804crf0395)

After installation your Linux distribution will be located at:
`%localappdata%\lxss\` This directory is marked as a hidden system folder for
a very good reason:

> Avoid creating and/or modifying files in this location using Windows tools
> and apps! If you do, it is likely that your Linux files will be corrupted
> and data loss may occur. Please read this [blog
> post](https://blogs.msdn.microsoft.com/commandline/2016/11/17/do-not-change-
> linux-files-using-windows-apps-and-tools/) for more information.

### Create a UNIX user

The first time you launch a Linux distribution in Windows, you will be
prompted to create a UNIX username and password.

[![A screenshot of a new UNIX user being created for Bash on Ubuntu on
Windows](/assets/wp-content/uploads/2017/06/new-user.webp)](/assets/wp-content/uploads/2017/06/new-user.webp)

This UNIX username and password has no relationship to your Windows username
and password, and it can be different.****

Use the same username that you use on remote Linux/UNIX systems, so you won't
need to specify it in individual configuration files, or every time you run
commands like `ssh`. [Read more](https://msdn.microsoft.com/en-
us/commandline/wsl/user_support).

### Update the Linux distribution

After you have set up your user, update the OS.

To do this on Debian/Ubuntu based distributions, run:

    sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y && sudo apt-get autoremove -y

### Install common tools

The Debian distribution for WSL is minimal, so many packages that you might
expect to be installed, such as ca-certificates, are not installed. To fix
this, run:

    sudo apt install -y ca-certificates findutils command-not-found vim nano curl
    openssh-client less screen apt-utils top htop whois git python3-pip

## Accessing the Windows filesystem from WSL

Windows drives are mounted by their drive letters under `/mnt`. For example,
your Windows C: drive is accessible via `/mnt/c.`

To make it easier to access your Windows user directory, consider adding a
symbolic link, such as:

    ln -s /mnt/c/Users/Sean/ ~/winhome

On Amazon WorkSpaces, this your Windows user directory is located in
`/mnt/d/Users`.

That way, your Windows user directory is accessible from `~/winhome`.

## Graphical Applications

In order to run Linux GUI applications using WSL, you must:

  1. Install a X server for Windows
  2. Configure bash to tell GUIs to use the local X server

### Install VcXsrv

In order to run graphical Linux applications, you'll need an X server.

[VcXsrv](https://sourceforge.net/projects/vcxsrv/) is the only fully open
source and up-do-date native X server for Windows. Download and run the latest
installer, then locate the XLaunch shortcut in the Start Menu, and click it.

You will be greeted with a setup wizard. Accept the default options. On the
last page of the wizard, click on the Save configuration button, and save the
configuration file in `%appdata%\Microsoft\Windows\Start
Menu\Programs\Startup`, so vcXsrv will launch at startup without asking about
these options, then click on the Finish button.

**You may receive a prompt to allow it through your firewall. Cancel/deny this
request! Otherwise, other computers on your network could access the server.**

A X icon will appear in your system tray.

### Configure bash to use the local X server

  1. In bash run:  
`echo "export DISPLAY=localhost:0.0" >> ~/.bashrc`

  2. To have the configuration changes take effect, restart bash, or run:  
`. ~/.bashrc`

### Instructions for fish shell users

If you use fish instead of bash:

  1. `echo "set -x DISPLAY localhost:0.0" >> ~/.config/fish/config.fish`
  2. To have the configuration changes take effect, restart fish, or run:  
`. ~/.config/fish/config.fish`

### Test a graphical application

  1. Install `x11-apps`  
`sudo apt-get install x11-apps`

  2. Run `xeyes`

A new window will open, containing a pair of eyes that will follow your mouse
movements.

## Running remote GUI applications over SSH

To use a GUI application from a server, simply use the `-X` switch with the
`ssh` command, for example:

    ssh -X user@server.example.com

And run the GUI application from the shell prompt.

## Using Visual Studio Code

Instead on installing the Linux version on Visual Studio Code on your WSL
Linux distribution, install Visual Studio Code in Windows, and add the [Remote
Development extension
pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-
remote.vscode-remote-extensionpack).

After reloading Visual Studio Code, click on the green arrows at the bottom
right corner of the window, and select `Remote-WSL: New window` action.

A new window will open with a Linux shell and editor. You will be able to edit
files on the Linux file system.

Any Visual Studio Code extensions need to be installed in your Windows
instance of Visual Studio Code first, and then on the WSL instance.

Recommended extensions for information security professionals include:

* [AsciiDoc](https://marketplace.visualstudio.com/items?itemName=joaompinto.asciidoctor-vscode)
* [Autoit](https://marketplace.visualstudio.com/items?itemName=Damien.autoit)
* [Beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify)
* [Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)
* [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
* [C#](https://marketplace.visualstudio.com/items?itemName=ms-vscode.csharp)
* [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)
* [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
* [DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv)
* [Edit CSV](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv)
* [Email](https://marketplace.visualstudio.com/items?itemName=leighlondon.eml)
* [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
* [Excel Viewer](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)
* [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) (Requires [git](https://git-scm.com/))
* [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) (Requires [git](https://git-scm.com/))
* [GnuPG-Tool](https://marketplace.visualstudio.com/items?itemName=JHeilingbrunner.vscode-gnupg-tool) (Requires [GnuPG4Win](https://www.gpg4win.org/) on Windows, gpg on Mac or Linux)
* [Haskell Syntax Highlighting](https://marketplace.visualstudio.com/items?itemName=justusadam.language-haskell)
* [Hexdump for VSCode](https://marketplace.visualstudio.com/items?itemName=slevesque.vscode-hexdump)
* [HTML CSS Support](https://marketplace.visualstudio.com/items?itemName=ecmel.vscode-html-css)
* [ini for VSCode](https://marketplace.visualstudio.com/items?itemName=DavidWang.ini-for-vscode)
* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
* [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
* [NDJSON Colorizer](https://marketplace.visualstudio.com/items?itemName=buster.ndjson-colorizer)
* [Output Colorizer](https://marketplace.visualstudio.com/items?itemName=IBM.output-colorizer)
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
* [REG](https://marketplace.visualstudio.com/items?itemName=ionutvmi.reg)
* [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
* [reStructuredText](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext)
* [tl;dr pages](https://marketplace.visualstudio.com/items?itemName=bmuskalla.vscode-tldr)
* [VBScript](https://marketplace.visualstudio.com/items?itemName=Darfka.vbscript)
* [VSCode Ruby](https://marketplace.visualstudio.com/items?itemName=wingrunr21.vscode-ruby)
* [x86 and x86_64 Assembly](https://marketplace.visualstudio.com/items?itemName=13xforever.language-x86-64-assembly)
* [XML Tools](https://marketplace.visualstudio.com/items?itemName=DotJoshJohnson.xml)
* [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
* [YARA](https://marketplace.visualstudio.com/items?itemName=infosec-intern.yara)

## References

* [Official install guide from Microsoft](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)
