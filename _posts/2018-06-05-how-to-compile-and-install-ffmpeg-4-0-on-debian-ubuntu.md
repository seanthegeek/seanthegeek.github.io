---
layout: post
status: publish
published: true
title: How to compile and install FFmpeg on Debian/Ubuntu
permalink: /455/how-to-compile-and-install-ffmpeg-4-0-on-debian-ubuntu
wordpress_id: 455
wordpress_url: https://seanthegeek.net/?p=455
date: '2018-06-05 00:26:08 +0000'
date_gmt: '2018-06-05 00:26:08 +0000'
categories:
- How-to Guides
tags:
- build guide
- ffmpeg
- open source
- video transcoding
comments:
- id: 549
  author: Walid
  author_url: ''
  date: '2018-07-05 13:04:05 +0000'
  date_gmt: '2018-07-05 13:04:05 +0000'
  content: This saved my life. Thanks
- id: 642
  author: Larry Hammer
  author_url: ''
  date: '2018-08-07 13:20:34 +0000'
  date_gmt: '2018-08-07 13:20:34 +0000'
  content: "this doesn't work for debian 8\r\nges/mysite/Build/aom# cmake aom/\r\nCMake
    Error at CMakeLists.txt:11 (cmake_minimum_required):\r\n  CMake 3.5 or higher
    is required.  You are running version 3.0.2\r\n\r\n\r\n-- Configuring incomplete,
    errors occurred!"
- id: 774
  author: Mike Perkinson
  author_url: ''
  date: '2018-10-03 20:24:39 +0000'
  date_gmt: '2018-10-03 20:24:39 +0000'
  content: "I tried this on an Ubuntu 18.04 and during the Build stage, the make fails:\r\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\r\nCC\tlibavcodec/lclenc.o\r\nCC\tlibavcodec/libaomdec.o\r\nCC\tlibavcodec/libaomenc.o\r\nlibavcodec/libaomenc.c:703:109:
    error: &lsquo;AOM_ERROR_RESILIENT_PARTITIONS&rsquo; undeclared here (not in a
    function); did you mean &lsquo;AOM_ERROR_RESILIENT_DEFAULT&rsquo;?\r\n                          \"
    is still done over the partition boundary.\",       0, AV_OPT_TYPE_CONST, {.i64
    = AOM_ERROR_RESILIENT_PARTITIONS}, 0, 0, VE, \"er\"},\r\n                                                                                                             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\r\n
    \                                                                                                            AOM_ERROR_RESILIENT_DEFAULT\r\nffbuild/common.mak:60:
    recipe for target 'libavcodec/libaomenc.o' failed\r\nmake: *** [libavcodec/libaomenc.o]
    Error 1\r\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\r\nJust thought
    I would pass it on."
- id: 787
  author: Feli
  author_url: ''
  date: '2018-10-12 10:36:25 +0000'
  date_gmt: '2018-10-12 10:36:25 +0000'
  content: I have the same issue as Mike Perkinson in Ubuntu 16.04
- id: 788
  author: Feli
  author_url: ''
  date: '2018-10-12 10:37:34 +0000'
  date_gmt: '2018-10-12 10:37:34 +0000'
  content: Did you solve the problem?
- id: 789
  author: Feli
  author_url: ''
  date: '2018-10-12 10:44:38 +0000'
  date_gmt: '2018-10-12 10:44:38 +0000'
  content: 'This commit solves the problem: https://git.videolan.org/?p=ffmpeg.git;a=commitdiff;h=b69ea742ab23ad74b2ae2772764743642212a139'
