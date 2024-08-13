import argparse
import pandas as pd

from PySide6.QtCore import  QDateTime, QTimeZone


def transform_date(utc, timezone=None):
    """Transform String to UTC-Date"""
    utc_fmt = 'yyyy-MM-ddTHH:mm:ss.zzzZ'
    new_date =QDateTime().fromString(utc, utc_fmt)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date
def read_date(file_name):
    # Read the CSV content
    df = pd.read_csv(file_name)
    # Remove wrong magnitudes
    df = df.drop(df[df.mag < 0].index)
    magnitudes = df['mag']
    # Set local timezone
    timezone = QTimeZone(b'Europe/Berlin')
    # Get timestamp transformed to our timezone
    times = df['time'].apply(lambda x: transform_date(x, timezone))
    return times, magnitudes


if __name__ == '__main__':
    options = argparse.ArgumentParser()
    options.add_argument('-f', '--file', type=str, required=True, help="Name of the CSV-file")
    args = options.parse_args()
    data = read_date(args.file)
    print(data)
