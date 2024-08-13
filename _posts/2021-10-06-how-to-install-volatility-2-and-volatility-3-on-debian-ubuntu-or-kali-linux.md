---
layout: post
status: publish
published: true
title: How to Install Volatility 2 and Volatility 3 on Debian, Ubuntu, or Kali Linux
permalink: /1172/how-to-install-volatility-2-and-volatility-3-on-debian-ubuntu-or-kali-linux/
description: A comprehensive guide to installing Volatility 2, Volatility 3, and all of their dependencies on Debian-based Linux like Ubuntu and Kali
image:
  path: /assets/images/memory-ram-close-up.jpg
wordpress_id: 1172
wordpress_url: https://seanthegeek.net/?p=1172
date: '2021-10-06 18:38:44 +0000'
date_gmt: '2021-10-06 18:38:44 +0000'
categories:
- Information Security
- How-to Guides
tags:
- forensics
- Volatility
- DFIR
- memory forenssics
- Python
comments:
- id: 6240
  author: Michael Edwards
  author_url: ''
  date: '2021-10-21 18:58:48 +0000'
  date_gmt: '2021-10-21 18:58:48 +0000'
  content: Thanks for taking the time on this , much appreciated.
- id: 6491
  author: Josafat Jauregui
  author_url: ''
  date: '2021-11-04 19:40:32 +0000'
  date_gmt: '2021-11-04 19:40:32 +0000'
  content: Thank you so much! You have helped me solve my problem :)
- id: 7029
  author: Vincent
  author_url: ''
  date: '2022-01-29 15:27:41 +0000'
  date_gmt: '2022-01-29 15:27:41 +0000'
  content: I have installed both volatility2 and volatility3 using sudo in front of
    the "python2 -m pip install" and "python3 -m pip install" commands so that volatility
    is installed for all users. I am able to call volatility2 by typing "vol.py" at
    the shell, but I don't know how to call volatility 3. Could you help me please.
    Thank you.
- id: 7045
  author: noname
  author_url: ''
  date: '2022-02-07 22:43:24 +0000'
  date_gmt: '2022-02-07 22:43:24 +0000'
  content: "vol\r\nvolshell\r\nvol.py"
- id: 7081
  author: Vincent
  author_url: ''
  date: '2022-02-26 00:27:48 +0000'
  date_gmt: '2022-02-26 00:27:48 +0000'
  content: Thank you for this tutorial. I am now up and running with both Volatility
    versions. I find that Volatility 3 is well developed for Windows plugins, but
    very lacking for Linux plugins. Is there a reason for that? Is it because Volatility
    2 is good enough for Linux systems?
