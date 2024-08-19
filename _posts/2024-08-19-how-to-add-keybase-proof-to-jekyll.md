---
layout: post
title: how-to-add-keybase-proof-to-jekyll
date: 2024-08-19 09:19 -0400
title: How to add a Keybase proof to a Jekyll static website
description: Adding a Keybase proof to a Jekyll site is easy once you know how
  to do it
image:
  path: /assets/images/keybase-logo.webp
categories:
  - Guides
tags:
  - Keybase
  - Jekyll
---

I got an email that the Keybase proof for this blog broke because I forgot to
copy over `keybase.txt` from my old web server before I deleted it. So I had to
revoke the old proof in Keybase, create the new proof in Keybase, and add that
proof to my Jekyell blog. If you still have a copy of your existing
`keybase.txt` file, you can reuse that proof instead of revoking it and
generating a new one.

## Revoke the old Keybase proof if needed

1. View your profile on the Keybase website
2. Click on `https` next to your blog domain and click revoke
3. Select command line with `keybase` and click continue
4. Use the provided `keybase` command in a terminal or Powershell prompt to revoke the key

## Generate a new Keybase proof

Run

```text
keybase prove web https://example.com
```

Replace `example.com` with the actual domain name of your website.

This will generate a new proof. **Keep the window open.**

## Add the Keybase proof to Jekyll

Create a new file at the root of your Jekyll project called `keybase.txt`.
Add the following content to that file:

```yaml
---
layout: none
permalink: /.well-known/keybase.txt
---
```

Then, copy and pase the copy and paste the `keybase` command under this.
Save the file, then push the changes to your Jekyll site. After a few minutes,
you should receive an email from Keybase stating that your web proof just
succeeded.
