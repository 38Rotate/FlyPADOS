#Version 1.0.10

import streamlit as st
import numpy as np
from ac_profile import moment as mm
from ac_profile import weights as wh
import math
import pandas as pd


st.title("FlyPad OS V1.0.10")

# ---------------------------- Data Definitions ----------------------------- #

# Landing performance
ffobs = [(0, 1550), (2500, 1615), (5000, 1695), (7500, 1770)]
grv = [(0, 525), (2500, 565), (5000, 610), (7500, 660)]

# Takeoff performance at different weights
altitudes = [0, 2000, 4000, 6000, 8000]
temperatures = [0, 20, 40, 60, 80, 100]
# ... (All your data arrays for ground_roll and obstacle distances, both for 1050 and 1320)

# Fixed variables
empty_weight = 738

ground_roll_1320 = [
    [589, 641, 696, 750, 812, 873],
    [681, 742, 805, 871, 939, 1010],
    [790, 860, 933, 1010, 1089, 1171],
    [917, 999, 1084, 1173, 1265, 1360],
    [1068, 1163, 1262, 1365, 1472, 1583],
]

obstacle_50ft_1320 = [
    [1091, 1188, 1291, 1397, 1519, 1647],
    [1263, 1380, 1505, 1642, 1790, 1954],
    [1474, 1619, 1777, 1952, 2150, 2379],
    [1742, 1927, 2138, 2384, 2680, 3060],
    [2097, 2355, 2671, 3082, 3678, 4720]
]

# Data for 1050lb

ground_roll_1050 = [
    [471, 513, 557, 600, 650, 699],
    [545, 594, 644, 697, 751, 808],
    [632, 688, 747, 808, 871, 937],
    [734, 799, 867, 938, 1012, 1088],
    [854, 930, 1010, 1092, 1178, 1267],
]

obstacle_50ft_1050 = [
    [951, 1034, 1122, 1212, 1314, 1421],
    [1098, 1197, 1303, 1416, 1539, 1673],
    [1277, 1397, 1528, 1672, 1830, 2008],
    [1499, 1651, 1821, 2012, 2233, 2497],
    [1787, 1990, 2226, 2511, 2877, 3387]
]

# ----------------------------------------------------------------------------#

# climb rate data

# 1320 data

climb_rates_1320 = [
    [1156, 1069, 985, 906, 831, 758],
    [1007, 921, 839, 761, 687, 616],
    [858, 774, 693, 617, 544, 474],
    [710, 627, 548, 473, 401, 333],
    [562, 481, 403, 330, 259, 192]
]

# 1050 data

climb_rates_1050 = [
    [1455, 1345, 1241, 1141, 1046, 956],
    [1268, 1160, 1057, 959, 865, 776],
    [1081, 975, 874, 777, 686, 598],
    [895, 790, 691, 596, 506, 420],
    [709, 606, 509, 416, 327, 243]
]

# ---------------------------- Helper Functions ----------------------------- #


def interpolate_data(weight, altitudes, temperatures, data_1050, data_1320):
    interpolated_data = np.array([
        data_1050[i][j] + (weight - 1050) * (data_1320[i]
                                             [j] - data_1050[i][j]) / (1320 - 1050)
        for i in range(len(altitudes)) for j in range(len(temperatures))
    ]).reshape(len(altitudes), len(temperatures))
    return interpolated_data


def get_interpolated_value(weight, altitude, temperature, data_1050, data_1320):
    interpolated_data = interpolate_data(
        weight, altitudes, temperatures, data_1050, data_1320)

    # Interpolate along the altitude axis
    df_alt = pd.DataFrame(
        interpolated_data, index=altitudes, columns=temperatures)
    interpolated_along_alt = df_alt.interpolate(method='index').loc[altitude]

    # Interpolate along the temperature axis
    df_temp = pd.Series(interpolated_along_alt, index=temperatures)
    result = df_temp.interpolate(method='index').loc[temperature]

    return result


def landing_roll(alt, grv, ffobs):
    grx, gry = zip(*grv)
    ffx, ffy = zip(*ffobs)
    return np.interp(alt, grx, gry), np.interp(alt, ffx, ffy)


