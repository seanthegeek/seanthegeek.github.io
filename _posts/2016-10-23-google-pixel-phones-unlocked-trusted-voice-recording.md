---
layout: post
status: publish
published: true
title: Google Pixel phones can be unlocked with a recording of a trusted voice by
  default
permalink: /190/google-pixel-phones-unlocked-trusted-voice-recording
description: 'When Trusted Voice is enabled on Google Pixel phones by default, allowing anyone with a recording of you saying "Ok Google" to unlock your phone.'
image:
  path: /assets/images/Trusted-Voice-Warning.png
wordpress_id: 190
wordpress_url: https://seanthegeek.net/?p=190
date: '2016-10-23 21:04:41 +0000'
date_gmt: '2016-10-23 21:04:41 +0000'
categories:
- Information Security
tags:
- Privacy
- Google Assistant
- Android
- Google Pixel
- Trusted Voice
comments: []
---
The headline feature of the new Google Pixel phones is deep integration
between the operating system and the [Google
Assistant](https://assistant.google.com/one-assistant/) AI. By default, the
Google Assistant can be activated even when the phone is locked and the
display is off, if the device hears the trusted voice say the hot word, "Ok
Google". This also has the effect of unlocking the device, meaning that anyone
with a recording of the trusted voice saying "Ok Google" -- or even someone
with a similar voice -- can easily unlock the device.

I recorded myself saying "Ok Google", and played it back while screencasting
my Google Pixel using [AllCast
Receiver](https://chrome.google.com/webstore/detail/allcast-
receiver/hjbljnpdahefgnopeohlaeohgkiidnoe) and [AllCast
Mirror](https://play.google.com/store/apps/details?id=com.koushikdutta.mirror&hl=en)
(since I don't have a tripod to record the phone itself.)  I cranked up the
volume on studio monitor speakers at my desk to ensure that the phone would
hear it for the demo; but if you wanted to break into a device discreetly, you
could use a small digital recorder or phone to play back the recording much
closer to the device, allowing for a very quiet volume.

## Trusted Voice

The ability to use "Ok, Google" to unlock a device use Google voice commands
is called Trusted Voice. It has actually been around for as long as "Ok
Google" itself. The difference with the Pixel phones is Trusted Voice is
enabled by default. This allows you to work with the Google Assistant from
across the room. Convenient to be sure, but it is also a substantial privacy
and security risk. If you manually enable Trusted Voice when it is disabled,
you will receive a warning about these risks, as shown in the featured image
of this post. If there was a warning about this during the initial setup of
the phone, I missed it in the excitement of setting up a new device.

To disable Trusted Voice, tap on the G logo in the upper-left of the Pixel
Launcher, then tap it again in the search bar. Tap on the menu icon in the
upper-left, the tap Settings, Voice "Ok Google" Detection, and turn off the
Trusted Voice switch.

[![A screenshot of ok google detection settings](/assets/images/ok-google-detection-
settings-e1477328370884)](/assets/images/ok-google-detection-
settings-e1477328370884.png)

## Trade-offs

With Trusted Voice off, your device will prompt you to unlock it before taking
any action if if hears you say "Ok Google" while the device is locked. It
would be nice if Google had settings to let the user ask general, non-personal
questions, or make phone calls with Trusted Voice disabled and the device is
locked. That's the way it works when giving voice commands on a Blutetooth
headset. The upcoming [Google Home](https://madeby.google.com/home/) will give
some convenience without having to use Trusted Voice on your phone.  For now
though, you'll have to choose between the convince of talking to your phone
from across a room, or having a decently secure device.
