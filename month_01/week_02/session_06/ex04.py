total_purchase = float (input("Xudaldan avaltiin dun: "))
is_member =""
# indentation - neg TAB xooson zai 
    
if total_purchase >= 200:  
        discount = 0.3 # 30% hongololt
                 
elif total_purchase < 200:
    is_member = input("Ta gishuun uu? (Tiim/Ugui): ").lower() == "tiim" 
    if is_member:
        discount = 0.2 # 20% hongololt
    else:
        discount = 0.1 # 10% hongololt
elif total_purchase >= 50:
    if is_member:
        discount = 0.1 # 10% hongololt
    else:
        discount = 0.05 # 5% hongololt
else:
    if is_member:
        discount = 0.05 # 5% hongololt
    else:
        discount = 0 # hongololtgui

final_price = total_purchase * (1 - discount)
print(f"Tanii toloh dun: {final_price:.2f}")

# float butarhai too utga, zarimdaa buhel too utga huleej avdag
# int buhel too utga, 
#is_member = input("Ta gishuun uu? (Tiim/Ugui): ").lower() == "tiim" 