import csv

fullPath = 'D:\Dev\Java\clinical-trials\\trials_combined_text.psv'


def read(path=fullPath, delimiter='|', encoding='utf-8'):
    correct_labels = []
    text_rows = []
    with open(path, encoding=encoding) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        next(reader, None)
        for row in reader:
            correct_labels.append(row[0])
            text_rows.append(row[1])
    return correct_labels, text_rows
