def read_input_file(file_path):

    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split('\t')
        for i in lines[1:]:
            values = i.strip().split('\t')
            row = dict(zip(header, values))
            data.append(row)
    return data


def write_ouput_file(data, output_file):

    unique_data = []
    unique_rows = set()

    with open(output_file, 'w') as file:
        headers = list(data[0].keys()) + ['Gross Salary']
        file.write(','.join(headers) + '\n')

        for i in data:
            gross_salary = float(i['basic_salary']) + float(i['allowances'])
            i['Gross Salary'] = str(gross_salary)
            row_value = tuple(i.values())

            if row_value not in unique_rows:
                unique_data.append(i)
                unique_rows.add(row_value)

        for i in unique_data:
            values = [i[header] for header in headers]
            file.write(','.join(values) + '\n')


def merge_input_files(file1, file2, output_file):
    data1 = read_input_file(file1)
    data2 = read_input_file(file2)
    sync_data = data1 + data2
    write_ouput_file(sync_data, output_file)

    salaries = [float(row['basic_salary']) + float(row['allowances']) for row in sync_data]
    sort_salaries = sorted(set(salaries), reverse=True)
    second_highest_salary = sort_salaries[1]
    average_gross_salary = sum(salaries) / len(salaries)

    with open(output_file, 'a') as file:
        file.write(f'Second Highest Salary={second_highest_salary}, Average Salary={average_gross_salary}\n')


file1_path = r"D:\Crest_test\Input file\DATA.dat"
file2_path = r"D:\Crest_test\Input file\DATA1.dat"

output_file_path = r"D:\Crest_test\Output file\Result.csv"

merge_input_files(file1_path, file2_path, output_file_path)

print("Data has been transferred and saved to Result.csv file")
