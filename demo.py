import random

# Step 1: User se saari initial inputs le lo
choice_for_number_str = input("Password mein Numbers (0-9) chahiye? (y/n): ").lower() # Input ko lowercase kar liya
password_length_str = input("Enter your pass length: ") # String mein input
user_length = int(password_length_str) # Integer mein convert kiya

# Step 2: Saare character sets define karo
number_chars = "1234567890" # Variable names thode clear kar diye
capital_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_chars = "abcdefghijklmnopqrstuvwxyz"
symbol_chars = "!@#$%&"

# Step 3: 'all_possibility' string ko user ki choice ke anusaar banao
# Pehle woh characters daalo jo hamesha rahenge
all_possibility = small_chars + capital_chars + symbol_chars

# Ab check karo ki numbers add karne hain ya nahi
if choice_for_number_str == 'y':
    all_possibility += number_chars  # Agar 'y' hai, toh numbers ko jod do
# Agar 'n' hai, toh kuch nahi karna, all_possibility jaisa tha waisa hi rahega (bina numbers ke)

# Step 4: Password generate karo (AB 'all_possibility' final ho chuka hai)
mera_password = ""
# Ek chhota sa check: Agar all_possibility khali hai (aisa is case mein nahi hoga, par good practice)
if not all_possibility:
    print("Error: Password banane ke liye koi characters nahi chune gaye!")
else:
    for _ in range(user_length):
        random_letter = random.choice(all_possibility)
        mera_password += random_letter

# Step 5: Final password print karo (sirf ek baar, sab kuch hone ke baad)
# Aapka 'elif choice_for_number == 'n':' wala print yahaan zaroori nahi hai,
# kyunki password toh banega hi (chahe numbers ke saath ya bina)
# aur hum use aakhir mein print karenge.
if mera_password: # Agar password bana hai (all_possibility khali nahi tha)
    print(f"Your password is: {mera_password}")
else:
    # Yeh tabhi print hoga jab upar 'if not all_possibility:' wala error aaya ho
    # Is specific code mein yeh print nahi hoga kyunki small, capital, symbol hamesha hain.
    print("Password generate nahi ho paaya.")
    

# print(f"your password is : {mera_password}")
