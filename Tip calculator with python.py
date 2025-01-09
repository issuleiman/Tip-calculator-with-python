print("""
 __        __         _                                      _               
 \\ \\      / /__  ___ | |_   _ __ ___   __ _ _ __   __ _  ___| | _____ _ __   
  \\ \\ /\\ / / _ \\/ _ \\| __| | '_ ` _ \\ / _` | '_ \\ / _` |/ __| |/ / _ \\ '__|  
   \\ V  V /  __/ (_) | |_  | | | | | | (_| | | | | (_| | (__|   <  __/ |     
    \\_/\\_/ \\___|\\___/ \\__| |_| |_| |_|\\__,_|_| |_|\\__,_|\\___|_|\\_\\___|_|     

                        Welcome to the Tip Calculator ☺
""")

bill=float(input("What is the total bill? :"))
tip=float(input("How much tip will you like to give? :"))
people= int(input("How many peole to splite the bill? :"))

bill_with_tip=tip /100 * bill
total_bill=bill_with_tip + bill
split_amont=total_bill / people
final_amont=round(split_amont, 2)
print(f"Each person should pay:${final_amont}")
