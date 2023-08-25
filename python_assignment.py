flight_table = [
    {"P_ID": "P1", "Process": "VSCode", "Start Time (ms)": 100, "Priority": "MID"},
    {"P_ID": "P23", "Process": "Eclipse", "Start Time (ms)": 234, "Priority": "MID"},
    {"P_ID": "P93", "Process": "Chrome", "Start Time (ms)": 189, "Priority": "High"},
    {"P_ID": "P42", "Process": "JDK", "Start Time (ms)": 9, "Priority": "High"},
    {"P_ID": "P9", "Process": "CMD", "Start Time (ms)": 7, "Priority": "High"},
    {"P_ID": "P87", "Process": "NotePad", "Start Time (ms)": 23, "Priority": "Low"}
]

def print_table(table):
    print("{:<5} {:<10} {:<20} {:<10}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
    print("="*50)
    for row in table:
        print("{:<5} {:<10} {:<20} {:<10}".format(row["P_ID"], row["Process"], row["Start Time (ms)"], row["Priority"]))

def sort_table(table, key):
    sorted_table = sorted(table, key=lambda x: x[key])
    return sorted_table

def main():
    print("Flight Table")
    print("[1. Sort by P_ID, 2. Sort by Start Time, 3. Sort by Priority]")
    choice = int(input("Enter your choice: "))
    
    sorting_key = None
    if choice == 1:
        sorting_key = "P_ID"
    elif choice == 2:
        sorting_key = "Start Time (ms)"
    elif choice == 3:
        sorting_key = "Priority"
    else:
        print("Invalid choice. Exiting.")
        return
    
    sorted_table = sort_table(flight_table, sorting_key)
    print("\nSorted Table:")
    print_table(sorted_table)

if __name__ == "__main__":
    main()
