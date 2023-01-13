import time

def remind_seatbelt():
    while True:
        # Check if the seatbelt is fastened
        is_fastened = input("Is the seatbelt fastened? (y/n) ")

        # If the seatbelt is not fastened, remind the passenger
        if is_fastened.lower() != "y":
            print("Please fasten your seatbelt.")
            time.sleep(5)  # Wait 5 seconds before checking again
        else:
            print("Seatbelt is fastened.")
            break  # Exit the loop

# Call the function
remind_seatbelt()
