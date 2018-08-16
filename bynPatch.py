import os
import sys

binData = None
fDir = sys.argv[1]
word = sys.argv[2]
patchString = sys.argv[3]

lenWord = len(word)
lenPatch = len(patchString)

if (lenWord > lenPatch):
    patchString = patchString.ljust(lenWord, ' ')

if (lenPatch > lenWord):
    patchString = patchString[:lenWord]

with open(fDir, "rb") as fHandle:
    binData = fHandle.read()

if (bytes(word) in binData):
    print ("Patching: "+word)
    print ("with: "+patchString)

    binMod = binData.replace((word), bytes(patchString));

    with open(fDir+"_MOD", "wb") as fHandle:
        fHandle.write(binMod)

        print ("Patched!")
else:
    print ("The patch string is not in the bin file.")
    print word
