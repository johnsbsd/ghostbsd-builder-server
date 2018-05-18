#!/bin/sh
zfs send zroot/builder/amd64-12/build@ready | ssh root@198.27.68.94 zfs recv zroot/usr/home/jails/pkg_server/repos/GhostBSD-18/amd64/build