- id: 7449
  author: Dino
  author_url: ''
  date: '2022-06-03 09:45:03 +0000'
  date_gmt: '2022-06-03 09:45:03 +0000'
  content: "Great tutorial - Installed both Vol 2 and Vol 3 on Kali 2022.2, whereas
    Vol 2 works like a charm while Vol 3 is somehow acting up and returning following
    messages:\r\n\r\n┌──(kali㉿kali)-[~]\r\n└─$ vol -f exam-sim-2.mem kdbgscan\r\nVolatility
    3 Framework 2.2.0\r\nusage: volatility [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]]
    [-e EXTEND] [-p PLUGIN_DIRS]\r\n                  [-s SYMBOL_DIRS] [-v] [-l LOG]
    [-o OUTPUT_DIR] [-q] [-r RENDERER] [-f FILE] [--write-config]\r\n                  [--save-config
    SAVE_CONFIG] [--clear-cache] [--cache-path CACHE_PATH] [--offline]\r\n                  [--single-location
    SINGLE_LOCATION] [--stackers [STACKERS ...]]\r\n                  [--single-swap-locations
    [SINGLE_SWAP_LOCATIONS ...]]\r\n                  plugin ...\r\nvolatility: error:
    argument plugin: invalid choice kdbgscan (choose from banners.Banners, configwriter.ConfigWriter,
    frameworkinfo.FrameworkInfo, isfinfo.IsfInfo, layerwriter.LayerWriter, linux.bash.Bash,
    linux.check_afinfo.Check_afinfo, linux.check_creds.Check_creds, linux.check_idt.Check_idt,
    linux.check_modules.Check_modules, linux.check_syscall.Check_syscall, linux.elfs.Elfs,
    linux.keyboard_notifiers.Keyboard_notifiers, linux.kmsg.Kmsg, linux.lsmod.Lsmod,
    linux.lsof.Lsof, linux.malfind.Malfind, linux.mountinfo.MountInfo, linux.proc.Maps,
    linux.psaux.PsAux, linux.pslist.PsList, linux.pstree.PsTree, linux.tty_check.tty_check,
    mac.bash.Bash, mac.check_syscall.Check_syscall, mac.check_sysctl.Check_sysctl,
    mac.check_trap_table.Check_trap_table, mac.ifconfig.Ifconfig, mac.kauth_listeners.Kauth_listeners,
    mac.kauth_scopes.Kauth_scopes, mac.kevents.Kevents, mac.list_files.List_Files,
    mac.lsmod.Lsmod, mac.lsof.Lsof, mac.malfind.Malfind, mac.mount.Mount, mac.netstat.Netstat,
    mac.proc_maps.Maps, mac.psaux.Psaux, mac.pslist.PsList, mac.pstree.PsTree, mac.socket_filters.Socket_filters,
    mac.timers.Timers, mac.trustedbsd.Trustedbsd, mac.vfsevents.VFSevents, timeliner.Timeliner,
    windows.bigpools.BigPools, windows.cachedump.Cachedump, windows.callbacks.Callbacks,
    windows.cmdline.CmdLine, windows.crashinfo.Crashinfo, windows.devicetree.DeviceTree,
    windows.dlllist.DllList, windows.driverirp.DriverIrp, windows.driverscan.DriverScan,
    windows.dumpfiles.DumpFiles, windows.envars.Envars, windows.filescan.FileScan,
    windows.getservicesids.GetServiceSIDs, windows.getsids.GetSIDs, windows.handles.Handles,
    windows.hashdump.Hashdump, windows.info.Info, windows.ldrmodules.LdrModules, windows.lsadump.Lsadump,
    windows.malfind.Malfind, windows.mbrscan.MBRScan, windows.memmap.Memmap, windows.modscan.ModScan,
    windows.modules.Modules, windows.mutantscan.MutantScan, windows.netscan.NetScan,
    windows.netstat.NetStat, windows.poolscanner.PoolScanner, windows.privileges.Privs,
    windows.pslist.PsList, windows.psscan.PsScan, windows.pstree.PsTree, windows.registry.certificates.Certificates,
    windows.registry.hivelist.HiveList, windows.registry.hivescan.HiveScan, windows.registry.printkey.PrintKey,
    windows.registry.userassist.UserAssist, windows.sessions.Sessions, windows.skeleton_key_check.Skeleton_Key_Check,
    windows.ssdt.SSDT, windows.statistics.Statistics, windows.strings.Strings, windows.symlinkscan.SymlinkScan,
    windows.vadinfo.VadInfo, windows.verinfo.VerInfo, windows.virtmap.VirtMap)\r\n\r\nUnfortunately
    I can't make much sense out of it, any hint what might be missing or where I might
    need to look into?"
- id: 9165
  author: Jen
  author_url: ''
  date: '2023-12-02 06:43:44 +0000'
  date_gmt: '2023-12-02 06:43:44 +0000'
  content: total lifesaver.  thanks so much
- id: 9208
  author: Lee
  author_url: ''
  date: '2023-12-13 15:37:13 +0000'
  date_gmt: '2023-12-13 15:37:13 +0000'
  content: Thank you great tutorial.
---
Volatility is a powerful memory forensics tool. This guide will show you how
to install Volatility 2 and Volatility 3 on Debian and Debian-based Linux
distributions, such as Ubuntu and Kali Linux.

With Volatility, you can read memory/RAM captures and determine all sorts of
things about the state of a system when the memory capture was made,
including, but not limited to:

