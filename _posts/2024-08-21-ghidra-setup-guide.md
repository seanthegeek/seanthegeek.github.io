---
layout: post
title: Ghidra setup guide
description: A complete setup guide to Ghidra, including perquisites, scripts, and
  extensions.
image:
  path: "/assets/images/ghidra-logo.webp"
categories:
- Reverse Engineering Malware
tags:
- Ghidra
date: 2024-08-21 19:56 -0400
---
Ghidra is an open-source software reverse engineering platform developed by the
US National Security Agency (NSA). It is a useful free alternative to
commercial reverse engineering platforms such as IDA or Binary Ninja. Each
platform has its strengths and weaknesses but a price tag of $0 is a powerful
adoption motivator. In fact, Ghidra has replaced IDA as in the SANS
FOR610: Reverse-Engineering Malware: Malware Analysis Tools and Techniques
course! Ghidra does require a few setup steps, which is what this guide is all
about!

## Install an OpenJDK build

Ghidra is written in Java. In order to use Ghidra you ned to have a Java Runtime
Environment (JRE) on your system. On April 16, 2019, Oracle changed the
license of their JRE to require payment for commercial use. To avoid licensing
issues, install a build of the OpenJDK JRE instead.

### OpenJDK on Linux

Each Linux distribution has their own package for the OpenJDK JRE. You'll need
to do some searching to find the right package name for the OpenJDK JRE for
the Linux distribution that you use.

### OpenJDK on macOS

