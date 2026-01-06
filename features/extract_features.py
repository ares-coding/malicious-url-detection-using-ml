import re
import math
import pandas as pd
from urllib.parse import urlparse

def has_ip(url):
    return bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))

def calculate_entropy(url):
    probabilities = [url.count(c) / len(url) for c in set(url)]
    return -sum(p * math.log2(p) for p in probabilities)

def extract_features(url):
    parsed = urlparse(url)

    features = {
        "url_length": len(url),
        "num_dots": url.count("."),
        "num_digits": sum(char.isdigit() for char in url),
        "has_ip": int(has_ip(url)),
        "num_special_chars": len(re.findall(r'[@\-?=&_]', url)),
        "uses_https": int(parsed.scheme == "https"),
        "entropy": calculate_entropy(url),
        "suspicious_word_count": sum(
            word in url.lower()
            for word in ["login", "verify", "bank", "secure", "account"]
        )
    }

    return features

def process_dataset(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    feature_rows = []

    for _, row in df.iterrows():
        features = extract_features(row["url"])
        features["label"] = row["label"]
        feature_rows.append(features)

    feature_df = pd.DataFrame(feature_rows)
    feature_df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    process_dataset(
        "data/raw/urls.csv",
        "data/processed/features.csv"
    )
