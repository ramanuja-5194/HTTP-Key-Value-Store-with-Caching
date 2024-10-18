# HTTP-Key-Value-Store-with-Caching
## Overview
This involves implementing a network topology with a client, cache, and server. The goal is to optimize client-server interactions using caching.

## Contents
- `basic/` - Implementation for HTTP client-server interaction (Question 4).
- `star/` - Implementation for the webcache topology (Question 5).
- `pcap/` - Captured network traffic files.
- `README.md` - This document.

## Running the Code
### Prerequisites
- Python 2.7
- Mininet environment set up in the provided VM.

### Steps
1. **Setup:**
   - Place `basic/` and `star/` directories in `/home/p4/tutorials/exercises/` in the VM.

2. **Basic Topology :**
   - Navigate to `basic/` directory.
   - Run:
     ```bash
     make clean
     make run
     ```
   - In Mininet, open H1 and H2 terminals, then:
     - On H2: `bash h2-arp.sh && python server.py`
     - On H1: `bash h1-arp.sh && python client.py`
   - enter any of the 4 given options PUT/GET/DEL/QUIT.

3. **Star Topology :**
   - Navigate to `star/` directory.
   - Run:
     ```bash
     make
     ```
   - Open H1, H2, H3 terminals, then:
     - On H3: `bash h3-arp.sh && python server.py`
     - On H2: `bash h2-arp.sh && python cache.py`
     - On H1: `bash h1-arp.sh && python client.py`
     - enter any of the 3 given options PUT/GET/QUIT.

## Capturing Traffic
- Use Wireshark in the VM to capture `.pcap` files during tests.
