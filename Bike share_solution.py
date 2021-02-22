#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries 
import time
import pandas as pd
import numpy as np


# In[2]:


#dict have csv files for cities being analyzed
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_list=['january', 'february', 'march ', 'april', 'may', 'june', 'all']

day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


# In[3]:


#first_FUNCTION
"""
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
def get_filters() :
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington).
    
    while True :
        city=input('please enter city name you need data about\t').lower()
        if city not in CITY_DATA:
            print ('please input city name correctly ')
        else:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month = input("please choose month 'or' all\t").lower()
        if month not in month_list:
            print ('please input month name correctly ')
        else:
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("please choose day 'or' all\t").lower()
        if day not in day_list:
            print ('please input day name correctly ')
        else:
            break
    
    print('-'*40)
    return city, month, day
        


# In[4]:


def load_data(city, month, day):
    
    print("\nLoading data...")
    
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
    
    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = month_list
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]#.title() converts to capital
    #print(df.head(number of rows you want to display))

    return df


# In[5]:


def display_raw_data(df):
    
    i=0
    answer = input('would you like to dispaly the first 5 rows of data?? yes/no:\t').lower()
    pd.set_option('display.max_columns', None)
    
    while True :
        if answer ==  'no':
            break
        print(df[i:i+5])
        answer = input('would you like to dispaly the next first 5 rows of data?? yes/no:\t').lower()
        i += 5


# In[6]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print ('the most common month is: ', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print ('the most common day: ', common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print ("the most common hour is: ", common_hour)
    

    #the time it took 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('the most commn start station is ', common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('the most commn end station is ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_from_start_to_end=( df['Start Station'] + '__' + df['End Station']).mode()[0]
    print ('the most common frequent combination of start and end stations is: ', common_from_start_to_end)

    #time token 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_duration = df['Trip Duration'].sum()
    print ('the total travel time is:', total_time_duration, 'seconds')


    # TO DO: display mean travel time
    avg_time = df['Trip Duration']
    print ('average travle time is:', avg_time, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 


# In[9]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types Subscriber or Customer
    user_type = df['User Type'].value_counts()
    print('counts of user type is ', user_type)

    # TO DO: Display counts of gender
    try:
        gender = df['gender'].vlaue_counts()
        print('the type of users by gender is ', gender)
    except:
        print('there is no gender coloums in this csv_file')

    # TO DO: Display earliest, most recent, and most common year of birth     
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("there is no birth year coloums in this csv_file")
    
    #
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

