import sys
print(sys.version)

print('.'.join((str(1062018).zfill(8)[0:2], 
                str(1062018).zfill(8)[2:4], 
                str(1062018).zfill(8)[-4:])))

