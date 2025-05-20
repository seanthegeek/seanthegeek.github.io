---
layout: post
title: How to stop all fans from running at 100% when a third-party GPU is installed
  in a 13th-generation Dell PowerEdge server
description: Use IPMI to configure the fan profile and stop the server from sounding like a jet after a third-party GPU is installed in a Dell PowerEdge T130, R230, T330, R330, R430, R530, R630, T630, M630, R730, R730xd, R830, FC830, R930, or C4130 server
image:
  path: /assets/images/dell-r730xd.webp
  alt: A picture of a Dell R730xd server
categories:
  - Guides
tags:
  - Dell
  - Servers
  - IPMI
date: 2025-05-20 17:05 -0400
---
I have a used Dell PowerEdge R730xd server in my basement running TrueNAS. The R70XD is a storage server that was originally launched in 2014. I use it mostly for storage and running a few virtual machines. Recently, I decided to add a refurbished Nvidia A5000 GPU so I could play around with LLMs and other AI tech in a VM with the GPU [passed through](posts/fix-for-vfio-gpu-passthrough-vfio-map-dma-failed-errors-in-truenas-proxmox-unraid-qemu/). As soon as the OS booted all of the fans sped up to 100% even though the system was just idling. A very helpful [YouTube video](https://www.youtube.com/watch?v=8wRFUxs3tPQ) by MadTc Tech explains how to fix this. I'm documenting the steps here on my blog so they are handy for me without needing to watch a 6 minute video, and for safekeeping if that video every disappears.

## Ensure IPMI is Enabled in iDRAC

The solution presented by MadTc Tech uses the (Integrated Dell Remote Access Controller (iDRAC))[Integrated Dell Remote Access Controller (iDRAC)] and [Intelligent Platform Management Interface (IPMI)](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface) to reconfigure the fan profiles.

First, access iDRAC via a web browser at the IP address assigned to the iDRAC network interface of the server. This IP address is displayed at he BIOS startup screen.

The default iDRAC credentials are username `root`, with the password `calvin`.

Once logged into the iDRAC, navigate to `Network` page, under `Overview> iDRAC Settings` in the navigation pane. Scroll Down to `IPMI Settings` and ensure that the `Enable IPMI for LAN` checkbox is checked, and `Channel Privilege Level` is set to `Administrator`.

## Install the Dell OpenManage BMC Utility

Download the Dell OpenManage BMC Utility, which can be found [here](https://www.dell.com/support/home/en-us/drivers/driversdetails?driverid=w9nmr&oscode=w12r2&productcode=poweredge-r730xd).

Install it by launching the exe, selecting a temporary path, and clicking `Unzip`. Navigate to that path in Explorer, and run `BMC.MSI`

## Run the IPMI command

Open PowerShell and run:

```powershell
cd 'C:\Program Files (x86)\Dell\SysMgt\bmc'
```

Then run `.\ipmitool.exe` with different command line arguments, depending on what you want to do. In these examples, replace `<IPADDRESS>` with the IP address of the iDRAC interface, `<USERNAME>` with the iRAC username, and `<PASSWORD>` with the iDRAC password.

### Set Third-Party PCIe Card Default Cooling Response Logic To Disabled

```powershell
.\ipmitool -I lanplus -H <IPADDRESS> -U <USERNAME> -P <PASSWORD> raw 0x30 0xce 0x00 0x16 0x05 0x00 0x00 0x00 0x05 0x00 0x01 0x00 0x00
```

### Set Third-Party PCIe Card Default Cooling Response Logic To Enabled

```powershell
.\ipmitool -I lanplus -H <IPADDRESS> -U <USERNAME> -P <PASSWORD> raw 0x30 0xce 0x00 0x16 0x05 0x00 0x00 0x00 0x05 0x00 0x00 0x00 0x00 
```

### Get Third-Party PCIe Card Default Cooling Response Logic Status

```powershell
.\ipmitool -I lanplus -H <IPADDRESS> -U <USERNAME> -P <PASSWORD> raw 0x30 0xce 0x01 0x16 0x05 0x00 0x00 0x00
```

The response data is:

```text
16 05 00 00 00 05 00 01 00 00 (Disabled)
16 05 00 00 00 05 00 00 00 00 (Enabled)
```

## Other References

- [Dell documentation](https://www.dell.com/support/kbdoc/en-us/000135682/how-to-disable-the-third-party-pcie-card-default-cooling-response-on-poweredge-13g-servers?msockid=284ce75c0b816bb60999f2fd0a0c6a29)
- [Silence Your Dell PowerEdge Server - SPX LABS](https://www.spxlabs.com/blog/2019/3/16/silence-your-dell-poweredge-server)
