---
layout: post
permalink: /862/how-to-forward-a-forensic-copy-of-an-email-as-an-attachment
title: How to forward a forensic copy of an email as an attachment
seo_title: How to forward email as an attachment - seanthegeek.net
description: Step-by-step instructions on how to many popular mail and webmail clients
  to properly forward emails as attachments with forensic headers intact
date: 2019-08-28 00:36:19 -0000
last_modified_at: 2022-01-19 20:50:36 -0000
publish: true
pin: false
image:
  path: /assets/wp-content/uploads/2019/08/stack-of-mail.webp
categories:
- How-to Guides
- Information Security
tags:
- email
- forensics
---
If you receive a fraudulent email, can be very useful to send a full forensic copy to an organization that is being spoofed, industry partners, and law enforcement.

When a user clicks forward in a mail client, the client copies the message's content and attachments to a new message. The original [message headers](<https://seanthegeek.net/861/how-to-view-email-headers/>) are **not** included.

In order to send a full forensic sample that includes the original message headers, the original message must be sent as an attachment in a new message. The process for doing this varies by mail client.

## AOL webmail

  1. In the list of emails in your in inbox or folder, right click on the message (not in the message itself)
  2. Click View Message Source
  3. Select the entire raw message content, copy it, paste it into an empty text editor, and save the file with a .eml file extension
  4. Attach the file to a new email, and send it

## Apple Mail on macOS

  1. Right click on the message in the list of messages
  2. Click Forward as Attachment
  3. Fill in the To field, and click send

## Gmail/Google Workspace webmail

  1. Open the message
  2. Click on the three vertical dots in the upper right
  3. Click Show original
  4. Click Download Original, save it, and send it as an attachment in a new message

## GoDaddy and Rackspace webmail

  1. Open the message you want to forward. To forward multiple emails, instead of opening an email, use the checkboxes to select the emails you want to forward.
  2. In the top right corner of the page, click the **More Actions** menu.
  3. Select **Fwd. as Attachment**.
  4. Click **Apply**. A new email is created with a `.eml` file attached.
  5. When the rest of the message is ready to go, click **Send**.

## GroupWise

  1. From the GroupWise item list, select the e-mail(s) you wish to forward (multiple messages can be selected with Shift-Click, Ctrl-Click, etc.)
  2. Select the Action Menu
  3. From the Action Menu, select the "Forward As Attachment" Item
  4. Fill in the To field, and click Send

## Notes

  1. Open the email
  2. Save it to a file by going to the File > Save As menu item
  3. Attach the file to a new email and send it

## Outlook.com/Office 365 webmail

  1. Open the web mail in two browser windows
  2. Create a new email in one browser window
  3. In the other browser window, drag the email you want to attach from your email list, and drop it in the blank email
  4. Fill out the To field, and click send

## Outlook for macOS

  1. In the messages list, right click the message you want to forward
  2. Click Forward As Attachment
  3. Fill in the To field, and click Send

## Outlook for Windows

  1. Create a new email
  2. Drag the message you want to forward from the messages list and drop it in the blank message body
  3. Fill in the To field, and click Send

## ProtonMail webmail

  1. Open the message you want to forward
  2. Click on the down arrow, to the tight of the forward button
  3. Click Export, and save the **decrypted** email
  4. Create a new email, and add the exported email as an attachment
  5. Fill out the To field, and click send

## Thunderbird

  1. In the messages list, right click on the message you want to forward (or select multiple messages and then right click)
  2. Select Forward as attachment
  3. Fill in the To field and click Send

## Windows 10 Mail app

  1. Open the message
  2. Click on the three horizontal dots in the upper right
  3. Click Save As, and save the email as a file
  4. Attach the saved file to a new email, fill in the To field, and click send

## Yahoo webmail

  1. Open the the message
  2. Click on the three horizontal dots in the upper right, and click View Raw Message
  3. Select the entire raw message content, copy it, paste it into an empty text editor, and save the file with a .eml file extension
  4. Attach the file to a new email, and send it
