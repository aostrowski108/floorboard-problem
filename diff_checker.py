import csv

def read_csv_to_set(file_name):
    numbers = set()
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for number in row:
                if number:  # To avoid empty strings
                    numbers.add(int(number))
    return numbers

def compare_files(file1, file2):
    set1 = read_csv_to_set(file1)
    set2 = read_csv_to_set(file2)

    in_file1_not_in_file2 = set1 - set2
    in_file2_not_in_file1 = set2 - set1

    return in_file1_not_in_file2, in_file2_not_in_file1

def main():
    file1 = 'python_conflict_list.csv'
    file2 = 'c-sharp/conflictList.csv'

    diff1, diff2 = compare_files(file1, file2)

    print(f"Numbers in {file1} but not in {file2}: {sorted(diff1)}")
    print(f"Numbers in {file2} but not in {file1}: {sorted(diff2)}")

if __name__ == '__main__':
    main()
