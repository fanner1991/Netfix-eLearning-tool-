lay2_endpoint_questions = [
    {
        "question": "Why are traditional network security perimeters not suitable for the latest consumer-based network endpoint devices?",
        "options": [
            "a) These devices are not managed by the corporate IT department.",
            "b) These devices pose no risk to security as they are not directly connected to the corporate network.",
            "c) These devices connect to the corporate network through public wireless networks.",
            "d) These devices are more varied in type and are portable."
        ],
        "answer": "d"
    },
    {
        "question": "What internal LAN element needs to be secured?",
        "options": [
            "a) edge routers",
            "b) fiber connections",
            "c) switches",
            "d) cloud-based hosts"
        ],
        "answer": "c"
    },
    {
        "question": "What is an example of traditional host-based security measures?",
        "options": [
            "a) NAS",
            "b) 802.1X",
            "c) antimalware software",
            "d) host-based NAC"
        ],
        "answer": "c"
    },
    {
        "question": "In an 802.1x deployment, which device is a supplicant?",
        "options": [
            "a) RADIUS server",
            "b) access point",
            "c) switch",
            "d) end-user station"
        ],
        "answer": "d"
    },
    {
        "question": "A company implements 802.1X security on the corporate network. A PC is attached to the network but has not authenticated yet. Which 802.1X state is associated with this PC?",
        "options": [
            "a) err-disabled",
            "b) disabled",
            "c) unauthorized",
            "d) forwarding"
        ],
        "answer": "c"
    },
    {
        "question": "Which command is used as part of the 802.1X configuration to designate the authentication method that will be used?",
        "options": [
            "a) dot1x system-auth-control",
            "b) aaa authentication dot1x",
            "c) aaa new-model",
            "d) dot1x pae authenticator"
        ],
        "answer": "b"
    },
    {
        "question": "What is involved in an IP address spoofing attack?",
        "options": [
            "a) A rogue node replies to an ARP request with its own MAC address indicated for the target IP address.",
            "b) Bogus DHCPDISCOVER messages are sent to consume all the available IP addresses on a DHCP server.",
            "c) A rogue DHCP server provides false IP configuration parameters to legitimate DHCP clients.",
            "d) A legitimate network IP address is hijacked by a rogue node."
        ],
        "answer": "d"
    },
    {
        "question": "At which layer of the OSI model does Spanning Tree Protocol operate?",
        "options": [
            "a) Layer 1",
            "b) Layer 2",
            "c) Layer 3",
            "d) Layer 4"
        ],
        "answer": "b"
    },
    {
        "question": "A network administrator uses the 'spanning-tree loopguard default' global configuration command to enable Loop Guard on switches. What components in a LAN are protected with Loop Guard?",
        "options": [
            "a) All Root Guard enabled ports.",
            "b) All PortFast enabled ports.",
            "c) All point-to-point links between switches.",
            "d) All BPDU Guard enabled ports."
        ],
        "answer": "c"
    },
     {
        "question": "What is an example of traditional host-based security measures?",
        "options": [
            "a) NAS",
            "b) 802.1X",
            "c) host-based IPS",
            "d) host-based NAC"
        ],
        "answer": "c"
    },



    {
        "question": "Which procedure is recommended to mitigate the chances of ARP spoofing?",
        "options": [
            "a) Enable DHCP snooping on selected VLANs.",
            "b) Enable IP Source Guard on trusted ports.",
            "c) Enable DAI on the management VLAN.",
            "d) Enable port security globally."
        ],
        "answer": "a"
    },
    {
        "question": "Which protocol should be used to mitigate the vulnerability of using Telnet to remotely manage network devices?",
        "options": [
            "a) SNMP",
            "b) TFTP",
            "c) SSH",
            "d) SCP"
        ],
        "answer": "c"
    },
    {
        "question": "How can DHCP spoofing attacks be mitigated?",
        "options": [
            "a) by disabling DTP negotiations on nontrunking ports",
            "b) by implementing port security",
            "c) by the application of the ip verify source command to untrusted ports​",
            "d) by implementing DHCP snooping on trusted ports"
        ],
        "answer": "d"
    },
    {
        "question": "Two devices that are connected to the same switch need to be totally isolated from one another. Which Cisco switch security feature will provide this isolation?",
        "options": [
            "a) PVLAN Edge",
            "b) DTP",
            "c) SPAN",
            "d) BPDU guard"
        ],
        "answer": "a"
    },
    {
        "question": "What is the behavior of a switch as a result of a successful CAM table attack?",
        "options": [
            "a) The switch will drop all received frames.",
            "b) The switch interfaces will transition to the error-disabled state.",
            "c) The switch will forward all received frames to all other ports.",
            "d) The switch will shut down."
        ],
        "answer": "c"
    },
    {
        "question": "Which protocol defines port-based authentication to restrict unauthorized hosts from connecting to the LAN through publicly accessible switch ports?",
        "options": [
            "a) RADIUS",
            "b) TACACS+",
            "c) 802.1x",
            "d) SSH"
        ],
        "answer": "c"
    },
    {
        "question": "What device is considered a supplicant during the 802.1X authentication process?",
        "options": [
            "a) the router that is serving as the default gateway",
            "b) the authentication server that is performing client authentication",
            "c) the client that is requesting authentication",
            "d) the switch that is controlling network access"
        ],
        "answer": "c"
    },
    {
        "question": "Which term describes the role of a Cisco switch in the 802.1X port-based access control?",
        "options": [
            "a) authenticator",
            "b) supplicant",
            "c) agent",
            "d) authentication server"
        ],
        "answer": "a"
    },
    {
        "question": "What type of data does the DLP feature of Cisco Email Security Appliance scan in order to prevent customer data from being leaked outside of the company?",
        "options": [
            "a) inbound messages",
            "b) outbound messages",
            "c) messages stored on a client device",
            "d) messages stored on the email server"
        ],
        "answer": "b"
    },
    {
        "question": "What is the goal of the Cisco NAC framework and the Cisco NAC appliance?",
        "options": [
            "a) to ensure that only hosts that are authenticated and have had their security posture examined and approved are permitted onto the network",
            "b) to monitor data from the company to the ISP in order to build a real-time database of current spam threats from both internal and external sources",
            "c) to provide anti-malware scanning at the network perimeter for both authenticated and non-authenticated devices",
            "d) to provide protection against a wide variety of web-based threats, including adware, phishing attacks, Trojan horses, and worms"
        ],
        "answer": "a"
    },
    {
        "question": "Which Cisco solution helps prevent MAC and IP address spoofing attacks?",
        "options": [
            "a) Port Security",
            "b) DHCP Snooping",
            "c) IP Source Guard",
            "d) Dynamic ARP Inspection"
        ],
        "answer": "c"
    },
    {
        "question": "What Layer 2 attack is mitigated by disabling Dynamic Trunking Protocol?",
        "options": [
            "a) VLAN hopping",
            "b) DHCP spoofing",
            "c) ARP poisoning",
            "d) ARP spoofing"
        ],
        "answer": "a"
    },
    {
        "question": "What is the result of a DHCP starvation attack?",
        "options": [
            "a) Legitimate clients are unable to lease IP addresses.",
            "b) Clients receive IP address assignments from a rogue DHCP server.",
            "c) The attacker provides incorrect DNS and default gateway information to clients.",
            "d) The IP addresses assigned to legitimate clients are hijacked."
        ],
        "answer": "a"
    },
    {
        "question": "A network administrator is configuring DAI on a switch with the command ip arp inspection validate dst-mac. What is the purpose of this configuration command?",
        "options": [
            "a) to check the destination MAC address in the Ethernet header against the MAC address table",
            "b) to check the destination MAC address in the Ethernet header against the user-configured ARP ACLs",
            "c) to check the destination MAC address in the Ethernet header against the target MAC address in the ARP body",
            "d) to check the destination MAC address in the Ethernet header against the source MAC address in the ARP body"
        ],
        "answer": "c"
    }




]
