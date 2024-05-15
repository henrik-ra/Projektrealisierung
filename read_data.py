data  = []
columns = []
def read_csv(file):
    global columns
    normal_row =None 
    wrong_rows = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader)
        for row in tqdm(reader):
            if len(row)>10:
                wrong_rows.append(row)
            else:
                normal_row = row
                data.append(row)

        df = pd.DataFrame(data, columns=columns)
    return data, wrong_rows

csv_file = 'Daten/ZYXW_tripfiles.csv' 
data, wrong_rows = read_csv(csv_file)
df_data = pd.DataFrame(data, columns=columns)
data = df_data
