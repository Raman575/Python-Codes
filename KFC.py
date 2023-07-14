"""message= 
SWIGGYIT
20% off on select items
Use code SWIGGYIT & get 20% off on orders above ₹159. Applicable on select items. Maximum discount: ₹50
WELCOMEBACK
Get 60% off
Use code WELCOMEBACK & get 60% off on orders above ₹159. Maximum discount: ₹100.
"""

Amount=int(input("Enter Total Amount: "))
Promo_code=input("Enter Promo Code: ")

if Promo_code == "SWIGGYIT" :
   if Amount >= 159:
          print ("Promo code applied succesfully")
          
          discount = 0.20 * Amount
          
          if discount >= 50:
               discount = 50
          amount_to_pay = Amount - discount
          print("Please Pay: \u20b9", amount_to_pay)
      else :
                 print ("Amount is lesser for promo code")
                print("Please Pay: \u20b9", Amount)
      elif     Promo_code = "WELCOMEBACK"
            if Amount >= 159:
                print ("Promo code applied succesfully")
          
          discount = 0.60 * Amount
          
          if discount >= 100:
               discount = 100
          amount_to_pay = Amount - discount
          print("Please Pay: \u20b9", amount_to_pay)
      
else:
              print("you cannot apply promo code")       