- id: 825
  author: IanB
  author_url: ''
  date: '2018-10-29 14:08:01 +0000'
  date_gmt: '2018-10-29 14:08:01 +0000'
  content: "Even after apply the patch I cannot get to compile\r\n\r\n/usr/bin/ld:
    /usr/local/lib/libaom.a(aom_config.c.o): relocation R_X86_64_32 against `.rodata.str1.8'
    can not be used when making a shared object; recompile with -fPIC\r\n/usr/local/lib/libaom.a:
    error adding symbols: Bad value\r\ncollect2: error: ld returned 1 exit status\r\nffbuild/library.mak:102:
    recipe for target 'libavcodec/libavcodec.so.58' failed\r\nmake: *** [libavcodec/libavcodec.so.58]
    Error 1"
- id: 827
  author: Ian Blakeley
  author_url: ''
  date: '2018-10-30 09:21:15 +0000'
  date_gmt: '2018-10-30 09:21:15 +0000'
  content: Tried using the latest snapshot, exactly the same issue.
- id: 831
  author: Yaroslav Udovenko
  author_url: ''
  date: '2018-11-02 15:49:35 +0000'
  date_gmt: '2018-11-02 15:49:35 +0000'
  content: try to update to latest aom. works on november builds
- id: 832
  author: Ian Blakeley
  author_url: ''
  date: '2018-11-04 06:24:40 +0000'
  date_gmt: '2018-11-04 06:24:40 +0000'
  content: "I got aom again, cloned git but still it is the same as before. I can
    compile the latest snapshot manually following  https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu
    or using the scripts from https://github.com/rdp/ffmpeg-windows-build-helpers
    but not the relase branch.\r\n\r\nFor now I can stick with snapshot"
- id: 837
  author: Guillermo
  author_url: ''
  date: '2018-11-14 15:21:03 +0000'
  date_gmt: '2018-11-14 15:21:03 +0000'
  content: "When I'm trying to compile ffmpeg, I have this error\r\n\r\nnasm/yasm
    not found or too old. Use --disable-x86asm for a crippled build.\r\n\r\nIf you
    think configure made a mistake, make sure you are using the latest\r\nversion
    from Git.  If the latest version fails, report the problem to the\r\nffmpeg-user@ffmpeg.org
    mailing list or IRC #ffmpeg on irc.freenode.net.\r\nInclude the log file \"ffbuild/config.log\"
    produced by configure as this will help\r\nsolve the problem."
- id: 863
  author: Herbert Nachtnebel
  author_url: ''
  date: '2018-12-07 04:24:46 +0000'
  date_gmt: '2018-12-07 04:24:46 +0000'
  content: "I solved this compile error with adding the PIC compile flag to the aom
    library, try this patch in directory ffmpegtemp/aom/aom:\r\n\r\ndiff --git a/build/cmake/compiler_flags.cmake
    b/build/cmake/compiler_flags.cmake\r\nindex 79192c1fa..ec8d214a5 100644\r\n---
    a/build/cmake/compiler_flags.cmake\r\n+++ b/build/cmake/compiler_flags.cmake\r\n@@
    -17,6 +17,9 @@ include(CheckCCompilerFlag)\r\n include(CheckCXXCompilerFlag)\r\n
    include(\"${AOM_ROOT}/build/cmake/compiler_tests.cmake\")\r\n \r\n+set(AOM_EXTRA_C_FLAGS
    \"-fPIC\")\r\n+\r\n # Strings used to cache flags.\r\n set(AOM_C_FLAGS)\r\n set(AOM_CXX_FLAGS)"
- id: 868
  author: Rebecca
  author_url: ''
  date: '2018-12-10 01:43:48 +0000'
  date_gmt: '2018-12-10 01:43:48 +0000'
  content: "I ran into this problem as well. After I ran this I got farther:\r\nsudo
    apt install nasm"
- id: 1362
  author: Daniel
  author_url: ''
  date: '2019-03-27 07:27:59 +0000'
  date_gmt: '2019-03-27 07:27:59 +0000'
  content: "compile aom with option:\r\n\r\ncmake aom/ -DAOM_EXTRA_C_FLAGS=-fPIC\r\n\r\nworked
    for me."
- id: 1582
  author: erflungued
  author_url: ''
  date: '2019-04-25 12:38:25 +0000'
  date_gmt: '2019-04-25 12:38:25 +0000'
  content: "I solved the ffmpeg issue with aom by compiling aom as a shared library:\r\n
    \ cmake aom/ -DBUILD_SHARED_LIBS=1\r\nas per (aom/README.md)"
- id: 1583
  author: erflungued
  author_url: ''
  date: '2019-04-25 13:23:01 +0000'
  date_gmt: '2019-04-25 13:23:01 +0000'
  content: "..then after running ldconfig:\r\nerflungued@minty:~/src/ffmpegtemp/ffmpeg-4.1.3$
    make check\r\nworked fine.\r\nThanks for this tute @Sean"
- id: 1600
  author: Jane
  author_url: ''
  date: '2019-04-29 08:17:35 +0000'
  date_gmt: '2019-04-29 08:17:35 +0000'
  content: "After removing libavcodec I ended up in command line on boot.\r\nLooks
    like libs from this custom ffmpeg package were not linked properly. Any suggestions
    how to fix?"
- id: 1638
  author: kano kan
  author_url: ''
  date: '2019-05-07 03:28:28 +0000'
  date_gmt: '2019-05-07 03:28:28 +0000'
  content: "I'm stuck there too... really wish someone answered with a solution. Google
    isn't helping much... =/\r\n\r\nLD      libavcodec/libavcodec.so.58\r\n/usr/bin/ld:
    /usr/local/lib/libaom.a(noise_model.c.o): relocation R_X86_64_PC32 against symbol
    `stderr@@GLIBC_2.2.5' can not be used when making a shared object; recompile with
    -fPIC\r\n/usr/bin/ld: final link failed: Bad value\r\ncollect2: error: ld returned
    1 exit status\r\nffbuild/library.mak:102: recipe for target 'libavcodec/libavcodec.so.58'
    failed\r\nmake: *** [libavcodec/libavcodec.so.58] Error 1"
