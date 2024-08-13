---
layout: post
status: publish
published: true
title: How to forward a forensic copy of an email as an attachment
description: Step-by-step instructions on how to many popular mail and webmail clients to properly forward emails as attachments with forensic headers intact
permalink: /862/how-to-forward-a-forensic-copy-of-an-email-as-an-attachment/
image:
  path: /assets/images/stack-of-mail.jpg
wordpress_id: 862
wordpress_url: https://seanthegeek.net/?p=862
date: '2019-08-28 00:36:19 +0000'
date_gmt: '2019-08-28 00:36:19 +0000'
categories:
- Information Security
- How-to Guides
tags:
- email
- forensics
comments:
- id: 4204
  author: abc

  author_url: ''
  date: '2020-06-25 06:44:29 +0000'
  date_gmt: '2020-06-25 06:44:29 +0000'
  content: tried yahoo mail. it works. thanks man!
- id: 4670
  author: Coco M.

  author_url: ''
  date: '2020-11-07 00:13:53 +0000'
  date_gmt: '2020-11-07 00:13:53 +0000'
  content: Used the yahoo mail instructions with great success.  Very simply and understandable
    instructions, though being VERY low tech., I had to research "text editor".
- id: 4846
  author: Suzana Correa

  author_url: ''
  date: '2020-12-12 16:51:04 +0000'
  date_gmt: '2020-12-12 16:51:04 +0000'
  content: Sean - I followed your yahoo instructions and I'm wondering what you're
    talking about. The text attachment comes in as a messy text. You think people
    want to read that? If there is no solution, then don't post one.
- id: 5028
  author: Doris L corea

  author_url: ''
  date: '2021-01-11 22:36:37 +0000'
  date_gmt: '2021-01-11 22:36:37 +0000'
  content: How do I send an attachment of a spoofed email from my yahoo email app!
    I have no computer. I only have my iPhoneXR. In this case it&rsquo;s a spoofed
    Walmart email in my yahoo app inbox.
- id: 5317
  author: Cecilia

  author_url: ''
  date: '2021-03-23 08:18:44 +0000'
  date_gmt: '2021-03-23 08:18:44 +0000'
  content: perfect for yahoo mail. Thank you
- id: 5486
  author: Paul Roetter

  author_url: ''
  date: '2021-05-20 20:58:12 +0000'
  date_gmt: '2021-05-20 20:58:12 +0000'
  content: "Suzana,\r\n\r\nSpeaking as a cybersecurity expert and cyber forensic professional...
    what you see as \"messy text\" is the meat and potatoes of what we do for a living.\r\n\r\nThose
    of us who do cyber security, as well as programmers and other computer experts,
    can make perfect sense out of that \"messy text\", and it allows us to determine
    where the email is trying to re-direct you to, and what other malicious activity
    it might want to cause on your system.\r\n\r\nTo paraphrase your last line...
    \"If you don't know what you're talking about, you should probably keep quiet.\""
- id: 5974
  author: Premnath

  author_url: ''
  date: '2021-07-26 11:41:45 +0000'
  date_gmt: '2021-07-26 11:41:45 +0000'
  content: Works perfectly for Yahoo mail. I wonder how much of learning and research
    you must have done to give solutions for different applications !!! Great work.
- id: 7575
  author: Ovidiu

  author_url: ''
  date: '2022-07-05 13:44:02 +0000'
  date_gmt: '2022-07-05 13:44:02 +0000'
  content: "Finally a solution for the Yahoo mail!\r\nThank you very much!"
- id: 8054
  author: Simon H

  author_url: ''
  date: '2022-10-23 12:18:19 +0000'
  date_gmt: '2022-10-23 12:18:19 +0000'
  content: "Fantastic! I've been trying to figure out how to export original/forensic
    e-mails from Yahoo Mail to the MS Outlook client on Win10 since Yahoo disabled
    creation of app passwords for new POP/SMTP connections months ago.\r\n\r\nI knew
    I could view each raw message but not that saving as a .eml file would allow such
    files to be opened directly from disk by the Outlook client, with no need to forward
    anything.\r\n\r\nThank you so much!"
- id: 9543
  author: John Corkren

  author_url: ''
  date: '2024-03-13 18:48:52 +0000'
  date_gmt: '2024-03-13 18:48:52 +0000'
  content: I'm a little late here, but good response, this one goes on the wall,  for
    all to read.
