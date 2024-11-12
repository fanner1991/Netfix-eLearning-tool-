mon_devices_questions = [
    {
        "question": "A network administrator is analyzing the features supported by the multiple versions of SNMP. What feature is supported by SNMPv3 but not by SNMPv1 or SNMPv2c?",
        "options": [
            "a) community-based security",
            "b) SNMP trap mechanism",
            "c) message encryption",
            "d) bulk retrieval of MIB information"
        ],
        "answer": "c"
    },
    {
        "question": "Which privilege level is predefined for the privileged EXEC mode?",
        "options": [
            "a) level 0",
            "b) level 1",
            "c) level 15",
            "d) level 16"
        ],
        "answer": "c"
    },
    {
        "question": "What is a requirement to use the Secure Copy Protocol feature?",
        "options": [
            "a) At least one user with privilege level 1 has to be configured for local authentication.",
            "b) A command must be issued to enable the SCP server side functionality.",
            "c) A transfer can only originate from SCP clients that are routers.",
            "d) The Telnet protocol has to be configured on the SCP server side."
        ],
        "answer": "b"
    },
    {
        "question": "Which syslog message type is accessible only to an administrator and only via the Cisco CLI?",
        "options": [
            "a) errors",
            "b) alerts",
            "c) debugging",
            "d) emergency"
        ],
        "answer": "c"
    },
    {
        "question": "Which command will move the show access-lists command to privilege level 14?",
        "options": [
            "a) router(config)# privilege level 14 command show access-lists",
            "b) router(config)# privilege exec level 14 show access-lists",
            "c) router(config)# set privilege level 14 show access-lists",
            "d) router(config)# show access-lists privilege level 14"
        ],
        "answer": "b"
    },
    {
        "question": "Which authentication method stores usernames and passwords in the router and is ideal for small networks?",
        "options": [
            "a) server-based AAA over TACACS+",
            "b) local AAA over RADIUS",
            "c) server-based AAA",
            "d) local AAA over TACACS+",
            "e) local AAA",
            "f) server-based AAA over RADIUS"
        ],
        "answer": "e"
    },
    {
        "question": "A student is learning about role-based views and role-based view configurations. The student enters the Router(config)# parser view TECH-view command. What is the purpose of this command?",
        "options": [
            "a) to create a CLI view named TECH-view",
            "b) to enter the superview named TECH-view",
            "c) to check the current setup of the CLI view named TECH-view",
            "d) to enter the CLI view named TECH-view"
        ],
        "answer": "a"
    },
    {
        "question": "What is a characteristic of the Cisco IOS Resilient Configuration feature?",
        "options": [
            "a) It maintains a mirror image of the configuration file in RAM.",
            "b) It sends a backup copy of the IOS image to a TFTP server.",
            "c) It saves a secure copy of the primary image and device configuration that cannot be removed by a user.",
            "d) It is a universal feature that can be activated on all Cisco devices."
        ],
        "answer": "c"
    },
    {
        "question": "What IOS privilege levels are available to assign for custom user-level privileges?",
        "options": [
            "a) levels 1 through 15",
            "b) levels 0, 1, and 15",
            "c) levels 2 through 14",
            "d) levels 0 and 1"
        ],
        "answer": "c"
    },
    {
        "question": "What is the biggest issue with local implementation of AAA?",
        "options": [
            "a) Local implementation supports only TACACS+ servers.",
            "b) Local implementation cannot provide secure authentication.",
            "c) Local implementation does not scale well.",
            "d) Local implementation supports only RADIUS servers."
        ],
        "answer": "c"
    },
    {
        "question": "Which task is necessary to encrypt the transfer of data between the ACS server and the AAA-enabled router?",
        "options": [
            "a) Configure the key exactly the same way on the server and the router.",
            "b) Specify the single-connection keyword.",
            "c) Create a VPN tunnel between the server and the router.",
            "d) Use identical reserved ports on the server and the router."
        ],
        "answer": "a"
    },
    {
        "question": "A student is learning role-based CLI access and CLI view configurations. Which command should be used first for creating a CLI view named TECH-View?",
        "options": [
            "a) Router# enable view",
            "b) Router(config)# aaa new-model",
            "c) Router# enable view TECH-view",
            "d) Router(config)# parser view TECH-view"
        ],
        "answer": "b"
    },
    {
        "question": "Because of implemented security controls, a user can only access a server with FTP. Which AAA component accomplishes this?",
        "options": [
            "a) accessibility",
            "b) accounting",
            "c) auditing",
            "d) authentication",
            "e) authorization"
        ],
        "answer": "e"
    },
    {
        "question": "Which AAA component can be established using token cards?",
        "options": [
            "a) accounting",
            "b) authorization",
            "c) auditing",
            "d) authentication"
        ],
        "answer": "d"
    },
    {
        "question": "What is the primary function of the aaa authorization command?",
        "options": [
            "a) permit AAA server access to AAA client services",
            "b) limit authenticated user access to AAA client services",
            "c) permit authenticated user access to AAA client services",
            "d) limit AAA server access to AAA client services"
        ],
        "answer": "b"
    },  
    {
        "question": "An administrator needs to create a user account with custom access to most privileged EXEC commands. Which privilege command is used to create this custom account?",
        "options": [
            "a) privilege exec level 15",
            "b) privilege exec level 0",
            "c) privilege exec level 1",
            "d) privilege exec level 2"
        ],
        "answer": "d"
    },
    {
        "question": "A network administrator is analyzing the features supported by the multiple versions of SNMP. What feature is supported by SNMPv3 but not by SNMPv1 or SNMPv2c?",
        "options": [
            "a) community-based security",
            "b) SNMP trap mechanism",
            "c) message source validation",
            "d) bulk retrieval of MIB information"
        ],
        "answer": "c"
    },
    {
        "question": "A network administrator is configuring an AAA server to manage TACACS+ authentication. What is one of the attributes of TACACS+ authentication?",
        "options": [
            "a) TCP port 40",
            "b) single process for authentication and authorization",
            "c) UDP port 1645",
            "d) encryption for only the password of a user",
            "e) separate processes for authentication and authorization"
        ],
        "answer": "e"
    },
    {
        "question": "Which of the following is a characteristic of the RADIUS protocol?",
        "options": [
            "a) encryption of the entire body of the packet",
            "b) the use of UDP ports for authentication and accounting",
            "c) the separation of the authentication and authorization processes",
            "d) the use of TCP port 49"
        ],
        "answer": "b"
    },
    {
        "question": "What is the one major difference between local AAA authentication and using the login local command when configuring device access authentication?",
        "options": [
            "a) The login local command requires the administrator to manually configure the usernames and passwords, but local AAA authentication does not.",
            "b) Local AAA authentication allows more than one user account to be configured, but login local does not.",
            "c) Local AAA authentication provides a way to configure backup methods of authentication, but login local does not.",
            "d) The login local command uses local usernames and passwords stored on the router, but local AAA authentication does not."
        ],
        "answer": "d"
    },
    {
        "question": "A network administrator is configuring an AAA server to manage TACACS+ authentication. What is one of the attributes of TACACS+ authentication?",
        "options": [
            "a) TCP port 40",
            "b) single process for authentication and authorization",
            "c) UDP port 1645",
            "d) encryption for only the password of a user",
            "e) Encryption for all communication"
        ],
        "answer": "e"
    }
]
