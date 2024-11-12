int_prevention_questions = [
    {
        "question": "What is a characteristic of both IPS and IDS sensors?",
        "options": [
            "a) neither introduce latency or jitter",
            "b) both use signatures to detect patterns",
            "c) both are deployed inline in the data stream",
            "d) both can stop trigger packets"
        ],
        "answer": "b"
    },
    {
        "question": "What is an advantage of using an IPS?",
        "options": [
            "a) It is installed outside of the data traffic flow.",
            "b) It does not impact network traffic if there is a sensor overload.",
            "c) It can stop trigger packets.",
            "d) It has no impact on network latency."
        ],
        "answer": "c"
    },
    {
        "question": "What is a characteristic of an IDS?",
        "options": [
            "a) It can affect network performance by introducing latency and jitter.",
            "b) It often requires assistance from other network devices to respond to an attack.",
            "c) It is installed inline with the network traffic flow.",
            "d) It can be configured to drop trigger packets that are associated with a connection."
        ],
        "answer": "b"
    },
    {
        "question": "What characteristic of an IPS operating in promiscuous mode?",
        "options": [
            "a) It can stop malicious traffic from reaching the intended target for all types of attacks.",
            "b) It sits directly in the path of the traffic flow.",
            "c) It requires the assistance of another network device to respond to an attack.",
            "d) It sends alerts and drops any malicious packets."
        ],
        "answer": "c"
    },
    {
        "question": "Which tool can perform real-time traffic and port analysis, and can also detect port scans, fingerprinting and buffer overflow attacks?",
        "options": [
            "a) SIEM",
            "b) Nmap",
            "c) Snort",
            "d) Netflow"
        ],
        "answer": "c"
    },
    {
        "question": "Which Snort IPS feature enables a router to download rule sets directly from cisco.com or snort.org?",
        "options": [
            "a) Snort rule set pull",
            "b) Signature allowed listing",
            "c) Snort rule set push",
            "d) Snort rule set updates"
        ],
        "answer": "a"
    },
    {
        "question": "What is a minimum system requirement to activate Snort IPS functionality on a Cisco router?",
        "options": [
            "a) at least 4 GB RAM",
            "b) at least 4 GB flash",
            "c) ISR 2900 or higher",
            "d) K9 license"
        ],
        "answer": "d"
    },
    {
        "question": "What is PulledPork?",
        "options": [
            "a) an open source network IPS that performs real-time traffic analysis and generates alerts when threats are detected on IP networks",
            "b) a centralized management tool to push the rule sets based on preconfigured policy, to Cisco routers",
            "c) a virtual service container that runs on the Cisco ISR router operating system",
            "d) a rule management application that can be used to automatically download Snort rule updates"
        ],
        "answer": "d"
    },
    {
        "question": "What action can an IPS perform whenever a signature detects the activity for which it is configured?",
        "options": [
            "a) disable the link",
            "b) reconverge the network",
            "c) drop or prevent the activity",
            "d) restart the infected device"
        ],
        "answer": "c"
    },
    {
        "question": "Which IPS signature trigger category uses a decoy server to divert attacks away from production devices?",
        "options": [
            "a) honey pot-based detection",
            "b) policy-based detection",
            "c) pattern-based detection",
            "d) anomaly-based detection"
        ],
        "answer": "a"
    },
    {
        "question": "What situation will generate a true negative IPS alarm type?",
        "options": [
            "a) normal traffic that generates a false alarm",
            "b) a verified security incident that is detected",
            "c) a known attack that is not detected",
            "d) normal traffic that is correctly being ignored and forwarded"
        ],
        "answer": "d"
    },
    {
        "question": "What is provided by the fail open and close functionality of Snort IPS?",
        "options": [
            "a) provides the ability to automatically disable problematic signatures that routinely cause false positives and pass traffic",
            "b) blocks the traffic flow or bypasses IPS checking in the event of an IPS engine failure",
            "c) keeps Snort current with the latest threat protection and term-based subscriptions",
            "d) keeps track of the health of the Snort engine that is running in the service container"
        ],
        "answer": "b"
    },
    {
        "question": "What is a characteristic of the Community Rule Set type of Snort term-based subscriptions?",
        "options": [
            "a) it has 60-day delayed access to updated signatures",
            "b) it uses Cisco Talos to provide coverage in advance of exploits",
            "c) it is fully supported by Cisco",
            "d) it is available for free"
        ],
        "answer": "d"
    },
    {
        "question": "What is a characteristic of the connectivity policy setting when configuring Snort threat protection?",
        "options": [
            "a) it attempts to balance network security with network performance",
            "b) it prioritizes security over connectivity",
            "c) it provides the lowest level of protection",
            "d) it enables the highest number of signatures to be verified"
        ],
        "answer": "c"
    },
    {
        "question": "What is contained in an OVA file?",
        "options": [
            "a) a current compilation of known threats and prevention mechanisms",
            "b) an installable version of a virtual machine",
            "c) a list of atomic and composite signatures",
            "d) a set of rules for an IDS or IPS to detect intrusion activity"
        ],
        "answer": "b"
    },
    {
        "question": "What is a network tap?",
        "options": [
            "a) a Cisco technology that provides statistics on packets flowing through a router or multilayer switch",
            "b) a technology used to provide real-time reporting and long-term analysis of security events",
            "c) a feature supported on Cisco switches that enables the switch to copy frames and forward them to an analysis device",
            "d) a passive device that forwards all traffic and physical layer errors to an analysis device"
        ],
        "answer": "d"
    },
    {
        "question": "Which statement describes the function of the SPAN tool used in a Cisco switch?",
        "options": [
            "a) It is a secure channel for a switch to send logging to a syslog server.",
            "b) It provides interconnection between VLANs over multiple switches.",
            "c) It supports the SNMP trap operation on a switch.",
            "d) It copies the traffic from one switch port and sends it to another switch port that is connected to a monitoring device."
        ],
        "answer": "d"
    },
    {
        "question": "A network administrator is trying to download a valid file from an internal server. However, the process triggers an alert on a NMS tool. What condition describes this alert?",
        "options": [
            "a) false negative",
            "b) false positive",
            "c) true negative",
            "d) true positive"
        ],
        "answer": "b"
    },
    {
        "question": "What is an advantage of HIPS that is not provided by IDS?",
        "options": [
            "a) HIPS provides quick analysis of events through detailed logging.",
            "b) HIPS deploys sensors at network entry points and protects critical network segments.",
            "c) HIPS monitors network processes and protects critical files.",
            "d) HIPS protects critical system resources and monitors operating system processes."
        ],
        "answer": "d"
    },
    {
        "question": "What information must an IPS track in order to detect attacks matching a composite signature?",
        "options": [
            "a) the total number of packets in the attack",
            "b) the state of packets related to the attack",
            "c) the attacking period used by the attacker",
            "d) the network bandwidth consumed by all packets"
        ],
        "answer": "b"
    }
]
