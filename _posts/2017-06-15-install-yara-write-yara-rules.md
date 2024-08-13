---
layout: post
status: publish
published: true
title: How to install YARA and write basic YARA rules to identify malware
permalink: /257/install-yara-write-yara-rules
description: 'A complete YARA guide, covering installation, practical examples for writing YARA rules, and using YARA to identify, sort, and collect malware samples.'
image:
  path: /assets/images/sample-yara-rule.png
  alt: A screenshot of a YARA rule
wordpress_id: 257
wordpress_url: https://seanthegeek.net/?p=257
date: '2017-06-15 14:58:36 +0000'
date_gmt: '2017-06-15 14:58:36 +0000'
categories:
- Information Security
- How-to Guides
tags:
- YARA
- signatures
- DFIR
comments:
- id: 248
  author: Patrick Hermann
  author_url: ''
  date: '2017-12-18 18:05:38 +0000'
  date_gmt: '2017-12-18 18:05:38 +0000'
  content: "Hi Sean,\r\n\r\ncan you send me a quick mail, i have question regarding
    chuckoo sandbox.\r\n\r\nthx\r\npatrick"
- id: 772
  author: cryptoparty
  author_url: ''
  date: '2018-10-02 13:36:02 +0000'
  date_gmt: '2018-10-02 13:36:02 +0000'
  content: "Hey man!\r\n\r\nI need your help with ur cuckoo introduction.\r\n\r\nPlz
    contact  me"
- id: 1417
  author: vikas
  author_url: ''
  date: '2019-04-02 13:15:35 +0000'
  date_gmt: '2019-04-02 13:15:35 +0000'
  content: "i have folder containing different yara signatures files. \r\ncould you
    tell me how can use yara tool on given samples and apply all signatures on it?"
- id: 2959
  author: kim
  author_url: ''
  date: '2019-12-05 06:38:48 +0000'
  date_gmt: '2019-12-05 06:38:48 +0000'
  content: you have to use yara  yarafile.yara  -r /root/foldername
---
YARA is described as "The pattern matching Swiss knife for malware researchers
(and everyone else)". Think of it as like `grep`, but instead of matching
based on one pattern, YARA matches based on a set of rules, with each rule
capable of  containing multiple patterns, and complex condition logic for
further refining matches. It's a very useful tool. Let's go over some
practical examples of how to use it.

## Installing YARA

Official Windows binaries [can be found
here](https://yara.readthedocs.io/en/v3.9.0/gettingstarted.html#installing-on-
windows). Unfortunately, as of the time of this writing, practically every
Linux distribution's repository contains an out-of-date version of YARA that
has [one or more](https://security-tracker.debian.org/tracker/source-
package/yara) security vulnerabilities. Follow the instructions below to
compile and install the latest release with all features enabled on a Debain
or Ubuntu system. The steps should be similar in other Linux distributions.

