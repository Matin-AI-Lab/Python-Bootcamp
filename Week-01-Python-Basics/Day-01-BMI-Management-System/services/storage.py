import json

# Load json File #
def load_patients():
    try:
        with open("data\patients.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save Automatically #
def save_patients(patients):
    with open ("data\patients.json", "w", encoding="utf-8") as file:
        json.dump(patients, file, indent=4)






        