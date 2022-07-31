import random 

H = 40
X_MIN = -100
X_MAX = 100
Y_MIN = -100
Y_MAX = 100

LEVELS = [12, 20, 28, 36]

TARGET_ISOLINE = 36
INITIAL_POSITIONS_PRESET = [
    [45, 35, 'green', 1],
    [-20, 44, 'red', 2],
    [33, -4, 'blue', 3],
    [43, -47, 'yellow', 4],
    [-10, 35, 'orange', 5],
    [0, 12, 'pink', 6],
    [-19, 7, 'black', 7],
    [-32, -39, 'gray', 8],
    [-32, 47, 'cyan', 9],
] 

GENERATED_AGENTS_NUMBER = 25
INITIAL_POSITIONS_GENERATED = [
    [random.randint(X_MIN / 2, X_MAX / 2), random.randint(Y_MIN / 2, Y_MAX / 2), [random.random(), random.random(), random.random()], random.randint(0, GENERATED_AGENTS_NUMBER)]
    for i in range(GENERATED_AGENTS_NUMBER)
]

INITIAL_POSITIONS = INITIAL_POSITIONS_GENERATED

MAX_TRACK = 10
VISION = 20

PERIOD = 2000 #ticks
OVERALL_DURATION = 30
#DISPLAY_FREQUENCY = 1000 #ms
