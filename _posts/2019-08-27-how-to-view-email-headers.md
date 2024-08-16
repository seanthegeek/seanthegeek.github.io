---
layout: post
permalink: /861/how-to-view-email-headers
title: How to view email headers
description: Step by step instructions for viewing email message headers using popular
  mail clients and webmail services, including Outlook, Gmail, and more.
date: 2019-08-27 21:41:51 -0000
last_modified_at: 2022-01-19 20:46:22 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2019/08/email-headers-screenshot.png
  alt: A screenshot of email headers
categories:
- Information Security
- How-to Guides
tags:
- email
- forensics
---
Email headers contain very useful information for tracing a message's origin
and troubleshooting its delivery. Email headers are written with the oldest
headers at the bottom, and the newest headers at the top. By reading the
headers in the correct order, you can see how the message was passed from one
mail server to another, and the actions each mail server took along the way.

Most email clients have a function to display a message's headers. The exact
steps depends on the client.

## AOL webmail

  1. In the list of emails in your in inbox or folder, right click on the message (not in the message itself)
  2. Click View Message Source

The message headers are located at the top of the message source.

## Apple Mail on macOS

  1. Select the message or open it
  2. In the Menu Bar, click View> Message > All Headers

## Gmail/G Suite webmail

  1. Open the message
  2. Click on the three vertical dots in the upper right
  3. Click Show original

The message headers are located at the top part of the message source, under
the Copy to clipboard button.

## GoDaddy and Rackspace webmail

  1. Open the message
  2. From the **More Actions** drop down list, select View Full Header, and then click Apply

## GroupWise

  1. Open the message
  2. In the message window select: File > Attachments > View
  3. Select the Mime.822 attachment

The message headers are located at the top of the message source.

## Notes

  1. In Notes 6.x, open the email document. For Notes 5.x, open your inbox.
  2. In Notes 6.x, from the menu, select View/Show Page Source. In Notes 5.x, highlight the message.
  3. Select File> Export.
  4. Type a file name, leave the type as Structured Text, and click Export.
  5. In the dialog box, select Selected Documents and click OK.
  6. Open the file in a text editor, such as [Visual Studio Code](https://code.visualstudio.com/).

The message headers are located at the top of the message source.

## Outlook.com/Office 365 webmail

  1. Open the message
  2. Click on the three horizontal dots in the upper right
  3. Scroll down in the menu, and click show message details

## Outlook for macOS

  1. Right click on the message in the list of messages
  2. Click View Source

The message headers are located at the top of the message source.

## Outlook for Windows

  1. Open the message
  2. Click File
  3. Under the Info category click on the Properties button.

The headers are listed as "Internet headers"

## ProtonMail mobile app

  1. Open the message
  2. Tap on the three dots in the upper right
  3. Tap on View Headers

## ProtonMail webmail

  1. Open the message
  2. Click on the down arrow, to the tight of the forward button
  3. Click view headers

## Thunderbird

  1. Open the message
  2. Click on the three vertical dots in the upper right
  3. Click view message source

The message headers are located at the top of the message source.

## Windows 10 Mail app

  1. Open the message
  2. Click on the three horizontal dots in the upper right
  3. Click Save As, and save the email as a file
  4. Open the file in a text editor, such as [Visual Studio Code](https://code.visualstudio.com/)

The message headers are located at the top of the mail file.

## Yahoo webmail

  1. Open the the message
  2. Click on the three horizontal dots in the upper right, and click View Raw Message
