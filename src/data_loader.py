import pandas as pd

def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load raw dataset from given path.
    """
    df = pd.read_csv(path)
    return df


if __name__ == "__main__":
    df = load_raw_data("../data/raw/customer_support_tickets.csv")
    print(df.shape)