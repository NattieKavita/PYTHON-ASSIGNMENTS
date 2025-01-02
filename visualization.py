import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weather_data = pd.read_csv('weather.csv') 



try:
    df = pd.read_csv('weather.csv')
    print("Dataset loaded successfully")
except FileNotFoundError:
    print("Error: The dataset file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#task 1
# first few rows 

print("First few rows of the dataset:")
print(weather_data.head())

# check missing values
print("\nMissing values per column:")
print(weather_data.isnull().sum())

# task 2
statistics = weather_data.describe()

# task 3

# Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'])


# Set the date as the index
df.set_index('date', inplace=True)


# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(df['temp_max'], label='Max Temperature', color='orange')
plt.title('Daily Maximum Temperature in Seattle')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid()
plt.show()


# Resample the data to monthly averages
monthly_precipitation = df['precipitation'].resample('M').mean()


# Plotting the bar chart
plt.figure(figsize=(12, 6))
monthly_precipitation.plot(kind='bar', color='blue')
plt.title('Average Monthly Precipitation in Seattle')
plt.xlabel('Month')
plt.ylabel('Average Precipitation (mm)')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Plotting the histogram
plt.figure(figsize=(12, 6))
sns.histplot(df['temp_max'], bins=30, kde=True, color='purple')
plt.title('Distribution of Daily Maximum Temperatures')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid()
plt.show()

# Plotting the scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['temp_max'], df['temp_min'], alpha=0.6, color='green')
plt.title('Scatter Plot of Max vs. Min Temperatures')
plt.xlabel('Max Temperature (°C)')
plt.ylabel('Min Temperature (°C)')
plt.grid()
plt.show()


