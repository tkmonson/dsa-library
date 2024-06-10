'''
Encode and Decode Strings (#271)

A list of strings is encoded into a string. The encoded string is then sent
over a network and is decoded back into the original list of strings. Design
the encoding and decoding algorithms.
'''

def encode(strs: list[str]) -> str:
    result = []
    for s in strs:
        result.append(f'{len(s)}/')
        result.append(s)
    return ''.join(result)


def decode(s: str) -> list[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] != '/':
            j += 1
        size = int(s[i:j])
        i = j + 1 + size
        result.append(s[j + 1 : i])

    return result


if __name__ == '__main__':
    strs = ['my', 'cat', 'obliterates', '/12/', 'grapes']
    enc = encode(strs)
    print(enc)
    dec = decode(enc)
    print(dec)

'''
To preserve the separation between the strings within the encoded string, you
could use a special delimiter. However, this delimiter could be present in one
of the input strings. To avoid this confusion, we can prefix the delimiters
with the lengths of their upcoming strings. Then, we can skip over that many
characters (including any characters that match the delimiter).
'''

