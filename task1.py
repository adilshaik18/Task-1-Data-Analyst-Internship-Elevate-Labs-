import pandas as pd

df = pd.read_csv("sales data.csv")

print(df.isnull().sum())

df = df.dropna(axis=0, how="any")

df = df.drop_duplicates()

df = df.reset_index(drop=True)

for i in range(len(df["Row ID"])):
        
    if(len(str(df["Order Date"][i])) < 10):
        date = str(df["Order Date"][i]).split("/")
        if(len(date[0]) == 1):
            date[0] = "0" + date[0]
        if(len(date[1]) == 1):
            date[1] = "0" + date[1]
        if(len(date[2]) == 2):
            date[2] = "20" + date[2]
        df.loc[i,"Order Date"] = date[0] + "/" + date[1] + "/" + date[2]
    
    if(len(str(df["Ship Date"][i])) < 10):
        date = str(df["Ship Date"][i]).split("/")
        if(len(date[0]) == 1):
            date[0] = "0" + date[0]
        if(len(date[1]) == 1):
            date[1] = "0" + date[1]
        if(len(date[2]) == 2):
            date[2] = "20" + date[2]
        df.loc[i,"Ship Date"] = date[0] + "/" + date[1] + "/" + date[2]

df["Row ID"] = df["Row ID"].astype(int)
df["Order ID"] = df["Order ID"].astype(str)
df["Order Date"] = pd.to_datetime(df["Order Date"], format='%d/%m/%Y')
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format='%d/%m/%Y')
df["Ship Mode"] = df["Ship Mode"].astype(str).str.lower()
df["Customer ID"] = df["Customer ID"].astype(str)
df["Customer Name"] = df["Customer Name"].astype(str).str.title()
df["Segment"] = df["Segment"].astype(str).str.lower()
df["Country"] = df["Country"].astype(str).str.title()
df["City"] = df["City"].astype(str).str.title()
df["State"] = df["State"].astype(str).str.title()
df["Postal Code"] = df["Postal Code"].astype(int)
df["Region"] = df["Region"].astype(str).str.title()
df["Product ID"] = df["Product ID"].astype(str)
df["Category"] = df["Category"].astype(str).str.lower()
df["Sub-Category"] = df["Sub-Category"].astype(str).str.lower()
df["Product Name"] = df["Product Name"].astype(str).str.title()
df["Cost"] = df["Cost"].astype(float)
df["Price"] = df["Price"].astype(float)
df["Profit"] = df["Profit"].astype(float)
df["Quantity"] = df["Quantity"].astype(int)
df["Sales"] = df["Sales"].astype(float)

df.rename(columns={"Row ID": "row_id",
                    "Order ID": "order_id",
                    "Order Date": "order_date",
                    "Ship Date": "ship_date",
                    "Ship Mode": "ship_mode",
                    "Customer ID": "customer_id",
                    "Customer Name": "customer_name",
                    "Segment": "segment",
                    "Country": "country",
                    "City": "city",
                    "State": "state",
                    "Postal Code": "postal_code",
                    "Region": "region",
                    "Product ID": "product_id",
                    "Category": "category",
                    "Sub-Category": "sub_category",
                    "Product Name": "product_name",
                    "Cost": "cost",
                    "Price": "price",
                    "Profit": "profit",
                    "Quantity": "quantity",
                    "Sales": "sales"}, inplace=True)

print(df.info())

df.to_csv("cleaned_sales_data.csv")