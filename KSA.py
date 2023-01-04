s = []
for x in range(256):
    s.append(x)

input_key = 'saputra1'
k = bytearray(input_key, "utf8")

j = 0
for i in range(256):
    j = (j + s[i] + k[i % len(input_key)]) % 256
    c = s[i]
    s[i] = s[j]
    s[j] = c

print(s)