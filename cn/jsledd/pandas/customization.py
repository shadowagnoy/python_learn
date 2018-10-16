import pandas as pd

print("display.max_rows = ", pd.get_option("display.max_rows"))
print("display.max_columns = ", pd.get_option("display.max_columns"))
pd.set_option("display.max_rows", 80)
pd.reset_option("display.max_rows")
print("after set display.max_rows = ", pd.get_option("display.max_rows"))
print(pd.describe_option("display.max_rows"))
with pd.option_context("display.max_rows", 10):
    print(pd.get_option("display.max_rows"))
