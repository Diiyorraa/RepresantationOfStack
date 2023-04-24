from stack import Stack
def convert_to_Binary(dec_num):
    if dec_num==0:
        return 0
    s = Stack()
    while dec_num>0:
        answer= dec_num %2
        s.push(answer)
        dec_num= dec_num//2

    bin_number = ""
    while not s.is_empty():
        bin_number+=str(s.pop())
    return bin_number

convert_to_Binary(34)
print(convert_to_Binary(34))