# Forensics

## Digital Camouflage
Download the pcap file, open in wireshark and look for the http POST.
In the HTML form we find 

```
"userid" = "spiveyp"
"pswrd" = "S04xWjZQWFZ5OQ=="
```

Decoding the password from base64, and we get the password 

`KN1Z6PXVy9`.

---

## Special Agent User
Same as above.
In the request to "/" we find the user-agent string

`Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))\r\n`

This says that the browser in use is IE 9.

---

# Cryptography

## keyz
Just add your public ssh key and log in.
The flag is

`who_needs_pwords_anyways`

---

## Substitute
A basic substitution cipher. Perform frequency analysis reveals the flag

`IFONLYMODERNCRYPTOWASLIKETHIS`

---

## Hash101
The first problem is just binary to ascii conversion.

In the second problem we take each letter and convert it into hexadecimal.

The third problem is just the integer value of the above hexadecimal value.

In the fourth problem, we can just search for the MD5 hash online and find its pre-image.

---

## computeAES
Just base64 decode the cipher text and key, then run AES to decrypt the text. The flag is

`do_not_let_machines_win_3a0260e6`

---

## computeRSA
Just calculate the message using

`m = c^d (mod N) = 150815^1941 (mod 435979) = 133337`

---

# Reverse Engineering

## Hex2Raw
Convert the hex string to actual characters using

`echo <hex-string> | xxd -r -p | ./hex2raw`

The flag is

`75d3080d00407fa709c18a6cc69d1edc`

---

## Raw2Hex
Convert the byte array to a hex string using

`./raw2hex | xxd -p`

The flag is

`54686520666c61672069733ac3aeefde2d8fa0bc81f955314447a348`

---

# Web Exploitation

## What is Web
Looking around in the source code for the webpage reveals three parts of the flag:

* In the HTML file: `fab79c49d9e`
* In the CSS file:  `5ba511a0f24`
* In the JS file:   `36308e33e85`

---

# Binary Exploitation

## Bash Loop
A simple bash loop to enumerate all possible values:

```
for i in `seq 0 4096`;
do
	./bashloop $i | grep -i y
done
```

The flag is

`bcf9ac72d8721c303ae95239c2deacb3`

---

## Just No
The program is looking at an relative path for the _auth_ file. If we create a directory in our home folder named /problems/_hex-string_ and put an auth file in that directory with any string other than _no_, running the program will reveal the flag.

The flag is 

`08c0c2008f63cd44596dc13be08dd3ac`

---

# Misc

## Internet Kitties
Just connect to the service

`nc shell2017.picoctf.com 43099`

The flag is

`3f6cd68a982d8f0b72b04faf389e6a51`

---

## Piazza
Create an account at Piazza...

The flag is

`ask_and_hop3fully_we_can_help`

---

## Leaf of the Tree
Just follow the trunk folders

The flag is

`88636e09e72bafb444e7f6a8105dbc5d`

---

## looooong
Create a python script that generates the desired output.

The flag is

`with_some_recognition_and_training_delusions_become_glimpses_fbafb1011720def036b5aa32671f3710`

---

## Leaf of the Forest
Just run a simple _find_:

`find . -name "flag"`

The flag is 

`6c0d4a69fdff4ea12609fd1989749dd5`

---

## Worldchat
Connect to the chat and grep for _flagperson_.

`nv shell2017.picoctf.com 14747 | grep -i flagperson`

The flag is

`ab4b181f3bc927589e0d79a4845a3ace`

---
