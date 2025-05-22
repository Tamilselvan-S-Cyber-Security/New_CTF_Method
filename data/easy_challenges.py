# This file contains challenge data for the CTF platform

easy_challenges = [
    {
        "name": "Hidden Message",
        "description": "There's a hidden message in this image. Can you find it?",
        "points": 100,
        "flag": "flag{hidden_in_plain_sight}",
        "difficulty": "Easy",
        "hints": ["Try looking at the metadata", "EXIF data might be helpful"]
    },
    {
        "name": "Simple Cipher",
        "description": "Can you decode this message? Nzou{fvzcyr_pvcure_genatsbezngvba}",
        "points": 150,
        "flag": "flag{simple_cipher_transformation}",
        "difficulty": "Easy",
        "hints": ["This is a rotation cipher", "Think about ROT13, but with a different shift"]
    },
    {
        "name": "Web Inspection",
        "description": "The flag is hidden somewhere on this webpage. Use your browser tools to find it.",
        "points": 100,
        "flag": "flag{inspect_element_ftw}",
        "difficulty": "Easy",
        "hints": ["Right-click and inspect", "Check the HTML comments"]
    },
    {
        "name": "Binary Basics",
        "description": "Convert this binary to text: 01100110 01101100 01100001 01100111 01111011 01100010 01101001 01101110 01100001 01110010 01111001 01011111 01100011 01101111 01101110 01110110 01100101 01110010 01110011 01101001 01101111 01101110 01111101",
        "points": 100,
        "flag": "flag{binary_conversion}",
        "difficulty": "Easy",
        "hints": ["Each byte (8 bits) represents one ASCII character", "Use an online binary to text converter"]
    },
    {
        "name": "Reverse String",
        "description": "Sometimes the simplest challenges are about looking at things differently. Try reversing this string: }gnisrever_gnirts{galf",
        "points": 50,
        "flag": "flag{string_reversing}",
        "difficulty": "Easy",
        "hints": ["Read it backwards", "Start from the end and go to the beginning"]
    },
    {
        "name": "Base64 Decode",
        "description": "Decode this Base64 string: ZmxhZ3tiYXNlNjRfZGVjb2Rpbmd9",
        "points": 120,
        "flag": "flag{base64_decoding}",
        "difficulty": "Easy",
        "hints": ["Use an online Base64 decoder", "This is a common encoding format used to represent binary data in ASCII"]
    },
    {
        "name": "Hidden Header",
        "description": "The flag is hidden in one of the HTTP response headers. Use a tool like curl to examine the headers.",
        "points": 150,
        "flag": "flag{http_headers_examination}",
        "difficulty": "Easy",
        "hints": ["Try using developer tools in your browser", "Look for custom headers"]
    },
    {
        "name": "Simple XOR",
        "description": "This text has been XORed with a single byte. Find the key and decrypt: 7b120c0f09150a48070915150a0e061c0f0907150e061b7d",
        "points": 200,
        "flag": "flag{xor_encryption_basics}",
        "difficulty": "Easy",
        "hints": ["Try all possible single-byte keys (0-255)", "XOR is reversible with the same key"]
    },
    {
        "name": "URL Decode",
        "description": "Decode this URL-encoded string: flag%7Burl%5Fencoding%5Fbasics%7D",
        "points": 100,
        "flag": "flag{url_encoding_basics}",
        "difficulty": "Easy",
        "hints": ["Replace %7B with {", "Replace %7D with }", "Replace %5F with _"]
    },
    {
        "name": "Hex to ASCII",
        "description": "Convert this hexadecimal string to ASCII: 666c61677b6865785f746f5f61736369697d",
        "points": 120,
        "flag": "flag{hex_to_ascii}",
        "difficulty": "Easy",
        "hints": ["Each pair of hex digits represents one ASCII character", "Use an online hex to ASCII converter"]
    }
]