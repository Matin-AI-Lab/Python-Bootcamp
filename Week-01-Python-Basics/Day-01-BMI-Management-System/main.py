#----------------------------Import----------------------------#
from services.bmi import (
    calculate_bmi,
    get_bmi_category
)

from services.storage import (
    load_patients,
    save_patients
)

from ui.menu import show_menu

patients = load_patients()

#--------------------------- Function -------------------------------#


# Weight Function #
def get_valid_weight():
    while True:
         try:
            weight = float(input("\n Enter your Weight (KG) :  "))
         
            if weight <= 0:
               print("Invalid Range! Weight must be bigger than zero!")
               continue

            return weight

         except ValueError:
               print(" Please enter a valid number!")

# Height Function #
def get_valid_height():
    while True:
        try:
           height_cm = float(input(" Enter your Height (CM) :  "))

           if height_cm <=0:
               print("Invalid range! Height must be bigger than Zero!")
               continue
           
           return height_cm
        
        except ValueError:
            print("Please Enter a Valid number! ")


# Patients Record Function #
def create_patient_record(patient_id, weight, height_cm, bmi, category):
    return {
        "id": patient_id,
        "weight" : weight,
        "height_cm" : height_cm,
        "bmi" : bmi,
        "category" : category
     }

# Search by Patient ID Function #
def search_patient(patients):

    try:
        search_id = int(input("\nEnter Patient ID To Search :"))

    except ValueError:
        print("Invalid input")
        return
    
    for patient in patients:

        if patient["id"] == search_id:
            print("\nPatient Found")
            display_patient(patient)
            return

    print("\nPatient Not Found")



# Delete by Patient ID Function #
def delete_patient(patients):

    try:
        delete_id = int(input("\nEnter Patient ID to Delete :"))

    except ValueError:
        print("Invalid Input")
        return
    
    for patient in patients:
        if patient ["id"] == delete_id:
            patients.remove(patient)
            save_patients(patients)
            print("\nPatient Deleted")
            return
        
    print("\nPatient Not Found")

# Statistics Function #
def show_statistics(patients):
    if len(patients) == 0:
        print("\nPatient Not Found")
        return

    total_patients = len(patients)

    bmi_values = []

    underweight_count = 0
    normal_count = 0
    overweight_count = 0
    obesity_count = 0

    for patient in patients :

        bmi_values.append(patient["bmi"])

        if patient["category"] == "Underweight":
            underweight_count += 1

        elif patient["category"] == "Normal":
            normal_count += 1

        elif patient["category"] == "Overweight":
            overweight_count += 1

        elif patient["category"] == "Obesity":
            obesity_count += 1

    average_bmi = round(sum(bmi_values) / len(bmi_values), 2)
    max_bmi = max(bmi_values)
    min_bmi = min(bmi_values)

    print("\n======================= Statistics ======================")

    print("Total Patients :", total_patients)
    print("Average Bmi :", average_bmi)
    print("Max BMI :", max_bmi)
    print("Min BMI :", min_bmi)    

    print("\nBMI Categories :")

    print("Underweight :", underweight_count)
    print("Normal :", normal_count)
    print("Overweight :", overweight_count)
    print("Obesity :", obesity_count)


# Update by Patient ID Function #
def update_patient(patients):

    try:
        update_id = int(input("\nEnter Patient ID to Update :"))

    except ValueError:
        print("Invalid Input")
        return

    for patient in patients:
        if patient["id"] == update_id:
            print("\nPatient Found")
            display_patient(patient)

            new_weight = get_valid_weight()
            new_height = get_valid_height()
            new_bmi = calculate_bmi(new_weight, new_height)

            new_category = get_bmi_category(new_bmi)

            patient["weight"] = new_weight
            patient["height_cm"] = new_height
            patient["bmi"] = new_bmi
            patient["category"] = new_category

            save_patients(patients)

            print("\nPatient Updated Successfully")
            display_patient(patient)

            return

    print("\nPatient Not Found")



# Patient ID Function #
def generate_patient_id(patients):
    if len(patients) == 0:
        return  1
    else:
        return patients [-1] ["id"] + 1


# Display Function #
def display_patient(patient):
    print("\n====================================================================================")
    print("================================= Patient Information ==============================")
    print("====================================================================================")

    print("Patient ID: ", patient["id"])
    print("Patient Weight: ", patient["weight"], "KG")
    print("Height: ", patient["height_cm"], "CM")
    print("BMI: ", patient["bmi"])
    print("Category: ", patient["category"])

    print("\n===================================================================================\n")


# ------------------------------------------------------------------------------------#


#-------------------------------- MAIN BODY ------------------------------------------#

# Main Loop #
while True:

    show_menu()

    choice = input(" choose option: ")

    if choice == "1":
        weight = get_valid_weight()
        
        height_cm = get_valid_height()
        
        bmi = calculate_bmi(weight , height_cm)
        
        category = get_bmi_category(bmi)
        
        patient_id = generate_patient_id(patients)

        patient_record = create_patient_record(
            patient_id,
            weight,
            height_cm,
            bmi,
            category
            )
        
        patients.append(patient_record)
        save_patients(patients)
        print("Patient Added Successfully")



    elif choice == "2":
        if len(patients) == 0:
            print("\nNo Patients Found")

        else :
            for index, patient in enumerate(patients, start=1):
                print(f"\npatient {index}")
                display_patient(patient)

    elif choice == "3":
        search_patient(patients)

    elif choice == "4":
        delete_patient(patients)

    elif choice =="5":
        update_patient(patients)

    elif choice == "6":
        show_statistics(patients)

    elif choice == "7":
        save_patients(patients)

        print("\nData Saved Successfully")
        break

    else:
        print("\nInvalid Choice")



