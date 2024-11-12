vpn_questions = [
    {
        "question": "What statement describes the IPsec protocol framework?",
        "options": [
            "a) AH provides integrity and authentication.",
            "b) AH provides encryption and integrity.",
            "c) ESP uses UDP protocol 51.",
            "d) AH provides both authentication and encryption."
        ],
        "answer": "a"
    },
    {
        "question": "What technology is used to negotiate security associations and calculate shared keys for an IPsec VPN tunnel?",
        "options": [
            "a) PSK",
            "b) SHA",
            "c) 3DES",
            "d) IKE"
        ],
        "answer": "d"
    },
    {
        "question": "What takes place during IKE Phase 2 when establishing an IPsec VPN?",
        "options": [
            "a) Traffic is exchanged between IPsec peers.",
            "b) IPsec security associations are exchanged.",
            "c) ISAKMP security associations are exchanged.",
            "d) Interesting traffic is identified."
        ],
        "answer": "b"
    },
    {
        "question": "Router R1 has configured ISAKMP policies numbered 1, 5, 9, and 203. Router R2 only has default policies. How will R1 attempt to negotiate the IKE Phase 1 ISAKMP tunnel with R2?",
        "options": [
            "a) R1 and R2 cannot match policies because the policy numbers are different.",
            "b) R1 will attempt to match policy #1 with the most secure matching policy on R2.",
            "c) R1 will try to match policy #203 with the most secure default policy on R2.",
            "d) R1 will begin to try to match policy #1 with policy #65514 on R2."
        ],
        "answer": "b"
    },
    {
        "question": "When the CLI is used to configure an ISR for a site-to-site VPN connection, what is the purpose of the crypto map command in interface configuration mode?",
        "options": [
            "a) to configure the transform set",
            "b) to bind the interface to the ISAKMP policy",
            "c) to force IKE Phase 1 negotiations to begin",
            "d) to negotiate the SA policy"
        ],
        "answer": "b"
    },
    {
        "question": "Which statement describes the effect of key length in deterring an attacker from hacking through an encryption key?",
        "options": [
            "a) The length of a key does not affect the degree of security.",
            "b) The shorter the key, the harder it is to break.",
            "c) The length of a key will not vary between encryption algorithms.",
            "d) The longer the key, the more key possibilities exist."
        ],
        "answer": "d"
    },
    {
        "question": "What statements describe a remote access VPN?",
        "options": [
            "a) It requires hosts to send TCP/IP traffic through a VPN gateway.",
            "b) It connects entire networks to each other.",
            "c) It is used to connect individual hosts securely to a company network over the Internet.",
            "d) It requires static configuration of the VPN tunnel."
        ],
        "answer": "c"
    },
    {
        "question": "Which protocol creates a virtual point-to-point connection to tunnel unencrypted traffic between Cisco routers from a variety of protocols?",
        "options": [
            "a) IKE",
            "b) IPsec",
            "c) OSPF",
            "d) GRE"
        ],
        "answer": "d"
    },
    {
        "question": "How is 'tunneling' accomplished in a VPN?",
        "options": [
            "a) New headers from one or more VPN protocols encapsulate the original packets.",
            "b) All packets between two hosts are assigned to a single physical medium to ensure that the packets are kept private.",
            "c) Packets are disguised to look like other types of traffic so that they will be ignored by potential attackers.",
            "d) A dedicated circuit is established between the source and destination devices for the duration of the connection."
        ],
        "answer": "a"
    },
    {
        "question": "What scenario is an example of remote access VPNs?",
        "options": [
            "a) All users at a large branch office can access company resources through a single VPN connection.",
            "b) A small branch office with three employees has a Cisco ASA that is used to create a VPN connection to the HQ.",
            "c) A toy manufacturer has a permanent VPN connection to one of its parts suppliers.",
            "d) An employee who is working from home uses VPN client software on a laptop in order to connect to the company network."
        ],
        "answer": "d"
    },
    {
        "question": "Which statement accurately describes a characteristic of IPsec?",
        "options": [
            "a) IPsec works at the application layer and protects all application data.",
            "b) IPsec is a framework of standards developed by Cisco that relies on OSI algorithms.",
            "c) IPsec is a framework of proprietary standards that depend on Cisco specific algorithms.",
            "d) IPsec works at the transport layer and protects data at the network layer.",
            "e) IPsec is a framework of open standards that relies on existing algorithms."
        ],
        "answer": "e"
    },
    {
        "question": "Which is a requirement of a site-to-site VPN?",
        "options": [
            "a) It requires hosts to use VPN client software to encapsulate traffic.",
            "b) It requires the placement of a VPN server at the edge of the company network.",
            "c) It requires a VPN gateway at each end of the tunnel to encrypt and decrypt traffic.",
            "d) It requires a client/server architecture."
        ],
        "answer": "c"
    },
    {
        "question": "Consider the following configuration on a Cisco ASA: crypto ipsec transform-set ESP-DES-SHA esp-des esp-sha-hmac. What is the purpose of this command?",
        "options": [
            "a) to define the ISAKMP parameters that are used to establish the tunnel",
            "b) to define the encryption and integrity algorithms that are used to build the IPsec tunnel",
            "c) to define what traffic is allowed through and protected by the tunnel",
            "d) to define only the allowed encryption algorithms"
        ],
        "answer": "b"
    },
    {
        "question": "What is needed to define interesting traffic in the creation of an IPsec tunnel?",
        "options": [
            "a) security associations",
            "b) hashing algorithm",
            "c) access list",
            "d) transform set"
        ],
        "answer": "c"
    },
    {
        "question": "What is a function of the GRE protocol?",
        "options": [
            "a) to configure the set of encryption and hashing algorithms that will be used to transform the data sent through the IPsec tunnel",
            "b) to encapsulate multiple OSI Layer 3 protocol packet types inside an IP tunnel",
            "c) to configure the IPsec tunnel lifetime",
            "d) to provide encryption through the IPsec tunnel"
        ],
        "answer": "b"
    },
    {
        "question": "Two corporations have just completed a merger. The network engineer has been asked to connect the two corporate networks without the expense of leased lines. Which solution would be the most cost effective method of providing a proper and secure connection between the two corporate networks?",
        "options": [
            "a) Cisco AnyConnect Secure Mobility Client with SSL",
            "b) Cisco Secure Mobility Clientless SSL VPN",
            "c) Frame Relay",
            "d) remote access VPN using IPsec",
            "e) site-to-site VPN"
        ],
        "answer": "e"
    },
    {
        "question": "What type of traffic is supported by IPsec?",
        "options": [
            "a) IPsec supports all IPv4 traffic.",
            "b) IPsec supports layer 2 multicast traffic.",
            "c) IPsec supports all traffic permitted through an ACL.",
            "d) IPsec only supports unicast traffic."
        ],
        "answer": "d"
    }
]
