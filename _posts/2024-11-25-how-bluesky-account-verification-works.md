---
layout: post
title: How Bluesky account verification works
description: Account verification on Bluesky is different, yet simple and transparent
image:
  path: /assets/images/bluesky-logo.webp
  alt: The Bluesky logo
categories: ["Guides"]
tags: ["Bluesky"]
date: 2024-11-25 10:35 -0500
---

Starting out, all Bluesky account handles end with `.bsky.social`. News organizations, businesses, non-profits, politicians, lawyers, celebrities, podcast hosts, bloggers, and others all have official websites that are easy to recognize. Bluesky allows any user that owns a domain name (e.g., `example.com`) or subdomain to use that domain name as their account handle. The result is easily identifiable [verified accounts](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial) like [@wyden.senate.gov](https://bsky.app/profile/wyden.senate.gov), [@cnn.com](https://bsky.app/profile/cn.com), [@npr.org](https://bsky.app/profile/npr.org), [@washingtonpost.com](https://bsky.app/profile/washingtonpost.com), [@arstechnica.com](https://bsky.app/profile/arstechnicia.com).

To do this, all you or whoever manages your domain/website need to do is prove that you control the domain or subdomain in a way that a computer can verify. It only takes a few minutes to do and it is fully automated.

## Advantages

1. It is transparent: The methodology is open.
2. It is equal for all: No one decides if you are notable enough to have a verified account.
3. It respects privacy: No Personally Identifiable Information (PII) is exchanged or stored.
4. It is self-service: Accounts can be verified in minutes.
5. Subdomains can be used to verify an individual's relationship to an organization.

## Disadvantages

### Switching a handle leaves your old handle open for squatting

Once your handle is changed to a domain the old `.bsky.social` handle is free for anyone to take over.

## Your handle will no longer match your X handle

Many X to Bluesky migration tools will search for matching accounts based on your X handle ending with `.bsky.social`.

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
