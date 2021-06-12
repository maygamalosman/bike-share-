import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def check_input(input_str,input_type):
    while True:
        selected_enter=input(input_str).lower()
        try:
            if selected_enter in ['chicago', 'new york city', 'washington'] and input_type ==1: 
                break
            elif selected_enter in ['january', 'february', 'march', 'april', 'may', 'june', 'all'] and input_type ==2:
                break 
            elif selected_enter in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] and input_type ==3:
                break
            else:
                if input_type ==1:
                    print ('this city is not avilable ,please select the city chicago , new york city or washington ')
                if input_type ==2:
                    print('this month is not avilable ,please select month january, february, march, april, may, june, all ')
                if input_type==3:
                    print('this day is not right ,please select monday, tuesday, wednesday, thursday, friday, saturday, all ')
                
        except ValueError:
            print('Please enter the right selection to allow me helping you ')
    return selected_enter

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city= check_input('chicago , new york city or washington ',1)

    month= check_input('january, february, march, april, may, june, all ',2)


    day=check_input('monday, tuesday, wednesday, thursday, friday, saturday, all ',3)

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
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    start_time = time.time()
    print('\nCalculating The Most Frequent Times of Travel...\n')
    

    

    commen_month=df['month'].mode()[0]
    print('commen month:', commen_month)

    popular_day=df['day'].mode()[0]
    print('Most Popular day:', popular_day)

    popular_hour=(df['hour'].mode()[0])
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""  
    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    start_time = time.time() 
    
    start_station=df['Start Station'].mode()[0]
    print('Most commonly start station: ', start_station)
  
    end_station=df['End Station'].mode()[0]
    print('Most commonly end station: ', end_station)
    
    frequent_combination = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1)
    
    print("\nthe most frequent combination of start station and end station trip is :\n")
    print(frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    travel_time=df['Trip Duration'].sum()
    print('total travel time is: ',travel_time)
   
    mean_travel_time=df['Trip Duration'].mean()
    print('average travel time is: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print ('counts of user types\n',user_types)

    
    if 'Gender'in df:
        gender_types=df['Gender'].value_counts()
        print ('counts of Gender\n',gender_types)
    else:  
        print ('Sorry,the city you entered has no avilable data  for GENDER to show try new york city or chicago.')

        

    if 'Birth Year'in df:
        earliest=df['Birth Year'].min()
        print('earliest year of birth is :',earliest)
        recent=df['Birth Year'].max()
        print('earliest year of birth is :',recent)
        common=df['Birth Year'].mode()[0]
        print('most common year of birth is :',common)
    else:  
        print ('Sorry,the city you entered has no avilable data for BIRTH DAY to show try new york city or chicago.')
    print("\nThis t'ook %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        viewData = input("Would you like to see the raw data? Type 'Yes' or 'No'.")
        if viewData == "Yes".lower():
            row = 0
            print("dataframe from row 0 to 5")
            
            row += 5
            print (df.head(row))
            
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                    break
        else:
            
            
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                    break

        
if __name__ == "__main__":
    main()

