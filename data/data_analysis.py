import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a list of file paths
# return a dictionary with the file label as the key and the dataframe as the value
def load_data(file_paths):
    data = {}
    for label, path in file_paths.items():
        try:
            data[label] = pd.read_csv(path)
        except Exception as e:
            print(f"Could not process file {label}: {e}")
    return data

# print the column names for a single dataframe
def print_columns(data):
    for label in data.columns:
        print(f"{label}: {data[label].dtype}")
# x-axis is the 'Date & Time' column

def plot_int64_v_date_time(date_time, column, column_name):
    # plt.figure(figsize=(12, 8))
    plt.plot(date_time, column)
    plt.title(column_name + " Over Time")
    plt.xlabel("Date & Time")
    plt.xticks(rotation=45)
    plt.xticks(date_time[::500])
    plt.ylabel(column_name)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def check_data(data_frame_columns):
    for column, expected_value in data_frame_columns:
        index = 0
        # print(expected_value)
        for x in column:
            if x != expected_value:
                print(f"{column.name} at index {index} is {x}")
            index += 1

def plot_data(data):
    plt.figure(figsize=(12, 8))

    for label, df in data.items():
        if 'Date & Time' in df.columns:
            df['Date & Time'] = pd.to_datetime(df['Date & Time'])
            df = df.sort_values(by='Date & Time')

            for column in df.columns:
                if column != 'Date & Time':
                    plt.plot(df['Date & Time'], df[column], label=f"{label} - {column}")
        else:
            print(f"File {label} does not have the required 'timestamp' column.")

    plt.title("Data Trends Over Time")
    plt.xlabel("Date & Time", fontsize=1)
    plt.legend()
    plt.grid(True)
    # plt.tight_layout()
    plt.show()

data_files = {
    # "airview": 'p2p_testing/data/airviewdata.csv',
    # "amdata": 'p2p_testing/data/amdata.csv',
    # "status": 'p2p_testing/data/status.csv',
    # "iperf": 'p2p_testing/data/iperf.csv'
    "airview": 'airviewdata.csv',
    "amdata": 'amdata.csv',
    "status": 'status.csv',
    "iperf": 'iperf.csv'
}

data = load_data(data_files)
# print_columns(data['airview'])
# airview_columns_constants = [(data['airview']['stFreqGridNumPts'], 648), 
#                              (data['airview']['stPowrMin'], -125), 
#                              (data['airview']['stPowrNum'], 64), 
#                              (data['airview']['stPowrDel'], 2), 
#                              (data['airview']['mtUpdateInterval'], 60), 
#                              (data['airview']['mtFreqGridNumPts'], 161),
#                              (data['airview']['ltFreqGridNumPts'], 161), 
#                              (data['airview']['instantPowerNumFrames'], 8), 
#                              (data['airview']['mtTimeNum'], 24), 
#                              (data['airview']['ltTimeNum'], 24)]
# airview_list_constants = [(data['airview']['stFreqGridLabels'], data['airview']['stFreqGridLabels'][0]),
#                           (data['airview']['mtFreqGridLabels'], data['airview']['mtFreqGridLabels'][0]),
#                           (data['airview']['ltFreqGridLabels'], data['airview']['ltFreqGridLabels'][0])]

# print_columns(data['amdata'])
# amdata_list_constants = [(data['amdata']['chan_info'], data['amdata']['chan_info'][0]), 
#                             (data['amdata']['freq_info'], data['amdata']['freq_info'][0])]

# print_columns(data['status'])
# status_columns_constants = [
    # (data['status']['chain_names'], data['status']['chain_names'][0]),
    # (data['status']['genuine'], data['status']['genuine'][0]),
    # (data['status']['services'], data['status']['services'][0]),
    # (data['status']['firewall'], data['status']['firewall'][0]),
    # (data['status']['portfw'], data['status']['portfw'][0]),
    # (data['status']['provmode'], data['status']['provmode'][0]),
    # (data['status']['ntpclient'], data['status']['ntpclient'][0]),
    # (data['status']['unms'], data['status']['unms'][0])
# ]

# print_columns(data['iperf'])

# plot_int64_v_date_time(data['airview']['Date & Time'], data['airview']['ltUpdateInterval'], 'ltUpdateInterval')
# print(len(data['airview']['ltUpdateInterval'])/3)

print(data['airview']['pwrHistogram'])