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