Download the source code .tar.gz for the [latest stable
release](https://github.com/virustotal/yara/releases).

### Install the dependencies

```bash
sudo apt-get install -y automake libtool make gcc flex bison libssl-dev libjansson-dev libmagic-dev
```

### Build the project

```bash
tar -zxf v3.9.0.tar.gz
rm v3.9.0
cd yara-3.9.0
./bootstrap.sh
./configure --with-crypto --enable-profiling --enable-macho --enable-dex --enable-cuckoo --enable-magic --enable-dotnet
make
```

### Install as a Debian package

```bash
sudo apt-get install -y checkinstall
sudo apt-get remove -y libyara3 yara python-yara # Remove any existing install from distro repos
sudo checkinstall -y --deldoc=yes

# Cleanup
cd ..
rm -rf yara-3.9.0/
```

### Install the Python package

```bash
sudo apt-get install -y python-pip python3-pip
sudo -H pip install -U pip
sudo -H pip3 install -U pip
sudo -H pip install -U git+https://github.com/VirusTotal/yara-python@3.9.0
sudo -H pip3 install -U git+https://github.com/VirusTotal/yara-python@3.9.0
```

## Introduction to YARA rules

Let's start by looking at the different components that can be part of a rule.

At a minimum, a rule must have a name, and a condition. The simplest possible
rule is:

```yara
rule dummy { condition: false }
```

That rule does nothing. Inversely, this rule matches on anything:

```yara
rule dummy { condition: true }
```

Here's a slightly more useful example that will match on any file over 500 KB:

```yara
rule over_500kb {condition: filesize > 500KB}
```

Most often though, you'll write rules with a meta section, a strings section,
and a condition section:

```yara
rule silent_banker : banker {
 
meta:
  description = "This is just an example"
  threat_level = 3
  in_the_wild = true
 
strings:
   $a = {6A 40 68 00 30 00 00 6A 14 8D 91}
   $b = {8D 4D B0 2B C1 83 C0 27 99 6A 4E 59 F7 F9}
   $c = "UVODFRYSIHLNWPEJXQZAKCBGMT"
 
condition:
  all of them
}
```

The `:` after the rule name indicates the start of a list of rule tags, which
are separated by spaces. These tags are not used frequently, but you should be
aware that they exist. C-style comments can be used anywhere.

The `meta` section consists of a set of arbitrary key-value pairs that can be
used to describe the rule, and/or the type of content that it matches. Meta
values can be strings, integers, decimals, or booleans. The meta values can be
viewed by the application that is using YARA when a match occurs.

The strings section defines variables as content to be matched. These can be:

* Hexadecimal byte patterns (in `{}`, with support for wildcards and jumps). Often used to identify unique code, such as an unpacking mechanism
* Text strings
* [Regular expressions](https://yara.readthedocs.io/en/v3.6.1/writingrules.html#regular-expressions) (between `//`)

The condition section is where the true power an flexibility of YARA can be
found. Here are a few common example condition statements

**Condition** | **Meaning**  
---|---  
`any of them` | The rule will match on anything containing any of the strings defined in the rule  
`all of them` | The rule will only match if all of the defined strings are in the content  
`3 of them` | The rule will match anything containing **_at least_** three of the defined strings  
`$a and 3 of ($s*)` |  Match content that contains string `$a` and _**at least**_ three strings whose variable begins with `$s`  
  
## Practical examples

It would be very useful to check the attachments of suspected phishing emails
reported to you by your users. PDF attachments with a link to a phishing site
have become a common tactic, because many email gateways still do not check
URLs in attached files. This rule checks for links in PDFs:

```yara
rule pdf_1.7_contains_link {

meta:
  author = "Sean Whalen"
  last_updated = "2017-06-08"
  tlp = "white"
  category = "informational"
  confidence = "high"
  description = "A PDFv1.7 that contains a link or external content"

strings:
  $pdf_magic = {25 50 44 46}
  $s_anchor_tag = "<a " ascii wide nocase
  $s_uri = /\(http.+\)/ ascii wide nocase

condition:
  $pdf_magic at 0 and any of ($s*)
}
```

The first part of the condition checks if the first few bytes of the file
match the [magic
numbers](https://en.wikipedia.org/wiki/Magic_number_\(programming\)#Magic_numbers_in_files)
([list here](https://en.wikipedia.org/wiki/List_of_file_signatures)) for a
PDF, allowing the rule to quickly disregard anything that isn't a PDF. Filters
like these can greatly increase speed when scanning a large amount of data.
The second part of the condition strings whose variable begins with `$s`.

`$s_uri` is a regular expression that matches any URI/URL in parenthesis,
which will match the PDF standard for URI actions and URLs in forms.

`$s_anchor_tag` matches any HTML anchor tag, which some PDF converters may
leave an a document converted from HTML.

The `ascii`, `wide` , and `nocase` keywords tell YARA to search for ASCII and
wide strings, and to be case-insensitive. By default, it will only search for
ASCII strings, including substrings, and it will be case-sensitive. There are
many more keywords for matching other kinds of strings.

But lots of legitimate PDFs (brochures, invoices, etc) contain links, so a
better indicator of badness may be a PDF that contains a single link.
Unfortunately, most PDF generators like Microsoft Office will save the PDF as
multiple "versions"  in the same file, so we should give the rule a little
flexibility, and allow for up to two URIs in a PDF.

```yara
rule pdf_1.7_contains_few_links {

meta:
  author = "Sean Whalen"
  last_updated = "2017-06-08"
  tlp = "white"
  category = "malicious"
  confidence = "medium"
  killchain_phase = "exploit"
  description = "A PDFv1.7 that contains one or two links - a common phishing tactic"

strings:
  $pdf_magic = {25 50 44 46}
  $s_anchor_tag = "<a " ascii wide nocase
  $s_uri = /\(http.+\)/ ascii wide nocase

condition:
  $pdf_magic at 0 and (#s_anchor_tag == 1 or (#s_uri > 0 and #s_uri < 3))
}
```

It's good to keep both of these rules, that way you have an informational one
that should always match on any PDF with any number of links, and another that
provides a higher confidence of badness.

Also, these rules only match PDFs with links that were generated according to
the latest PDF standard (1.7). Any suggestions for older versions are
appreciated.

## Viewing strings in a file

To view a list of strings in a file, simply run the `strings` command on a
Linux/MacOS/BSD or other UNIX-like system. You can pipe the output to `less`
to view it one page at a time. For example:

```bash
strings rat.exe | less
```

## Strings vs Bytes

the `strings` section in YARA rules can be made up of any combination of
strings, bytes, and regular expressions. Most YARA rules are made up entirely
of strings. These kinds of rules are relatively simple to write, but it is
also very easy for malware authors to change or obscure strings in order to
avoid detection in future builds. If a sample has few or no usable strings,
that sample has likely been packed, meaning that any strings are built or
decoded at runtime. YARA can scan processes, and you probably would have
better luck scanning active memory for strings, but that won't help if your
goal is to identify samples at rest.

Bytes in YARA are represented as hexadecimal strings, and can include
wildcards and/or jumps. Bytes can be used to identify specific variations of
code, such as a unique method of unpacking. Writing signatures based on bytes
requires some knowledge of assembly, APIs provided by the OS, and specialized
software.

IDA Pro is the [industry standard platform](https://www.hex-
rays.com/products/ida/) for software reverse engineering. It is also [very
expensive](https://www.hex-rays.com/products/ida/order.shtml). Currently, a
the Starter Edition of IDA (which can only process 32 bit files) for one named
user, along with the X86 Hex-Rays decompiler costs about $2,700. If you want
to be able to decompile x86 AMD64 files, the cost is about $4,400 for IDA Pro,
x86, and x64 compilers for one named user. Fortunately, a couple open source
alternatives exist.

In early 2019, the NSA released an open source Software Reverse Engineering
(SRE) suite called [Ghidra](https://ghidra-sre.org/). It includes a
decomplier, and a very simillar feel to IDA.

The open source Radare Framework provides [many of the same
features](http://www.radare.org/r/cmp.html) of IDA (and a few more) for free,
under a GNU GPL license. Radare does not currently have a decomplier though.

If you're new to assembly, check out this [Crash Course in x86 Assembly for
Reverse
Engineers](https://sensepost.com/blogstatic/2014/01/SensePost_crash_course_in_x86_assembly-.pdf).

## Testing YARA rules

To test your rules against some sample files, run a command like this:

```bash
yara -rs dev/yararules/files.yar samples/pdf
```

Where `dev/yararules/files.yar` is the path to the file containing your rules
and `samples/pdf` is the path to a directory containing sample files to test
against. This will output a list of files matches, and the strings that make
up each match.

To find samples that do not match your rules, run a command like this:

```bash
yara -rn dev/yararules/files.yar samples/pdf
```

Note that this will give a a result for each rule that each file does not
match. Use grep to narrow this down. For example, if you only wanted to see
the results for rules with a name that contains `pdf_`, you could run:

```bash
yara -rs dev/yararules/files.yar samples/pdf | grep pdf_
```

It's good practice to keep your rule names consistent. That makes testing much
easier.

## Generating rules

yarGen is an open source utility by Florian Roth that generates YARA rules for
a given set of samples. It's not magic, and generally won't do a better than
writing a rule manually. But, if you are mostly making rules out of strings
rather than bytes, it can give you a great starting point to tweak and tune
into a better rule. I use yarGen when I've some across a set of samples that I
know are related, but have seemingly very different strings.

yarGen will generate many different rules for a given set of files, and the
condition for each rule will likely be very narrow (i.e. all of them). I
usually combine these rules based on what I suspect are the most reliable
strings, and group the strings as needed in the condition statement.

You can download yarGen from its [GitHub
repository](https://github.com/Neo23x0/yarGen).

## Learning more

Take some time to review the comprehensive [official
documentation](https://yara.readthedocs.io/) for YARA. There, you will find
complete details on writing rules, and using the command-line program, the
Python API, and the C API.

Once you feel comfortable working with YARA, consider joining the YARA
[Exchange](http://www.deependresearch.org/2012/08/yara-signature-exchange-
google-group.html). The Exchange is a very active and helpful group of
information security professionals that share rules and tips for writing them.
You can even get access to VirusTotal Intelligence for free through the
exchange, if your company doesn't already pay for it.  In return, they only
ask that you participate, share with others, and don't hog the VirusTotal
Intelligence monthly quotas that are shared across the whole group.

With VirusTotal Intelligence access, you can set up alerts to notify you when
samples are uploaded to VirusTotal that match your YARA rules, without using
any quotas. It's a fantastic way to stress test your rules (your inbox/alert
queue will fill up very quickly if you match false-positives), and for
identifying new samples, and new waves of attacks. Quotas are used for
searching, downloading, and using Retro Hunt on VirusTotal Intelligence. Retro
Hunt takes a set of YARA rules, runs a scan on about the last three months of
all files that were uploaded to VirusTotal (literally terabytes of data), and
returns a list of file hashes that matched your rules, and which rules they
matched.

Check out this great talk on getting the most out of VirusTotal Intelligence
and YARA by Wyatt Roersma at GrrCon 2016:

### Books

* [Practical Malware Analysis](https://www.nostarch.com/malware)
* [Malware Analyst's Cookbook](http://www.wiley.com/WileyCDA/WileyTitle/productCd-0470613033.html)

### Other resources

* [Public rule repository](https://github.com/Yara-Rules/rules)
* [YARA for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=infosec-intern.yara)
* [Atom editor package](https://atom.io/packages/language-yara) for YARA syntax highlighting
