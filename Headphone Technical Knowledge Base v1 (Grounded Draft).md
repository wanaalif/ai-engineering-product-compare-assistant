# Headphone Technical Knowledge Base v1 (Grounded Draft)

Prepared 20 Nov 2026 for the headphone product-compare RAG assistant.

## 0. Status and scope (read first)

- **Fully grounded entries in this draft: 80 (Pass 1: 31, Pass 2: 49).** Target was 150-250. Every entry below is built only from sources retrieved during this build. I did not fill the gap from memory.
- **Remaining roster (Section 7):** about 90 further candidate terms are listed by name only, with no definitions, so nothing in them is unsourced. Each needs its own retrieval pass before it becomes an entry.
- **Still not grounded after Pass 2:** primary-source specs for SBC and AAC, plus every term in the Section 7 roster. THD, SNR, Soundstage, Imaging, Adaptive ANC, Transparency Mode, ENC, Beamforming and AI Noise Reduction were added in Pass 2 (HKB-032 to HKB-047).
- **Wording:** Definitions, consumer meanings and comparison guidance are my paraphrases of the cited sources. No source text is reproduced. "n/g" means not grounded in the retrieved sources.

### Confidence rubric (judgment-based, not statistical)

| Grade | Score | Meaning |
| --- | --- | --- |
| A | 0.85-0.95 | Standards body or vendor primary source, plus at least one agreeing source |
| B | 0.70-0.84 | Several reputable secondary sources agree, or a single vendor primary source |
| C | 0.50-0.69 | Single secondary source, or sources conflict on details |
| D | below 0.50 | Weak or contested. Do not use for automated claims |

### RAG usage notes

- Each entry is one retrieval chunk (ID HKB-nnn). Retrieve by Term, then check Cautions before comparing products.
- Treat any spec number as a vendor claim unless the product page cites a test.

## 1. Entries

### Audio Fundamentals

#### HKB-001 Frequency Response

- **Definition:** How the headphone's output level varies across frequencies, usually shown as a curve on the spec sheet. It differs from frequency range, which only gives the lowest and highest frequencies reproduced. \[S15\]\[S16\]
- **Consumer Meaning:** Shows whether a model leans toward more or less bass, mids or treble. A wider range means more of the music's content can be reproduced. \[S15\]\[S17\]
- **Technical Notes:** Hearing is individual, so the same curve is heard differently by different people. \[S15\]
- **Common Marketing Claims:** Wide ranges such as 5 Hz-30 kHz, quoted without a tolerance. \[S18\]
- **Comparison Guidance:** Compare curves, not just range endpoints. Prefer figures that state a tolerance such as +/- dB. \[S18\]\[S15\]
- **Cautions:** A range figure without a tolerance is not meaningful. \[S18\]
- **Sources:** S15, S16, S17, S18 | **Confidence:** A (0.85)

#### HKB-002 Sensitivity

