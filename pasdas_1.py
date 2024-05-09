#r w
import pandas as pd;

csv_file=pd.read_csv('../dataset/property_listing_data_in_Bangladesh.csv');
print(csv_file)
print(csv_file.shape)
print(csv_file.info)
print(csv_file.head(15))
print(csv_file.tail(15));
all_data=pd.set_option('display.max_rows',7557);
print(all_data);