Install OpenJDK via [Homebrew](https://brew.sh/)

```bash
brew install openjdk
```

### OpenJDK on Windows

Microsoft provides an OpenJDK build that is distributed [via a MSI](https://learn.microsoft.com/en-us/java/openjdk/install#install-on-windows-via-msi).

> In order to install the MSI correctly, you must run `msiexec` with the proper
> options, rather than just double-clicking on the MSI.
{: .prompt-danger }

```powershell
msiexec /i <package>.msi ADDLOCAL=FeatureMain,FeatureEnvironment,FeatureJarFileRunWith,FeatureJavaHome INSTALLDIR="C:\Program Files\Microsoft\" /quiet
```

> Replace `<package>` with the actual MSI filename.
{: .prompt-info }

## Python

Ghidra Scripts are written in Java and Python 2, which are processed by Ghidra
itself without needing Python 2 installed. However, a project by Mandiant
called [Ghidrathon](https://github.com/mandiant/Ghidrathon) allows an external
Python 3 interpreter to be used for really cool things like CAPA for Ghidra.

### Python on Linux

Most Linux distributions have Python preinstalled.

### Python on macOS

Although macOS includes Python, having a separate, newer install via Homebrew is
ideal.

```bash
brew install python@3.12
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
```

### Windows

Python installers for windows can be downloaded from the
[Python website](https://www.python.org/downloads/).

> Make sure to check the option about adding Python to the `PATH`.
{: .prompt-warning}

#### Microsoft build tools

Some Python packages (including Ghidrathon) require native C++ modules to be
built when they are installed. To build those, the Microsoft Build Tools must be
installed. To install the build tools, go to the
[Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/)
page. Do not download the full Visual Studio installer. Instead, scroll down to
All Downloads, expand the Tools for Visual Studio section, and download the
Build Tools for Visual Studio 2022.

Then run the following command to install just the build tools that are needed:

```powershell
vs_BuildTools.exe --add Microsoft.VisualStudio.Workload.VCTools
```

Then click Install.

## Create directories to store Ghidra projects and Ghidra scripts

Create the following directories your user's home directory:

- `ghidra_scripts`
- `ghidra_gdt`
- `Ghidra Projects`

## Download Ghidra

Download the latest release of Ghidra
[from GitHub](https://github.com/NationalSecurityAgency/ghidra/releases)
and extract the ZIP file to somewhere you would like to keep Ghidra.

Rename the directory and remove the version information, so that the
directory is called `ghidra`.

## Add Ghidra Data Type (GDT) files

Ghidra understands some Windows API data structures out of the box, but it
doesn't understand some key ones, such as those related to internet
connectivity. To fix this, you'll need to download Ghidra Data Type (.gdt)
files, and tell Ghidra where to find them.

 Fortunately, someone generated .gtd files for Windows APIs and posted them on
 GitHub.

You can find them at [https://github.com/0x6d696368/ghidra-data/](https://github.com/0x6d696368/ghidra-data/) under the `typeinfo` directory. In that directory, the only files
needed are:

- `ntddk_32.gdt`
- `ntddk_64.gdt`
- `winapi_32.gdt`
- `winapi_64.gdt`

I have also included them [here](/assets/data/ghidra_gdt.zip) for convenance and
preservation.

Copy the `.gdt` files to the `ghidra_gdt` directory you created earlier.

## Useful Ghidra scripts

### LazyGhidra

The GitHub user AllsafeCyberSecurity created a set of scripts for converting
data types under the MIT license called LazyGhidra. I have included them
[here](/assets/data/AllsafeCyberSecurity-LazyGhidra.zip)

Extract the zip, then copy the files in `scripts` to the
`ghidra_scripts` directory that you created earlier.

### CAPA for Ghidra

[CAPA for Ghidra](https://github.com/mandiant/capa/tree/master/capa/ghidra)
is awesome. However, it's a little bit of a process to get it set up.

[`capa_explorer.py`](https://raw.githubusercontent.com/mandiant/capa/master/capa/ghidra/capa_explorer.py)

Adds bookmarks bookmarks, symbols, and comments to each function that matched
a capability that is mapped to a MITRE ATT&CK and/or Malware Behavior Catalog
(MBC) technique.

[`capa_ghidra.py`](https://raw.githubusercontent.com/mandiant/capa/master/capa/ghidra/capa_ghidra.py)

Outputs text-based CAPA results that mirror the output of CAPA’s standalone
tool. You can execute this script using Ghidra’s Script Manager and view its
output in Ghidra’s Console window. You can also execute `capa_ghidra.py`
using Ghidra's Headless Analyzer to view its output in a terminal window.

Download and copy both scrips to your `ghidra_scripts` directory.

#### Ghidrathon

The CAPA scripts require [Ghidrathon](https://github.com/mandiant/ghidrathon?tab=readme-ov-file#installing-ghidrathon) to be installed so that
Ghidra can run Python 3 scripts. Here's how to do that:

1. Download the latest [release](https://github.com/mandiant/Ghidrathon/releases) and unzip it.
2. `cd` to the extracted directory.
3. Install the Python requirements by running `python -m pip -r requirements.txt`
4. Run `python ghidrathon_configure.py <absolute_path_to_ghidra_install_dir>`
5. Run Ghidra
6. Accept any license agreement and close any What's New window
7. Click File> Install Extension
8. Click on the plus button in the upper-right of the window
9. Select the Ghidrathon zip file that was inside the zip file that you unzipped
10. Click `Install Anyway` when warned about a version mismatch
11. Restart Ghidra when prompted

#### CAPA rules

1. Download the latest release of the [CAPA rules](https://github.com/mandiant/capa-rules/releases).
2. Upzip the downloaded zip file
3. Rename the unzipped directory `capa-rules`
4. Move `capa-rules` to your user's home directory

You will be prompted for this directory when you run the CAPA scripts for
Ghidra.

## Pick a UI theme

In the main Ghidra window, click Edit> Theme > Switch. I personally prefer the
Flat Dark Theme.

## Create the first Ghidra project

Some settings are only accessible when a file is open. So, we'll create a new project, open a benign executable with it, change some Ghidra settings, close the project, delete the project, shut down the VM, and create a new VM snapshot.

Create a new project by clicking File> New Project. Select Non-Shared Project, then click Next.

Select the `Ghidra Projects` directory you created earlier as the Project Directory, and give the project a name, such as `Demo`, then click Finish. This will create a new project directory under `Ghidra Projects` called `Demo.rep`.

In the Ghidra window, drag and drop a simple benign executable such as `C:\Windows\System32\PING.EXE`, click OK, then double-click on `PING.EXE` in the project window. This will open `PING.EXE` in the CodeBrowser tool.

Click Yes when Prompted to analyze the file. Then, click `Analyze`.

## Add the data types

You can see the progress of the analysis by watching the progress par in the bottom right. Once the analysis has completed, look at the `Data Type Manager`, in the bottom left. Click on the down arrow in the title bar, and click Edit Archive Paths. Add the `ghidra-ght` directory that you created earlier. Then click Ok. Then for each file in `ghidra-gdt`, click the down arrow again, click open file archive, and select the `.ght` file.

You will only need to do this once, and the new data types will be visible in in the Data Type Manager all future projects.

## Cleanup

1. Close the Code Browser indow
2. In the main Ghidra window, select File> Close Project
3. Select File> Delete Project
4. Shut down your VM
5. Take a snapshot
