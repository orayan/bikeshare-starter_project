import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """Get user input for city, month, and day."""

    print("Hello! Let's explore some US bikeshare data!")

    # City input
    while True:
        selected_city = input("Choose a city (chicago, new york city, washington): ").lower()
        if selected_city in CITY_DATA:
            break
        print("Invalid city. Try again.")

    # Month input
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        selected_month = input("Choose a month (all, january–june): ").lower()
        if selected_month in months:
            break
        print("Invalid month. Try again.")

    # Day input
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        selected_day = input("Choose a day (all, monday–sunday): ").lower()
        if selected_day in days:
            break
        print("Invalid day. Try again.")

    print('-' * 40)
    return selected_city, selected_month, selected_day


def load_data(selected_city, selected_month, selected_day):
    """Load and filter data."""

    file_path = CITY_DATA[selected_city]
    city_data = pd.read_csv(file_path)

    city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
    city_data['month'] = city_data['Start Time'].dt.month
    city_data['day_of_week'] = city_data['Start Time'].dt.day_name()

    # Filter by month
    if selected_month != 'all':
        month_index = ['january','february','march','april','may','june'].index(selected_month) + 1
        city_data = city_data[city_data['month'] == month_index]

    # Filter by day
    if selected_day != 'all':
        city_data = city_data[city_data['day_of_week'] == selected_day.title()]

    return city_data


def time_stats(city_data):
    """Show most common times."""

    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("Most common month:", city_data['month'].mode()[0])
    print("Most common day:", city_data['day_of_week'].mode()[0])
    print("Most common hour:", city_data['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(city_data):
    """Show most popular stations."""

    print('\n Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("Start station:", city_data['Start Station'].mode()[0])
    print("End station:", city_data['End Station'].mode()[0])

    city_data['Trip'] = city_data['Start Station'] + " -> " + city_data['End Station']
    print("Most common trip:", city_data['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(city_data):
    """Show trip duration stats."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("Total duration:", city_data['Trip Duration'].sum())
    print("Average duration:", city_data['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city_data):
    """Show user stats."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("User types:\n", city_data['User Type'].value_counts())

    if 'Gender' in city_data:
        print("\nGender:\n", city_data['Gender'].value_counts())

    if 'Birth Year' in city_data:
        print("\nEarliest:", int(city_data['Birth Year'].min()))
        print("Most recent:", int(city_data['Birth Year'].max()))
        print("Most common:", int(city_data['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        selected_city, selected_month, selected_day = get_filters()
        city_data = load_data(selected_city, selected_month, selected_day)

        time_stats(city_data)
        station_stats(city_data)
        trip_duration_stats(city_data)
        user_stats(city_data)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
    