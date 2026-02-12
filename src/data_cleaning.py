import pandas as pd

DROP_COLUMNS = [
    "Resolution",
    "Time to Resolution",
    "Customer Satisfaction Rating",
    "First Response Time",
    "Customer Name",
    "Customer Email"
]

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw dataset by removing unusable and irrelevant columns.
    """

    df = df.drop(columns=DROP_COLUMNS, errors="ignore")

    # Combine subject and description into single text field
    df["text"] = df["Ticket Subject"] + " " + df["Ticket Description"]

    df = df.drop(columns=["Ticket Subject", "Ticket Description"])

    return df

if __name__ == "__main__":
    from data_loader import load_raw_data

    df = load_raw_data("../data/raw/customer_support_tickets.csv")
    df_clean = clean_data(df)

    print(df_clean.columns)
    print(df_clean.shape)