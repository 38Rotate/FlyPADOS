# RV-12 Standard with the Rotax 912 ULS engine
# Variables with 0 are the same as null or N/A

weights = {
    'empty_unusable': 738,  # oil + coolant
    'fully_empty': 0,  # purely airframe
    'usable': 0,  # payload
    'MTOW': 1320,  # max takeoff weight
    'utility': 0,  # utility category of weight (lighter than normal)
    'normal': 0,  # normal category of weight
    'light_sport': (0, 1320),  # light sport category (sub 1500)
    'max_fuel_usable': 0,  # in pounds excluding fuel that sits
    'max_oil': 5.625,  # in pounds converted from quarts / 3 quarts recommended
    'max_fuel': (0, 118.8),  # pounds (19.8)
    'max_pilots': (0, 250),  # 300 per seat / accounts for both front seats
    'max_pax': 0,  # accounts for two passengers aft of pilots
    # baggage compartment either aft of pilots or aft of pilots and pax
    'bag_a': (0, 50),
    'bag_b': 0,  # seperate baggage compartment located in a seperate container aft of bag a
    'max_ramp_util': 0,
    'max_ramp_mormal': 0,
    'max_to_land_util': 0,
    'max_to_land_normal': 0,
    'max_ramp_light_sport': 1320,
    'max_to_land_sport': 1320,

}

speeds = {
    'Vy': 75,  # rate of climb
    'Vx': 60,  # angle of climb
    'Vr': (50, 55),
    'vb': 108,  # max gust
    'Va': 90,  # @1320
    'Vg': 63,  # best glide
    'Vo': (72, 90),  # 850/1320lbs
    'Vne': 136,  # below 16,000
    'vc': 114,  # cruise @1320
    'Vno': 108,  # start of yellow arc
    'Vap': 60,  # approach speed / 55 min kias
    'Vle': 0,  # landing gear speed
    'Vmca': 0,  # for multi engine use, speed at which a clean twin can no longer fly straight using flight controls due to thrust differential
    'Vref': 55,  # final app spd
    'VS1': (41, 45),  # clean stall @1050,1320
    'Vso': (37, 51),  # landing config stall @1050,1320
    'Vfe10': 82,
    'Vfe20': 82,
    'Vfe30': 82,
    'Vfe40': 82,
    'White_Arc': (0, 0),
    'Green_Arc': (45, 108),
    'Yellow_Arc': (108, 136),
    'Red_Arc': (0, 0),
    'Red_Line': 136,

}

moment = {
    'empty': 60468,
    'pilots': (0, 19713.157894736843),
    'pax': (0, 0),
    'bag_a': (0, 5541),
    'bag_b': (0, 0),
    'fuel': (0, 13101),
    'oil': (0, 0),
}

weight_moment_ranges = {
    'pilots': (0, 600),
    'pax': (0, 0),
    'bag_a': (0, 50),
    'bag_b': (0, 0),
    'fuel': (0, 118.8),
    'oil': (0, 5.625),
}

# no cg found in POH

cg = {
    'empty': (0, 0),
    'pilots': (0, 0),
    'pax': (0, 0),
    'bag_a': (0, 0),
    'bag_b': (0, 0),
    'fuel': (0, 0),
    'oil': (0, 0),
    'max_range': (80.49, 85.39),
}

weight_cat = {
    'utility': (0, 0),
    'normal': (0, 0),
    'light_sport': (738, 1320),
}

g_limits = {
    'utility': (0, 0),
    'normal': (0, 0),
    'light_sport': (-2, 4),
}

engine = {
    'hp_lim': 100,  # @5min of max rpm
    'rpm_lim': 5800,  # 5min max
    'min_caution_rpm_range': (1400, 1800),
    'normal_rpm_range': (1800, 5500),
    'max_caution_rpm_range': (5500, 5800),
    'red_line': 5800,
    'no_start_temp_range': (-25, 50),  # celcius -13/120 for F
    'displacement': 1312,  # cc
    'hp_rec': 95,
    'rpm_rec': 5500,
}

ac_spec = {
    'unusable_fuel_climb': 24,  # 4 gal
    'ceiling': 15000,  # ft @ 26c/80f OAT OR fuel temp @20C
    'wing_area': 127,  # ft squared
    'wing_loading': 10.4,  # lb/ft squared
}

# Define the data from the tables
climb_1050 = {
    0: {  # Pressure altitude in ft
        0: 1455,  # Temperature in °F : Climb rate in ft/min
        20: 1345,
        40: 1241,
        60: 1141,
        80: 1046,
        100: 956
    },
    8000: {  # Pressure altitude in ft
        0: 709,  # Temperature in °F : Climb rate in ft/min
        20: 606,
        40: 509,
        60: 416,
        80: 327,
        100: 243
    }
}

climb_1320 = {
    0: {  # Pressure altitude in ft
        0: 1156,  # Temperature in °F : Climb rate in ft/min
        20: 1069,
        40: 985,
        60: 906,
        80: 831,
        100: 758
    },
    8000: {  # Pressure altitude in ft
        0: 562,  # Temperature in °F : Climb rate in ft/min
        20: 481,
        40: 403,
        60: 330,
        80: 259,
        100: 192
    }
}

roll_1050 = {
    0: {  # Pressure altitude in ft
        0: 471,  # Temperature in °F : Climb rate in ft/min
        20: 513,
        40: 557,
        60: 600,
        80: 650,
        100: 699
    },
    8000: {  # Pressure altitude in ft
        0: 854,  # Temperature in °F : Climb rate in ft/min
        20: 930,
        40: 1010,
        60: 1092,
        80: 1178,
        100: 1267
    }
}

roll_1320 = {
    0: {  # Pressure altitude in ft
        0: 589,  # Temperature in °F : Climb rate in ft/min
        20: 641,
        40: 696,
        60: 750,
        80: 812,
        100: 873
    },
    8000: {  # Pressure altitude in ft
        0: 1068,  # Temperature in °F : Climb rate in ft/min
        20: 1163,
        40: 1262,
        60: 1365,
        80: 1472,
        100: 1583
    }
}

landing = {
    0: 525,
    2500: 565,
    5000: 610,
    7500: 660,
}

fifty_ft_obs = {
    0: 1550,
    2500: 1615,
    5000: 1695,
    7500: 1770,
}

# decrase landing distance by 10% for 5 knots of headwind

gallons_per_hour = {
    2500: {
        5000: 4.4,
        5500: 5.7,
    },
    5000: {
        5000: 4.0,
        5500: 5.0,
    },
    7500: {
        5000: 3.7,
        5500: 4.6,
    },
    10000: {
        5000: 3.4,
        5500: 4.2,
    }
}

x_wind = {
    'max_total_wind': 30,  # knots
    'max_direct_xwind': 11,
}

extra = {
    'max_pilots': 300,
    'max_bags': 50,
    'weight_min_max': (738, 1506.8),
}

climb_rates_1050 = {
    'temp': (0, 100),
    'rate_sl': (1455, 956),
    'rate_2k': (1268, 776),
    'rate_4k': (1081, 598),
    'rate_6k': (895, 420),
    'rate_8k': (709, 243),
}

climb_rates_1320 = {
    'temp': (0, 100),
    'rate_sl': (1156, 758),
    'rate_2k': (1007, 616),
    'rate_4k': (858, 474),
    'rate_6k': (710, 333),
    'rate_8k': (562, 192),
}
