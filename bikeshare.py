import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello all! Let\'s explore some US bikeshare data!')
    while True:
       city = input('City to explore chicago, new york city or washington? \n> ').lower()
       if city in CITIES:
           break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input ("Please input month name(all, january, ..., june: ").lower()
        if month in MONTHS:
           break
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
        
    while True:
        day = input("Please input day of week (all, monday, ... sunday): ").lower()
        if day in DAYS:
           break


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("Common month is :", common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("Common day of week is :", common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].value_counts().idxmax()
    print("Common start hour is :", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    #common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    #print("The most commonly used start station and end station : {}, {}"\
        #    .format(common_start_end_station[0], common_start_end_station[1]))

    df['routes'] = df['Start Station']+ "-" + df['End Station'] 
    print("The most common start and end station combo is: {}".format(df['routes'].value_counts().idxmax()))
   
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:")
    print(df['User Type'].value_counts())

 
    if city != 'washington': 
        # Display counts of gender 
            print("Here are the counts of gender:") 
            print(df['Gender'].value_counts())
        
        # Display earliest, most recent, and most common year of birth         
            print("The earliest birth year is: {}".format(str(df['Birth Year'].min())))
            
            print("The latest birth year is: {}".format(str(df['Birth Year'].max())))
             
            print("The most common birth year is: {}".format(str(df['Birth Year'].mode().values[0])))
            


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
            
    
        start_nr = 0
        end_nr = 5
        
        display_active = input("More raw data(yes or no)?: ").lower()
            
        while display_active == 'yes': 
              

              print(df.iloc[start_nr:end_nr,:]) 
              start_nr += 5 
              end_nr += 5 
                    
              display_active = input("Do you wish to continue(yes or no)?").lower()
               # if end_display == 'no': 
                 #   break 

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart or quit? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