* Cached files
* Cached RSA private/public keys
* Clipboard contents
* Command history
* Driver/kernel module details
* Keyboard buffer contents
* Open sockets
* Registry contents
* Running processes
* [Shellbags](https://medium.com/ce-digital-forensics/shellbag-analysis-18c9b2e87ac7)

Unfortunately, most of these features/plugins only apply to memory captures of
systems running Windows.

## Volatility 2 vs Volatility 3

Volatility 2 is written for Python 2. Python 2 reached End of Life (EOL) in
2020. Volatility 3 is written for Python 3, and is much faster. However,
Volatility 3 currently does not have anywhere near the same number of
plugins/features as Volatility 2, so is is best to install both versions side-
by-side and use whichever version is best suited for a particular task, which
for now is most likely Volatility 2.

## Install system dependencies

```bash
sudo apt install -y build-essential git libdistorm3-dev yara libraw1394-11 libcapstone-dev capstone-tool tzdata
```

## Install pip for Python 2

```bash
sudo apt install -y python2 python2.7-dev libpython2-dev
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
sudo python2 -m pip install -U setuptools wheel
```

## Install Volatility 2 and its Python dependencies

To install system-wide for all users, use the `sudo` command in front of the
`python2` commands.

```bash
python2 -m pip install -U distorm3 yara pycrypto pillow openpyxl ujson pytz ipython capstone
sudo python2 -m pip install yara
sudo ln -s /usr/local/lib/python2.7/dist-packages/usr/lib/libyara.so /usr/lib/libyara.so
python2 -m pip install -U git+https://github.com/volatilityfoundation/volatility.git
```

## install pip for Python 3

```bash
sudo apt install -y python3 python3-dev libpython3-dev python3-pip python3-setuptools python3-wheel
```

## Install Volatility 3 and its Python dependencies

To install system-wide for all users, use the `sudo` command in front of the
`python3` commands.

```bash
python3 -m pip install -U distorm3 yara pycrypto pillow openpyxl ujson pytz ipython capstone
python3 -m pip install -U git+https://github.com/volatilityfoundation/volatility3.git
```

## Adding your user bin to your PATH

Installing Volatility as a user instead of as `root` allows you to install
Volatility and its dependencies without polluting your system's Python
environment. Installed commands are not in your `PATH` by default, so if you
try running `vol.py` (Volatility 2) or `vol`/`volshell` (Volatility 3) in your
shell, the command will not be found.

To fix this you need to add `/home/username/.local/bin` to your the `PATH`,
replacing `username` with your actual username. The process for doing this
varies, depending which shell you are using.

### bash (The default shell)

  1. Open a terminal or SSH session
  2. Make sure you are in a `bash` shell. If not, type `bash` and hit enter
  3. Type the following commands and press enter after each line (replace `username` with your actual username)  
`echo 'export PATH=/home/username/.local/bin:$PATH' >> ~/.bashrc`  
`. ~/.bashrc`

### fish (My personal favorite shell)

  1. Open a terminal or SSH session
  2. Make sure you are in a `fish` shell. If not, type `fish` and hit enter
  3. Type the following commands and press enter after each line (replace `username` with your actual username)  
`mkdir -p ~/.config/fish`  
`echo 'set -x PATH /home/username/.local/bin $PATH' >>
~/.config/fish/config.fish`  
`. ~/.config/fish/config.fish`

### ksh or sh

  1. Open a terminal or SSH session
  2. Make sure you are in a `ksh` or `sh` shell. If not, type `ksh` or `sh` and hit enter
  3. Type the following commands and press enter after each line (replace `username` with your actual username)  
`echo 'export PATH=/home/username/.local/bin:$PATH' >> ~/.profile`  
`. ~/.profile`

### zsh

  1. Open a terminal or SSH session
  2. Make sure you are in a `zsh` shell. If not, type `zsh` and press enter
  3. Type the following commands and press enter after each line (replace `username` with your actual username)  
`echo 'export PATH=/home/username/.local/bin:$PATH' >> ~/.zshrc`  
`. ~/.zshrc`
