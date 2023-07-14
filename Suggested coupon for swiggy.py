"""message= 
SWIGGYIT
20% off on select items
Use code SWIGGYIT & get 20% off on orders above ₹159. Applicable on select items. Maximum discount: ₹50
WELCOMEBACK
Get 60% off
Use code WELCOMEBACK & get 60% off on orders above ₹299. Maximum discount: ₹100.
"""
bill=int(input("Enter the bill:"))
print("You have two promo codes SWIGGYIT(20%) & WELCOMEBACK(60%)")
promo_code=(input("Enter the promo code:"))
if promo_code=="SWIGGYIT":
    if bill>=159:
        print("Promo Code is applied")
        discount=0.20*bill
        if discount>=50:
            discount=50
        total_bill=bill-discount
        print("Total bill to pay :",total_bill)
    else:
        print("Bill is lesser for promo code")
        print("Please pay the full bill")
else: 
     promo_code == "WELCOMEBACK" 
     if bill >= 299:
          print("Promo Code is applied")
          discount=0.60*bill
          if discount >= 100:
             discount = 100
             total_bill=bill-discount
             print("Total bill to pay  :",total_bill)
     else:
              print("Bill is lesser for promo code")
              print("Please pay the full bill")    
             