- id: 1639
  author: aco
  author_url: ''
  date: '2019-05-07 03:50:03 +0000'
  date_gmt: '2019-05-07 03:50:03 +0000'
  content: Thank you for this very helpful comment!
- id: 1775
  author: Roel Van de Paar
  author_url: ''
  date: '2019-05-31 05:46:01 +0000'
  date_gmt: '2019-05-31 05:46:01 +0000'
  content: "1) Small typo in instructions; \r\n--enable-small--enable-avisynth \r\nshould
    read:\r\n--enable-small --enable-avisynth\r\n2) git clone ...\r\ncan be \r\ngit
    clone --depth=1 ...\r\nto avoid unecessary repo history\r\n3) aom: for this error:
    \"relocation R_X86_64_PC32 against symbol `stderr@@GLIBC_2.2.5' can not be used
    when making a shared object; recompile with -fPIC\" the following works:\r\n delete
    ffmpegtemp directory, take all same steps for aom again, but change;\r\ncmake
    aom/\r\nto;\r\ncmake aom/ -DAOM_EXTRA_C_FLAGS=-fPIC \r\nthen just go back to ffmpeg
    directory and type make again, build will complete\r\n4) Latest: https://ffmpeg.org/releases/ffmpeg-4.1.3.tar.gz\r\n\r\nEnjoy
    &amp; God bless"
- id: 1792
  author: vanya
  author_url: ''
  date: '2019-06-03 15:07:19 +0000'
  date_gmt: '2019-06-03 15:07:19 +0000'
  content: "HI, \r\n\r\nI have this warning:\r\n\r\n/usr/bin/ld: warning: libavcodec.so.57,
    needed by /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libchromaprint.so,
    may conflict with libavcodec.so.58\r\n/usr/bin/ld: warning: libavutil.so.55, needed
    by /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libchromaprint.so,
    may conflict with libavutil.so.56\r\n/usr/bin/ld: warning: libswresample.so.2,
    needed by //usr/lib/x86_64-linux-gnu/libavcodec.so.57, may conflict with libswresample.so.3\r\n\r\n\r\nThen:\r\nsupport@Bench-PC-01:~/ffmpegtemp/ffmpeg-4.0$
    ffmpeg \r\nffmpeg: error while loading shared libraries: libavdevice.so.58: cannot
    open shared object file: No such file or directory"
