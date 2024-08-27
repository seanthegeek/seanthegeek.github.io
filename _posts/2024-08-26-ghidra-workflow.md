---
layout: post
title: Ghidra workflow
date: 2024-08-26 18:37 -0400
description: My workflow when using Ghidra, plus tips to fix common issues.
image:
  path: /assets/images/ghidra-logo.webp
categories:
  - Reverse Engineering Malware
tags:
  - Ghidra
---

> This guide assumes that you have followed my [Ghidra setup guide](/posts/ghidra-setup-guide).
{: .prompt-info}

## Automatic function data type annotation

You should see these entries in Data Table Manager window:

- `ntddk_32`
- `ntddk_64`
- `winapi_32`
- `winapi_64`

Right click on the API that matches your sample (i.e. 32 or 64 bit), and click
"Apply Function Data Types". After that, click on the Listing window, then click
on the Analysis menu, and select
One Shot> WindowsPE x86 Propagate External Parameters.

The function parameters in calls to known Windows will be identified in the code
listing as comments.

![A call to HttpSendRequestA without Propagate External Parameters applied](/assets/images/before-propagate-external-parameters.webp)
_A call to HttpSendRequestA without Propagate External Parameters applied_

![A call to HttpSendRequestA with Propagate External Parameters applied](/assets/images/after-propagate-external-parameters.webp)
_A call to HttpSendRequestA with Propagate External Parameters applied_

## Run CAPA

Navigate to Window> Script Manager, and filter on `capa`. Run the
`capa_explorer.py` script by double clicking on it, and point it to the
directory containing your CAPA rules.

This will generate a new Namespace in the Symbol Tree called `capa`, which
will help you identify interesting functions.

![A screenshot of the Symbols Tree Window in Ghidra](/assets/images/capa-symbol-tree.webp)
_The Ghidra Symbol Tree after `capa_explorer.py` was ran on a sample of Locky_

## Navigate to API calls

To get a listing of API calls used in a sample,
Select Window> Symbol references. Imported functions appear in red. If you want,
you can set a filter to display only imported functions. To do this, click on
the gear icon in the top-right of the Symbol Table's title bar Uncheck every
Symbol Source except Imported, and click ok.

Click on an API name to see a list of instances where that API is mentioned.
Look for instances with an Access type of Call. Double click on the From
Location cell of that row to navigate to that specific call in the Listing
window.

![A screenshot of the Symbol references window](/assets/images/ghidra-symbol-references.webp)
_The Symbol References window inside the Ghidra CodeBrowser_

## Function call trees

Function call trees list function calls used within the current function, and
all functions that call the current function. To view it,
select Window> Function Call Tree.

![A screenshot of Ghidra Function Call Trees](/assets/images/ghidra-function-call-trees.webp)
_Function call trees for a reconnaissance function in a sample of Locky ransomware_

## Symbolic constants

Symbolic constants are human-friendly strings that are converted to specific
hex values at compile time. For example, this Locky sample passes
`0x80000001` as the `hKey` parameter when calling `RegOpenKeyExA`.

![A screenshot of a call to RegOpenKeyExA](/assets/images/ghidra_hkey_hex.webp)
_0x80000001 isn't very human friendly_

To convert a hex value back to its human friendly symbolic constant, right click
on it, and click Set Equate, or press `E`. This will bring up a list of
matching symbolic constants from across different libraries to select from.

![A screenshot of the Set Equate Window in Ghidra](/assets/images/ghidra_set_equate.webp)
_Sometimes the correct value is obvious_

If you know the API call well, you might not need to look up which value in the
Set Equate list to use. If you don't know, you can always check the
documentation.

Microsoft's [documentation](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regopenkeyexa#parameters)
for `RegOpenKeyExA` states the `hKey` parameter
must be either `HKEY_CLASSES_ROOT` `HKEY_CURRENT_CONFIG` `HKEY_CURRENT_USER`
`HKEY_LOCAL_MACHINE` or `HKEY_USERS`.

So in this case, from the options in the Set Equate list, the only value that
is valid is `HKEY_CURRENT_USER`.

![A screenshot of the code with the hex value replaced by the symbolic constant](/assets/images/ghidra_hkey_symboloic_constant.webp)
_Much more human friendly!_

## Setting data types

Sometimes Ghidra will get the data type of a structure wrong. For example:

When calling `HttpOpenRequestA`, `lpszVerb` is a pointer to a string of the
HTTP verb to use when making the request.

![Screenshot of an HttpOpenRequestA call in Ghidra](/assets/images/ghidra-httpopenrequesta-call.webp)

However, after double clicking on the pointer, we can see that the data type is not defined.

![Screenshot of lpszVerb as an undefined datatype](/assets/images/ghidra-lpszverb-before.webp)

We know from Microsoft's documentation that this value should be a string. Set
the data type by right clicking the `DAT_` reference, and select Data> String.
The corrected datatype will now be reflected.

![Screenshot of lpszVerb as a string datatype](/assets/images/ghidra-lpszverb-after.webp)

And when mousing over the pointer in the function.

![Screenshot of lpszVerb as a string datatype mousing over](/assets/images/ghidra-lpszverb-after-mouseover.webp)
