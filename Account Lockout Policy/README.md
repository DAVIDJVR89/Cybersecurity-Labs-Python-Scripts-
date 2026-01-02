# Account Lockout Policy Simulation (Python)

### 🛡️ Objective
This project simulates a fundamental security control: the **Account Lockout Policy**. It implements a mechanism that monitors login attempts and disables access after a predefined threshold of failures, effectively mitigating automated brute-force attacks.

---

### 🛠️ Technical Implementation
* **Language:** Python
* **Control Flow:** Nested `while` loops for continuous user validation and credential checking.
* **Logic:**  `intentos_restantes`: A dynamic counter to track remaining attempts.
* `exit()`: Immediate termination of the session upon security violation.

---

### 🔍 Code Highlights & Logic
This script processes security access in two distinct phases:

# **User Identification:** 

**The script ensures the user exists before prompting for a password.**


If the input is different from usuario_correcto, using "continue" the script runs an infinite loop for the username input until it matches the record:

    while True:
        usuario_entrada = input(f"Introduzca su usuario:  ")
        if usuario_entrada != usuario_correcto:
            print("Usuario no válido, intente de nuevo.  ")
            continue

Once the previous condition does not occur and the input (usuario_entrada) matches with the correct one, the username will be identified and the script will proceed with the password validation.

        else:
            print("Usuario correcto.")



# **Credential Validation & Lockout:**

**First, we have to create the counter**

       while intentos_restantes > 0:
       
**We can calculate the current attempt number (1, 2, or 3)**

       intentos_actuales = max_intentos - intentos_restantes + 1  
       
**If the password is correct, access is granted and the script ends**

       if entrada_contraseña == contraseña_correcta:
           print("ACCESO AUTORIZADO")
           exit()
   
**If it fails, the counter decreases until it arrives to the third attempt. In the script, we will find this situation with the last "else":**

       else:
           intentos_restantes -= 1
            if intentos_restantes > 0:
                print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos. ")

            else:
                print(f"Máximo de intentos superados. Cuenta bloqueada por seguridad.")
                exit()
                
**Once intentos_restantes reaches zero, the exit() function prevents any further interaction, simulating a blocked account status.**
  
---

### ⚠️ Cybersecurity Significance
In a real-world environment, this policy is critical because:

- Brute-Force Protection: It prevents attackers from using automated scripts to guess thousands of password combinations.

- Risk Mitigation: It reduces the attack surface by limiting the time and attempts an unauthorized user has to gain access.

- Incident Detection: Frequent lockouts can serve as an Indicator of Compromise (IoC), alerting security teams to potential targeted attacks
