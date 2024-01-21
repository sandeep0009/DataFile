#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# Read the Excel file
file_path = r'C:\Users\HP\OneDrive\Desktop\Assignment_Timecard.xlsx'
df = pd.read_excel(file_path)

# Convert 'Timecard Hours (as Time)' column to numeric
df['Timecard Hours (as Time)'] = pd.to_numeric(df['Timecard Hours (as Time)'], errors='coerce')

# Print employees who have worked for 7 consecutive days
consecutive_days = 7
consecutive_days_employees = df[df.groupby('Employee Name')['Pay Cycle Start Date'].diff().dt.days == consecutive_days - 1]
print(f"\nEmployees who have worked for {consecutive_days} consecutive days:")
if not consecutive_days_employees.empty:
    print(consecutive_days_employees[['Employee Name', 'Position ID']])
else:
    print("No data")

# Print employees with less than 10 hours between shifts but greater than 1 hour
min_hours_between_shifts = 1
max_hours_between_shifts = 10
shifts_between_hours = df.groupby('Employee Name')['Time'].diff().dt.total_seconds() / 3600
between_shifts_employees = df[(shifts_between_hours > min_hours_between_shifts) & (shifts_between_hours < max_hours_between_shifts)]
print(f"\nEmployees with less than {max_hours_between_shifts} hours between shifts but greater than {min_hours_between_shifts} hours:")
if not between_shifts_employees.empty:
    print(between_shifts_employees[['Employee Name', 'Position ID']])
else:
    print("No data")

# Print employees who have worked for more than 14 hours in a single shift
max_hours_single_shift = 14
long_shift_employees = df[df['Timecard Hours (as Time)'] > max_hours_single_shift]
print(f"\nEmployees who have worked for more than {max_hours_single_shift} hours in a single shift:")
if not long_shift_employees.empty:
    print(long_shift_employees[['Employee Name', 'Position ID']])
else:
    print("No data")


# In[ ]:




