# Automates weekly and daily directory creation while preserving 
# content from the previous day/week.

#!/bin/bash
echo "Enter Week Number for TODAY (e.g., 01):"
read week
echo "Enter Day Number for TODAY (e.g., 02):"
read day

# Convert inputs to integers to calculate yesterday
w_num=$((10#$week))
d_num=$((10#$day))

# Calculate previous day and week
if [ $d_num -eq 1 ]; then
    # If today is Day 01, yesterday was Day 05 (or 07) of the previous week
    prev_w=$((w_num - 1))
    prev_d=5 # Change to 7 if you code 7 days a week
else
    prev_w=$w_num
    prev_d=$((d_num - 1))
fi

# Format back to 2 digits (e.g., 1 becomes 01)
prev_week_str=$(printf "%02d" $prev_w)
prev_day_str=$(printf "%02d" $prev_d)

prev_dir="week-$prev_week_str/day-$prev_day_str"
target_dir="week-$week/day-$day"

# 1. Create the new folder
mkdir -p "$target_dir"

# 2. Copy code from the previous day if it exists
if [ -d "$prev_dir" ]; then
    cp -r "$prev_dir"/* "$target_dir/"
    echo "Successfully cloned your code from $prev_dir!"
else
    echo "Couldn't find $prev_dir. Starting with an empty folder."
fi