- **Definition:** Sound pressure level produced for a 1 mW input, in dB per mW. At the same input, higher sensitivity is louder. \[S16\]
- **Consumer Meaning:** How loud the headphones get on weak sources like phones. About 100 dB/mW or more is generally easy to drive portably. \[S17\]
- **Technical Notes:** A 3 dB difference or more is generally audible. \[S16\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Judge together with impedance and your source. Lower sensitivity is not worse, only harder to drive. \[S17\]\[S18\]
- **Cautions:** Do not treat sensitivity as a sound-quality score. \[S17\]
- **Sources:** S16, S17, S18 | **Confidence:** A (0.85)

#### HKB-003 Impedance

- **Definition:** Opposition to the AC audio signal, in ohms. It mainly reflects the voice-coil resistance, plus cable resistance. \[S15\]\[S16\]
- **Consumer Meaning:** Low-impedance models suit phones and laptops. Models near 100 ohms and above often benefit from a dedicated amplifier. \[S16\]\[S17\]
- **Technical Notes:** The source's output impedance should be much lower than the headphone's, often by a factor of about 8. \[S15\] Higher sensitivity with lower impedance converts a given electrical signal into sound more effectively. \[S18\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Compare against your source. Most new models sit well below 100 ohms. \[S18\]
- **Cautions:** A higher ohm figure does not mean better sound. \[S15\] Very low impedance can sound bass-light on weak amplifiers. \[S18\]
- **Sources:** S15, S16, S17, S18 | **Confidence:** A (0.85)

### Drivers

#### HKB-004 Dynamic Driver

- **Definition:** A magnet and voice coil move a diaphragm to make sound. It is the simplest driver design. \[S22\]\[S24\]
- **Consumer Meaning:** The common, affordable type, also used in some high-end models. \[S24\]\[S27\]
- **Technical Notes:** Typically uses a neodymium magnet. \[S24\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Do not assume planar or electrostatic is better. Dynamic development is mature. \[S25\]
- **Cautions:** Quality depends on implementation, not driver type alone. \[S25\]
- **Sources:** S22, S24, S25, S27 | **Confidence:** A (0.85)

#### HKB-005 Balanced Armature (BA) Driver

- **Definition:** A coil wraps an armature between two magnets. Current makes the armature oscillate and move a diaphragm. \[S24\]
- **Consumer Meaning:** Small and efficient, common in in-ear monitors and earbuds. \[S22\]\[S44\]
- **Technical Notes:** Several BA drivers can share one earpiece, each covering a frequency region. \[S44\] Bass reproduction is harder than with dynamic drivers. \[S24\]
- **Common Marketing Claims:** Driver counts such as multi-driver IEMs. \[S44\]
- **Comparison Guidance:** Check whether a dynamic driver is added for bass (see hybrid). \[S24\]
- **Cautions:** More drivers do not guarantee better sound. This is derived from S44 and S26, which tie results to tuning and build quality (C).
- **Sources:** S22, S24, S26, S44 | **Confidence:** B (0.80)

#### HKB-006 Planar Magnetic Driver

- **Definition:** A thin diaphragm with embedded conductor traces sits between magnets, so the signal passes through the diaphragm itself. \[S22\]\[S25\]
- **Consumer Meaning:** Often larger, heavier and pricier, and may need more amplification than phones provide. \[S23\]\[S26\]
- **Technical Notes:** Typically better bass extension than comparable dynamic models. \[S23\] More unit-to-unit variance and more sound leakage in open-back designs. \[S23\]
- **Common Marketing Claims:** Low distortion, fast transient response. \[S27\]
- **Comparison Guidance:** Check weight and amp requirements. \[S26\]
- **Cautions:** Not necessarily better than dynamic. \[S25\]
- **Sources:** S22, S23, S25, S26, S27 | **Confidence:** B (0.80)

#### HKB-007 Electrostatic Driver

- **Definition:** An ultra-thin charged diaphragm sits between two metal grids (stators). The signal is applied to the stators, not the diaphragm. \[S22\]
- **Consumer Meaning:** Rare and expensive, not portable, and needs a special amplifier. \[S27\]\[S44\]
- **Technical Notes:** Stax is cited as the best-known maker. \[S25\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Treat as a home-listening category. \[S27\]
- **Cautions:** Do not confuse with piezoelectric (PZT) drivers. \[S24\]
- **Sources:** S22, S24, S25, S27, S44 | **Confidence:** B (0.80)

#### HKB-008 Hybrid Driver

- **Definition:** Combining driver types, most often balanced armature plus dynamic, to use BA precision with dynamic bass. \[S26\]
- **Consumer Meaning:** Multi-driver in-ears, for example the Shure AONIC 4. \[S24\]
- **Technical Notes:** Results depend on build quality and tuning. \[S26\]
- **Common Marketing Claims:** "Best of both worlds" style claims. \[S26\]
- **Comparison Guidance:** Compare tuning reviews, not driver count. \[S26\]
- **Cautions:** Hybrid can also mean other combinations. \[S24\]
- **Sources:** S24, S26 | **Confidence:** C (0.65)

### Bluetooth Codecs

#### HKB-009 Bit Rate

- **Definition:** Audio data sent per second, usually kbps. For uncompressed audio it equals sample rate times bit depth. \[S9\]
- **Consumer Meaning:** Higher bit rate means more data, not automatically better sound. \[S9\]
- **Technical Notes:** Codecs trade noise floor and bit depth to save rate, and heavy compression can add distortion. \[S11\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Compare codec and measured results together. \[S11\]
- **Cautions:** Bit rate alone does not decide quality. \[S11\]
- **Sources:** S9, S11 | **Confidence:** B (0.80)

#### HKB-010 SBC

- **Definition:** The mandatory codec of Classic Bluetooth audio. \[S32\]
- **Consumer Meaning:** The universal fallback codec. \[S32\]
- **Technical Notes:** Maximum bit rate stated as 328 kbps by S9. SIG-derived comparisons cite 240 kbps. \[S9\]\[S33\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Treat as the baseline.
- **Cautions:** Figures conflict between sources. Use as indicative only.
- **Sources:** S9, S32, S33 | **Confidence:** C (0.60)

#### HKB-011 AAC

- **Definition:** A widely supported Bluetooth codec. Apple headphones communicate via AAC. \[S41\]
- **Consumer Meaning:** The main option on iPhones. \[S8\]
- **Technical Notes:** Maximum rate quoted at 250-320 kbps depending on implementation. \[S41\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Needs support on both devices. Confirm each end.
- **Cautions:** Single secondary source for the numbers. Retrieve a primary spec before use.
- **Sources:** S8, S41 | **Confidence:** C (0.50)

#### HKB-012 aptX

- **Definition:** Qualcomm codec. Vendor table: 16-bit, 384 kbps at 48 kHz (325 at 44.1 kHz), THD+N -85 dB, SNR 93 dB, response 20 Hz-22.7 kHz. \[S6\]
- **Consumer Meaning:** Needs aptX in both the source and the headphones. \[S7\]
- **Technical Notes:** Third parties cite 352 kbps. \[S9\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Use the vendor table for spec comparison. \[S6\]
- **Cautions:** Vendor figures are claims, not measurements.
- **Sources:** S6, S7, S9 | **Confidence:** B (0.78)

#### HKB-013 aptX HD

- **Definition:** Qualcomm codec with 24-bit support. Vendor table: 570 kbps, THD+N -90 dB, SNR 129 dB. \[S6\]
- **Consumer Meaning:** Introduced 2016. Falls back to classic aptX when needed. \[S14\]\[S13\]
- **Technical Notes:** Others cite 576 kbps. Sample-rate claims conflict: 48 kHz \[S9\] versus up to 96 kHz \[S8\]. \[S8\]\[S9\]
- **Common Marketing Claims:** "Hi-res" labeling by some outlets. \[S13\]
- **Comparison Guidance:** Supplanted by aptX Adaptive. \[S13\]
- **Cautions:** Treat sample-rate claims as unresolved.
- **Sources:** S6, S8, S9, S13, S14 | **Confidence:** C (0.65)

#### HKB-014 aptX Low Latency

- **Definition:** Low-delay aptX variant: 16-bit, 352 kbps. \[S6\]
- **Consumer Meaning:** For gaming and video sync. Latency about 38-40 ms versus up to 320 ms on other codecs. \[S13\]\[S8\]
- **Technical Notes:** Latency depends on devices. \[S13\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Needs both devices to support it.
- **Cautions:** Figures are approximate.
- **Sources:** S6, S8, S13 | **Confidence:** B (0.75)

#### HKB-015 aptX Adaptive

- **Definition:** Qualcomm codec with variable bit rate that adapts to connection quality. Vendor table: 24-bit, 276-420 kbps. \[S6\]\[S7\]
- **Consumer Meaning:** Aims to avoid dropouts and keep lip sync. \[S14\]
- **Technical Notes:** Another source quotes 279-420 kbps and up to 24-bit/96 kHz. \[S8\]
- **Common Marketing Claims:** Low-latency gaming and glitch-free audio. \[S7\]
- **Comparison Guidance:** Treat as the current successor to aptX HD and LL. \[S8\]
- **Cautions:** Vendor claims.
- **Sources:** S6, S7, S8, S14 | **Confidence:** B (0.80)

#### HKB-016 aptX Lossless

- **Definition:** Extension of aptX Adaptive, exclusive to Snapdragon Sound. \[S7\]\[S8\]
- **Consumer Meaning:** Needs Snapdragon Sound support on both ends. \[S7\]
- **Technical Notes:** Lossless at 16-bit/44.1 kHz, lossy up to 24-bit/96 kHz, dynamic 140 kbps to over 1 Mbps. \[S8\] Qualcomm cites up to 24-bit/96 kHz. \[S7\]
- **Common Marketing Claims:** Streams audio exactly as intended. \[S7\]
- **Comparison Guidance:** Confirm the product is Snapdragon Sound certified.
- **Cautions:** Claims differ in how lossless is defined.
- **Sources:** S7, S8 | **Confidence:** B (0.72)

#### HKB-017 LDAC

- **Definition:** Sony codec, up to 990 kbps. Modes: 330/660/990 kbps; adaptive default switches by connection strength. \[S10\]\[S9\]\[S12\]
- **Consumer Meaning:** Sony certifies it for Hi-Res Audio Wireless at 990 kbps. \[S10\]
- **Technical Notes:** 909 kbps applies to 44.1/88.2 kHz. \[S12\] Tests found only the 990 mode meets hi-res frequency criteria, and the 330 mode measured worse than CD quality. \[S11\]
- **Common Marketing Claims:** Hi-Res and "3x data". \[S10\]
- **Comparison Guidance:** Check which mode actually runs. \[S12\]
- **Cautions:** Can fall to 330 kbps in crowded radio environments. \[S41\]
- **Sources:** S9, S10, S11, S12, S41 | **Confidence:** A (0.85)

#### HKB-018 LC3

- **Definition:** Mandatory codec of LE Audio, also designed for low power. \[S1\]\[S5\]
- **Consumer Meaning:** Better quality at lower rates than SBC, per SIG comparison (160 vs 240 kbps). \[S33\]
- **Technical Notes:** Designed by Fraunhofer. \[S34\] May later be optional on Classic. \[S1\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Look for LE Audio support, not just a version number.
- **Cautions:** Quality claims come from SIG-derived material.
- **Sources:** S1, S5, S33, S34 | **Confidence:** A (0.85)

#### HKB-019 Hi-Res Audio Wireless

- **Definition:** Japan Audio Society certification. LDAC and LHDC were the only certified codecs per the Wikipedia article. \[S12\]
- **Consumer Meaning:** A badge, not a guarantee of identical-to-source audio. \[S11\]
- **Technical Notes:** Sony says LDAC meets the requirement at 990 kbps. \[S10\]
- **Common Marketing Claims:** "Hi-Res" on packaging. \[S10\]
- **Comparison Guidance:** Verify codec and mode.
- **Cautions:** Tests say Bluetooth cannot pass hi-res content unaltered. \[S11\]
- **Sources:** S10, S11, S12 | **Confidence:** C (0.65)

### Noise Control

#### HKB-020 Active Noise Cancellation (ANC)

- **Definition:** Microphones capture noise and the driver plays out-of-phase anti-noise to cancel it. \[S19\]\[S21\]
- **Consumer Meaning:** Reduces ambient noise, but never fully. \[S19\]
- **Technical Notes:** Needs precise phase alignment and DSP processing. \[S19\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check topology: feedforward, feedback, hybrid. \[S19\]
- **Cautions:** Implementations vary in quality. \[S19\]
- **Sources:** S19, S21 | **Confidence:** A (0.85)

#### HKB-021 Feedforward ANC

- **Definition:** Noise microphones sit outside the ear cup. \[S19\]\[S21\]
- **Consumer Meaning:** Good at mid-frequency noise. \[S19\]
- **Technical Notes:** More sensitive to wind and incidental noise. \[S19\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Compare wind-noise results. \[S19\]
- **Cautions:** Can amplify unpredictable noise. \[S19\]
- **Sources:** S19, S21 | **Confidence:** A (0.85)

#### HKB-022 Feedback ANC

- **Definition:** The microphone sits inside the ear cup or ear, and the error signal drives the control filter. \[S21\]\[S19\]
- **Consumer Meaning:** Self-correcting for fit differences. Most effective at low frequencies. \[S19\]
- **Technical Notes:** Risk of runaway amplification or ringing. \[S19\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Weaker at high frequencies. \[S19\]
- **Cautions:** Needs careful tuning.
- **Sources:** S19, S21 | **Confidence:** A (0.85)

#### HKB-023 Hybrid ANC

- **Definition:** Combines feedforward and feedback microphones and processing. \[S20\]\[S21\]
- **Consumer Meaning:** Broadest frequency coverage, usually costlier. \[S19\]
- **Technical Notes:** Lower risk of feedback issues. \[S19\]
- **Common Marketing Claims:** "Hybrid" as a quality label. \[S19\]
- **Comparison Guidance:** Prefer where available.
- **Cautions:** Not an automatic guarantee of quality. \[S19\]
- **Sources:** S19, S20, S21 | **Confidence:** A (0.88)

#### HKB-024 Passive Isolation

- **Definition:** Blocking sound with materials and a tight seal, with no electronics. \[S20\]
- **Consumer Meaning:** Works without power. Silicone or foam tips improve it. \[S19\]\[S21\]
- **Technical Notes:** Poor at low frequencies. \[S19\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Fit matters. Compare earbuds versus closed-back cups. \[S19\]
- **Cautions:** Leaks reduce it. \[S21\]
- **Sources:** S19, S20, S21 | **Confidence:** A (0.85)

### Connectivity

#### HKB-025 LE Audio

- **Definition:** Next-generation Bluetooth audio built on Bluetooth Low Energy, adding LC3, hearing-aid support and Auracast. \[S4\]\[S5\]
- **Consumer Meaning:** Lower power and broadcast sharing. \[S5\]
- **Technical Notes:** Full spec suite completed 12 July 2022. \[S4\] Introduced with Core 5.2. \[S46\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Confirm real LE Audio support.
- **Cautions:** Product support may lag the spec.
- **Sources:** S4, S5, S46 | **Confidence:** A (0.90)

#### HKB-026 Auracast

- **Definition:** Broadcast audio where one transmitter streams to an unlimited number of receivers. \[S2\]\[S5\]
- **Consumer Meaning:** Share audio in public venues or with friends. \[S5\]
- **Technical Notes:** Receivers need Core 5.2 or later plus LC3. \[S3\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check Auracast support explicitly.
- **Cautions:** One source wrongly ties Auracast to Bluetooth 5.4. SIG sources contradict this (S47).
- **Sources:** S2, S3, S5 | **Confidence:** A (0.90)

#### HKB-027 Bluetooth 5.2

- **Definition:** Core version unveiled at CES 2020, hardware basis for LE Audio. \[S31\]\[S28\]
- **Consumer Meaning:** Can support LE Audio and Auracast. \[S28\]
- **Technical Notes:** Backward compatible. Only shared features are used. \[S28\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Version is not feature proof.
- **Cautions:** Version number differs from implemented features.
- **Sources:** S28, S31 | **Confidence:** B (0.80)

#### HKB-028 Bluetooth 5.3

- **Definition:** Successor to 5.2 in 2022, focused on efficiency, reliability and power management. \[S31\]\[S30\]
- **Consumer Meaning:** Modest everyday change. \[S30\]
- **Technical Notes:** n/g
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Do not rank by version alone. \[S30\]
- **Cautions:** Audio quality depends on codec and profiles. \[S30\]
- **Sources:** S30, S31 | **Confidence:** C (0.68)

#### HKB-029 Bluetooth 5.4

- **Definition:** Adds Periodic Advertising with Responses and Encrypted Advertising Data. \[S30\]
- **Consumer Meaning:** Built for IoT and retail more than audio. \[S29\]
- **Technical Notes:** May improve multipoint reliability via newer chipsets. \[S29\]
- **Common Marketing Claims:** "Better sound". \[S30\]
- **Comparison Guidance:** 5.4 layers on top of 5.3. \[S29\]
- **Cautions:** It does not guarantee better sound. \[S30\]
- **Sources:** S29, S30 | **Confidence:** B (0.75)

#### HKB-030 Multipoint

- **Definition:** Pairing that lets headphones switch between two source devices. \[S42\]
- **Consumer Meaning:** Use a phone and laptop without re-pairing. \[S42\]
- **Technical Notes:** Reliability varies by chipset. \[S29\]
- **Common Marketing Claims:** "Seamless switching". \[S42\]
- **Comparison Guidance:** Check how many devices connect at once and whether audio switches automatically.
- **Cautions:** Not defined by a primary source in this pass. Related "dual audio" is different. \[S28\]\[S48\]
- **Sources:** S28, S29, S42, S48 | **Confidence:** C (0.50)

#### HKB-031 IP Rating

- **Definition:** Ingress Protection code under IEC 60529. Two digits: first is solids (0-6), second is water (0-9). "X" means not tested. \[S40\]\[S35\]\[S36\]
- **Consumer Meaning:** IPX4 means splash resistant. IPX7 means submersion up to 1 m for 30 minutes. IP57 adds dust protection. \[S40\]\[S38\]
- **Technical Notes:** IPX6 means powerful water jets. \[S40\] Charging cases may be rated differently or not at all. \[S37\] Fresh water only. \[S39\]
- **Common Marketing Claims:** "Waterproof" versus "water resistant". \[S35\]
- **Comparison Guidance:** Check earbud and case separately. Look for the dust digit.
- **Cautions:** Some sources quote 1.5 m or 3.3 ft for submersion. A missing rating may mean untested. \[S36\]\[S40\]
- **Sources:** S35, S36, S37, S38, S39, S40 | **Confidence:** A (0.88)

## 2. Known source conflicts

- aptX HD bit rate: 570 vs 576 kbps; sample rate 48 vs 96 kHz.
- aptX Adaptive: 276 vs 279 kbps minimum.
- SBC maximum: 328 vs 240 kbps depending on source.
- Auracast and Bluetooth 5.4: one Russian-language retail blog attributes Auracast to 5.4. SIG documents tie it to LE Audio on Core 5.2 or later. Reject that claim. \[S47\]\[S3\]

## 3. Original roster (superseded by Section 7)

**Audio fundamentals:** THD, THD+N, SNR, Dynamic range, Soundstage, Imaging, Frequency range, Maximum input power, Driver diameter, Harman target curve, Sound signature, Bass boost, Equalizer (EQ), Crosstalk, Sibilance, Transient response, Group delay, Damping, Isolation (dB), Distortion.

**Drivers and design:** Piezoelectric driver, Bone conduction, Dual-chamber driver, Diaphragm material, Beryllium, Graphene, LCP, Neodymium magnet, Open-back, Closed-back, Semi-open, Over-ear, On-ear, In-ear, True wireless, Neckband, Open-ear, Earpad, Ear tips, Memory foam, Detachable cable, MMCX, 2-pin, 3.5 mm, 4.4 mm balanced, 2.5 mm, USB-C audio.

**Codecs and wireless:** LHDC, LLAC, aptX LL, A2DP, AVRCP, HFP, HSP, Hi-Res Audio, MQA, Sample rate, Bit depth, Lossless, Lossy, Codec negotiation, Dual audio, Snapdragon Sound, Bluetooth 5.0, 5.1, 6.0, Range, Bluetooth Class, Pairing, Fast Pair, Swift Pair, Find My, LE Power Control, EATT, CIS, BIS, Auracast Assistant, PBP, TMAP, HAP.

**Latency and gaming:** Latency, Game Mode, Low-latency mode, 2.4 GHz dongle, Dual-mode, Lip-sync.

**Noise control:** Adaptive ANC, Transparency Mode, Ambient Sound, Wind noise reduction, Conversation awareness, ANC depth, NRR, Adaptive EQ, Occlusion effect, Pressure feeling.

**Microphone and calls:** ENC, Beamforming, AI Noise Reduction, MEMS microphone, Bone-conduction VAD, Wind-resistant mic, Microphone sensitivity, Sidetone, Mic polar pattern, Boom mic, HD Voice, Wideband speech, LC3plus, mSBC.

**Spatial audio:** Spatial Audio, Dolby Atmos, 360 Reality Audio, Head tracking, HRTF, Virtual surround, DTS Headphone:X, Binaural, 7.1.

**Power and charging:** Battery life, Charging case, Fast charge, Wireless charging, Qi, USB-C PD, Battery capacity (mAh), Standby time, Talk time, Battery health.

**Durability and fit:** IPX4, IPX7, IP57, IP rating of case, Sweat resistance, Weight, Clamping force, Headband, Foldable, Fit tests, Ear detection, Wear sensor.

**Controls and software:** Touch controls, Companion app, Firmware update, Voice assistant, Multi-device, Auto-pause, Customizable EQ, Personalized sound, Hearing test, Safe volume limit, Hearing protection, EN 50332, dB(A).

**Standards and certification:** IEC 60268-7, IEC 60529, Bluetooth SIG qualification, Hi-Res Audio logo, JAS, THX, Dolby, Qualcomm certified, MFi, Made for Android.

**Product claims:** Studio-grade, Audiophile, Flagship ANC, Up to X hours, Military-grade, Lag-free, Lossless, 4K audio, Crystal clear calls.

## 4. Source register

- S1 Bluetooth SIG, LE Audio FAQs. https://www.bluetooth.com/media/le-audio/le-audio-faqs/
- S2 Bluetooth SIG, Auracast Overview (PDF, 2024). https://bluetooth.com/wp-content/uploads/2024/05/2403\_Auracast\_Overview.pdf
- S3 Bluetooth SIG, Auracast Earbuds (PDF, 2024). https://bluetooth.com/wp-content/uploads/2024/05/2403\_Auracast\_Earbuds.pdf
- S4 Bluetooth SIG blog, LE Audio specifications complete. https://bluetooth.com/blog/just-announced-the-complete-suite-of-le-audio-specifications-is-now-available
- S5 Bluetooth SIG, LE Audio overview. https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/le-audio/
- S6 aptX family specification table. https://aptx.com/about
- S7 Qualcomm aptX pages. https://www.qualcomm.com/products/aptx-low-latency and https://www.qualcomm.com/audio/technologies/aptx
- S8 Android Authority, Bluetooth codecs. https://www.androidauthority.com/bluetooth-codecs-997074
- S9 Android Authority, Sony LDAC. https://www.androidauthority.com/sony-ldac-codec-790690/
- S10 Sony, LDAC. https://www.sony.co.jp/en/Products/LDAC/
- S11 SoundGuys, LDAC isn't Hi-Res. https://www.soundguys.com/the-ultimate-guide-to-bluetooth-headphones-aac-vs-sbc-20026/
- S12 Wikipedia, LDAC (mirror). https://en.wikipedia-on-ipfs.org/wiki/LDAC\_(codec)
- S13 Digital Trends, aptX codecs. https://www.digitaltrends.com/home-theater/what-is-aptx-qualcomm-bluetooth-codecs-explained/
- S14 Yamaha, aptX. https://hub.yamaha.com/aptx-the-next-level-of-bluetooth-audio/
- S15 Shure, Specifications explained. https://www.shure.com/en-US/insights/earphone-headphone-specifications-explained
- S16 Audio-Technica, Headphone specs. https://audio-technica.com/en-us/support/audio-solutions-question-week-headphone-specs-mean-important
- S17 Panasonic, Comparing specs. https://www.panasonic.com/sg/consumer/headphones-earphones-learn/tips/how-to-compare-headphones-specs-decoding-audio-jargon.html
- S18 Sound on Sound, Neumann review. https://www.soundonsound.com/node/4920127
- S19 SoundGuys, ANC explained. https://www.soundguys.com/noise-canceling-explained-28344/
- S20 Audio-Technica, ANC types. https://audio-technica.com/en-us/support/audio-solutions-question-of-the-week-how-do-different-active-noise-cancelling-headphones-work
- S21 US Patent 9,293,128 (ANC topologies). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9293128
- S22 Headphones.com, Driver types. https://headphones.com/blogs/features/headphone-driver-types-explained
- S23 RTINGS, Dynamic vs planar. https://rtings.com/headphones/learn/dynamic-vs-planar-magnetic
- S24 MakeTechEasier, Drivers. https://www.maketecheasier.com/what-is-earphones-driver/
- S25 Addicted to Audio, Headphone tech. https://www.addictedtoaudio.com.au/blogs/how-things-work/headphone-tech-explainer-the-machines-behind-the-sound
- S26 Xbitlabs, Headphone drivers. https://www.xbitlabs.com/?p=22767
- S27 Trusted Reviews, Dynamic vs planar. https://www.trustedreviews.com/opinions/dynamic-vs-planar-magnetic-drivers
- S28 RTINGS, Bluetooth versions. https://www.rtings.com/headphones/learn/bluetooth-versions-comparison-profiles
- S29 NearHub, 5.3 vs 5.4. https://www.nearhub.us/blog/bluetooth-five-four-headset-guide
- S30 Analytics Insight, 5.3 vs 5.4. https://www.analyticsinsight.net/technology/bluetooth-53-vs-bluetooth-54-key-differences-explained
- S31 Trusted Reviews, Bluetooth 5.2. https://www.trustedreviews.com/explainer/what-is-bluetooth-5-2-4515024
- S32 freeCodeCamp, LE Audio handbook. https://freecodecamp.org/news/the-bluetooth-le-audio-handbook
- S33 All About Circuits, LE Audio. https://www.allaboutcircuits.com/news/bluetooth-le-audio-set-to-tune-up-hearable-experience/
- S34 ST Wiki, LE Audio intro. https://wiki.st.com/stm32mcu/wiki/Connectivity:Introduction\_to\_Bluetooth\_LE\_Audio
- S35 Jabra, IP ratings. https://www.jabra.com/blog/waterproof-or-water-resistant-whats-behind-an-ip-rating/
- S36 RTINGS, IP ratings. https://rtings.com/headphones/learn/ip-ratings
- S37 Huawei FreeArc specs. https://consumer.huawei.com/bd/audio/freearc/specs
- S38 Bang & Olufsen support, IP57. https://support.bang-olufsen.com/hc/en-us/articles/40069093295505
- S39 Reviewed, IP ratings. https://reviewed.com/headphones/features/what-do-waterproof-and-water-resistant-really-mean
- S40 HeadphonesAddict, IP rating. https://headphonesaddict.com/ip-rating-explained/
- S41 Spider's Web, lossless over Bluetooth (2026). https://spidersweb.pl/2026/06/streaming-bezstratny-dzwiek-lossless-bluetooth-jakosc.html
- S42 Shokz, 5.3 vs 5.4. https://ca.shokz.com/blogs/news/bluetooth-5-3-vs-5-4
- S44 HeadphonesAddict, Drivers. https://headphonesaddict.com/headphone-drivers-explained/
- S46 MathWorks, Bluetooth LE Audio. https://au.mathworks.com/help/bluetooth/ug/bluetooth-le-audio.html
- S47 DoctorHead (conflicting claim on Auracast and 5.4, rejected). https://doctorhead.ru/blog/bluetooth-5-4-vs-5-3-obzor-i-sravnenie-versiy\_abc/
- S48 HeadphonesAddict, Bluetooth versions (dual audio). https://headphonesaddict.com/?p=3535

## 5. Pass 2 entries (HKB-032 to HKB-080)

Same template and confidence rubric as Section 0. Source IDs S49 onward are in Section 8.

### Audio Fundamentals (Pass 2)

#### HKB-032 THD (Total Harmonic Distortion)

- **Definition:** Ratio of the summed power of all harmonics to the power of the fundamental, shown as a percentage or in dB. Harmonics are whole-number multiples of the tone fed in. \[S50\]\[S52\]
- **Consumer Meaning:** How much extra tone the headphone adds to the signal. Lower is cleaner. \[S49\]
- **Technical Notes:** Distortion follows the signal, while noise is unrelated and random. \[S50\] One test lab measures at 94 and 104 dB SPL and caps results at 10 kHz. \[S50\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Compare only figures measured at the same level and frequency. \[S50\]
- **Cautions:** THD is the most basic distortion measure and misses other types such as intermodulation. \[S49\] A percentage-to-dB conversion in S51 looks off, so recompute before use.
- **Sources:** S49, S50, S51, S52 | **Confidence:** B (0.78)

#### HKB-033 THD+N

- **Definition:** Ratio of noise plus distortion to the signal, the inverse view of SINAD. \[S53\]
- **Consumer Meaning:** One number covering both hiss and distortion. \[S53\]
- **Technical Notes:** Chip datasheets list THD, THD+N and SNR with named test conditions. \[S55\] Bluetooth codec tables also quote THD+N, for example aptX at -85 dB. \[S6\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check the test level and bandwidth behind the figure. \[S55\]
- **Cautions:** The larger of noise and distortion dominates the ratio, so it can hide one of them. \[S53\]
- **Sources:** S6, S53, S55 | **Confidence:** B (0.75)

#### HKB-034 SNR (Signal-to-Noise Ratio)

- **Definition:** Ratio of output signal power to output noise power at the same reference point, in dB. Higher means less noise on the signal. \[S54\]
- **Consumer Meaning:** An SNR of 100 dB means the signal sits 100 dB above the noise floor. \[S56\]
- **Technical Notes:** Datasheets often measure it as idle-channel noise, A-weighted. \[S55\]
- **Common Marketing Claims:** High figures such as 129-135 dB in codec tables. \[S6\]
- **Comparison Guidance:** For high-fidelity gear one source suggests 90 dB or more. \[S56\]
- **Cautions:** Very high SNR may not be audible, since quiet rooms rarely drop below roughly 30 dB. \[S56\]
- **Sources:** S6, S54, S55, S56 | **Confidence:** A (0.85)

#### HKB-035 Soundstage

- **Definition:** The perceived space the sound seems to come from, covering width, depth and height. \[S59\]\[S60\]
- **Consumer Meaning:** Whether music feels wide and airy or close and intimate. Imaging is separate. \[S57\]
- **Technical Notes:** It is a perceptual result, not a specification. It depends on the recording first, then the transducer. \[S60\] Open-back designs and over-ear cups are commonly credited with a larger stage. \[S59\]\[S72\]
- **Common Marketing Claims:** "Wide soundstage" with no test data. n/g for specifics.
- **Comparison Guidance:** Use design cues such as open-back and over-ear, not a numeric spec. \[S59\]
- **Cautions:** The term is used inconsistently and some experts dispute its meaning. \[S62\] There is no standard metric. The driver-size claim rests on one source. \[S59\]
- **Sources:** S57, S59, S60, S62, S72 | **Confidence:** C (0.55)

#### HKB-036 Imaging

- **Definition:** How precisely each instrument or sound is placed inside the soundstage. \[S57\]\[S58\]
- **Consumer Meaning:** Can you point to where the guitar or vocal sits. \[S58\]
- **Technical Notes:** A system can have a wide stage with vague placement, or pinpoint imaging in a small stage. \[S61\]
- **Common Marketing Claims:** "Precise imaging". n/g for specifics.
- **Comparison Guidance:** Use reviewer descriptions, since no metric exists.
- **Cautions:** Subjective and not equal to Spatial Audio. \[S58\]
- **Sources:** S57, S58, S61 | **Confidence:** C (0.55)

#### HKB-037 Harman Target Curve

- **Definition:** A headphone frequency response shown in Harman listening research to satisfy the preferences of most listeners. \[S63\]
- **Consumer Meaning:** A benchmark, not a promise that everyone will like it. \[S65\]
- **Technical Notes:** The further a response deviates from the target, the lower the perceived quality in the research. \[S63\] Three versions exist, and Harman is re-examining the target for in-ear models. \[S65\] Newer fixtures such as the B&K 5128 lack equivalent preference data. \[S66\]
- **Common Marketing Claims:** "Harman-tuned" or "Harman target". \[S65\]
- **Comparison Guidance:** Use closeness to the target as context for a measured curve. \[S64\]
- **Cautions:** Preference curves are context, not objective truth. \[S64\]
- **Sources:** S63, S64, S65, S66 | **Confidence:** B (0.78)

### Form Factors and Acoustic Design

#### HKB-038 Open-Back Headphones

- **Definition:** Ear cups with open outer surfaces, so sound and air can pass through. \[S68\]\[S69\]
- **Consumer Meaning:** Spacious sound for quiet home listening, but they leak sound and let in outside noise. \[S67\]\[S70\]
- **Technical Notes:** Mostly over-ear, with very few wireless examples. \[S68\]\[S70\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Not suited to commuting. ANC works best on closed designs. \[S68\]
- **Cautions:** Closed-back models can also leak at high volume. \[S70\]
- **Sources:** S67, S68, S69, S70 | **Confidence:** B (0.82)

#### HKB-039 Closed-Back Headphones

- **Definition:** Enclosed ear cups that block the acoustic path between the outside and the ear. \[S69\]
- **Consumer Meaning:** Best isolation and more bass weight. Also used for studio vocal tracking to prevent leakage. \[S71\]\[S67\]
- **Technical Notes:** Finite rear volume, unlike open-back. \[S69\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Best base for ANC. \[S68\]
- **Cautions:** Not ideal where you need traffic awareness. \[S71\]
- **Sources:** S67, S68, S69, S71 | **Confidence:** B (0.80)

#### HKB-040 Semi-Open Headphones

- **Definition:** A mix of open and closed designs. S69 defines it as acoustically closed at the front with an open rear, or the reverse. \[S69\]
- **Consumer Meaning:** A compromise with some airflow and limited isolation. \[S73\]
- **Technical Notes:** Terms vary across brands. \[S69\]
- **Common Marketing Claims:** "Best of both worlds". \[S71\]
- **Comparison Guidance:** Treat with caution.
- **Cautions:** Can keep drawbacks of both. \[S68\]\[S71\]
- **Sources:** S68, S69, S71, S73 | **Confidence:** C (0.65)

#### HKB-041 Form Factors (Over-Ear, On-Ear, In-Ear, Open-Ear, True Wireless)

- **Definition:** Over-ear (circumaural) cups enclose the ear, on-ear (supra-aural) cups rest on it, in-ear models sit in the ear canal, open-ear models sit outside the canal, and true wireless earbuds are fully cable-free with a charging case. \[S67\]\[S71\]\[S73\]
- **Consumer Meaning:** Pick by use: over-ear for home, in-ear and true wireless for pocketability. \[S73\]
- **Technical Notes:** Over-ears interact more with the outer ear, which may add to perceived soundstage. \[S72\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Compare within the same form factor first.
- **Cautions:** Open or closed is a separate axis from form factor. \[S67\]
- **Sources:** S67, S71, S72, S73 | **Confidence:** B (0.78)

### Noise Control (Pass 2)

#### HKB-042 Adaptive ANC

- **Definition:** ANC that monitors surroundings and adjusts cancellation level automatically. \[S74\]
- **Consumer Meaning:** Saves manual switching between settings. \[S74\]
- **Technical Notes:** Draws more battery than fixed ANC. \[S74\] Digit separates it from adjustable ANC, where you set the level. \[S75\] Apple's Adaptive Audio and Google's Adaptive Audio are blended modes with different names. \[S76\]\[S77\]
- **Common Marketing Claims:** "Adaptive", "Smart" ANC. \[S83\]
- **Comparison Guidance:** Ask what it adapts to and what the user can still control.
- **Cautions:** Same word, different features across brands. \[S77\]
- **Sources:** S74, S75, S76, S77, S83 | **Confidence:** C (0.62)

#### HKB-043 Transparency Mode

- **Definition:** Outside microphones feed ambient sound into the ear so you can hear surroundings. It depends on ANC hardware. \[S78\]
- **Consumer Meaning:** Hear announcements without removing the buds. \[S78\]
- **Technical Notes:** Brand names include Transparency (Apple), Aware (Bose) and Ambient (Sony). \[S78\] It uses battery even with no audio playing. \[S79\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check whether the mix level is adjustable. \[S78\]
- **Cautions:** It is not hearing protection. \[S78\]
- **Sources:** S77, S78, S79 | **Confidence:** A (0.85)

#### HKB-044 Claimed ANC Noise Reduction (dB)

- **Definition:** Vendor-stated amount of noise reduction, in dB. \[S80\]
- **Consumer Meaning:** Reductions of 20-30 dB are described as effective. \[S80\]\[S81\]
- **Technical Notes:** Claims range up to 45-50 dB in vendor material, with no test method stated. \[S83\]
- **Common Marketing Claims:** "Up to 50 dB". \[S83\]
- **Comparison Guidance:** Use independent measurements instead. Fit strongly affects results. \[S74\]
- **Cautions:** ANC is best on steady low-frequency noise and weak on sudden or high-pitched sounds. \[S74\] Treat as D for automated ranking.
- **Sources:** S74, S80, S81, S83 | **Confidence:** C (0.50)

### Microphone and Calls

#### HKB-045 ENC (Environmental Noise Cancellation)

- **Definition:** Reduces background noise in your outgoing voice during calls. It affects what others hear, not what you hear. \[S75\]\[S81\]
- **Consumer Meaning:** Clearer voice on calls. \[S80\]
- **Technical Notes:** Multiple microphones separate voice from noise, then DSP filters the rest. \[S81\] Two mics per earbud typically beat one. \[S80\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Count microphones and look for call tests. \[S81\]
- **Cautions:** Poor ENC can distort speech. \[S81\] One vendor describes ENC as generating anti-noise, which conflicts with the other sources. \[S80\]
- **Sources:** S75, S80, S81 | **Confidence:** B (0.78)

#### HKB-046 Beamforming

- **Definition:** A microphone array uses timing differences between microphones to form a directional pickup from omnidirectional mics. \[S82\]
- **Consumer Meaning:** Focuses on your voice. \[S82\]
- **Technical Notes:** Digit pairs beamforming mics with algorithms that suppress non-speech noise. \[S75\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check array size and call tests.
- **Cautions:** One vendor blog is the main source. More mics are not always better. \[S82\]
- **Sources:** S75, S82 | **Confidence:** C (0.62)

#### HKB-047 AI Noise Reduction (Calls)

- **Definition:** A neural network trained to recognize voice and separate it from wind, traffic and keyboard sounds in the microphone signal. \[S82\]
- **Consumer Meaning:** Cleans your voice before it leaves the device. \[S82\]
- **Technical Notes:** Works on any app, since it is applied before transmission. \[S82\]
- **Common Marketing Claims:** "AI" call noise reduction. \[S82\]
- **Comparison Guidance:** Compare call recordings.
- **Cautions:** Vendor-only source. Treat as unverified. \[S82\]
- **Sources:** S82 | **Confidence:** C (0.50)

#### HKB-048 A2DP

- **Definition:** Bluetooth profile for one-way stereo audio from source to headphones. SBC support is mandatory under the A2DP specification. \[S28\]\[S85\]
- **Consumer Meaning:** The profile used for music. It carries no microphone audio. \[S28\]
- **Technical Notes:** Source and sink roles. \[S85\]\[S87\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Assume all modern headphones support it. \[S28\]
- **Cautions:** Devices use only profiles both support. \[S28\]
- **Sources:** S28, S85, S87 | **Confidence:** A (0.85)

#### HKB-049 AVRCP

- **Definition:** Remote-control profile for play, pause, skip, volume and track metadata. \[S28\]\[S85\]
- **Consumer Meaning:** Lets headphone buttons control the phone. \[S28\]
- **Technical Notes:** Usually paired with A2DP. \[S85\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Not a differentiator.
- **Cautions:** n/g
- **Sources:** S28, S85 | **Confidence:** B (0.82)

#### HKB-050 HFP and HSP

- **Definition:** Profiles for phone-call audio. HSP is simpler and older. HFP adds features and better compatibility. \[S28\]
- **Consumer Meaning:** Used for calls and assistants. Headphones usually switch from A2DP to HFP during a call. \[S28\]
- **Technical Notes:** Narrowband speech uses CVSD, wideband uses mSBC. \[S85\] HFP 1.6 added wideband speech. \[S86\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Call quality differs from music quality.
- **Cautions:** Switching to HFP is why audio quality drops on calls. This is derived from S28.
- **Sources:** S28, S85, S86 | **Confidence:** B (0.80)

#### HKB-051 mSBC

- **Definition:** A 16 kHz mono configuration of SBC for wideband speech in HFP. \[S86\]
- **Consumer Meaning:** Better call clarity than narrowband speech. \[S87\]
- **Technical Notes:** Added in HFP 1.6. \[S86\] Microsoft guidelines require careful frame alignment. \[S85\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Look for wideband speech support in spec sheets.
- **Cautions:** Support must exist on both ends.
- **Sources:** S85, S86, S87 | **Confidence:** B (0.78)

### Latency and Gaming

#### HKB-052 Latency

- **Definition:** Delay between an audio event and when you hear it. \[S88\]
- **Consumer Meaning:** Matters for games and video sync. Bluetooth generally lags behind 2.4 GHz and wired. \[S88\]
- **Technical Notes:** Quoted ranges vary widely, for example SBC at 100-200 ms and aptX LL at about 40 ms. \[S89\]
- **Common Marketing Claims:** "Ultra-low latency". \[S92\]
- **Comparison Guidance:** Prefer independent measurements. Support for low-latency codecs is inconsistent. \[S88\]
- **Cautions:** Most figures come from retail or marketing blogs. \[S91\]
- **Sources:** S88, S89, S91, S92 | **Confidence:** C (0.55)

#### HKB-053 2.4 GHz Wireless Dongle (Dual-Mode)

- **Definition:** A proprietary USB dongle link that bypasses Bluetooth. Many headsets add Bluetooth as a second mode. \[S88\]\[S89\]
- **Consumer Meaning:** Better for competitive gaming. Bluetooth is fine for music and calls. \[S89\]
- **Technical Notes:** Figures of 12-28 ms appear, from lower-quality sources. \[S91\]
- **Common Marketing Claims:** "As low as 20 ms". \[S92\]
- **Comparison Guidance:** Confirm the dongle is in the box and works with your platform.
- **Cautions:** Some listings mislabel dongle-only headsets as Bluetooth-compatible. \[S91\]
- **Sources:** S88, S89, S91 | **Confidence:** C (0.58)

#### HKB-054 Low-Latency / Gaming Mode (Bluetooth)

- **Definition:** A mode on Bluetooth earbuds that reduces delay, distinct from a 2.4 GHz link. \[S90\]
- **Consumer Meaning:** Better for phone games. \[S90\]
- **Technical Notes:** One vendor claims about 60 ms. \[S92\]
- **Common Marketing Claims:** "Gaming mode". \[S90\]
- **Comparison Guidance:** A real 2.4 GHz connection performed best in one test. \[S90\]
- **Cautions:** Vendor figure only.
- **Sources:** S90, S92 | **Confidence:** C (0.50)

### Spatial Audio

#### HKB-055 Spatial Audio

- **Definition:** A broad category of 3D sound technologies. \[S93\]
- **Consumer Meaning:** Sound placed around you instead of inside your head. \[S94\]
- **Technical Notes:** Uses HRTF-based binaural rendering. \[S94\] Dolby Atmos is one format, others include DTS:X and Sony 360 Reality Audio. \[S93\]\[S96\]
- **Common Marketing Claims:** "Immersive audio". \[S93\]
- **Comparison Guidance:** Ask which format and whether head tracking is included.
- **Cautions:** Not every song uses spatial formats. \[S93\]
- **Sources:** S93, S94, S96 | **Confidence:** B (0.80)

#### HKB-056 Dolby Atmos (for Headphones)

- **Definition:** An object-based spatial format. For headphones its object metadata is converted to a binaural 360-degree output for two drivers. \[S95\]\[S93\]
- **Consumer Meaning:** Works on ordinary stereo headphones via software. \[S93\]
- **Technical Notes:** Apple Music provides spatial audio in Dolby Atmos. \[S96\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check content support, not just logos.
- **Cautions:** The default renderer uses one average HRTF. \[S97\]
- **Sources:** S93, S95, S96, S97 | **Confidence:** B (0.75)

#### HKB-057 Head Tracking

- **Definition:** Sensors report head rotation to the renderer in real time. \[S94\]
- **Consumer Meaning:** Sound stays anchored when you turn your head. \[S93\]
- **Technical Notes:** Without it, sounds often seem to sit inside the head. \[S94\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Needs support in the headphones and the device. \[S93\]
- **Cautions:** Less common feature.
- **Sources:** S93, S94 | **Confidence:** B (0.78)

#### HKB-058 HRTF (Head-Related Transfer Function)

- **Definition:** The effect of shoulders, head and outer ears on sound arriving at the eardrums. \[S95\]
- **Consumer Meaning:** Why 3D audio sounds different for each person. \[S97\]
- **Technical Notes:** Convolving audio with an HRTF pair makes it seem to come from a direction. \[S94\] Dolby offers a personalized HRTF app. \[S97\]
- **Common Marketing Claims:** "Personalized spatial audio". \[S97\]
- **Comparison Guidance:** Look for personalization options.
- **Cautions:** Most renderers use one average HRTF. \[S97\]
- **Sources:** S94, S95, S97 | **Confidence:** B (0.80)

#### HKB-059 Binaural Audio

- **Definition:** Recordings made with microphones in the ears or a dummy head, reproducing natural hearing. \[S95\]\[S94\]
- **Consumer Meaning:** Realistic 3D playback on headphones. \[S95\]
- **Technical Notes:** Rendering simulates a speaker layout through psychoacoustics. \[S96\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Needs matching content.
- **Cautions:** Niche. \[S95\]
- **Sources:** S94, S95, S96 | **Confidence:** B (0.78)

#### HKB-060 Virtual Surround

- **Definition:** Software applies an HRTF-based binaural algorithm to place multichannel audio around each ear. \[S95\]
- **Consumer Meaning:** Surround effect on two-driver headphones. \[S95\]
- **Technical Notes:** With head tracking, virtual speakers stay fixed. \[S95\]
- **Common Marketing Claims:** "7.1 surround". \[S95\]
- **Comparison Guidance:** Distinguish true multi-driver from virtual. \[S95\]
- **Cautions:** Quality varies.
- **Sources:** S95 | **Confidence:** C (0.62)

### Standards and Safe Listening

#### HKB-061 EN 50332

- **Definition:** European standard series for maximum sound pressure level measurement of headphones used with personal music players. It has applied since January 2013 and is mandatory in the EU and Switzerland. \[S98\]
- **Consumer Meaning:** Players that can exceed 85 dB(A) must warn the user and may not exceed 100 dB(A). \[S99\]
- **Technical Notes:** Part 2 covers player and headphone tested separately: a 27 mV warning and a 150 mV maximum, with headphone sensitivity specified. \[S99\] Part 3 covers sound-dose measurement. \[S102\]
- **Common Marketing Claims:** "EN 50332 compliant". \[S80\]
- **Comparison Guidance:** Treat as a regional safety baseline, not a quality grade.
- **Cautions:** Pairing with a different headphone can invalidate the output assumptions. \[S100\]
- **Sources:** S80, S98, S99, S100, S102 | **Confidence:** A (0.85)

#### HKB-062 Safe Listening (WHO/ITU H.870)

- **Definition:** Guideline to limit weekly sound dose to the equivalent of 80 dB(A) for 40 hours a week. \[S102\]
- **Consumer Meaning:** Higher volume shortens safe listening time. A stricter 75 dB(A) mode applies to sensitive users such as children. \[S100\]
- **Technical Notes:** H.870 was published August 2018, based on EN 50332-3. \[S102\] The iPhone Health app has shown weekly dose since October 2019. \[S102\]
- **Common Marketing Claims:** "Safe volume limit". \[S100\]
- **Comparison Guidance:** Look for dose tracking, not just a fixed cap.
- **Cautions:** Standards are not uniform worldwide. \[S98\]
- **Sources:** S98, S100, S102 | **Confidence:** A (0.82)

#### HKB-063 dB(A)

- **Definition:** Decibels of sound pressure level measured with the A-weighting network. \[S101\]
- **Consumer Meaning:** The unit used in safe-listening limits. \[S101\]
- **Technical Notes:** A-weighting approximates loudness at low levels. \[S101\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Do not mix dB SPL and dB(A) without conversion.
- **Cautions:** Conversion between dB SPL and dB(A) is context dependent.
- **Sources:** S101 | **Confidence:** A (0.85)

#### HKB-064 SPL (Sound Pressure Level)

- **Definition:** Logarithm, in decibels, of the ratio of sound pressure to a reference pressure. \[S101\]
- **Consumer Meaning:** How loud something is. Used in sensitivity and distortion tests. \[S50\]\[S16\]
- **Technical Notes:** n/g beyond the definition.
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check the reference condition.
- **Cautions:** The reference value in S101 appears garbled. Verify against a primary source.
- **Sources:** S16, S50, S101 | **Confidence:** B (0.75)

#### HKB-065 Volume-Limited Headphones

- **Definition:** Headphones marketed as capping output, often near 85 dB. \[S100\]
- **Consumer Meaning:** Intended for children. \[S100\]
- **Technical Notes:** A study found packaging labels ambiguous, and some players exceeded 85 dB(A). \[S100\]
- **Common Marketing Claims:** "Safe for kids". \[S100\]
- **Comparison Guidance:** Ask what source and test were used.
- **Cautions:** An unknown headphone swap makes exposure calculations meaningless. \[S100\]
- **Sources:** S100 | **Confidence:** B (0.78)

### Connectors and Cables

#### HKB-066 3.5 mm TRS (Unbalanced)

- **Definition:** Standard headphone jack. 3.5 mm and 6.3 mm are TRS unbalanced connectors. \[S103\]\[S105\]
- **Consumer Meaning:** Works with nearly all sources. \[S103\]
- **Technical Notes:** 2.5 mm and 4.4 mm are mainly used for balanced connections. \[S105\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check which plug is on the headphone end and which on the source.
- **Cautions:** n/g
- **Sources:** S103, S105 | **Confidence:** B (0.80)

#### HKB-067 Balanced Connections (4.4 mm, 2.5 mm)

- **Definition:** Balanced means signal sent on separate positive and negative terminals. \[S103\]
- **Consumer Meaning:** Needs a balanced output on the source. \[S104\]
- **Technical Notes:** 4.4 mm is TRRRS and 2.5 mm is TRRS. \[S103\] Pentaconn is built to the 4.4 mm standard, but not all 4.4 mm is Pentaconn. \[S104\] 2.5 mm came first and is smaller and more fragile. \[S104\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Pick the one your source offers. \[S104\]
- **Cautions:** Audible benefit is mostly cited for multi-driver IEMs. \[S104\]
- **Sources:** S103, S104, S105 | **Confidence:** B (0.75)

#### HKB-068 MMCX, 2-Pin and Detachable Cables

- **Definition:** The two main detachable IEM connector standards. \[S103\]
- **Consumer Meaning:** Lets you replace or upgrade cables. \[S104\]
- **Technical Notes:** 2-pin is commonly 0.78 or 0.75 mm. \[S120\] Audio-Technica uses its own A2DC connector on many headphones. \[S106\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check compatibility before buying a cable.
- **Cautions:** One source says there is no sound difference. \[S103\] Sources disagree on which is more secure. \[S103\]\[S104\]
- **Sources:** S103, S104, S106, S120 | **Confidence:** B (0.75)

### Battery and Charging

#### HKB-069 Battery Life (Playback and Total with Case)

- **Definition:** Rated hours per charge, usually given separately with ANC on and off, and as a total including the charging case. \[S107\]\[S116\]
- **Consumer Meaning:** Real use depends on ANC, codec and call mode. \[S107\]
- **Technical Notes:** One vendor lists AAC at 10 hours ANC off and 6 on, and LDAC at 6 and 4.5. \[S107\] A reviewer saw Jabra's claimed 5.5 and 7 hours almost exactly. \[S110\]
- **Common Marketing Claims:** "Up to X hours". \[S116\]
- **Comparison Guidance:** Compare like for like: same ANC state and codec.
- **Cautions:** Case totals include recharges and are not single-session times. \[S116\]
- **Sources:** S107, S110, S116 | **Confidence:** A (0.82)

#### HKB-070 Fast Charge

- **Definition:** Short charge giving extra playback. \[S109\]
- **Consumer Meaning:** Examples are 5 minutes for 1 hour on one model and 15 minutes for 1 hour on another. \[S109\]\[S110\]
- **Technical Notes:** One vendor lists 10 minutes for 2.2 hours with ANC off and 1.6 hours with ANC on. \[S108\]
- **Common Marketing Claims:** "10 minutes for X hours". \[S122\]
- **Comparison Guidance:** Compare the minutes-to-hours ratio, ANC state included.
- **Cautions:** A retailer listing of 10 hours from 10 minutes conflicts with the vendor's own support page. \[S122\]\[S108\]
- **Sources:** S108, S109, S110, S122 | **Confidence:** B (0.72)

#### HKB-071 Qi Wireless Charging and USB-C

- **Definition:** Charging methods, usually applied to the case. \[S109\]\[S110\]
- **Consumer Meaning:** Place the case on a Qi charger, or use the case's USB-C port. \[S112\]
- **Technical Notes:** Some cases support both. \[S110\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check whether Qi is on the case or the earbuds.
- **Cautions:** Not every model supports Qi. \[S116\]
- **Sources:** S109, S110, S112, S116 | **Confidence:** B (0.78)

#### HKB-072 Battery Capacity (mAh)

- **Definition:** Rated cell capacity for earbuds and case. One earbud pair lists 60 mAh per earbud and 472 mAh for the case. \[S111\] Another lists a 410 mAh case. \[S115\]
- **Consumer Meaning:** Runtime, not mAh, is what to compare. \[S107\]
- **Technical Notes:** n/g
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Use only as supporting data.
- **Cautions:** Capacity does not predict runtime, since ANC and codec change it. \[S107\]
- **Sources:** S107, S111, S115 | **Confidence:** C (0.60)

### Additional Wireless Terms

#### HKB-073 Snapdragon Sound

- **Definition:** Qualcomm platform combining audio, connectivity and voice technologies, with a logo on certified products. \[S7\]
- **Consumer Meaning:** The route to aptX Lossless. \[S7\]
- **Technical Notes:** Built on S3, S5 and S7 sound platforms. \[S7\]
- **Common Marketing Claims:** "Lossless", "low latency". \[S7\]
- **Comparison Guidance:** Check that both phone and headphones are certified.
- **Cautions:** Vendor sources only.
- **Sources:** S7 | **Confidence:** B (0.78)

#### HKB-074 LHDC

- **Definition:** A codec reported to be certified for Hi-Res Audio Wireless alongside LDAC. \[S12\]
- **Consumer Meaning:** Less widely supported. n/g
- **Technical Notes:** One 2026 source says up to 24-bit/192 kHz at 900 kbps or more in theory. \[S41\]
- **Common Marketing Claims:** "Hi-res". \[S12\]
- **Comparison Guidance:** Do not use without a primary source.
- **Cautions:** Two weak sources. Treat as D.
- **Sources:** S12, S41 | **Confidence:** D (0.45)

#### HKB-075 Sample Rate and Bit Depth

- **Definition:** Codec specs list bit depth, shown as word depth, for example 16-bit versus 24-bit. \[S6\] Uncompressed bit rate equals sample rate times bit depth. \[S9\]
- **Consumer Meaning:** Higher values allow finer detail on paper. \[S6\]
- **Technical Notes:** Hi-res targets such as 24-bit/96 kHz are not preserved intact by Bluetooth. \[S11\]
- **Common Marketing Claims:** "24-bit" and "96 kHz". \[S10\]
- **Comparison Guidance:** Compare measured noise floor too. \[S11\]
- **Cautions:** Standalone definitions of both terms were not retrieved. Treat as partial.
- **Sources:** S6, S9, S10, S11 | **Confidence:** C (0.55)

#### HKB-076 Lossless vs Lossy (Bluetooth)

- **Definition:** SBC, AAC and aptX are typically lossy at 16-bit/44.1 kHz. \[S13\] LDAC at 909 kbps can stream 16-bit/44.1 kHz losslessly. \[S12\] aptX Lossless is lossless at 16-bit/44.1 kHz. \[S8\]
- **Consumer Meaning:** "Lossless" is only true in specific modes. \[S12\]\[S8\]
- **Technical Notes:** Bluetooth cannot pass hi-res content unaltered. \[S11\]
- **Common Marketing Claims:** "Lossless over Bluetooth". \[S7\]
- **Comparison Guidance:** Check mode, device pairing and bit rate.
- **Cautions:** Claims often drop to lossy in poor radio conditions. \[S41\]
- **Sources:** S7, S8, S11, S12, S13, S41 | **Confidence:** C (0.62)

#### HKB-077 Dual Audio

- **Definition:** One source streaming to two sound devices at once. \[S48\]
- **Consumer Meaning:** Share audio with two headphones or two speakers. \[S48\]
- **Technical Notes:** RTINGS groups it with multipoint under Bluetooth 5.0. \[S28\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Do not confuse with multipoint.
- **Cautions:** Thin sourcing. Treat as D.
- **Sources:** S28, S48 | **Confidence:** D (0.45)

#### HKB-078 Bluetooth 5.0

- **Definition:** 2016 core version with 2 Mbps BLE, up to 240 m line-of-sight range and 8x broadcast capacity. \[S28\]
- **Consumer Meaning:** Mainstream in most current headphones. \[S28\]
- **Technical Notes:** Range is quoted as up to 800 feet (240 m). \[S48\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Fine for typical use. It lacks LE Audio hardware. \[S28\]
- **Cautions:** Range is open-air, not indoors.
- **Sources:** S28, S48 | **Confidence:** B (0.75)

#### HKB-079 Isochronous Channels (CIS and BIS)

- **Definition:** New LE Audio transport replacing SCO and ACL for audio, in unicast (CIS) and broadcast (BIS) forms. \[S32\]
- **Consumer Meaning:** Underpins multi-stream and Auracast. \[S34\]
- **Technical Notes:** The Core Specification added LE Isochronous Channels in December 2019. \[S117\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Not shown on spec sheets.
- **Cautions:** n/g
- **Sources:** S32, S34, S117 | **Confidence:** B (0.80)

#### HKB-080 Auracast Assistant

- **Definition:** A device role that receives Auracast advertisements and helps a receiver find and join a broadcast. \[S3\]\[S33\]
- **Consumer Meaning:** Often a phone. n/g beyond role names.
- **Technical Notes:** Roles: transmitter, receiver and assistant. \[S3\]
- **Common Marketing Claims:** n/g
- **Comparison Guidance:** Check how a product joins broadcasts.
- **Cautions:** Role naming varies in SIG documents. \[S2\]
- **Sources:** S2, S3, S33 | **Confidence:** B (0.75)

## 6. Pass 2 source conflicts and flags

- **Latency:** SBC quoted at 100-200 ms by retail blogs, 150-300 ms by another, and aptX LL at about 40 ms. Treat all as indicative. \[S89\]\[S91\]
- **MMCX vs 2-pin:** one source says MMCX is more secure, another says 2-pin seats more firmly. \[S103\]\[S104\]
- **ENC:** one vendor describes anti-noise generation, others describe DSP filtering of the voice. \[S80\]\[S81\]
- **THD:** one source gives a percentage-to-dB conversion that looks wrong. Recompute from 20 log10. \[S51\]
- **Fast charge:** one retailer listing conflicts with the vendor's support page. \[S122\]\[S108\]
- **Low-quality sources:** several latency figures come from Alibaba insight pages and a retail blog. They are marked C and should not be used for ranking. \[S91\]

## 7. Roster status after Pass 2

**Total entries: 80** (HKB-001 to HKB-080). Items below from the original roster are now covered by an entry above, though some only partially.

**Now covered:** THD, THD+N, SNR, Soundstage, Imaging, Harman target curve, Frequency range, Open-back, Closed-back, Semi-open, Over-ear, On-ear, In-ear, True wireless, Open-ear, Adaptive ANC, Transparency Mode, Ambient Sound, ANC depth claims, ENC, Beamforming, AI Noise Reduction, A2DP, AVRCP, HFP, HSP, mSBC, Wideband speech, Latency, 2.4 GHz dongle, Dual-mode, Game Mode, Spatial Audio, Dolby Atmos, Head tracking, HRTF, Binaural, Virtual surround, EN 50332, Safe volume limit, dB(A), 3.5 mm, 2.5 mm, 4.4 mm balanced, MMCX, 2-pin, Detachable cable, Battery life, Charging case, Fast charge, Qi, USB-C charging, Battery capacity, Snapdragon Sound, LHDC, Sample rate, Bit depth, Lossless, Lossy, Dual audio, Bluetooth 5.0, CIS, BIS, Auracast Assistant, IEC 60529, IPX4, IPX7, IP57, Hi-Res Audio Wireless.

**Remaining roster (names only, no content):**

**Audio fundamentals:** Dynamic range, Sound signature, Bass boost, Equalizer (EQ), Crosstalk, Sibilance, Transient response, Group delay, Damping, Isolation (dB), Intermodulation distortion, Maximum input power, Driver diameter.

**Drivers and design:** Piezoelectric driver, Bone conduction, Dual-chamber driver, Diaphragm material, Beryllium, Graphene, LCP, Neodymium magnet, Neckband, Earpad, Ear tips, Memory foam, USB-C audio, 6.35 mm, XLR.

**Codecs and wireless:** LLAC, MQA, Hi-Res Audio (wired), Bluetooth 5.1, Bluetooth 6.0, Bluetooth Class, Range, Pairing, Fast Pair, Swift Pair, Find My, LE Power Control, EATT, PBP, TMAP, HAP, Codec negotiation.

**Noise control:** Wind noise reduction, Conversation awareness, NRR, Adaptive EQ, Occlusion effect, Pressure feeling.

**Microphone and calls:** MEMS microphone, Bone-conduction VAD, Wind-resistant mic, Microphone sensitivity, Sidetone, Mic polar pattern, Boom mic, HD Voice, LC3plus.

**Spatial audio:** 360 Reality Audio, DTS Headphone:X, 7.1.

**Power, durability and fit:** Standby time, Talk time, Battery health, USB-C PD, Sweat resistance, IP rating of case, Weight, Clamping force, Headband, Foldable, Fit tests, Ear detection, Wear sensor.

**Controls and software:** Touch controls, Companion app, Firmware update, Voice assistant, Multi-device, Auto-pause, Customizable EQ, Personalized sound, Hearing test, Hearing protection.

**Standards and certification:** IEC 60268-7, Bluetooth SIG qualification, Hi-Res Audio logo, JAS, THX, Dolby, Qualcomm certified, MFi, Made for Android.

**Product claims:** Studio-grade, Audiophile, Flagship ANC, Military-grade, Lag-free, 4K audio, Crystal clear calls.

## 8. Source register addendum (Pass 2)

- S49 RTINGS, Distortion audibility. https://www.rtings.com/headphones/learn/research/distortion-audibility
- S50 RTINGS, Harmonic distortion test. https://www.rtings.com/headphones/tests/sound-quality/harmonic-distortion
- S51 SoundGuys, What is THD. https://soundguys.com/what-is-distortion-thd-47149/
- S52 Head-Fi, Interpreting THD graphs. https://www.head-fi.org/threads/tutorial-%E2%80%93-interpreting-thd-and-thd-n-graphs.885876/
- S53 Headphones.com, SINAD. https://headphones.com/pages/evaluating-sinad-why-its-not-important
- S54 Texas Instruments SDAA313. https://www.ti.com/lit/pdf/sdaa313
- S55 Texas Instruments TLV320AIC3100 datasheet. https://ti.com/document-viewer/tlv320aic3100/datasheet
- S56 PS Audio, Audio specs. https://www.psaudio.com/blogs/copper/from-em-the-audiophile-s-guide-em-audio-specs-and-measuring
- S57 MakeUseOf, Soundstage vs imaging. https://www.makeuseof.com/soundstage-vs-audio-imaging/
- S58 Tom's Guide, Headphone jargon. https://www.tomsguide.com/audio/headphones/what-does-soundstage-mean-8-headphone-jargon-terms-explained
- S59 HeadphonesAddict, Soundstage. https://headphonesaddict.com/what-is-soundstage/
- S60 The Audio Stuff, Soundstage glossary. https://theaudiostuff.com/glossary/soundstage/
- S61 Science Insights, Soundstage. https://scienceinsights.org/what-is-soundstage-in-audio-and-why-does-it-matter/
- S62 Head-Fi, Soundstage vs imaging discussion. https://www.head-fi.org/threads/how-do-you-differentiate-between-soundstage-width-and-depth-and-accurate-imaging.851060
- S63 Harman Pro, AKG reference response. https://pro.harman.com/insights/akg/defining-the-standard-the-science-behind-akg-reference-response-studio-headphones/
- S64 SoundGuys, Target curves. https://www.soundguys.com/the-house-curve-how-we-make-our-target-headphone-responses-54290/
- S65 Crutchfield, Harman visit. https://www.crutchfield.com/learn/crutchfield-visits-harman.html
- S66 RTINGS, Target curve research. https://www.rtings.com/headphones/learn/research/frequency-response-1-8
- S67 Beyerdynamic, Headphone types. https://blog-na.beyerdynamic.com/what-types-of-headphones-are-there/
- S68 TechRadar, Open vs closed back. https://www.techradar.com/audio/headphones/open-back-vs-closed-back-headphones
- S69 Headphones.com, Open vs closed. https://headphones.com/pages/open-vs-closed-headphones
- S70 RTINGS, Open vs closed back. https://www.rtings.com/headphones/learn/open-vs-closed-back
- S71 What Hi-Fi? Headphone jargon (PressReader). https://www.pressreader.com/uk/what-hi-fi-uk/20190626/286500094708336
- S72 RTINGS, Headphone types. https://www.rtings.com/headphones/learn/over-ear-vs-on-ear-vs-in-ear-vs-earbuds-comparison
- S73 Soundcore, Types of headphones. https://www.soundcore.com/uk/blogs/headphones/types-of-headphones
- S74 LG, How noise cancelling works. https://www.lg.com/ae/lg-story/helpful-guide/how-does-noise-cancelling-work
- S75 Digit, ANC vs ENC. https://www.digit.in/features/audio-video/noise-cancellation-explained-anc-or-enc.html
- S76 Apple Support, ANC and Transparency. https://support.apple.com/en-kg/HT210643
- S77 Google Pixel Buds Help. https://support.google.com/googlepixelbuds/answer/7685360?hl=en-IN
- S78 TechRadar, Transparency mode. https://www.techradar.com/audio/headphones/what-is-transparency-mode
- S79 Screen Rant, AirPods Transparency. https://screenrant.com/apple-airpods-transparency-mode-works-purpose-benefits-explained/
- S80 Belkin, ANC and ENC. https://www.belkin.com/sg/company/blog/noise-cancelling-headphones-earbuds/
- S81 SlashGear, ANC vs ENC. https://www.slashgear.com/1988625/anc-vs-enc-noise-cancellation-pros-cons
- S82 Baseus, Mic array blog (vendor). https://www.baseus.com/blogs/content/how-a-5-mic-ai-array-creates-crystal-clear-call-quality
- S83 Shokz, Best earbuds guide (vendor). https://uk.shokz.com/blogs/guides/what-hifi-best-earbuds
- S85 Espressif, Bluetooth profiles. https://docs.espressif.com/projects/esp-idf/en/v6.1/esp32/api-guides/classic-bt/profiles-protocols.html
- S86 Wikiwand, A2DP. https://wikiwand.com/en/A2DP
- S87 NTI Audio, Testing Bluetooth. https://www.nti-audio.com/en/support/know-how/how-to-test-bluetooth-devices
- S88 Engadget, Bluetooth for gaming. https://www.engadget.com/2240120/bluetooth-headset-skip-for-better-gaming-experience/
- S89 Evetech, Reducing audio lag. https://evezone.evetech.co.za/deep-dives/how-to-reduce-audio-lag-when-using-a-wireless-gaming-headset
- S90 Digital Trends, Gaming mode test. https://digitaltrends.com/?p=3138306
- S91 Alibaba Product Insights, Latency (low quality). https://www.alibaba.com/product-insights/wireless-gaming-headset-vs-wired-is-latency-still-an-issue.html
- S92 HotHardware, Razer Hammerhead Pro. https://hothardware.com/news/razer-hammerhead-pro-hyperspeed-thx-earbuds-dongle-gaming
- S93 Bose, What is spatial audio. https://www.bose.com/stories/what-is-spatial-audio
- S94 IEEE TechNav, Spatial audio. https://technav.ieee.org/topic/spatial-audio/
- S95 SoundGuys, Surround headphones guide. https://www.soundguys.com/surround-sound-headphones-guide-49389/
- S96 Digital Trends, Spatial audio. https://digitaltrends.com/?p=2714175
- S97 Sound on Sound, Dolby PHRTF. https://www.soundonsound.com/node/4927301
- S98 ITU, Safe listening standards analysis. https://www.itu.int/en/ITU-T/Workshops-and-Seminars/safelistening/Documents/Standards\_for\_safe\_listening\_devices\_situation\_analysis\_report.pdf
- S99 ITU, Lund presentation. https://www.itu.int/en/ITU-T/Workshops-and-Seminars/safelistening/Documents/Abstracts-and-Presentations/S2P1-Thomas-Lund.pdf
- S100 PMC, Volume-limited headphones study. https://pmc.ncbi.nlm.nih.gov/articles/PMC6928536
- S101 ITU-T technical paper on H.870. https://www.itu.int/dms\_pub/itu-t/opb/tut/T-TUT-EHT-2024-2-MSW-E.docx
- S102 Hearing Review, Safe listening standards. https://hearingreview.com/hearing-loss/hearing-loss-prevention/risk-factors/standards-for-safe-listening-past-present-and-future
- S103 Bloom Audio, Connections guide. https://bloomaudio.com/blogs/articles/audiophile-101-headphone-connections-and-terminations
- S104 Campfire Audio, IEM cable guide. https://www.campfireaudio.com/blogs/insights/iem-cable-guide
- S105 HeadphonesAddict, Jacks and plugs. https://headphonesaddict.com/headphone-jacks-and-plugs/
- S106 Audio-Technica, A2DC connector. https://www.audio-technica.com/en-us/support/audio-solutions-question-of-the-week-why-does-audio-technica-use-the-a2dc-connector-for-many-of-its-headphones-with-detachable-cables
- S107 Nothing Support, Earbuds battery life. https://support.nothing.tech/hc/en-us/articles/47974705954961-How-long-is-the-battery-life-of-the-Earbuds
- S108 Nothing Support, Fast charging. https://support.nothing.tech/hc/en-us/articles/26184771466385-Do-the-Buds-support-fast-charging
- S109 Samsung, Galaxy Buds Live. https://www.samsung.com/hk\_en/news/product/galaxy-buds-live-wireless-noise-cancelling-earbuds
- S110 Best Buy Canada, Jabra Elite 85t review. https://blog.bestbuy.ca/?p=221272
- S111 iFixit, Galaxy Buds Live. https://www.ifixit.com/Topic/Samsung\_Galaxy\_Buds\_Live
- S112 Logitech, Zone True Wireless. https://logitech.com/zonetruewireless
- S115 Philips, earbuds spec sheet. https://www.documents.philips.com/assets/20231204/87bbc0e8ac8d46f78a72b0ce0049413e.pdf
- S116 Tom's Guide, Earbud battery life. https://www.tomsguide.com/opinion/i-test-headphones-and-these-5-wireless-earbuds-have-the-best-battery-life
- S117 Bluetooth SIG, LE Audio architecture (Dec 2019). https://bluetooth.com/?p=85903
- S120 Headphone Zone, IEM cables. https://www.headphonezone.in/collections/iem-cables?page=2
- S122 Currys, Nothing Ear listing. https://www.currys.co.uk/products/nothing-ear-wireless-bluetooth-noisecancelling-earbuds-white-10265525.html
