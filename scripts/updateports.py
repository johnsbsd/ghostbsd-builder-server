import pexpect
from subprocess import Popen, PIPE, call
from getpass import getpass
from os import path, chdir
from sys import argv
import getopt
 
password = ''
#try:
#    myopts, args = getopt.getopt(argv[1:], "p:")
#except getopt.GetoptError as e:
#    print(str(e))
#    print("Usage: %s -p passphrase" % argv[0])
#    exit()
 
#for output, arg in myopts:
#    if output == '-p':
#        password = arg

if path.isdir('/root/freebsd-ports') is False:
    foo = pexpect.spawn('git clone git+ssh://git@github.com/GhostBSD/freebsd-ports.git')
    foo.expect('Enter passphrase')
    foo.sendline(password)
    foo.interact()

remotegit = Popen('cd freebsd-ports && git remote', stdout=PIPE, shell=True)
if 'fbsdports' not in remotegit.stdout.read():
    call('cd freebsd-ports && git remote add fbsdports https://github.com/freebsd/freebsd-ports.git', shell=True)

call('cd freebsd-ports && git checkout master', shell=True)
call('cd freebsd-ports && git fetch fbsdports', shell=True)
call('cd freebsd-ports && git merge fbsdports/master', shell=True)

pex = pexpect.spawn('sh pushports.sh')
pex.expect('Enter passphrase')
pex.sendline(password)
pex.interact()

