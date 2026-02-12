import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def create_tfidf_features(df: pd.DataFrame, max_features: int = 5000):
    """
    Convert cleaned text into TF-IDF features
    """

    vectorizer = TfidfVectorizer(
        max_features=max_features,
        stop_words="english"
    )

    X = vectorizer.fit_transform(df["clean_text"])

    return X, vectorizer

if __name__ == "__main__":
    from data_loader import load_raw_data
    from data_cleaning import clean_data
    from text_preprocessing import preprocess_dataframe

    df = load_raw_data("../data/raw/customer_support_tickets.csv")
    df = clean_data(df)
    df = preprocess_dataframe(df)

    X, vectorizer = create_tfidf_features(df)

    print("Feature shape:", X.shape)