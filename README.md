# CaesarCipherCracker

## What Is Caesar Cipher
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.[1]

The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security.

*Taken From WIKI*

## Installing Process

* Download Python 3
* Download This Repo
* Type The Following Commands

```bash
cd CaesarCipherCracker
pip3 install -r requirements.txt 
```
#### Syntax
```bash
python3 casesar.py [keyword] [text] [key]
```
here, 
**keyword** = *"ENCRYPT" or "DECRYPT"* 
**text** = *"ANYTHING"* **key** = *"1-26"* 


## Usage
### Encryption

#### Example
```
python caesar.py ENCRYPT "Cryptic" 3
```
#### Output
```
Encrypted Text: "FU1SWLF"
```

### DECRYPTION
#### Syntax

```bash
python caesar.py DECRYPT "Cryptic" 
```
#### Output

```
[+] Attempt -- Shift: 1 Text: ET0RVKE
[+] Attempt -- Shift: 2 Text: DSZQUJD
[+] Attempt -- Shift: 3 Text: CRYPTIC
[+] Attempt -- Shift: 4 Text: BQXOSHB
[+] Attempt -- Shift: 5 Text: APWNRGA
[+] Attempt -- Shift: 6 Text:  OVMQF
[+] Attempt -- Shift: 7 Text: ?NULPE?
[+] Attempt -- Shift: 8 Text: *MTKOD*
[+] Attempt -- Shift: 9 Text: &LSJNC&
[+] Attempt -- Shift: 10 Text: #KRIMB#
[+] Attempt -- Shift: 11 Text: $JQHLA$
[+] Attempt -- Shift: 12 Text: @IPGK @
[+] Attempt -- Shift: 13 Text: !HOFJ?!
[+] Attempt -- Shift: 14 Text: 9GNEI*9
[+] Attempt -- Shift: 15 Text: 8FMDH&8
[+] Attempt -- Shift: 16 Text: 7ELCG#7
[+] Attempt -- Shift: 17 Text: 6DKBF$6
[+] Attempt -- Shift: 18 Text: 5CJAE@5
[+] Attempt -- Shift: 19 Text: 4BI D!4
[+] Attempt -- Shift: 20 Text: 3AH?C93
[+] Attempt -- Shift: 21 Text: 2 G*B82
[+] Attempt -- Shift: 22 Text: 1?F&A71
[+] Attempt -- Shift: 23 Text: 0*E# 60
[+] Attempt -- Shift: 24 Text: Z&D$?5Z
[+] Attempt -- Shift: 25 Text: Y#C@*4Y
[+] Attempt -- Shift: 26 Text: X$B!&3X
[+] Attempt -- Shift: 27 Text: W@A9#2W
[+] Attempt -- Shift: 28 Text: V! 8$1V
[+] Attempt -- Shift: 29 Text: U9?7@0U
[+] Attempt -- Shift: 30 Text: T8*6!ZT
[+] Attempt -- Shift: 31 Text: S7&59YS
[+] Attempt -- Shift: 32 Text: R6#48XR
[+] Attempt -- Shift: 33 Text: Q5$37WQ
[+] Attempt -- Shift: 34 Text: P4@26VP
[+] Attempt -- Shift: 35 Text: O3!15UO
[+] Attempt -- Shift: 36 Text: N2904TN
[+] Attempt -- Shift: 37 Text: M18Z3SM
[+] Attempt -- Shift: 38 Text: L07Y2RL
[+] Attempt -- Shift: 39 Text: KZ6X1QK
[+] Attempt -- Shift: 40 Text: JY5W0PJ
[+] Attempt -- Shift: 41 Text: IX4VZOI
[+] Attempt -- Shift: 42 Text: HW3UYNH
[+] Attempt -- Shift: 43 Text: GV2TXMG
[+] Attempt -- Shift: 44 Text: FU1SWLF
[+] Attempt -- Shift: 45 Text: ET0RVKE
[+] Attempt -- Shift: 46 Text: DSZQUJD
[+] Attempt -- Shift: 47 Text: CRYPTIC
[+] Attempt -- Shift: 48 Text: BQXOSHB
[+] Attempt -- Shift: 49 Text: APWNRGA
[+] Attempt -- Shift: 50 Text:  OVMQF
[+] Attempt -- Shift: 51 Text: ?NULPE?
[+] Attempt -- Shift: 52 Text: *MTKOD*
[+] Attempt -- Shift: 53 Text: &LSJNC&
[+] Attempt -- Shift: 54 Text: #KRIMB#
[+] Attempt -- Shift: 55 Text: $JQHLA$
[+] Attempt -- Shift: 56 Text: @IPGK @
[+] Attempt -- Shift: 57 Text: !HOFJ?!
[+] Attempt -- Shift: 58 Text: 9GNEI*9
[+] Attempt -- Shift: 59 Text: 8FMDH&8
[+] Attempt -- Shift: 60 Text: 7ELCG#7
[+] Attempt -- Shift: 61 Text: 6DKBF$6
[+] Attempt -- Shift: 62 Text: 5CJAE@5
[+] Attempt -- Shift: 63 Text: 4BI D!4
[+] Attempt -- Shift: 64 Text: 3AH?C93
[+] Attempt -- Shift: 65 Text: 2 G*B82
[+] Attempt -- Shift: 66 Text: 1?F&A71
[+] Attempt -- Shift: 67 Text: 0*E# 60
[+] Attempt -- Shift: 68 Text: Z&D$?5Z
[+] Attempt -- Shift: 69 Text: Y#C@*4Y
[+] Attempt -- Shift: 70 Text: X$B!&3X
[+] Attempt -- Shift: 71 Text: W@A9#2W
[+] Attempt -- Shift: 72 Text: V! 8$1V
[+] Attempt -- Shift: 73 Text: U9?7@0U
[+] Attempt -- Shift: 74 Text: T8*6!ZT
[+] Attempt -- Shift: 75 Text: S7&59YS
[+] Attempt -- Shift: 76 Text: R6#48XR
[+] Attempt -- Shift: 77 Text: Q5$37WQ
[+] Attempt -- Shift: 78 Text: P4@26VP
[+] Attempt -- Shift: 79 Text: O3!15UO
[+] Attempt -- Shift: 80 Text: N2904TN
[+] Attempt -- Shift: 81 Text: M18Z3SM
[+] Attempt -- Shift: 82 Text: L07Y2RL
[+] Attempt -- Shift: 83 Text: KZ6X1QK
[+] Attempt -- Shift: 84 Text: JY5W0PJ
[+] Attempt -- Shift: 85 Text: IX4VZOI
[+] Attempt -- Shift: 86 Text: HW3UYNH
[+] Attempt -- Shift: 87 Text: GV2TXMG
[+] All Possible Combination Tried!
```

#### Final Conclusion

```
[+] Attempt -- Shift: 3 Text: CRYPTIC
```

### Contribution
MIT. Feel Free Support Me.

