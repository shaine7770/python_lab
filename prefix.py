def mask_function(long_mask):
    long_mask = [int(i) for i in long_mask] 
    for long in range(5):
        if long_mask[long] != 255:
            if long_mask[long] != 0:
                return long
            else:
                return long - 1

mask = input("enter the mask ").split(".") 
print(mask_function(mask))