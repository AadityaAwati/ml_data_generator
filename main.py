import pandas
import random

from datetime import datetime
import time

try:
    print(" ---- TEST and TRAIN Data Generator ----")
    print("Designed By Aaditya Awati! (https://aadityaawati.github.io/cv/)\n\n")

    def fetch_columns_number():
        try:
            columns_number = int(input("Enter No. Of Columns -> "))
            print("\n")
        except ValueError:
            print("Sorry, that is not a number. Please try again.")
            columns_number = 0
            fetch_columns_number()

        return columns_number

    no_of_columns = fetch_columns_number()
    randomizer = random.Random()

    columns = []
    all_column_data = []

    def fetch_column_data():
        for x in range(0, no_of_columns):
            column_data = []

            column_name = input(f"\nPlease Enter Name Of Column {x} -> ")
            column_type = input("Enter Type Of Data Of Column (str/int/float) -> ")

            if column_type in ("str", "float", "int"):

                column_data.append(column_name)
                column_data.append(column_type)

                if column_type == "int":
                    print("\n")
                    min_value = int(input("Enter Minimum Value -> "))
                    max_value = int(input("Enter Maximum Value -> "))

                    column_data.append(min_value)
                    column_data.append(max_value)

                if column_type == "float":
                    print("\n")
                    min_value = float(input("Enter Minimum Value -> "))
                    max_value = float(input("Enter Maximum Value -> "))

                    column_data.append(min_value)
                    column_data.append(max_value)

                all_column_data.append(column_data)
                columns.append(column_name)

            else:
                print(f"Sorry, '{column_type}' is not an option. Please try again.")
                fetch_column_data()

    fetch_column_data()

    def fetch_entries_number():
        try:
            entries_number = int(input("Please Enter The No. Of Entries -> "))
        except ValueError:
            print("Sorry, that is not a number. Please try again.")
            entries_number = 0
            fetch_entries_number()

        return entries_number

    no_of_entries = fetch_entries_number()

    dataframe = pandas.DataFrame(columns=columns)
    dataframe_dict = dataframe.to_dict()

    for column in columns:
        current_col_data = all_column_data[columns.index(column)]

        for y in range(0, no_of_entries):
            if current_col_data[1] == "int":
                dataframe_dict[column][y] = randomizer.randint(current_col_data[2], current_col_data[3])
            elif current_col_data[1] == "float":
                dataframe_dict[column][y] = randomizer.randint(int(current_col_data[2]), int(current_col_data[3])) + randomizer.randint(0, 100) / 100
            else:
                letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

                if no_of_entries > 26:
                    repeat_times = int(no_of_entries / 26)
                    extra_values = no_of_entries - 26 * repeat_times
                else:
                    repeat_times = 1
                    extra_values = 0

                index_count = 0
                for z in range(0, repeat_times):
                    if no_of_entries > 26:
                        for w in range(0, 26):
                            dataframe_dict[column][index_count] = letters[w] + str(z)
                            index_count += 1
                    else:
                        for w in range(0, no_of_entries):
                            dataframe_dict[column][index_count] = letters[w] + str(z)
                            index_count += 1
                if no_of_entries > 26:
                    for w in range(0, extra_values):
                        dataframe_dict[column][index_count] = letters[w] + str(repeat_times + 1)
                        index_count += 1
                break

    dataframe = pandas.DataFrame(dataframe_dict)

    print("\n")
    print("Data Has Been Generated - Please take a look at the DataFrame Below:")
    print(dataframe)
    print("\n")

    time.sleep(1)

    current_time = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
    dataframe.to_csv(f"Generated Data/record_{current_time}.csv", index=False)

    print("\n")
    print(f"The Record Has Been Saved in path -> Generated Data/record_{current_time}.csv")
    print("\n")

    print("PROGRAM END.")
except KeyboardInterrupt:
    print("\n\n---- PROGRAM END ----")
    time.sleep(1)
