---
layout: post
title: How to verify your Jekyll site on Bluesky
description: Your Jekyll site can be used to verify your identify on Bluesky or other platforms that use the AT Protocol
image:
  path: /assets/images/jekyll-bluesky.webp
  alt: The Jekyll and Bluesky logos
date: 2024-11-23 10:08 -0500
categories: ["Guides"]
tags: ["Jekyll", "Bluesky", "AT Protocol"]
---

Bluesky has emerged as the [leading alternative](https://www.forbes.com/sites/anishasircar/2024/11/21/bluesky-vs-x-can-the-decentralized-platform-dethrone-elon-musks-x-twitter/) to Elon Musk's X (formerly known as Twitter). Users can verify control of an internet domain or subdomain and use that as their Bluesky username. That way, news organizations, businesses, government entities, and high-profile individuals can have verified profiles. Bluesky [describes it](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial) as "our version of a 'blue check.'". Examples of verified profiles include [@npr.org](https://bsky.app/profile/npr.org), [@wyden.senate.gov](https://bsky.app/profile/wyden.senate.gov), or anyone else with control of a domain or subdomain, [like me](https://bsky.app/profile/seanthegeek.net).

To use a domain name or subdomain as your Bluesky username, navigate to Settings> Account> Handle, then click "I have my own domain". Fill in your domain or subdomain. "DNS panel" is selected by default. This method requires you to add a `TXT` resource record to the domain's DNS zone at `_atproto` with specific content, which isn't helpful in situations where you don't own the domain, such as `github.io`.

![A screenshot of the Bluesky DNS verification prompt](/assets/images/bluesky-dns-verification.webp)

> Use subdomains to give each employee/volunteer representing your organization their own verified account
{: .prompt-tip}

Select "No DNS panel" to switch to the file verification method. This simply requires you to have file at `/.well-known/atproto-did` with specific content that is accessible over HTTPS. That way, you can verify use of a domain or subdomain without needing the control the domain's DNS zone. This works with GitHub Pages sites hosted on subdomains of `github.io`. Even though I have my own domain and could use the DNS method, I prefer the file method because it's easer than logging into my DNS provider to add a record, and it seems a little more transparent to include it in my GitHub repository.

![A screenshot of the Bluesky file verification prompt](/assets/images/bluesky-file-verification.webp)

To add this file on a Jekyll site, create a new file in the root of your project. The file can have any name, but it must **not** have any file extension. On my site I used `bluesky` to remind myself that this file is for Bluesky verification, so I don't accidentally delete it. Add the following content to the top of the file.

```markdown
---
layout: none
permalink: /.well-known/atproto-did
---
```

This bit of [front matter](https://jekyllrb.com/docs/front-matter/) tells Jekyll two things: `layout: none` says to not use any layout template, and `permalink: /.well-known/atproto-did` tells Jekyll to host the file exactly where Bluesky expects it.

Place the content given by Bluesky at the bottom of this file. Save the file and push your changes. Then click the "Verify Text File" button on Bluesky.

> You can add verification strings from multiple AT Protocol servers to the same file, one per line.
{: .prompt-tip}

Your Bluesky username will now be your domain name or subdomain.
