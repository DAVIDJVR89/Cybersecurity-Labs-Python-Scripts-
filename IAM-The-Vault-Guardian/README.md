# 🛡️ Vault Guardian: Python Hashing System

I’ve been having a blast exploring Python Identity and Access Management! 

While looking for hands-on exercises, I came across 'The Vault Guardian'. It has been an incredible learning experience, and I wanted to share the key security concepts I've mastered through this project.

---

## 🧠 Technical Workflow

### 1. Cryptographic Library
The first step is to import `hashlib`, the Python library responsible for hashing and cryptography.

**Important:** Hashing is a one-way process; once content is hashed, it can **NEVER** be decrypted.

---

### 2. The Hashing Function
**The `generar_hash(password)`** function defines how the system processes raw text before storage.
* **`def`**: Used to define the function for generating the password hash.
* **`.encode()`**: Converts the password string into binary format.
* **`.sha256()`**: Acts as a "shredder," creating a non-human-readable object that Python can process.
* **`.hexdigest()`**: Transforms the internal object into a readable string of letters (a-f) and numbers (0-9).
* **`return`**: Instructs the system to save this information as `hash_resultante` for database storage.

---

### 3. Data Storage
The system utilizes an in-memory database that exists only while the program is running.
* It uses a dictionary structure: `base_de_datos = {}`.
* It starts empty and is populated during execution.

---

### 4. User Registration (`registrar_usuario`)
This function handles the creation of new credentials:
* It captures a username and password via `input`.
* The script `base_de_datos[usuario] = generar_hash(password)` is vital as it hashes the input and stores the result inside the user profile in the database.
* This ensures the username and password correspond and are saved in the same location.

---

### 5. Authentication Logic (`login`)
The login process uses an intuitive `if/else` flow to verify access:
* **Username Check**: It verifies if the `usuario_ingresado` exists in the database.
* **Hash Validation**: It generates a new hash for the entered password and compares it against the hash stored in the database.
* **Access Control**: 
    * If they match, it prints "Access granted".
    * If they do not match, it prints "Incorrect password" or "User does not exist".
 
---

### 6. Interactive Menu
A `while True` loop provides a continuous interface for the user:
* **Option 1**: Register a new user.
* **Option 2**: Log in.
* **Option 3**: View the database status (Usernames and Hashes).
* **Option 4**: Exit the system using the `break` command to end the loop.
* **Error Handling**: Any other input is marked as invalid.

---

## 🔒 Security Summary
By selecting Option 3, you can view the stored usernames and their corresponding hashes. Even with this visibility, the original passwords remain **completely unknown** and protected by the SHA-256 algorithm.

---

![](https://img.shields.io/badge/SECURITY-UPGRADED-green?style=for-the-badge&logo=github)

## 🛡️ Security Upgrade: Protection against Brute-Force

I have upgraded the authentication engine to include two critical security layers that protect against common unauthorized access attempts:

### 1. Pre-Authentication User Validation
* **The Logic:** The system now verifies if a username exists in the database *before* proceeding to password entry.
* **IAM Impact:** This streamlines the authentication workflow and ensures that the system only processes credentials for valid identities, improving resource management.

### 2. Account Lockout Policy (Brute Force Protection)
* **The Logic:** A login attempt counter has been implemented. If the user exceeds the maximum allowed attempts, the system denies further access.
* **IAM Impact:** This is a fundamental defense mechanism against **Brute Force** and **Dictionary Attacks**. It prevents automated scripts from guessing passwords by enforcing a lockout period, significantly reducing the attack surface.

---

![](https://img.shields.io/badge/SECURITY-UPGRADED-green?style=for-the-badge&logo=github)

## 🔒 Latest Security Enhancements: Password Complexity Policy

I have upgraded the authentication engine to include a robust **Password Complexity Validator**. This ensures that all user credentials meet modern security standards before being processed.

### 1. Multi-Factor Character Validation
The system now enforces a strict policy where every password must contain at least:
* **One Uppercase Letter** (`A-Z`): To prevent simple lowercase-only attacks.
* **One Numeric Digit** (`0-9`): To increase the search space for brute-force attempts.
* **One Special Character** (e.g., `!@#$%^&*`): Utilizing the `string.punctuation` library to ensure high entropy.

### 2. Pre-Authentication Identity Check
* The system verifies if a username exists in the database *before* requesting a password, streamlining the IAM workflow.

### 3. Account Lockout Mechanism
* A login attempt counter protects the system against **Brute Force** and **Dictionary Attacks** by blocking access after 3 failed attempts.

### 4. Secure Hashing (SHA-256)
* Credentials are never stored in plain text. The system uses the `hashlib` library to generate and store secure SHA-256 hashes.

  

## 🧠 Technical Logic: For Loop & Flag System

To implement the **Password Complexity Policy**, the system uses a robust scanning logic based on a `for` loop and boolean flags (markers).

### 1. The "Scanner" (The For Loop)
The password is treated as a collection of individual characters. The script initiates a loop that iterates through every single character:
* `for caracter in password:`: This line tells Python to pick up the first letter, process it, then the second, and so on, until the entire string has been scanned.

### 2. The "Detectors" (The Flags)
Before the scan begins, the system initializes three boolean variables (flags) set to `False`:
* `has_capital = False`
* `has_number = False`
* `has_symbol = False`

As the loop processes each character, it uses conditional statements (`if`) to check the character type. For example, if a number is detected, the `has_number` flag is flipped to `True`. Once a flag is set to `True`, it remains "active" regardless of what the following characters are.

### 3. The Final Validation
The final security check occurs **outside** the loop. The system only grants access if all three flags are `True`. This ensures the entire password has been evaluated against the IAM policy before any hash is generated or any user is created.

---

## 🛠️ Key IAM Concepts Applied

* **Authentication:** Robust identity verification.
* **Availability:** Preventing service exhaustion by blocking malicious actors.
* **Security Best Practices:** Implementing "Fail-Safe" mechanisms to protect user credentials.


---


*Developed as part of a Cybersecurity & IAM learning path.*
