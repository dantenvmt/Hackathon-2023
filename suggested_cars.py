# %%
import pandas as pd
from textblob import TextBlob

# Load data
data = pd.read_csv('output.csv')

# Ask user for desired price range
min_price = int(input("Enter minimum price: "))
max_price = int(input("Enter maximum price: "))

# Filter data based on price range
filtered_data = data.loc[(data['PRICE'] >= min_price)
                         & (data['PRICE'] <= max_price)]

# Define list of plus features
plus_features = ['Alloy wheels', 'Auto High-beam Headlights', 'Bumpers: body-color', 'Delay-off headlights', 'Fully automatic headlights',
                 'Heated door mirrors', 'Power door mirrors', 'Spoiler', 'Turn signal indicator mirrors', 'Air Conditioning']

# Analyze sentiment of plus features
plus_features_sentiment = []
for feature in plus_features:
    blob = TextBlob(feature)
    sentiment = blob.sentiment.polarity
    plus_features_sentiment.append(sentiment)

# Get average sentiment of plus features
avg_sentiment = sum(plus_features_sentiment) / len(plus_features_sentiment)

# Suggest cars with plus features if sentiment is positive
if avg_sentiment > 0:
    suggested_cars = filtered_data.loc[filtered_data['Features'].apply(
        lambda x: any(feature in x for feature in plus_features))]
else:
    suggested_cars = filtered_data

# Check if any cars are available
if suggested_cars.empty:
    print("No cars are available within the specified price range and with the desired features.")
else:
    # Print suggested cars
    print("Suggested cars:")
    print(suggested_cars[['VIN', 'MILEAGE', 'PRICE', 'Link']].head(5))
    suggested_cars.to_csv('suggested_cars.csv', index=False)


# %%
