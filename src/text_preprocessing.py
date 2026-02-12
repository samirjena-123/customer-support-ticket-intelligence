import re
import pandas as pd

def clean_text(text: str) -> str:
    """
    Basic text cleaning:
    - lowercase
    - remove special characters
    - remove numbers
    - remove extra whitespace
    """

    # convert to string
    text = str(text)

    # lowercase
    text = text.lower()

    # remove special characters and numbers
    text = re.sub(r"[^a-z\s]", " ", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply text cleaning to dataframe
    """

    df["clean_text"] = df["text"].apply(clean_text)

    return df

if __name__ == "__main__":
    from data_loader import load_raw_data
    from data_cleaning import clean_data

    df = load_raw_data("../data/raw/customer_support_tickets.csv")
    df = clean_data(df)
    df = preprocess_dataframe(df)

    print(df[["text", "clean_text"]].head())