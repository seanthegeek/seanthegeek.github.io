---
layout: post
status: publish
published: true
title: How to inspect the certificate of a mail server over a CLI
permalink: /how-to-inspect-the-certificate-of-a-mail-server-over-a-cli
wordpress_id: 562
wordpress_url: https://seanthegeek.net/?p=562
date: '2018-11-29 23:17:15 +0000'
date_gmt: '2018-11-29 23:17:15 +0000'
categories:
- Information Security
- How-To Guides
tags: []
comments:
- id: 876
  author: Montana

  author_url: ''
  date: '2018-12-16 07:46:02 +0000'
  date_gmt: '2018-12-16 07:46:02 +0000'
  content: Many thanks for this post, really helped me. :)
---
<p><!-- wp:paragraph --></p>
<p>If you ever need to inspect the certificate of a remote SMTP server, you can use the <code>openssl</code> CLI tool.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>If you need to check <code>STARTTLS</code>:</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:preformatted --></p>
<pre class="wp-block-preformatted">openssl s_client -connect mail.example.com:25 -starttls smtp</pre>
<p><!-- /wp:preformatted --></p>
<p><!-- wp:paragraph --></p>
<p>Or, for a standard secure SMTP port:</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:preformatted --></p>
<pre class="wp-block-preformatted">openssl s_client -connect mail.example.com:465</pre>
<p><!-- /wp:preformatted --></p>
<p><!-- wp:paragraph --></p>
<p>To save the certificate to a file, just redirect the output:</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:preformatted --></p>
<pre class="wp-block-preformatted">openssl s_client -connect mail.example.com:25 -starttls smtp > mail.example.com.crt</pre>
<p><!-- /wp:preformatted --></p>
<p><!-- wp:tadv/classic-paragraph --></p>
<p>You can also check SMTP TLS using <a href="https://mxtoolbox.com/diagnostic.aspx" target="_blank" rel="noopener noreferrer">MX Toolbox</a> or <a href="https://www.checktls.com/TestReceiver" target="_blank" rel="noopener noreferrer">Check TLS</a>.</p>
<p><!-- /wp:tadv/classic-paragraph --></p>
