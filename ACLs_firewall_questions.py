firewall_questions = [
    {
        "question": "What step provides the quickest way to completely remove an ACL from a router?",
        "options": [
            "a) Removal of the ACEs is the only step required.",
            "b) Modify the number of the ACL so that it doesn’t match the ACL associated with the interface.",
            "c) Copy the ACL into a text editor, add 'no' before each ACE, then copy the ACL back into the router.",
            "d) Use the no access-list command to remove the entire ACL.",
            "e) Use the 'no' keyword and the sequence number of every ACE within the named ACL to be removed."
        ],
        "answer": "d"
    },
    {
        "question": "What possible limitation of using a firewall in a network?",
        "options": [
            "a) It provides accessibility of applications and sensitive resources to external untrusted users.",
            "b) It increases security management complexity by requiring off-loading network access control to the device.",
            "c) A misconfigured firewall can create a single point of failure.",
            "d) It cannot sanitize protocol flows."
        ],
        "answer": "c"
    },
    {
        "question": "What statement describes the characteristics of IPv6 access control lists?",
        "options": [
            "a) They permit ICMPv6 router advertisements by default.",
            "b) They can be named or numbered.",
            "c) They include two implicit permit statements by default.",
            "d) They are applied to an interface with the ip access-group command."
        ],
        "answer": "c"
    },
    {
        "question": "When creating an ACL, which keyword should be used to document and interpret the purpose of the ACL statement on a Cisco device?",
        "options": [
            "a) remark",
            "b) description",
            "c) established",
            "d) eq"
        ],
        "answer": "a"
    },
    {
        "question": "In the creation of an IPv6 ACL, what is the purpose of the implicit final command entries, permit icmp any any nd-na and permit icmp any any nd-ns?",
        "options": [
            "a) to allow forwarding of ICMPv6 packets",
            "b) to allow automatic address configuration",
            "c) to allow IPv6 to MAC address resolution",
            "d) to allow forwarding of IPv6 multicast packets"
        ],
        "answer": "c"
    },
    {
        "question": "What statement describes the characteristics of IPv6 access control lists?",
        "options": [
            "a) They permit ICMPv6 router advertisements by default.",
            "b) They can be named or numbered.",
            "c) They are applied to an interface with the ip access-group command.",
            "d) They use prefix lengths to indicate how much of an address to match."
        ],
        "answer": "d"
    },
    {
        "question": "What statement describes the configuration model for Cisco IOS firewalls?",
        "options": [
            "a) ZPF must be enabled in the router configuration before enabling an IOS Classic Firewall.",
            "b) IOS Classic Firewalls and ZPF models can be enabled on a router concurrently.",
            "c) Both IOS Classic Firewall and ZPF models require ACLs to define traffic filtering policies.",
            "d) IOS Classic Firewalls must be enabled in the router configuration before enabling ZPF."
        ],
        "answer": "b"
    },
    {
        "question": "When implementing components into an enterprise network, what is the purpose of a firewall?",
        "options": [
            "a) A firewall is a system that inspects network traffic and makes forwarding decisions based solely on Layer 2 Ethernet MAC addresses.",
            "b) A firewall is a system that is designed to secure, monitor, and manage mobile devices, including corporate-owned devices and employee-owned devices.",
            "c) A firewall is a system that stores vast quantities of sensitive and business-critical information.",
            "d) A firewall is a system that enforces an access control policy between internal corporate networks and external networks."
        ],
        "answer": "d"
    },
    {
        "question": "Which type of firewall makes use of a proxy server to connect to remote servers on behalf of clients?",
        "options": [
            "a) stateful firewall",
            "b) stateless firewall",
            "c) packet filtering firewall",
            "d) application gateway firewall"
        ],
        "answer": "d"
    },
    {
        "question": "What step provides the quickest way to completely remove an ACL from a router?",
        "options": [
            "a) Removal of the ACEs is the only step required.",
            "b) Modify the number of the ACL so that it doesn’t match the ACL associated with the interface.",
            "c) Copy the ACL into a text editor, add 'no' before each ACE, then copy the ACL back into the router.",
            "d) Use the 'no' keyword and the sequence number of every ACE within the named ACL to be removed."
            "e) Remove the inbound/outbound reference to the ACL from the interface.",
        ],
        "answer": "e"
    },
    {
        "question": "How does a firewall handle traffic when it is originating from the public network and traveling to the private network?",
        "options": [
            "a) Traffic that is originating from the public network is not inspected when traveling to the private network.",
            "b) Traffic that is originating from the public network is usually blocked when traveling to the private network.",
            "c) Traffic that is originating from the public network is usually permitted with little or no restrictions when traveling to the private network.",
            "d) Traffic that is originating from the public network is selectively permitted when traveling to the private network."
        ],
        "answer": "c"
    },
    {
        "question": "What statement describes the configuration model for Cisco IOS firewalls?",
        "options": [
            "a) ZPF must be enabled in the router configuration before enabling an IOS Classic Firewall.",
            "b) The IOS Classic Firewall and ZPF cannot be combined on a single interface.",
            "c) Both IOS Classic Firewall and ZPF models require ACLs to define traffic filtering policies.",
            "d) IOS Classic Firewalls must be enabled in the router configuration before enabling ZPF."
        ],
        "answer": "b"
    },
    {
        "question": "Designing a ZPF requires several steps. Which step involves dictating the number of devices between most-secure and least-secure zones and determining redundant devices?",
        "options": [
            "a) determine the zones",
            "b) design the physical infrastructure",
            "c) establish policies between zones",
            "d) identify subsets within zones and merge traffic requirements"
        ],
        "answer": "b"
    },
    {
        "question": "When using Cisco IOS zone-based policy firewall, where is the inspection policy applied?",
        "options": [
            "a) to a global service policy",
            "b) to a zone",
            "c) to an interface",
            "d) to a zone pair"
        ],
        "answer": "d"
    },
    {
        "question": "What is the first step in configuring a Cisco IOS zone-based policy firewall via the CLI?",
        "options": [
            "a) Define traffic classes.",
            "b) Assign router interfaces to zones.",
            "c) Define firewall policies.",
            "d) Assign policy maps to zone pairs.",
            "e) Create zones."
        ],
        "answer": "e"
    },
    {
        "question": "What is one benefit of using a stateful firewall instead of a proxy server?",
        "options": [
            "a) ability to perform user authentication",
            "b) better performance",
            "c) ability to perform packet filtering",
            "d) prevention of Layer 7 attacks"
        ],
        "answer": "b"
    },
    {
        "question": "Which statement describes a typical security policy for a DMZ firewall configuration?",
        "options": [
            "a) Traffic that originates from the DMZ interface is selectively permitted to the outside interface.",
            "b) Return traffic from the inside that is associated with traffic originating from the outside is permitted to traverse from the inside interface to the outside interface.",
            "c) Return traffic from the outside that is associated with traffic originating from the inside is permitted to traverse from the outside interface to the DMZ interface.",
            "d) Traffic that originates from the inside interface is generally blocked entirely or very selectively permitted to the outside interface.",
            "e) Traffic that originates from the outside interface is permitted to traverse the firewall to the inside interface with few or no restrictions."
        ],
        "answer": "a"
    },
     {
        "question": "What rule about interfaces is valid when implementing a Zone-Based Policy Firewall?",
        "options": [
            "a) If both interfaces are members of the same zone, all traffic will be passed.",
            "b) If one interface is a zone member, but the other is not, all traffic will be passed.",
            "c) If both interfaces belong to the same zone-pair and a policy exists, all traffic will be passed.",
            "d) If one interface is a zone member and a zone-pair exists, all traffic will be passed."
        ],
        "answer": "a"
    },
    {
        "question": "What is one limitation of a stateful firewall?",
        "options": [
            "a) weak user authentication",
            "b) cannot filter unnecessary traffic",
            "c) not as effective with UDP- or ICMP-based traffic",
            "d) poor log information"
        ],
        "answer": "c"
    },
    {
        "question": "What characteristic is shared by both standard and extended ACLs?",
        "options": [
            "a) Both kinds of ACLs can filter based on protocol type.",
            "b) Both can permit or deny specific services by port number.",
            "c) Both can be created by using either a descriptive name or number.",
            "d) Both filter packets for a specific destination host IP address."
        ],
        "answer": "c"
    },
    {
        "question": "Which statement describes Cisco IOS Zone-Based Policy Firewall operation?",
        "options": [
            "a) The pass action works in only one direction.",
            "b) Router management interfaces must be manually assigned to the self zone.",
            "c) A router interface can belong to multiple zones.",
            "d) Service policies are applied in interface configuration mode."
        ],
        "answer": "a"
    },
    {
        "question": "What is the result in the self zone if a router is the source or destination of traffic?",
        "options": [
            "a) No traffic is permitted.",
            "b) All traffic is permitted.",
            "c) Only traffic that originates in the router is permitted.",
            "d) Only traffic that is destined for the router is permitted."
        ],
        "answer": "b"
    },
    {
        "question": "What is a characteristic of ACLs?",
        "options": [
            "a) Standard ACLs can filter on source TCP and UDP ports.",
            "b) Extended ACLs can filter on source and destination IP addresses.",
            "c) Standard ACLs can filter on source and destination IP addresses.",
            "d) Standard ACLs can filter on source and destination TCP and UDP ports."
        ],
        "answer": "b"
    },
    {
        "question": "What single access list statement matches all of the following networks? 192.168.16.0, 192.168.17.0, 192.168.18.0, 192.168.19.0",
        "options": [
            "a) access-list 10 permit 192.168.16.0 0.0.3.255",
            "b) access-list 10 permit 192.168.16.0 0.0.0.255",
            "c) access-list 10 permit 192.168.16.0 0.0.15.255",
            "d) access-list 10 permit 192.168.0.0 0.0.15.255"
        ],
        "answer": "a"
    },
    {
        "question": "What characteristic is shared by both standard and extended ACLs?",
        "options": [
            "a) Both kinds of ACLs can filter based on protocol type.",
            "b) Both can permit or deny specific services by port number.",
            "c) Both include an implicit deny as a final statement.",
            "d) Both filter packets for a specific destination host IP address."
        ],
        "answer": "c"
    },
    {
        "question": "If the provided ACEs are in the same ACL, which ACE should be listed first in the ACL according to best practice?",
        "options": [
            "a) permit ip any any",
            "b) permit udp 172.16.0.0 0.0.255.255 host 172.16.1.5 eq snmptrap",
            "c) permit tcp 172.16.0.0 0.0.3.255 any established",
            "d) permit udp any any range 10000 20000",
            "e) deny udp any host 172.16.1.5 eq snmptrap",
            "f) deny tcp any any eq telnet"
        ],
        "answer": "b"
    },
    {
        "question": "To facilitate the troubleshooting process, which inbound ICMP message should be permitted on an outside interface?",
        "options": [
            "a) echo request",
            "b) echo reply",
            "c) time-stamp request",
            "d) time-stamp reply",
            "e) router advertisement"
        ],
        "answer": "b"
    },
    {
        "question": "What is a characteristic of a stateful firewall?",
        "options": [
            "a) uses static packet filtering techniques",
            "b) analyzes traffic at Layers 3, 4 and 5 of the OSI model",
            "c) uses complex ACLs which can be difficult to configure",
            "d) prevents Layer 7 attacks"
        ],
        "answer": "b"
    },
    {
        "question": "When implementing a ZPF, what is the default security setting when forwarding traffic between two interfaces in the same zone?",
        "options": [
            "a) Traffic between interfaces in the same zone is selectively forwarded based on Layer 3 information.",
            "b) Traffic between interfaces in the same zone is not subject to any policy and passes freely.",
            "c) Traffic between interfaces in the same zone is blocked.",
            "d) Traffic between interfaces in the same zone is selectively forwarded based on the default policy restrictions."
        ],
        "answer": "b"
    },
    {
        "question": "What rule about interfaces is valid when implementing a Zone-Based Policy Firewall?",
        "options": [
            "a) If neither interface is a zone member, then the action is to pass traffic.",
            "b) If one interface is a zone member, but the other is not, all traffic will be passed.",
            "c) If both interfaces belong to the same zone-pair and a policy exists, all traffic will be passed.",
            "d) If one interface is a zone member and a zone-pair exists, all traffic will be passed."
        ],
        "answer": "a"
    }
]
