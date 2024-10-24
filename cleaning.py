import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")
# print(df)
# print(df.info())

df = df.set_index("Transaction ID")

df = df.drop(columns=["Till ID"])

# this method will allow you to remove indavidual rows but can be time consuming if trying to remove
# multiple rows
# df = df.drop([6.0])

df = df.dropna(how="any")

df = df.drop_duplicates()

df.at[15.0, "Cost"] = 6.00

def float_to_time(time_record):
    # convert float to a string 
    time_record = str(time_record)
    # split the input string at the decimal point
    hours, minutes = time_record.split('.')
    # format the hours and minuets into HH:MM
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return timestamp

df["Time"] = df["Time"].apply(float_to_time)

df["Time"] = pd.to_datetime(df["Time"])


def split_basket(basket_item):
    items = basket_item.split(",")
    stripped_items = [item.strip() for item in items]
    return(stripped_items)

df["Basket"] = df["Basket"].apply(split_basket)
print(df["Basket"])

# exploded_data = df.explode("Basket", ignore_index=False)
# print(exploded_data["Basket"])





