# This file contains challenge data for the CTF platform

medium_challenges = [
    {
        "name": "SQL Injection",
        "description": """You have found a login page for a vulnerable website. 
Can you bypass the authentication and find the flag?

Example login form:
```
Username: admin
Password: password
```

Hint: The query might look like:
```sql
SELECT * FROM users WHERE username = '[INPUT]' AND password = '[INPUT]';
```""",
        "points": 250,
        "flag": "flag{sql_injection_master}",
        "difficulty": "Medium",
        "hints": ["Try using the ' character to break the SQL query", "Consider what happens when you inject OR 1=1"]
    },
    {
        "name": "Broken Hashing",
        "description": """We found this hash in a database: 5f4dcc3b5aa765d61d8327deb882cf99
Can you figure out what it hashes to? The flag is flag{plaintext}""",
        "points": 200,
        "flag": "flag{password}",
        "difficulty": "Medium",
        "hints": ["This is an MD5 hash", "Try using rainbow tables or online hash crackers"]
    },
    {
        "name": "Buffer Overflow",
        "description": """This program has a buffer overflow vulnerability. Exploit it to get the flag.

```c
#include <stdio.h>
#include <string.h>

void win() {
    printf("Congratulations! Here's your flag: flag{buffer_overflows_are_classic}\n");
}

void vulnerable() {
    char buffer[64];
    gets(buffer);
}

int main() {
    vulnerable();
    return 0;
}
```""",
        "points": 300,
        "flag": "flag{buffer_overflows_are_classic}",
        "difficulty": "Medium",
        "hints": ["The buffer is 64 bytes, what happens if you input more?", "You need to overwrite the return address to point to the win() function"]
    },
    {
        "name": "Cookie Monster",
        "description": """This website stores a cookie with your role. Can you change it to 'admin' to get the flag?

Example cookie:
```
user_role=guest
```""",
        "points": 250,
        "flag": "flag{cookie_monster_ate_security}",
        "difficulty": "Medium",
        "hints": ["Use browser dev tools to inspect cookies", "Try modifying the cookie value"]
    },
    {
        "name": "JWT Weakness",
        "description": """This API uses JWT for authentication. We found a token:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZSI6InVzZXIiLCJpYXQiOjE1MTYyMzkwMjJ9.J_RIFkHSFZO4uk8SvhhzTJO9HmLLKzJ5f87dpLfFN4w
```

Can you modify it to gain admin access?""",
        "points": 350,
        "flag": "flag{jwt_algorithm_confusion}",
        "difficulty": "Medium",
        "hints": ["Look at the algorithm being used", "JWT has a 'none' algorithm vulnerability"]
    },
    {
        "name": "Steganography",
        "description": "There's a message hidden in this innocent-looking image. Can you extract it?",
        "points": 300,
        "flag": "flag{hidden_in_plain_pixels}",
        "difficulty": "Medium",
        "hints": ["Look at the least significant bits (LSB)", "Try using steganography tools like steghide or zsteg"]
    },
    {
        "name": "Command Injection",
        "description": """This web application runs a ping command on user input:

```php
<?php
   $target = $_GET['ip'];
   system("ping -c 3 " . $target);
?>
```

Can you inject a command to read the flag file located at /var/www/flag.txt?""",
        "points": 250,
        "flag": "flag{command_injection_vulnerability}",
        "difficulty": "Medium",
        "hints": ["Think about how to terminate the ping command", "Try using ; or && to add another command"]
    },
    {
        "name": "RSA Decrypt",
        "description": """We intercepted this RSA encrypted message:
Ciphertext (decimal): 101...123

With the following parameters:
n = 143...789
e = 65537
d = 285...365

Decrypt it to find the flag.""",
        "points": 400,
        "flag": "flag{rsa_decryption_success}",
        "difficulty": "Medium",
        "hints": ["Use the formula m = c^d mod n to decrypt", "You may need to convert the result to ASCII"]
    },
    {
        "name": "Memory Forensics",
        "description": "We have a memory dump from a compromised system. Analyze it to find the flag that was in the running process.",
        "points": 350,
        "flag": "flag{memory_forensics_expert}",
        "difficulty": "Medium",
        "hints": ["Try using Volatility for memory analysis", "Look for strings in the memory dump"]
    },
    {
        "name": "Web API Exploitation",
        "description": """This API has an endpoint that returns user data:
```
GET /api/users/{id}
```

But it doesn't check if you're authorized to view that user. Can you exploit this IDOR vulnerability to find the flag in the admin's profile (id=1)?""",
        "points": 300,
        "flag": "flag{idor_vulnerability_exploited}",
        "difficulty": "Medium",
        "hints": ["Try changing the ID parameter", "The admin user likely has ID 1"]
    }
]