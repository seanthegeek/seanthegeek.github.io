---
layout: post
title: Fix for VFIO GPU Passthrough VFIO_MAP_DMA Failed Errors in TrueNAS/Proxmox/Unraid/QEMU
date: 2025-05-19 17:16 -0400
description: To fix VFIO_MAP_DMA errors, reduce VM RAM allocation or configure hugepages on the host
image:
  path: /assets/images/truenas-qemu-vm-memory-error.webp
  alt: A screenshot of a VFIO_MAP_DMA error error when trying to boot a QEMU VM with an attached GPU in TrueNAS
categories:
  - Guides
tags:
  - Virtualization
  - QEMU
  - GPU passthrough
  - TrueNAS
  - Proxmox
  - Unraid
  - AMD
  - Nvidia
  - Hugepages
---
I wanted to passthrough a GPU to a Nvidia GPU (specifically an A5000) to VM on TrueNAS SCALE so I could try out some local LLMs. I properly [isolated the GPU](https://www.truenas.com/docs/scale/25.04/scaletutorials/systemsettings/advanced/managegpuscale/) so the host OS didn't try to use it, edited the VM, and set the GPU to the isolated GPU. But, when I tried to start the VM I got a long pause and an error like this:

```text
[EFAULT] internal error: qemu unexpectedly closed the monitor: ...

VFIO_MAP_DMA failed: Bad address

vfio 0000:82:00.1: failed to setup container for group XX: memory listener initialization failed...
```

After lots of poking around on the internet, I've found that the this error is due to the OS trying and failing to map a large amount of memory for the VM and the GPU.

## Reduce the amount of RAM allocated to the VM

You hve likely allocated too much RAM to that VM, try reducing it a little bit at a time until you find an amount that is bootable.

## Hugepages

If you find that the amount of memory that the system will boot with is not enough for your use case, you can try enabling Hugepages by configuring the kernel option `vm.nr_hugepages` on the host system. To reserve an amount of system memory for mapping purposes.

Unfortunately, I have found that for some reason, each time I shut down the VM, an increase in `vm.nr_hugepages` was required to get the VM to start again without rebooting the host system, so Hugepages was not a viable solution for me. I don't know why.

Hugepages come in 2 MB chunks by default on most systems. So, the formula is:

```text
vm.nr_hugepages = (Desired RAM in MB) / 2
```

| Memory to Reserve | Hugepages Needed |
| ----------------- | ---------------- |
| 1 GB (1024 MB)    | 512              |
| 2 GB              | 1024             |
| 4 GB              | 2048             |
| 8 GB              | 4096             |

And so on.

Start small. To set `vm.nr_hugepages` to `512`, run

```bash
sudo sysctl -w vm.nr_hugepages=512
```

Next, run this command to apply the change without needing a reboot.

```bash
sudo sysctl -p
```

Then try running the VM. Increase the number of hugepages as needed until the VM boots successfully. Once you have found a value that works, write it to a `sysctl` configuration file so the change is applied at boot, like this:

```bash
sudo cat vm.nr_hugepages=512 > /etc/sysctl.d/10-hugepages.conf
```

Otherwise, the change will not persist after a reboot of the host system.
