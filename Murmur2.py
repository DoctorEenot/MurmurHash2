def int_to_4bytes(input:int):
    return input&0xffffffff

def murmur2(input:bytes,seed=0):
    m = 0x5bd1e995
    r = 24

    length = len(input)

    h = seed ^ length

    k = 0

    round = 0
    while length >= (round*4)+4:
        k = input[(round*4)]
        k |= input[(round*4)+1]<<8
        k |= input[(round*4)+2]<<16
        k |= input[(round*4)+3]<<24

        k = int_to_4bytes(k)

        k = int_to_4bytes(k*m)
        k ^= k>>r
        k = int_to_4bytes(k*m)

        h = int_to_4bytes(h*m)
        h ^= k

        round += 1

    length_diff = length - (round*4)

    if length_diff == 1:
        h ^= input[-1]
        h = int_to_4bytes(h*m)
    elif length_diff == 2:
        h ^= int_to_4bytes(input[-1]<<8)
    elif length_diff == 3:
        h ^= int_to_4bytes(input[-1]<<16)

    h ^= h>>13
    h = int_to_4bytes(h*m)
    h ^= h>>15

    return h
