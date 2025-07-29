import pandas as pd

@st.cache_data
    def load_data():
        return pd.read_pickle("merged_nse_df.pkl")
    merged_df = load_data()

def get_stock(merged_df, stock_name):
    individual_stock = merged_df[merged_df['Name'] == stock_name].copy()
    individual_stock["Date"] = pd.todatetime(individual_stock["Date"],errors = "coerce")
    individual_stock = individual_stock.sort_values('Date')
    return individual_stock