- id: 2030
  author: ricardo
  author_url: https://www.ricardosabino.com
  date: '2019-07-11 04:39:34 +0000'
  date_gmt: '2019-07-11 04:39:34 +0000'
  content: "Hi,\r\n\r\nI have the exact same problem mentioned above regarding not
    being able to open libavdevice.so.58\r\n\r\nAny suggestions?\r\nThank you."
- id: 2031
  author: ricardo
  author_url: https://www.ricardosabino.com
  date: '2019-07-11 04:48:36 +0000'
  date_gmt: '2019-07-11 04:48:36 +0000'
  content: Nevermind, I think "make install" did the trick.
- id: 2821
  author: FrancisGo
  author_url: ''
  date: '2019-11-10 23:14:06 +0000'
  date_gmt: '2019-11-10 23:14:06 +0000'
  content: What a pain in the lower rear... Can anybody provide an Ubuntu build with
    all the non-free stuff and VAAPI/GPU-encoding included?  (or even a Windows EXE
    to run in Wine, that would be super practical and straight forward...)
- id: 4572
  author: john dougherty
  author_url: ''
  date: '2020-10-13 00:20:12 +0000'
  date_gmt: '2020-10-13 00:20:12 +0000'
  content: "wow!  thank you Sean - this went very well.\r\n\r\njust one little fix
    on the page formatting: at installing the dependencies \r\n\"sudo apt-get -y install
    build-essential autoconf automake ...\\\"\r\n\r\nthere is white space after each
    backslash so if we paste the whole block in at the prompt it wants to checkinstall
    nasm - not the intended consequence!\r\n\r\nthe ./configure block is clear of
    any trailing white space and works as intended."
