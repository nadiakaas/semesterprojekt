import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def acc(sensor, col_name):
    data = []
    col_name = 'acc_' + col_name
    a = a_values[sensor][col_name]
    
    i = start_row
    for x in range(end_row - start_row):
        acc = a * df[col_name][i]
        data.append(acc)
        i += 1
    return data


def rot(sensor, col_name):
    data = []
    col_name = 'rot_' + col_name
    a = a_values[sensor][col_name]
    b = b_values[sensor][col_name]
    
    i = start_row
    for x in range(end_row - start_row):
        z = df[col_name][i]
        rot = (z - b) / a
        data.append(rot)
        i += 1
    return data


def plot(xpoints, xlabel, ypoints, ylabel):
    plt.plot(xpoints, ypoints)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()
    

# ----- udskift filnavn - lav \\ i stedet for / på windows - start med C: ved windows ----- #
filename = '/Users/nakn/OneDrive/SDU/sem2/SDI/squatdata.csv'
filename = '/Volumes/GoogleDrive/.shortcut-targets-by-id/1qxPPnQZ2u0IayHjF9CkcAfbKIhbo59x4/2. Semesterprojekt/Data/18_tibia.csv'
col_names = ['period','temp','acc_x','acc_y','acc_z','rot_x','rot_y', 'rot_z']

df = pd.read_csv(filename, ',', names=col_names, header=None)

#kalibrering af sportssensorerne 
a_values = {'18': {
                'acc_x': -1.0249,
                'acc_y': -1.010888,
                'acc_z': -1.0208,
                'rot_x': 0.01774006,
                'rot_y': 0.0260826,
                'rot_z': -0.01746456},
            '30': {
                'acc_x': -1.005,
                'acc_y': -1.0024,
                'acc_z': -1.09801,
                'rot_x': -0.0180593,
                'rot_y': 0.01843194,
                'rot_z': -0.01812283}
    }
b_values = {'18': {
                'rot_x': 0.0619,
                'rot_y': -0.11169,
                'rot_z': -0.1395},
            '30': {
                'rot_x': 0.012008,
                'rot_y': 0.09704,
                'rot_z': -0.04425}
    }

# ----- de rækker vi tager udgangspunkt i ----- #
start_row = 0
end_row = len(df) - 0


# ----- vælg rot() eller acc() funktion - '18' eller '30' er sensor ----- #
data = rot('18','z')

i = start_row
seconds = [0]
for x in range(end_row - start_row-1):
    s = df['period'][i]/1000000
    seconds.append(seconds[-1] + s)
    i += 1

xpoints = np.array(seconds)
ypoints = np.array(data)


# ----- lav flotte labels hvis du vil ----- #
plot(xpoints, "Seconds", ypoints, "Rot. z")
