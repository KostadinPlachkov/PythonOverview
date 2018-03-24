"""
25
NGINX (PRONOUNCED "ENGINE X") IS A WEB SERVER. IT CAN ACT AS A REVERSE PROXY SERVER FOR HTTP, HTTPS, SMTP, POP3, AND IMAP PROTOCOLS, AS WELL AS A LOAD BALANCER AND AN HTTP CACHE.

"""

try:

    key = int(input())
    user_str = str(input()).upper()
    crypt_str = ""
    normal_abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
    for char in user_str:
        num = ord(char)
        if num in range(32, 65):
            crypt_str += char
        else:
            if chr(num).isdigit():
                crypt_str += chr(num)
            elif key >= 25:
                index_char = normal_abc.index(char)
                crypt_char = normal_abc[index_char - key + 24]
                crypt_str += crypt_char
            else:
                index_char = normal_abc.index(char)
                crypt_char = normal_abc[index_char - key]
                crypt_str += crypt_char

    print(crypt_str)


except:
    print("INVALID INPUT")