- id: 4625
  author: Aresrin
  author_url: ''
  date: '2020-10-24 20:45:11 +0000'
  date_gmt: '2020-10-24 20:45:11 +0000'
  content: "I've been using linux for a couple years, but am still a novice, after
    a bunch of headaches, here are my notes from my install on MX linux 19 \r\n----------------------------------------------------------------------------------------------------------------------\r\n1.
    Before you start, you have to have to add MX Linux's AHS repository:\r\n\r\nLaunch
    synaptic package manager > settings > Repositories > New, then enter \r\nBinary:
    deb\r\nURI: https://mxrepo.com/mx/repo/\r\nDistribution: buster ahs\r\nClick OK\r\nCheck
    the Enabled box next to the new https://mxrepo.com/mx/repo/ entry\r\n\r\nor you
    run into a bunch of dependency errors when you try to install libsdl2-dev.\r\n----------------------------------------------------------------------------------------------------------------------\r\n2.
    Before you get to the installing libmysofa you have to install yasm by running:\r\n\r\nsudo
    apt get yasm\r\n\r\nor you'll get an error\r\n----------------------------------------------------------------------------------------------------------------------\r\n3.
    Running \"git clone https://github.com/hoene/libmysofa\" creates a folder called
    \"libmysofa\" not \"mysopha\", so after it finishes downloading run:\r\n\r\ncd
    libmysofa\r\n\r\ninstead of \"cd mysopha\"\r\n----------------------------------------------------------------------------------------------------------------------\r\n4.
    after running \"sudo dpkg -i *.deb\" in the mysofa run\r\n\r\ncd ..\r\n\r\ninstead
    of \"cd..\" because it's missing a space and so won't move up the directory.\r\n----------------------------------------------------------------------------------------------------------------------\r\n5.
    Before configuring the ffmpeg build you have to run: \r\n\r\nsudo apt install
    libdrm-dev\r\n\r\notherwise you get an error saying that the pkg can't find it.
    (added to the list below)\r\n----------------------------------------------------------------------------------------------------------------------\r\n6.
    When installing the long list of dependencies and running the ffmegpeg configuration
    MX Linux will ignore all the commands after the first  \\, so remove all of them
    and enter them as one long list instead:\r\n\r\nsudo apt-get -y install build-essential
    autoconf automake cmake libtool git checkinstall nasm yasm libass-dev libfreetype6-dev
    libsdl2-dev p11-kit libva-dev libvdpau-dev libvorbis-dev libxcb1-dev libxcb-shm0-dev
    libxcb-xfixes0-dev pkg-config texinfo wget zlib1g-dev libchromaprint-dev frei0r-plugins-dev
    gnutls-dev ladspa-sdk libcaca-dev libcdio-paranoia-dev libcodec2-dev libfontconfig1-dev
    libfreetype6-dev libfribidi-dev libgme-dev libgsm1-dev libjack-dev libmodplug-dev
    libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libopenjp2-7-dev libopenmpt-dev
    libopus-dev libpulse-dev librsvg2-dev librubberband-dev librtmp-dev libshine-dev
    libsmbclient-dev libsnappy-dev libsoxr-dev libspeex-dev libssh-dev libtesseract-dev
    libtheora-dev libtwolame-dev libv4l-dev libvo-amrwbenc-dev libvorbis-dev libvpx-dev
    libwavpack-dev libwebp-dev libx264-dev libx265-dev libxvidcore-dev libxml2-dev
    libzmq3-dev libzvbi-dev liblilv-dev libopenal-dev opencl-dev libjack-dev libdrm-dev\r\n\r\n./configure
    --enable-gpl --enable-version3 --disable-static --enable-shared --enable-small
    --enable-avisynth --enable-chromaprint --enable-frei0r --enable-gmp --enable-gnutls
    --enable-ladspa --enable-libaom --enable-libass --enable-libcaca --enable-libcdio
    --enable-libcodec2 --enable-libfontconfig --enable-libfreetype --enable-libfribidi
    --enable-libgme --enable-libgsm --enable-libjack --enable-libmodplug --enable-libmp3lame
    --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopencore-amrwb
    --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librsvg
    --enable-librubberband --enable-librtmp --enable-libshine --enable-libsnappy --enable-libsoxr
    --enable-libspeex --enable-libssh --enable-libtesseract --enable-libtheora --enable-libtwolame
    --enable-libv4l2 --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack
    --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libxml2
    --enable-libzmq --enable-libzvbi --enable-lv2 --enable-libmysofa --enable-openal
    --enable-opencl --enable-opengl --enable-libdrm --enable-nonfree --enable-libfdk-aac
    --enable-libbluray\r\n----------------------------------------------------------------------------------------------------------------------\r\nThanks
    for the guide, hopefully this will help others if they run into the same issues."
- id: 5179
  author: hiter1996
  author_url: ''
  date: '2021-02-23 06:24:09 +0000'
  date_gmt: '2021-02-23 06:24:09 +0000'
  content: how to configure 'const char *filter_descr' in https://github.com/FFmpeg/FFmpeg/blob/master/doc/examples/filtering_video.c
    to use atadenoise to do video processing in ffmepg
- id: 5462
  author: fatemeh karimi
  author_url: ''
  date: '2021-05-13 20:46:40 +0000'
  date_gmt: '2021-05-13 20:46:40 +0000'
  content: I was trying to compile ffmpeg for three days and I failed every time.
    this tutorial was a savior. thank you very much.
- id: 8326
  author: Capitalmind
  author_url: ''
  date: '2023-03-13 18:42:28 +0000'
  date_gmt: '2023-03-13 18:42:28 +0000'
  content: Very grateful for this guide. I would love to see it updated to include
    'all codecs' and cuda support for GPU processing. Am attempting to combine your
    guide with https://www.cyberciti.biz/faq/how-to-install-ffmpeg-with-nvidia-gpu-acceleration-on-linux/
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
