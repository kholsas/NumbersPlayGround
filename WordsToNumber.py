# Okay... So Tumelo challenged us to write something like this....
# Get a number in "Numerals in Words" converted to the methematical numbers....

def words_to_number(text):
    
    words = text.replace(",", "").lower().split() # We do not want surprises. So we press the entire input to lowercase
    # ... because our dictionary is in lowercase too. then we split that 
    
    num_dict = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, 
        "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1_000, "million": 1_000_000, 
        "billion": 1_000_000_000, "trillion": 1_000_000_000_000
    }

    current = 0  # Holds the current section of the number being built
    total = 0    # Holds the final number

    for word in words:
        if word in num_dict:
            value = num_dict[word]

            if value == 100:
                current = (current or 1) * 100  # Multiply by 100 if applicable
            elif value >= 1000:
                total += (current or 1) * value  # Apply larger multipliers
                current = 0  # Reset current after applying multiplier
            else:
                current += value  # Add normal numbers
        elif word == "and":
            continue  # Ignore "and"... or I could have just simply removed it when I cleaned out commas far above....
        else:
            return "Invalid input"

    print(f"{text} is {total + current}")

# This is where we check if we did it right LOL :) 
words_to_number("Seven hundred thousand, nine hundred and thirty four")
words_to_number("Three million, five hundred thousand and twenty")
words_to_number("One billion, two hundred thirty four million, five hundred sixty seven thousand, eight hundred ninety")
words_to_number("Two trillion, one hundred thirty billion, four hundred twenty million, five hundred sixty seven thousand, eight hundred ninety")
words_to_number("One hundred")
words_to_number("hundred")
words_to_number("fifteen")
words_to_number("One thousand")
words_to_number("One million and one")

# Tell me you are happy, and I shall tell thee that I knew it LOL :) Nice challenge though 