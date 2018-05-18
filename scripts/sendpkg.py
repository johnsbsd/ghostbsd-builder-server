#!/usr/bin/env python
import pexpect
 
password = ''

pex = pexpect.spawn("sh sendzfs.sh")
pex.expect('Enter passphrase')
pex.sendline(password)
pex.interact()

