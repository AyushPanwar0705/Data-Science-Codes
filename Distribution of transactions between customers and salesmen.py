import pandas as pd

# Create a DataFrame from the provided data
data = {
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.50, 270.65, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, 3045.60],
    'ord_date': ['05-10-2022', '09-10-2022', '05-10-2022', '08-17-2022', '10-09-2022', '07-27-2022',
                 '10-09-2022', '10-10-2022', '10-10-2022', '06-17-2022', '07-08-2022', '04-25-2022'],
    'customer_id': [5001, 5001, 5005, 5001, 5005, 5001, 5005, 5001, 5005, 5001, 5005, 5005],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
}

df = pd.DataFrame(data)

# Split the dataset into groups by 'customer_id' and 'salesman_id', then count the rows in each group
grouped = df.groupby(['customer_id', 'salesman_id']).size().reset_index(name='count')

print(grouped)
