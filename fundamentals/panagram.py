text="the quick brown fox jumps over a lazy dog"
alph="abcdefghijklmnopqresuvwxyz"

taxt=text.casefold()
is_panagram=True

for ch in alph:
    if text.count(ch)==0:
        is_panagram=False
        break
print(is_panagram)