+++
title = "Introduction to 3G network"
date = "2009-04-05T05:57:00Z"
slug = "introduction-to-3g-network"
canonicalURL = "https://netherlandsdaniel.blogspot.com/2009/04/introduction-to-3g-network.html"
bloggerID = "771316999248406169"
tags = ["Computer", "Mobile"]
[cover]
  image = "/images/blogger/771316999248406169/3413966068_b518685f39.jpg"
+++

[![Introduction to 3G network.png](/images/blogger/771316999248406169/3413966068_b518685f39.jpg)](http://www.flickr.com/photos/plateau/3413966068/ "Introduction to 3G network.png by plateaukao, on Flickr")  
  

It's a shame not knowing common knowledge of 3G networks while working in a mobile phone manufacturer. Well, Obviously, some people do not think so. Here's the brief outline of radio network change: from first generation to 2G, 2.5G, and 3G. Although 4G is coming on its way, knowing current technologies will help catching up the new ones.

- Introduction to 3G network
  - History
    - 1G
      - NMT (Nordic Mobile Telephone)
        - NMT-450
        - NMT-900
          - International Roaming is possible
        - Scandinavia, Ecntral and Southern Europe
      - TACS (Total Access Communications System)
        - UK standard, based on AMPS
        - 900 MHz
      - AMPS (Advanced Mobile Phone Service)
        - US standard
        - 800 MHz
      - MCS
        - NTT: first cellular network in Japan
    - 2G
      - Feature
        - use digital radio transmission for traffic
        - basic GSM uses 900 MHz
        - 1800 MHz
      - GSM (Global System for Mobile communications)
        - Most successful and widely used 2G system
        - TDMA
      - D-AMPS (digital AMPS)
        - US-TDMA, IS-136, or just TDMA
      - CDMA IS-95 (Code-division Multiple Access)
        - Developed by Qualcomm
        - the only 2G CDMA standard so far
        - IS-95 also called cdmaOne (brand name)
      - PDC (Personal Digital Cellular)
        - Frequency bands
          - 800 MHz
          - 1500 MHz
        - Feature
          - physical layer: similar to D-AMPS
          - protocal stack: resembles GSM
        - Only operated in Japan
      - Digital Cordless systems
        - CT2
        - DECT (Digital Enhanced Cordless Telecommunications)
        - PHS (Personal Handyphone System)
    - 2.5G
      - new technologies
        - HSCSD High-speed Circuit-switched Data)
          - allocate 4 time slots for transmisstion (9.6 Kbps or 14.4 x 4)
          - summary
            - Good: software updates to network, and phone; good for real time apps
            - Bad: usage of scarce radio resources
        - GPRS (General Packet Radio Services)
          - up to 115 Kbps
          - packet switched
          - suitable for non real-time apps
          - bursty data is well handled
          - do not guarantee an absolute maximum delay
        - EDGE (Enhanced Data Rates for Global Evolution)
          - 3 folds of original GSM speed
          - 8PSK (eight-phase shift keying)
          - + GPRS --> EGPRS
            - 384 Kbps maximum
      - IS-136 + (GPRS || EDGE) --> 2.5G
      - Qualcomm
        - CDMA2000 1xRTT
          - IS-95: 14.4 Kbps, 1xRTT: 64 Kbps
          - IS-95 + IS-95B or upgrade CDMA2000 1xRTT -->2.5G
        - HDR (High Data Rate)
          - 2.4 Mbps
          - standardized in IS-856
          - 1xEV-DO (1x Evolved Data Optimized)
            - Add a TDMA component beneath code component
      - PDC-P (NTT DoCoMo)
        - i-mode
  - 3G standard proposals
    - UMTS (Universal Mobile Telecommunications System)
      - Done by ETSI SMG (Special Mobile Group)
      - UMTS Forum was created in 1996
    - new technologies
      - WCDMA
        - the bandwidth is 5 MHz or more (144kbps, 384kbps or even 2Mbps
        - network
          - Synchronous
            - CDMA2000
              - compatible with IS-95
              - manufacturer: Qualcomm, Lucent, Motorola
              - use ANSI-41 core network
              - 3GPP2 (less support than 3GPP)
            - good/not good
              - good: effecient radio interface
              - bad: expensive H/W
          - Asynchronous
            - ETSI/ARIB WCDMA 
              - most popular 3G system
              - manufacturer: Ericsson, Nokia, NTT DocoMo
              - rename to UTRAN (FDD)
              - based on GSM MAP network
              - 3GPP
        - feature
          - fast power control
          - vary bit rate, service params on frame by frame basis
      - Advanced TDMA
        - UWC-136 only
      - Hybrid CDMA/TDMA
        - Not supported
        - in fact, it likes UTRAN TDD
      - OFDM
        - spectrum: effecient
        - user: DAB, DVB, 802.11a, 802.11g, ADSL
        - TDMA/CDMA possible
        - good
          - bandwidth effecient
          - resistance to
            - narrow band interference
            - multipath interefrence
    - IMT-2000
      - umbrella spec of all 3G systems (origin from ITU)
      - IMT Direct Spread (IMT-DS)
        - UTRA FDD
        - 3GPP
      - IMT Multicarrier (IMT-MC)
        - CDMA2000
        - 3GPP2
      - IMT Time Code (IMT-TC)
        - UTRA-TDD/TD-SCDMA narrowband TDD
        - 3GPP
      - IMT Single Carrier (IMT-SC)
        - UWC-136
      - IMT Frequency Time (IMT-FT)
        - DECT
  - 3GPP
    - an org that develops spec for 3g system based on UTRA radio interface
    - partners
      - ETSI
      - ARIB
      - TTA
      - TTC
      - CWTS(china wireless telecommunications Standard
    - ULTRA
      - FDD
        - vocabs
          - chip: a bit in a code word
          - spreading factor: chip rate / data bit rate
          - spreading code: a sequence of chips used to modulate the data bits
        - up/down use separate freq bands
        - chip rate: 3.84 Mcps
      - TDD
        - NOrmal: 3.84 Mcps
        - TD-SCDMA: 1.28 Mcps
      - channels
        - physical (air interface)
        - transport
          - between layer 1 and 2
          - define how data is sent over the air
        - logical
          - within layer 2
          - define the type of data to be sent
  - 3GPP2
    - should be backward compatible with IS-95

and here's the [Introduction to 3G network in tree view](http://daniel.kao.googlepages.com/Introductionto3Gnetwork.mm.html) for better reading.
