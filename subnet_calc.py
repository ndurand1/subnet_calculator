
def calculator(cidr):
    ip_addrs = 2**(32-cidr)
    print("\nNumber of possible IP addresses is: ")
    print(ip_addrs)
    print("\nNumber of possible hosts is: ")
    print(ip_addrs - 2)
    return

def subnet_mask(cidr2):
    ip_addrs2 = 2**(32-cidr2)
    if 24 <= cidr2 <= 30:
        print("\nSubnet mask is: ")
        print(f"255.255.255.{256 - ip_addrs2}")
    elif 16 <= cidr2 <= 23:
        print("\nSubnet mask is: ")
        print(f"255.255.{256 - (ip_addrs2 / 256)}")
    elif 9 <= cidr2 <= 15:
        print("\nSubnet mask is: ")
        print(f"255.{256 - (ip_addrs2 / 256 / 256)}.0")
    else:
        print("\nSubnet mask is: ")
        print(f"{256 - (ip_addrs2 / 256 / 256 / 256)}.0.0")


# take user input and convert to int
input_num = input("Enter CIDR number: ")
input_int = int(input_num)

if 0 <= input_int < 31:
    calculator(input_int)
    subnet_mask(input_int)
else:
    print("Invalid CIDR number")






