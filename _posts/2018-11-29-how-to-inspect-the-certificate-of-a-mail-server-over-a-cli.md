---
layout: post
permalink: /562/how-to-inspect-the-certificate-of-a-mail-server-over-a-cli
title: How to inspect the certificate of a mail server over a CLI
description: A tiny guide to using the openssl CLI tool to inspect and/or save the
  SSL.TLS certificates used by mail servers
date: 2018-11-29 23:17:15 -0000
publish: true
pin: false
categories:
- How-To Guides
tags: []
---
If you ever need to inspect the certificate of a remote SMTP server, you can use the `openssl` CLI tool.

If you need to check `STARTTLS`:

```bash
openssl s_client -connect mail.example.com:25 -starttls smtp
```

Or, for a standard secure SMTP port:

```bash
openssl s_client -connect mail.example.com:465
```

To save the certificate to a file, just redirect the output:

```bash
openssl s_client -connect mail.example.com:25 -starttls smtp > mail.example.com.crt
```

You can also check SMTP TLS using [MX Toolbox](<https://mxtoolbox.com/diagnostic.aspx>) or [Check TLS](<https://www.checktls.com/TestReceiver>).
