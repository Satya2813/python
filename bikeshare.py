import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA={'january':1,'february':2,
            'march':3,'april':4,
            'may':5,'june':6,'all':'all' }


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
    city=input("Please enter city among chicago, new york city, washington :")
    city=city.lower()
    
    my_city_list=['chicago', 'new york city', 'washington']
    
    while True:
        if(city in my_city_list):
            break
        else:
            city=input("Please enter city among chicago, new york city, washington :")
            city=city.lower()
                 
         

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Select a month among(all, january, february, ... , june) :")
    month=month.lower()

    my_month_list=['all','january','february','march','april','may','june']
    while True:
        if(month in my_month_list):
            break
        else:
            month=input("Select a month among(all, january, february, ... , june) :")
            month=month.lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Select a day of week among (all, monday, tuesday, ... sunday):")
    day=day.lower()
    
    day_list=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        if(day in day_list):
            break
        else:
            day=input("Select a day of week among (all, monday, tuesday, ... sunday):")
            day=day.lower()
            
    print('-'*40)
    
    #while True:
        #if(MONTH_DATA[month] in my_month_list):
            
    month=MONTH_DATA[month]
            
        
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
    
    df=pd.read_csv(CITY_DATA[city])
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time']=pd.to_datetime(df['End Time'])
    #name of the month to filter
    df['Month']=df['Start Time'].dt.month
    if(month !='all'):        
        df=df[df['Month']==month]    
    #name of the day of week to filter by
    df['Day']=df['Start Time'].dt.weekday_name.str.lower()
    if(day!='all'):
        df=df[df['Day']==day]
        
    return df


def time_stats(df):
    
    
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Month']=df['Start Time'].dt.month
    mostcommonmonth=df['Month'].mode()[0]
    print("The most common month is",mostcommonmonth)
    

    # TO DO: display the most common day of week
    df['Day']=df['Start Time'].dt.weekday_name
    mostcommonday=df['Day'].mode()[0]
    print("The most common day of week is",mostcommonday)

    # TO DO: display the most common start hour
    df['Hour']=df['Start Time'].dt.hour
    mostcommonhour=df['Hour'].mode()[0]
    print("The most common hour is",mostcommonhour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostpopularstation=df['Start Station'].mode()[0]
    print("The most commonly used start station is: ",mostpopularstation)
    


    # TO DO: display most commonly used end station
    mostpopularendstation=df['End Station'].mode()[0]
    print("The most commonly used end station is:",mostpopularendstation)


    # TO DO: display most frequent combination of start station and end station trip
    df['Roundtrip']=df['Start Station']+'-'+df['End Station']
    mostcombination=df['Roundtrip'].mode()[0]
    print("The most frequent combination of start station and end station trip is:",mostcombination)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Time']=df['Trip Duration']/60
    sum_travel=df['Time'].sum()
    print("Total travel time is",sum_travel)


    # TO DO: display mean travel time
    mean_travel=df['Time'].mean()
    print("The mean travel time is",mean_travel)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    
  
    # TO DO: Display counts of user types
    
    df['my_count']=1
    print(df.groupby('User Type').count()['my_count'])   


    # TO DO: Display counts of gender
    if(city!='washington'):
       
        df['gender_count']=1
       
        print(df.groupby('Gender').count()['gender_count'])

    # TO DO: Display earliest, most recent, and most common year of birth
    #earliest
    if(city!='washington'):
        
        earliest=df['Birth Year'].min()
        
        print(earliest)
    
    #Most Recent
    if(city!='washington'):
        
        Recent_year=df['Birth Year'].max()
        
        print(Recent_year)
    #Most Common
    if(city!='washington'):
        
    
        most_common_year =df['Birth Year'].mode()
        print(most_common_year[0])
    #Most_Common=df['Birth Year'].mode()[0]
    #print(Most_Common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        count=0
        while True:
            showdata = input('\nWould you like to see the next 5 lines of data? Enter yes or no.\n')
            if showdata.lower() != 'yes':
                break
            else:                
                print(df.iloc[count:count+4,:])
                count = count + 5


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
