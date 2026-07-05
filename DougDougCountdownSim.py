import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

fastest_success = 200000.0
slowest_success = 0.0
loop_total = 0.0
loop_success = 200000.0
closest_loop = 0
loop_result = []
bee_result = []

def time_converter(x):
    # Used to convert the important times into a more readable format.
    years = int(x // 31536000)
    months = int((x % 31536000) // 2592000)
    days = int((x % 2592000)// 86400)
    hours = int((x % 86400) // 3600)
    minutes = int((x % 3600) // 60)
    seconds = round((x % 60), 3)

    if years > 0:
        return f"{years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    elif months > 0:
        return f"{months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    elif days > 0:
        return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    elif hours > 0:
        return f"{hours} hours, {minutes} minutes, {seconds} seconds"
    elif minutes > 0:
        return f"{minutes} minutes, {seconds} seconds"
    else:
        return f"{seconds} seconds"

def generate_time_labels(max_value):
    # Generate dynamic time labels based on the maximum value in the data
    time_scales = [
        (1.0, '1s'), (10.0, '10s'), (60.0, '1m'), (600.0, '10m'), (3600.0, '1h'), (36000.0, '10h'),
        (86400.0, '1d'), (604800.0, '1w'), (2592000.0, '1mo'), (31536000.0, '1y'),
        (315360000.0, '10y'), (3153600000.0, '100y'), (31536000000.0, '1ky'),
        (315360000000.0, '10ky'), (3153600000000.0, '100ky'), (31536000000000.0, '1my'),
        (31536000000000000.0, '1by'), (31536000000000000000.0, '1ty'),
        (31536000000000000000000.0, '1qay'), (31536000000000000000000000.0, '1quiy')
    ]
    
    # Filter scales that are within the data range
    time_ticks = []
    time_labels = []
    for value, label in time_scales:
        if value <= max_value:
            time_ticks.append(float(value))
            time_labels.append(label)
    
    return time_ticks, time_labels

def countdown():
    # Simulates the actual countdown and returns the time it took to complete and the number of times Bee Mode was triggered.
    ticks = 600 # The time left on the timer
    global time_passed
    global bee_counter
    bee_counter = 0 # The number of times Bee Mode was triggered
    time_passed = 0.0 # The actual time that has passed in the simulation
    tick_time_ratio = 1.0 # The ratio of time passed to ticks.

    while ticks > 0:
        randomizer = random.randint(1, 101)
        if randomizer <= 5:
            # Ticks increase of 1
            ticks += 1
            time_passed += tick_time_ratio
        elif randomizer <= 6:
            # Ticks increase of 60
            ticks += 60
            time_passed += tick_time_ratio
        elif randomizer <= 7:
            # Ticks decrease of 60
            ticks -= 60
            time_passed += tick_time_ratio
        elif randomizer <= 12:
            # Time increases by 5
            time_passed += tick_time_ratio * 5
        elif randomizer <= 13:
            # Ticks doubles
            ticks = ticks * 2
            time_passed += tick_time_ratio
        elif randomizer <= 14:
            # Ticks halves
            ticks = ticks / 2
            time_passed += tick_time_ratio
        elif randomizer <= 15:
            # Ticks are converted to minutes and seconds, then the values are flipped and converted back.
            current_min = ticks // 60
            current_sec = ticks % 60
            ticks = (current_sec * 60) + current_min
            time_passed += tick_time_ratio
        elif randomizer <= 16:
            # Ticks are rounded to the nearest minute
            ticks = round(ticks / 60) * 60
            time_passed += tick_time_ratio
        elif randomizer == 17:
            # Represents the timer moving, which is not simulated here.
            time_passed += tick_time_ratio
        elif randomizer <= 18:
            # Ratio of ticks to time is halved
            tick_time_ratio /= 2
            time_passed += tick_time_ratio
        elif randomizer <= 19:
            # Ratio of ticks to time is doubled
            tick_time_ratio *= 2
            time_passed += tick_time_ratio
        elif randomizer == 20:
            # Bee Mode is triggered
            bee_counter += 1
            time_passed += tick_time_ratio
        else:
            # Ticks decreases by 1
            ticks -= 1
            time_passed += tick_time_ratio
    
    # Returns the time taken for ticks to reach zero, along with the number of times Bee Mode was triggered.
    return time_passed, bee_counter

# Prompts user for amount of countdowns to simulate
loop_count = int(input("How many countdowns do you want to simulate? "))

# Loops through the countdown function for the amount of times specified by the user, and stores the results in a pair of lists.
for i in range(loop_count):
    loop_time, bee_count = countdown()
    
    print(f"Loop {i + 1}: Countdown completed in {loop_time:.2f} seconds. ")

    loop_result.append(loop_time)
    bee_result.append(bee_count)

# Determines the countdown that is closest to 10 minutes (600 seconds)
for j in range(len(loop_result)):
    if abs(loop_result[j] - 600) < loop_success:
        loop_success = abs(loop_result[j] - 600)
        closest_loop = j
        print(f"Loop {j + 1} is the closest countdown to 10 minutes with a time of {loop_result[j]:.2f} seconds.")

    if loop_result[j] < fastest_success:
        fastest_success = loop_result[j]
        fastest_loop = j
        print(f"Loop {j + 1} is the fastest successful countdown with a time of {loop_result[j]:.2f} seconds.")

    elif loop_result[j] > slowest_success:
        slowest_success = loop_result[j]
        slowest_loop = j
        print(f"Loop {j + 1} is the slowest successful countdown with a time of {loop_result[j]:.2f} seconds.")

# Calculates a bunch of math stuff and converts the important times into a more readable format.
loop_success = time_converter(loop_result[closest_loop])
loop_average = time_converter(statistics.mean(loop_result))
loop_median = time_converter(statistics.median(loop_result))
loop_stdev = time_converter(statistics.stdev(loop_result))
loop_range = time_converter(max(loop_result) - min(loop_result))
loop_mode = time_converter(statistics.mode(loop_result))
bee_average = statistics.mean(bee_result)
fastest_success = time_converter(fastest_success)
slowest_success = time_converter(slowest_success)


# Prints the results of the simulation to the console.
print(f"\nTotal countdowns simulated: {loop_count}")

print(f"\nFastest successful countdown: Loop {fastest_loop + 1} ({fastest_success})")
print(f"Slowest successful countdown: Loop {slowest_loop + 1} ({slowest_success})")
print(f"Closest countdown to 10 minutes: Loop {closest_loop + 1} ({loop_success})")

print(f"\nAverage countdown time: {loop_average}")
print(f"Median countdown time: {loop_median}")
print(f"Standard deviation of countdown times: {loop_stdev}")
print(f"Range of countdown times: {loop_range}")
print(f"Mode of countdown times: {loop_mode}")

print(f"\nAverage bees collected: {bee_average:.2f}")
print(f"Total bees collected: {sum(bee_result)}")

# Create histogram of countdown times (\/ Mostly AI-generated code \/)
plt.figure(figsize=(10, 6))
# Use logarithmically spaced bins for better distribution with log scale
log_bins = np.logspace(np.log10(min(loop_result)), np.log10(max(loop_result)), 50)
n, bins, patches = plt.hist(loop_result, bins=log_bins, color='blue', edgecolor='black', alpha=0.7)

# Find the peak (bin with highest frequency)
peak_index = np.argmax(n)
peak_bin_center = (bins[peak_index] + bins[peak_index + 1]) / 2

plt.xlabel('Countdown Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Countdown Times (Log Scale)')
plt.xscale('log')
min_val = loop_result[fastest_loop]
max_val = loop_result[slowest_loop]
median_val = statistics.median(loop_result)
plt.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {loop_median}')
plt.axvline(min_val, color='blue', linestyle='--', linewidth=2, label=f'Minimum: {fastest_success}')
plt.axvline(max_val, color='red', linestyle='--', linewidth=2, label=f'Maximum: {slowest_success}')
plt.axvline(peak_bin_center, color='purple', linestyle='--', linewidth=2, label=f'Peak: {time_converter(peak_bin_center)}')
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Generate and apply custom x-axis labels dynamically based on data range
time_ticks, time_labels = generate_time_labels(max(loop_result))
plt.xticks(time_ticks, time_labels, rotation=45, ha='right')

plt.tight_layout()
plt.show()
