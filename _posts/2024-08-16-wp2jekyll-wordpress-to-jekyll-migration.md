---
layout: post
title: "Introducing wp2jekyll: A new way to migrate from WordPress to Jekyll"
description: Download your media, convert your content to Markdown, and keep
  your SEO optimizations with one Python script
date: 2024-08-16 20:50 -0400
image:
  path: /assets/images/wordpress-python-jekyll.webp
categories:
  - Guides
tags:
  - WordPress
  - Python
  - Jekyll
---

A few days ago, I wrote [a post](https://seanthegeek.net/posts/my-painful-but-worthwhile-migration-from-wordpress-to-jekyll/) about what I did
to migrate from my WordPress blog to this Jekyll blog. The process was, in a
word: manual. The Jekyll importer tools don't convert the post content to
Markdown, some don't download media files, and if they do, they don't update
the locations of the media in your content. Third-party importers crashed or
used obsolete dependencies. But I have good news. After getting a better
understanding of Jekyll, I wrote the WordPress to Jekyll export tool
I was looking for: [wp2jekyll](https://github.com/seanthegeek/wp2jekyll).

wp2jekyll is a Python 3 script that takes care of the details of migrating so
you don't have to. All you need to do is install its dependencies and give it
a WordPress export XML file that can be generated from the tools menu of the
WordPress admin interface. Then, wp2jekyll will download all media files from
WordPress, convert posts and pages to Markdown, and update the related media
URLs in your content to matching relative URLs. It will even write the Front
Data of each post or page so that it retains key SEO details, such as the
permalink, a featured image with `alt` text, and a `meta` description from
the popular Yoast SEO WordPress plugin.

**Update**: Here's a comparison to the [Jekyll Exporter](https://wordpress.org/plugins/jekyll-exporter/) WordPress plugin.

I tried using that plugin but it [crashed](https://github.com/benbalter/wordpress-to-jekyll-exporter/issues/319) on me. Since I haven't actually used that plugin, I can't say for sure, but a quick glance at its [source code](https://github.com/benbalter/wordpress-to-jekyll-exporter/blob/5333f4bbb71519361e0b79a2056a9d3d8acfd6d9/jekyll-exporter.php#L3) seems to show a few key things wp2jekyll does better than the WordPress plugin.

* By default, wp22jekyll will retain the existing permalink of posts and pages, so incoming links don't break.
* Rather than just dumping all WordPress post metadata to YAML in the Front Data, wp2jekyll only retains items useful for SEO (i.e, the featured image and Yoast metadata), and maps them to variable names that are expected by many Jekyll themes. This makes the Front Data much cleaner and useful.
* By default, wp2jekyll adjusts image/attachment URLs to be relative to the `assets` directory. I don't think the WordPress plugin does that.
* wp2jekyll keeps a copy of the original post HTML outside of the Jekyll build path so you can look at that in case the Markdown conversion botched some content.

Please give it a try and give me some feedback. I welcome bug reports, feature
requests, and pull requests.
