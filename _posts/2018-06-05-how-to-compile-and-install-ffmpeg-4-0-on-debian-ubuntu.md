---
layout: post
permalink: /455/how-to-compile-and-install-ffmpeg-4-0-on-debian-ubuntu
title: How to compile and install FFmpeg on Debian/Ubuntu
description: A guide to building and installing FFmpeg 4,0 from source as a custom
  Debian package on Debian/Ubuntu systems, without conflicting with downstream dependencies
date: 2018-06-05 00:26:08 -0000
last_modified_at: 2019-10-08 02:15:18 -0000
publish: true
pin: false
categories:
- How-to Guides
- Journal
tags:
- build guide
- ffmpeg
- open source
- video transcoding
---
Here's how to build and install FFmpeg from source with all the bells and
whistles (i.e codec support).  We'll install it as a custom Debian package
using `checkinstall`. That way, any other package that depends on the `ffmpeg`
package will recognize that it is already installed, and won't try to fetch it
from the Debian or Ubuntu software repositories.

## Install the dependencies

```bash
sudo apt-get -y install build-essential autoconf automake cmake libtool git
checkinstall

mkdir ffmpegtemp
cd ffmpegtemp

mkdir aom
cd aom
git clone https://aomedia.googlesource.com/aom
cmake aom/ -DBUILD_SHARED_LIBS=1
make
sudo checkinstall -y --deldoc=yes --pkgversion=1.0.0
cd ..

git clone https://github.com/hoene/libmysofa
cd mysopha
cd build
cmake ..
cd build
cpack
sudo apt-get remove libmysopha0 libmysopha-dev
sudo dpkg -i *.deb
cd..

sudo apt-get -y install build-essential autoconf automake cmake libtool git \      
checkinstall nasm yasm libass-dev libfreetype6-dev libsdl2-dev p11-kit \           
libva-dev libvdpau-dev libvorbis-dev libxcb1-dev libxcb-shm0-dev \                 
libxcb-xfixes0-dev pkg-config texinfo wget zlib1g-dev libchromaprint-dev \         
frei0r-plugins-dev gnutls-dev ladspa-sdk libcaca-dev libcdio-paranoia-dev \        
libcodec2-dev libfontconfig1-dev libfreetype6-dev libfribidi-dev libgme-dev \      
libgsm1-dev libjack-dev libmodplug-dev libmp3lame-dev libopencore-amrnb-dev \      
libopencore-amrwb-dev libopenjp2-7-dev libopenmpt-dev libopus-dev \                
libpulse-dev librsvg2-dev librubberband-dev librtmp-dev libshine-dev \             
libsmbclient-dev libsnappy-dev libsoxr-dev libspeex-dev libssh-dev \               
libtesseract-dev libtheora-dev libtwolame-dev libv4l-dev libvo-amrwbenc-dev \      
libvorbis-dev libvpx-dev libwavpack-dev libwebp-dev libx264-dev libx265-dev \      
libxvidcore-dev libxml2-dev libzmq3-dev libzvbi-dev liblilv-dev \    
libopenal-dev opencl-dev libjack-dev
```

Install the non-free dependencies too, if you want to convert decrypted Blu-
Ray content:

```bash
sudo apt-get -y install libbluray-dev libfdk-aac-dev

## Download and extract the FFmpeg source code

```bash
wget https://ffmpeg.org/releases/ffmpeg-4.2.1.tar.bz2
tar -xf ffmpeg-4.2.1.tar.bz2
rm ffmpeg-4.2.1.tar.bz2
cd ffmpeg-4.2.1
```

## Configure the build

### With free dependencies only

```bash
./configure --enable-gpl --enable-version3 --disable-static --enable-shared --enable-small --enable-avisynth --enable-chromaprint --enable-frei0r --enable-gmp --enable-gnutls --enable-ladspa --enable-libaom --enable-libass --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librsvg --enable-librubberband --enable-librtmp --enable-libshine --enable-libsmbclient --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtesseract --enable-libtheora --enable-libtwolame --enable-libv4l2 --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libxml2 --enable-libzmq --enable-libzvbi --enable-lv2 --enable-libmysofa --enable-openal --enable-opencl --enable-opengl --enable-libdrm
```

### Or, including non-free

```bash
./configure --enable-gpl --enable-version3 --disable-static --enable-shared --enable-small --enable-avisynth --enable-chromaprint --enable-frei0r --enable-gmp --enable-gnutls --enable-ladspa --enable-libaom --enable-libass --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librsvg --enable-librubberband --enable-librtmp --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtesseract --enable-libtheora --enable-libtwolame --enable-libv4l2 --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libxml2 --enable-libzmq --enable-libzvbi --enable-lv2 --enable-libmysofa --enable-openal --enable-opencl --enable-opengl --enable-libdrm --enable-nonfree --enable-libfdk-aac --enable-libbluray
```

## Build

```bash
make
```

## Purge any existing package installation

```bash
sudo apt-get -y purge ffmpeg "libav*" " libpostproc*"
sudo apt-get -y autoremove
```

## Install your custom FFmpeg build as a package

```bash
sudo checkinstall -y --deldoc=yes --pkgversion=10:4.2.1
cd ..
rm -rf ffmpegtemp
```
