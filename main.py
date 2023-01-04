from hashlib import sha1, sha256, sha512

pw = input("you password:")
mode = input("mode[sha1/SHA256/sha512]")
if mode == '':
    mode = 'sha1'
hash_ = {"sha1": sha1, "sha256": sha256, "sha512": sha512}[mode]
hx = pw[:]
for _ in range(3):
    hx = hash_(bytes(hx + "114",encoding="utf8")).hexdigest()

print('@#' + hx[:8].upper() + hx[8:])
input('...')
