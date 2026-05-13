import pandas as pd
import numpy as np


def load_data():
    readings = pd.read_csv("data/parcel_readings.csv")
    metadata = pd.read_csv("data/parcel_metadata.csv")

    return readings, metadata


def main():
    readings, metadata = load_data()

    print("Readings Shape:", readings.shape)
    print("Metadata Shape:", metadata.shape)


if __name__ == "__main__":
    main()
