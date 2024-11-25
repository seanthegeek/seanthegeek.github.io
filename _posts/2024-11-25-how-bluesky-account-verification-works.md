---
layout: post
title: How Bluesky account verification works
description: The account verification method on Bluesky is simple simple and transparent – but it comes with some major drawbacks
image:
  path: /assets/images/bluesky-logo.webp
  alt: The Bluesky logo
categories: ["Guides"]
tags: ["Bluesky"]
date: 2024-11-25 10:35 -0500
---

Starting out, all Bluesky account handles end with `.bsky.social`. News organizations, businesses, non-profits, politicians, lawyers, celebrities, podcast hosts, bloggers, and others often have official websites that are easy to recognize. Bluesky allows any user that owns a domain name (e.g., `example.com`) or subdomain to use that domain name as their account handle. The result is easily identifiable [verified accounts](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial) like [@wyden.senate.gov](https://bsky.app/profile/wyden.senate.gov), [@cnn.com](https://bsky.app/profile/cn.com), [@npr.org](https://bsky.app/profile/npr.org), [@washingtonpost.com](https://bsky.app/profile/washingtonpost.com), [@arstechnica.com](https://bsky.app/profile/arstechnicia.com).

To do this, all you or whoever manages your domain/website need to do is prove that you control the domain or subdomain in a way that a computer can verify. It only takes a few minutes to do and it is fully automated. That said, there are some disadvantages.

## Advantages

1. It is transparent: The methodology is open.
2. It is equal for all: No one decides if you are notable enough to have a verified account.
3. It respects privacy: No Personally Identifiable Information (PII) is exchanged or stored.
4. It is self-service: Accounts can be verified in minutes.
5. Subdomains can be used to verify an individual's relationship to an organization.

## Disadvantages

### Changing a handle leaves your old handle open for squatting

The Bluesky verification guide [warns](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial):

> If you change your default Bluesky username (with the .`bsky.social suffix`) to a website URL, your old username will be available for someone else to use. However, any tags or mentions with your old handle will still point to your account. If you'd like to keep your old `.bsky.social` username, we recommend creating a second account to hold that username.

Not an ideal situation.

### Your Bluesky handle will no longer match your X handle

After Elon started charging $100/month for X API access, X migration tools had to switch from using the X API to using a browser extention that pages though a list on the `following` page, where profile data can be truncated.

Migration tools like the Sky follower Bridge search for matching accounts based on an X handle ending with `.bsky.social`. If your Bluesky account handle does not match your X handle. the author of Sky Follower Bridge [recommends](https://github.com/kawamataryo/sky-follower-bridge/issues/64) making sure the display names at least match so it can still find your account that way.

### Lookalike domains

Someone could register a domain that is similar to the official one using a typo or a different TLD (e.g., `example.net` instead of `example.com`) and use that as a Bluesky account handle. Most organizations already register typos of their domains to prevent this sort of abuse, but individuals might not. Users should do a quick web search to find the user's actual website if they are suspicious or unsure.

### Not everyone has their own website

Mark Hamill is an example of a celebrity who does not have his own website, so Bluesky's account verification method won't work for him. [As he has pointed out](https://bsky.app/profile/markhamillofficial.bsky.social/post/3lbpyd7qbkc2z), a lot of accounts are impersonating him on Bluesky.

## How to verify your account

In Bluesky, go to Settings> Account> Handle, then click “I have my own domain”. Two different methods can be used.

### DNS-based verification

DNS based verification requires the ability to add a `TXT` record to the domain the DNS records for the domain. This method is selected by default.

### File-based identification

This method requires you to add a file to a specific location on your website with specific content. This is useful for if you have a website on a subdomain of a domain that you do not control, such as a congressional website or GitHub Pages.
