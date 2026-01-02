# My first Python SSH Dictionary Attack

**SSH Password Auditing:** From Logic Simulation to Virtual Lab

**📝 Project Overview**

This project documents my journey from understanding basic Python logic to implementing a functional cybersecurity tool. It demonstrates how a simple script can evolve into a practical security auditing tool when applied to a real-world environment.

---

**🛠 Phase 1: The Initial Logic (Conceptual Study)**

I started by creating a basic script to study how dictionary attacks work at a logical level.
My goal: To understand how a loop could iterate through a list of strings to find a match.

**Result:** A successful "proof of concept" that validated the logic of automated password guessing.

---

**🚀 Phase 2:  Real-World Application (The Virtual Lab)**

After mastering the logic, I wanted to see how it would perform in a live environment. I set up a specialized Virtual Lab:

- **Attacker:** Windows Host running Python.
- **Victim:** Kali Linux Virtual Machine with the SSH service active.
- **Connectivity:** I configured the VM's network to Bridge Mode. This was crucial to allow direct **IP** communication between the host and the guest, moving past initial "Connection Timed Out" obstacles.

---


**💻 Code Evolution & Features**

To make the script work against a real server, I integrated the **Paramiko** library. Key technical additions included:

- paramiko.SSHClient(): Used to programmatically manage the SSH connection.
- AutoAddPolicy(): To automatically handle SSH keys in a lab environment.
- try/except blocks: Vital for error handling; they allow the script to record a "failed attempt" and continue with the next password instead of crashing upon authentication failure.
- Timeouts: Implemented to manage network latency and improve script efficiency.

---

**📊 Results & Security Insights**

The script successfully identified the correct password (kali) within seconds. This experiment highlights several critical security vulnerabilities:

1. **Dictionary Vulnerability:** Using common or default passwords makes a system highly susceptible to automated attacks.
2. **The Need for Hardening:** This process shows why organizations must enforce Strong Password Policies.
3. **Mitigation Strategies:** To defend against the script I created, systems should implement:
    - Fail2Ban: To block IPs after multiple failed attempts.
    - SSH Key Authentication: Moving away from password-based logins entirely.
    - MFA (Multi-Factor Authentication): Adding an extra layer of defense.


---

**🧹 Lab Maintenance (Administrative Note)**
Following best practices for system administration, the environment was cleaned after the exercise:

Service Control: Stopped the SSH service on the target machine.

User Management: Deleted temporary test users and home directories.

Data Hygiene: Removed all temporary script files and logs from the virtual environment.
