def decrypt(cipher: str) -> str:
    result = []
    i = 0
    while i < len(cipher):
        if cipher[i] == '.':
            i += 1
            if i < len(cipher) and cipher[i] == '.':
                if result:
                    result.pop()
            else:
                continue
        else:
            result.append(cipher[i])
        i += 1

    return ''.join(result)


if __name__ == "__main__":
    import sys

    cipher_text = sys.stdin.read().strip()
    if cipher_text:
        print(decrypt(cipher_text))
    else:
        print("Cipher text is empty.")
