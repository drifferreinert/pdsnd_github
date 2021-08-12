import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_city = ['chicago', 'new york city', 'washington']

    city_choice = input('\n Which city would you like to see the data for? Please enter either Chicago, New York City, or Washington \n')

    if city_choice.lower() not in valid_city:
        while city_choice.lower() not in valid_city:
            print('This city is not in our database. Please chose either Chicago, New York City, or Washington \n')
            city_choice = input('\n Which city would you like to look see the data for? Please enter either Chicago, New York City, or Washington \n')


    else:
        print('You chose' + ' ' + city_choice.capitalize())

    # TO DO: get user input for month (all, january, february, ... , june)
    valid_month = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    month_choice = input('\n Which month would you like to see the data for? Please enter a month between January - June, or type "All" for no filters. \n')

    if month_choice.lower() not in valid_month:
        while month_choice.lower() not in valid_month:
            print('This month is not available. Please choose a month between January - June/')
            month_choice = input(' Which month would you like to see the data for? Please enter a month between January - June. \n')

    else:
        print('You chose' + ' ' + month_choice.lower())

    valid_day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    day_choice = input('Which day of the week would you like to see the data for?/ Choose "all" for no filter \n')

    if day_choice.lower() not in valid_day:
        while day_choice.lower() not in valid_day:
            print(' This day is not valid. Please choose a day of the week, or type "all" for no filter \n')
            day_choice = input('Which day of the week would you like to look at?/ Choose "all" for no filter \n')

    else:
        print('You chose' + ' ' + day_choice.capitalize())



    print('-'*40)
    return city_choice.lower(), month_choice.lower(), day_choice.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city == 'chicago':
        #chicago = pd.read_csv('chicago.csv')
        df = pd.read_csv('chicago.csv')

    elif city == 'new york city':
        #new_york_city = pd.read_csv('new_york_city.csv')
        df = pd.read_csv('new_york_city.csv')

    elif city == 'washington':
        #washington = pd.read_csv('washington.csv')
        df = pd.read_csv('washington.csv')

    else:
        print('This is not valid')

    '''Filter df on month and day
    Do not filter if all'''


    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day'] = df['Start Time'].dt.weekday_name


     # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

     # filter by day of week if applicable

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

#month, day, hour = load_data(city, month, day)

#def time_stats(month, day, hour):
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    print('The Most Popular Month To Use Bikeshare Is:' + ' ' + str(popular_month))


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.week
    popular_day = df['day'].mode()[0]

    print('The Most Popular Day Is:' + ' ' + str(popular_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print("The Most Popular Hour Is:" + " " + str(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most popular Start Station:' + ' ' + popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular End Station:' + ' ' + popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending = False)


    print('Popular Start & End Combination:' + ' ' + str(popular_start_end.head(1)))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()

    print('The total travel time in minutes is:' + ' ' + str(total_time))

    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print('The average travel time in minutes is:' + ' ' + str(average_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_count = df['User Type'].value_counts()
    print('Counts of User Types:' +  ' ' + str(type_count))


    # TO DO: Display counts of gender
    if 'Gender' in df:

        gender_count = df['Gender'].value_counts()

        print('Counts of Gender: ' + str(gender_count))

    else:
        print('Gender stats not in dataframe and cannot be calculated')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Birth Year of Users Is:' + ' ' + str(earliest_birth_year))

        recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year of Users Is:' + ' ' + str(recent_birth_year))

        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year of Users Is:' + ' ' + str(common_birth_year))

    else:
        print('Birth Year states not in dataframe and cannot be calculated')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def row_data(df):
    start_loc = 0
    view_data = input('Would you like to see 5 individual rows of data? Enter "Yes" or "No".').lower()

    while view_data != 'yes' and view_data != 'no':
        view_data = input('Your input is invalid. Please enter either "Yes" or "No"')

    if view_data == 'yes':
        while view_data == 'yes':

            print(df.iloc[0 + start_loc:5 + start_loc])
            start_loc += 5
            view_data = input('Would you like to see the next 5 rows of data? Enter "Yes" or "No".').lower()
            while view_data != 'yes' and view_data != 'no':
                view_data = input('Your input is invalid. Please enter either "Yes" or "No"')

    if view_data == 'no':
        print("Done! Thank you")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
