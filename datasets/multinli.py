import os
import pandas as pd
from datasets.dowloader import maybe_download, extract_zip

URL = "http://www.nyu.edu/projects/bowman/multinli/multinli_1.0.zip"
DATA_FILES = {
    "train": "multinli_1.0/multinli_1.0_train.jsonl",
    "dev_matched": "multinli_1.0/multinli_1.0_dev_matched.jsonl",
    "dev_mismatched": "multinli_1.0/multinli_1.0_dev_mismatched.jsonl",
}

def download_file_and_extract(local_cache_path=".", file_split="train"):
    """Download and extract the dataset files
    """
    file_name = URL.split("/")[-1]
    maybe_download(URL, file_name, local_cache_path)

    if not os.path.exists(os.path.join(local_cache_path, DATA_FILES[file_split])):
        extract_zip(os.path.join(local_cache_path, file_name), local_cache_path)

def load_pandas_df(local_cache_path=".", file_split="train"):
    """Loads extracted dataset into pandas
    """
    download_file_and_extract(local_cache_path=local_cache_path, file_split=file_split)
    path = os.path.join(local_cache_path, DATA_FILES[file_split])
    return pd.read_json(path, lines=True)

def load_multinli_text(local_cache_path=".", file_split="train"):
    data = load_pandas_df(local_cache_path=local_cache_path, file_split=file_split)
    # get unique sentences
    data = data[data["gold_label"] == "neutral"]
    # Keep only relevant columns
    return data[["genre", "sentence1"]]
