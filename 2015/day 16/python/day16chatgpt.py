# Open the file with the Aunt Sues' characteristics
with open("../input.txt") as f:
    # Read the characteristics provided by the MFCSAM
    characteristics = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    # Go through each line in the file
    for line in f:
        # Split the line by ':' to get the Aunt Sue's number and characteristics
        aunt_sue_number, aunt_sue_characteristics = line.split(": ",1)
        # Remove the word 'Sue' from the Aunt Sue's number
        aunt_sue_number = aunt_sue_number.replace("Sue ", "")
        # Split the Aunt Sue's characteristics by ', ' to get a list of characteristics
        aunt_sue_characteristics = aunt_sue_characteristics.split(", ")
        # Convert the list of characteristics into a dictionary
        aunt_sue_characteristics = {characteristic.split(": ")[0]: int(characteristic.split(": ")[1]) for characteristic in aunt_sue_characteristics}
        # Compare the Aunt Sue's characteristics with the ones provided by the MFCSAM
        match = True
        for characteristic, value in aunt_sue_characteristics.items():
            if characteristics[characteristic] != value:
                match = False
                break
        # If all the characteristics match, then this is the Aunt Sue who gave you the gift
        if match:
            print(f"Aunt Sue {aunt_sue_number} is the one who gave you the gift.")
            break

# Open the file with the Aunt Sues' characteristics
with open("../input.txt") as f:
    # Read the characteristics provided by the MFCSAM
    characteristics = {
        "children": 3,
        "cats": (7, float("inf")),
        "samoyeds": 2,
        "pomeranians": (-float("inf"), 3),
        "akitas": 0,
        "vizslas": 0,
        "goldfish": (-float("inf"), 5),
        "trees": (3, float("inf")),
        "cars": 2,
        "perfumes": 1
    }
    # Go through each line in the file
    for line in f:
        # Split the line by the first ':' to get the Aunt Sue's number and characteristics
        aunt_sue_number, aunt_sue_characteristics = line.split(":", 1)
        # Remove the word 'Sue' from the Aunt Sue's number
        aunt_sue_number = aunt_sue_number.replace("Sue ", "")
        # Split the Aunt Sue's characteristics by ', ' to get a list of characteristics
        aunt_sue_characteristics = aunt_sue_characteristics.split(", ")
        # Convert the list of characteristics into a dictionary
        aunt_sue_characteristics = {characteristic.split(": ")[0].strip(): int(characteristic.split(": ")[1]) for characteristic in aunt_sue_characteristics}
        # Compare the Aunt Sue's characteristics with the ones provided by the MFCSAM
        match = True
        for characteristic, value in aunt_sue_characteristics.items():
            if characteristic in ["cats", "trees"]:
                if not (characteristics[characteristic][0] < value):
                    match = False
                    break
            elif characteristic in ["pomeranians", "goldfish"]:
                if not (value < characteristics[characteristic][1]):
                    match = False
                    break
            elif characteristics[characteristic] != value:
                match = False
                break
        # If all the characteristics match, then this is the Aunt Sue who gave you the gift
        if match:
            print(f"Aunt Sue {aunt_sue_number} is the one who gave you the gift.")
            break
