---
layout: post
title: How to fix a broken UEFI GRUB bootloader in TrueNAS/Proxmox/Unraid/QEMU VMs
date: 2025-05-20 19:22 -0400
description: Navigation of the VM's BIOS menu and a few Linux commands will fix it
image:
  path: /assets/images/uefi-interactive-shell-prompt.webp
  description: A screenshot of the UEFI interactive shell prompt
categories:
  - Guides
tags:
  - GRUB
  - Virtualization
  - QEMU
  - TrueNAS
  - Proxmox
  - Unraid
---
I had provisioned more disk storage for a VM in TrueNAS than it needed, and I needed to make it use a smaller disk that wouldn't take up so much space when thick provisioned. So, I created a new, smaller zvol, attached it to the VM, booted into [GParted Live CD](https://gparted.org/livecd.php), and used the GParted GUI utility to shrink the partitions on the old, large zvol, and copy them to the new, smaller zvol. I shut down the VM, removed thd old zvol and the live CD ISO image, and booted the VM. After that I was greeted with a `Shell>` prompt shown in the screenshot above, which indicated that the boot had failed. If you find yourself in a similar situation, here's the quick and easy fix.

1. Exit the shell by typing `exit` and pressing enter. This will drop to the BIOS.
2. Use the keyboard arrow keys to select `Boot Resource Manager`, then press Enter.
3. Use the keyboard arrow keys to select `Boot From File`, then press Enter.
4. Use the keyboard arrow keys to select the drive then press Enter.
5. Use the keyboard arrow keys to select `<UEFI>`, then press Enter.
6. Use the keyboard arrow keys to select your Linux distribution, then press Enter.
7. Use the keyboard arrow keys to select `grubx64.efi`, then press Enter.
8. Once your system has temporarily booted, run `sudo grub-install /dev/sda` to properly install the GRUB bootloader on the drive.