def Descent_Rate():
    st.title("Calculate a Sudden Descent Rate")
    st.write("This calculates the fpm you need to maintain to hit a certain altitude within a certain distance")
    distance = st.number_input("Enter Distance You'd Be Traveling in NM")
    current_alt = st.number_input("Give Your Current Alt (Feet)")
    target_alt = st.number_input("Give Your Target Alt (Feet)")
    groundspeed = st.number_input(
        "Give An Average / Current Groundspeed (Knots)")

    gap = (current_alt - target_alt) / 100

    def glidepath(gap, distance):
        if distance == 0:
            st.warning("Distance cannot be zero!")
            return 0
        gp = gap / distance
        return gp

    def fpm(gp, groundspeed):
        desired_fpm = (gp * groundspeed) * (100/60)
        return desired_fpm

    gp = glidepath(gap, distance)

    desired_fpm = fpm(gp, groundspeed)

    st.write(f'You Should Maintain a Descent Rate of {desired_fpm} (+/-50fpm)')


def XWind():
    st.title("Crosswind Calculator")
    st.write(
        "Calculates xwind given your speed and the speed + direction of the wind.")
    hdg = st.number_input("Your Heading")
    xhdg = st.number_input("Wind Heading")
    xw = st.number_input("Wind Speed")

    def differ(hdg, xhdg):
        diff = abs(hdg - xhdg) % 360
        return min(diff, 360 - diff)

    def xwind_comp(diff, xw):
        xwind = xw * math.sin(math.radians(diff))
        return xwind

    diff = differ(hdg, xhdg)
    xwind = xwind_comp(diff, xw)

    st.write(f"Your Crosswind component is {xwind}")

    xwind = xwind_comp(diff, xw)


pages = {
    "Descent Rate": Descent_Rate,
    "XWind": XWind,
}

# Create a selectbox for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[selection]()


# ---------------------------- User Inputs via Streamlit ----------------------------- #


st.subheader("Enter Aircraft Parameters:")


cptwht = st.number_input(
    "Captain's/Left Seat Pilot's Weight (Max 300 Pounds):", max_value=300.0)
fowht = st.number_input(
    "First Officer's/Right Seat Pilot's Weight (Max 300 Pounds):", max_value=300.0)
payload = st.number_input(
    "Total Cargo Weight (Max 50 Pounds):", max_value=50.0)
fuel_load = st.number_input(
    "Total Fuel in Gallons (Limited to 19.8 capacity):", max_value=19.8)
altitude = st.number_input("Input Field Elevation:")
temperature = st.number_input("Field Temp:")

# Calculate total weight
fuel_converted = fuel_load * 6
weight = cptwht + fowht + payload + fuel_converted + empty_weight

# ---------------------------- Calculations ----------------------------- #

wht_totals = weight
pilot_moment = np.interp(cptwht, wh['max_pilots'], mm['pilots'])
fo_moment = np.interp(fowht, wh['max_pilots'], mm['pilots'])
cargo_moment = np.interp(payload, wh['bag_a'], mm['bag_a'])
fuel_moment = np.interp(fuel_converted, wh['max_fuel'], mm['fuel'])
total_moment = pilot_moment + fo_moment + \
    cargo_moment + fuel_moment + mm['empty']
cg = total_moment / wht_totals

# Performance
ground_roll = get_interpolated_value(
    weight, altitude, temperature, ground_roll_1050, ground_roll_1320)
obstacle_distance = get_interpolated_value(
    weight, altitude, temperature, obstacle_50ft_1050, obstacle_50ft_1320)
climb_rate = get_interpolated_value(
    weight, altitude, temperature, climb_rates_1050, climb_rates_1320)
igr, iff = landing_roll(altitude, grv, ffobs)

# ---------------------------- Display Results via Streamlit ----------------------------- #

st.subheader("Results:")
st.write(f"Your aircraft weighs {wht_totals} with a cg of {cg:.2f}")
st.write(
    f"Takeoff groundroll: {ground_roll:.2f} ft, Obstacle clearance alt: {obstacle_distance:.2f} ft")
st.write(f"Climb performance: {climb_rate:.2f} ft/min")
st.write(
    f"Landing roll: {igr:.2f} ft, 50-foot clearance distance: {iff:.2f} ft")

# To run the Streamlit app, save this code to a file, say "app.py", and then run `streamlit run app.py` in your terminal.

