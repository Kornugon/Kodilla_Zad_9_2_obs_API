import os
import csv
import pickle


def export_rates_to_csv(val: list):
    """
    Create or use existing folder to save a file.
    Save Rates list in to a .csv file
    """
    SAVED_FOLDER = 'Saved'

    file_path = os.path.join(SAVED_FOLDER, "Rates.csv")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=["currency", "code", "bid", "ask"])
        writer.writeheader()
        for item in val:
            writer.writerow(item)
    print("Successfully exported data to Rates.csv in Saved subfolder of the script")


def pick(val: list):
    ogorek = []
    for i in val:
        ogorek.append(i)
    return ogorek

