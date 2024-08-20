---
layout: post
permalink: /1189/how-to-update-the-firmware-on-a-samsung-monitor/
title: How to update the firmware on a Samsung monitor
description: This guide explains the exact steps for updating the firmware on Samsung
  monitor, and will hopefully save you a lot of searching.
date: 2021-11-25 01:47:35 -0000
last_modified_at: 2021-11-25 01:58:09 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2021/11/samsung-monitor-upgrade-scaled.webp
categories:
- Consumer Devices
- Guides
tags:
- Samsung
---
Almost every device you can buy nowadays has upgradable firmware. New firmware
versions can fix bugs, patch security vulnerability, improve features, or add
features. As computer monitors get more complex and feature-packed, it becomes
more important to use the latest firmware. Samsung doesn't provide
instructions on performing a firmware update in user guides on on download
pages. This guide explains the exact steps for updating the firmware on
Samsung monitor, and will hopefully save you a lot of searching.

## What you will need

* A Samsung monitor
* A flash drive that you you don't mind completely erasing
* An internet connection

## Check the monitor model and current firmware version

Use the little joystick under the monitor to navigate to Menu> Support>
Information. This will display:

* The full model number
* The serial number
* The software/firmware version
* HDR status
* Adaptive Sync status
* Active port
* Display resolution
* Refresh rate

## Acquire the firmware

To download the latest firmware for your monitor go to the Samsung
[support](https://www.samsung.com/us/support/) website, click search for your
model number, and enter your model number. Click on manuals and software.
Under firmware, click download.

Extract the .img firmware file from the downloaded ZIP.

## Prep the flash drive

Warning: This process will erase all data on the flash drive!

The flash drive needs to be formatted with a FAT32 filesystem. The easiest way
to do this is to use the free an open source drive flashing tool,
[Rufus](https://rufus.ie).

![Screenshot of Rufus](/assets/wp-content/uploads/2021/11/rufus-gui.webp)  
__Rufus is a simple GUI utility for flashing drives__

Plug in the flash drive, then run Rufus. Apply the following settings:

* Device: The drive you want to format
* Boot selection: Non bootable
* Partition scheme: MBR
* Target system: BIOS or UEFI
* File system: Large FAT32 (Default)
* Cluster size: 32 kilobytes

Click START, read the warning, and click OK.

![Screenshot of a warning from Rufus](/assets/wp-content/uploads/2021/11/formatting-warning.webp)  
__Rufus will warn you before taking action__

You might need to unplug the drive and reconnect it before it will appear
again.

Rufus will add the files `autorun.ico` and `autorun.inf` to the flash drive.
Delete these files.

![A screenshot of the files created by rufus](/assets/wp-content/uploads/2021/11/rufus-autorun-files.webp)  
__Rufus creates these files to add an icon to the drive label__

Copy the .img file you extracted earlier to the flash drive.

Eject and remove the flash drive.

## Connect the flash drive

Before connecting the flash drive, unplug all USB devices that are connected
to the monitor, **including any USB type B cable** between the monitor and
computer.

Plug the flash drive into the USB Type A port labeled Service. Same Samsung
monitors have two USB Type A ports, but only one of those ports is a service
port that can be used to upgrade firmware.

![Diagrams of the ports on Samsung monitors](/assets/wp-content/uploads/2021/11/samsung-monitor-ports.webp)  
Some monitors only have a service port. Others have multiple USB ports, with
only one port as a service port.

## Start the update

Use the little joystick under the monitor to navigate to Menu> Support>
Software Update. Once the update is finished, you can unplug the flash drive
and reconnect any USB devices you disconnected before the update.
