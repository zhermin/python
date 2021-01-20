import re

def get_isbn(user_input):

    product_list = []
    ibsn_list = []

    # Use Regex to find the 9 digit Product ID from the given string of text and adds them to [product_list], ignores prefixes and dashes
    for item in re.finditer(r"(\d{3})?-?(\d)-?(\d{2})-?(\d{6})", user_input):
        product_list.append("".join(item.group(2,3,4)))

    # Loop through every item in [product_list]
    for product_item in product_list:
        # Turn the string of numbers into integers
        to_integer = [int(i) for i in product_item]

        # Multiply each number with their corresponding multipliers
        multiplied = [a*b for a,b in zip(reversed(range(2,11)), to_integer)]

        # Add the list of multipled numbers together (9 of them)
        added = sum(multiplied)

        # Obtain the Error Digit
        error_digit = (added//11+1)*11 - added

        # Change the Error Digit if they are either 10 or 11 (0 because it's divisible by 11)
        if error_digit == 10:
            error_digit = "x"
        elif error_digit == 11:
            error_digit = "0"

        # Compile the results
        generated_isbn = f"{product_item}{error_digit}"
        ibsn_list.append(generated_isbn)

    return product_list, ibsn_list


if __name__ == "__main__":

    print("This script takes in any amount of text and outputs thier corresponding ISBN-10 Numbers if it finds any Product Number")
    print("Example Text: These are some Valid Product IDs - 978037541457, 978-0-37-428158 and 155192370\n")

    user_input = None
    # If the user types "/q" at the end then the script shuts down
    while user_input != "/q":
        user_input = input("\n\nEnter any amount of text containing Product IDs\n>> ")

        product_list, ibsn_list = get_isbn(user_input)
        print(f"\nFound {len(ibsn_list)} Product ID(s)\n")

        for i in range(len(ibsn_list)):
            print(f"{i+1}. Product ID (w/o prefix) : {product_list[i]} | ISBN-10 Number : {ibsn_list[i]}\n")

        user_input = input("Enter Anything to Restart (/q to Exit)\n> ")

    print("EXITED")
    exit()