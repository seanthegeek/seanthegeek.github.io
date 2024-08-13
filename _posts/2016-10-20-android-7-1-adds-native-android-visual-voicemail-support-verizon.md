---
layout: post
status: publish
published: true
title: Android 7.1 adds native android visual voicemail support for Verizon
permalink: /174/android-7-1-adds-native-android-visual-voicemail-support-verizon
description: No more cryptic text messages when getting Verizon voicemails on Nexus devices. Android 7.1 adds support for Verizon visual voicemail in the native dialer.
image:
  path: /assets/images/mailboxes.jpg
wordpress_id: 174
wordpress_url: https://seanthegeek.net/?p=174
date: '2016-10-20 16:37:38 +0000'
date_gmt: '2016-10-20 16:37:38 +0000'
categories:
- Consumer devices
tags:
- Visual Voicemail
- Android 7.1
- Nexus
- Verizon
comments:
- id: 23
  author: DaveH
  author_url: ''
  date: '2016-12-07 17:31:03 +0000'
  date_gmt: '2016-12-07 17:31:03 +0000'
  content: Yes - Basic Voicemail feature on Nexus 6P running 7.1.1 will not work.
    Dialing *86 and the phone will hang up. You have to switch your VZW account to
    the free Basic Visual Voice Mail or the Premium Visual Voice Mail with TEXT.  You
    might want to add this bit of info to your article.
- id: 26
  author: Sean Whalen

  author_url: ''
  date: '2016-12-11 18:35:03 +0000'
  date_gmt: '2016-12-11 18:35:03 +0000'
  content: Done. Thanks!
---
After upgrading my Nexus 6P on Verizon to the Android 7.1.1 beta, I discovered
that Visual Voicemail in the native Android dialer works! You just need to
make sure that that basic (free) or premium visual voicemail is active on your
line. Voicemail-to-text works too, if you add Premium Visual Voicemail to your
line. Unfortunately, there is no sign of Wi-Fi calling support (yet?). HD
voice has always worked on the Nexus 6P.

When I first switched my Nexus 6P to from T-Mobile to Verizon, I noticed that
support for native visual voicemail in the Android dialer was missing. Worse,
I was getting cryptic text messages instead of the usual basic voicemail
notification.

A blog post from [Matt Cutts](https://www.mattcutts.com/blog/verizon-visual-
voicemail-texts/) describes this situation in detail. It turns out the text
messages are somehow used in the background by Verizon's proprietary visual
voicemail application. That application is not available to Nexus devices on
the Google Play store like the My Verizon app is. So the only solution to get
regular voicemail notifications working on Nexus devices was to have a Verizon
rep switch your line to basic voicemail. This option is different that basic
visual voicemail, which is on your line by default.

In an age of texting and messaging apps, loosing visual voicemail might not
seem like a big deal to most consumers, but I've found that the voicemail to
text feature is extremely useful when I need to discreetly check voicemails
from businesses and doctor's offices while on the go or at work. It's also
indispensable for those who are hearing impaired.  I wondered how Verizon and
Google were going to do Visual Voicemail on the Pixel phones, since Verizon's
Visual Voicemail app is not on [the
list](https://www.reddit.com/r/Android/comments/561wpq/google_pixel_preloaded_apps_including_some/)
of installed Verizon apps. Now we know.

[![A screenshot of the Verizon Wireless Premium Visual Voicemail welcome
message in the Android 7.1 Dialer on a Nexus 6P](/assets/images/vzw-vvm-android.png)](/assets/images/vzw-vvm-android.png)

Also, the Support tab in Settings is there, as seen on the Pixel phones.

[![A screenshot of the settings app in Android 7.1 on a Nexus 6P, showing the
support tab first seen on the Google Pixel
phones](/assets/images/android-7.1.1-settings.png)](/assets/images/android-7.1.1-settings.png)

~~This was one of the features that I thought was Pixel exclusive. It's nice
to see it included.~~   Hopefully ~~more~~ features from the Pixel phones like
the [Google Assistant](https://assistant.google.com/) will make their way to
Nexus devices over the next few months. That would go a long way towards
soothing the [outrage](https://www.androidpolice.com/2016/10/06/its-time-to-
talk-about-google-the-pixel-phones-and-feelings-of-abandonment/) of many Nexus
owners who feel left behind. It would certainly be in Google's long-term
interest to put the assistant in the hands of as many Android users as
possible once it has full integration with third party services.

**Update** : Unfortunately, the day after this post was published, Google
updated [Google Support
Services](https://play.google.com/store/apps/details?id=com.google.android.apps.helprtc)
that remove the phones and chat support buttons for Nexus devices :(

[![A screenshot of the support tab in settings as seen on a Nexus 5X after the
Google Support Services
update](/assets/images/nexus-5X-support.png)](/assets/images/nexus-5X-support.png)

You can get Android 7.1.1 on a Nexus device right now by signing up for the
[Android Beta](https://www.google.com/android/beta). It's actually very
stable, and I think it's snappier than 7.0.

My Google Pixel XL is due to arrive today. I'll have a full review here next
week.

Featured image by [Andrew Taylor](https://flic.kr/p/9Gkunr). Used under a [CC
BY 2.0](https://creativecommons.org/licenses/by/2.0/) license.