---
<p><!-- wp:tadv/classic-paragraph --></p>
<p>If you receive a fraudulent email, can be very useful to send a full forensic copy to an organization that is being spoofed, industry partners, and law enforcement.</p>
<p>When a user clicks forward in a mail client, the client copies the message's content and attachments to a new message. The original <a href="https://seanthegeek.net/861/how-to-view-email-headers/">message headers</a> are <strong>not</strong> included.</p>
<p>In order to send a full forensic sample that includes the original message headers, the original message must be sent as an attachment in a new message. The process for doing this varies by mail client.<!--more--></p>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>AOL webmail</h2>
<ol>
<li>In the list of emails in your in inbox or folder, right click on the message (not in the message itself)</li>
<li>Click View Message Source</li>
<li>Select the entire raw message content, copy it, paste it into an empty text editor, and save the file with a .eml file extension</li>
<li>Attach the file to a new email, and send it</li>
</ol>
<h2>Apple Mail on macOS</h2>
<ol>
<li>Right click on the message in the list of messages</li>
<li>Click Forward as Attachment</li>
<li>Fill in the To field, and click send</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>Gmail/Google Workspace webmail</h2>
<ol>
<li>Open the message</li>
<li>Click on the three vertical dots in the upper right</li>
<li>Click Show original</li>
<li>Click Download Original, save it, and send it as an attachment in a new message</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>GoDaddy and Rackspace webmail</h2>
<ol>
<li>Open the message you want to forward. To forward multiple emails, instead of opening an email, use the checkboxes to select the emails you want to forward.</li>
<li>In the top right corner of the page, click the <strong>More Actions</strong> menu.</li>
<li>Select <strong>Fwd. as Attachment</strong>.</li>
<li>Click <strong>Apply</strong>. A new email is created with a <code>.eml</code> file attached.</li>
<li>When the rest of the message is ready to go, click <strong>Send</strong>.</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>GroupWise</h2>
<ol>
<li>From the GroupWise item list, select the e-mail(s) you wish to forward (multiple messages can be selected with Shift-Click, Ctrl-Click, etc.)</li>
<li>Select the Action Menu</li>
<li>From the Action Menu, select the "Forward As Attachment" Item</li>
<li>Fill in the To field, and click Send</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>Notes</h2>
<ol>
<li>Open the email</li>
<li>Save it to a file by going to the File > Save As menu item</li>
<li>Attach the file to a new email and send it</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>Outlook.com/Office 365 webmail</h2>
<ol>
<li>Open the web mail in two browser windows</li>
<li>Create a new email in one browser window</li>
<li>In the other browser window, drag the email you want to attach from your email list, and drop it in the blank email</li>
<li>Fill out the To field, and click send</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>Outlook for macOS</h2>
<ol>
<li>In the messages list, right click the message you want to forward</li>
<li>Click Forward As Attachment</li>
<li>Fill in the To field, and click Send</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>Outlook for Windows</h2>
<ol>
<li>Create a new email</li>
<li>Drag the message you want to forward from the messages list and drop it in the blank message body</li>
<li>Fill in the To field, and click Send</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>ProtonMail webmail</h2>
<ol>
<li>Open the message you want to forward</li>
<li>Click on the down arrow, to the tight of the forward button</li>
<li>Click Export, and save the <strong>decrypted</strong> email</li>
<li>Create a new email, and add the exported email as an attachment</li>
<li>Fill out the To field, and click send</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>Thunderbird</h2>
<ol>
<li>In the messages list, right click on the message you want to forward (or select multiple messages and then right click)</li>
<li>Select Forward as attachment</li>
<li>Fill in the To field and click Send</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>Windows 10 Mail app</h2>
<ol>
<li>Open the message</li>
<li>Click on the three horizontal dots in the upper right</li>
<li>Click Save As, and save the email as a file</li>
<li>Attach the saved file to a new email, fill in the To field, and click send</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<h2>Yahoo webmail</h2>
<ol>
<li>Open the the message</li>
<li>Click on the three horizontal dots in the upper right, and click View Raw Message</li>
<li>Select the entire raw message content, copy it, paste it into an empty text editor, and save the file with a .eml file extension</li>
<li>Attach the file to a new email, and send it</li>
</ol>
<p><!-- /wp:tadv/classic-paragraph --></p>
