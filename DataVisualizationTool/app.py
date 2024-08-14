import argparse
import sys

import pandas as pd

from PySide6.QtCore import QDateTime, QTimeZone
from PySide6.QtWidgets import QApplication

from main_window import MainWindow
from main_widget import MainWidget


def transform_date(utc, timezone=None):
    """Transform String to UTC-Date"""
    utc_fmt = 'yyyy-MM-ddTHH:mm:ss.zzzZ'
    new_date = QDateTime().fromString(utc, utc_fmt)
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
    options.add_argument('-f', '--file', type=str, required=False, help="Name of the CSV-file")
    args = options.parse_args()
    # TODO data = read_date(args.file)
    data = read_date('all_day.csv')

    app = QApplication(sys.argv)

    widget = MainWidget(data)
    window = MainWindow(widget)
    window.show()
    sys.exit(app.exec())
