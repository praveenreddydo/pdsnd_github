import time
import pandas as pd
import numpy as np
import collections as col

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

sel_months=['all','january','february','march','aprail','may','june']
sel_days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    print("welcome to udacity project")
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #print("\n Hello! select the city  \n 1.chicago 2.new york city 3.washington ")
    
    city=""
    while True:
        cities=['chicago','new york city','washington']
        city=input("\n select  the city to know the data ? \n 1.chicago 2.new york city 3.washington :  ").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("\n try again by choosing available city in cities")
            
            
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month=input("\n which month do want to know ").lower()
        if month in sel_months:
            break
        else:
            print(" you need to select correct month " )
            
      # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)       
    while True: 
       day=input("\n which day do want to know ? all,monday,tuesday,wednesday,thursday,friday,saturday,sunday ").lower()
    
       if day in sel_days:
           break
       else:
           print(" oops! you need to select correct day of week " )
        

    print('-'*40)
    #return date
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
    
    
    #start time to date time
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    df['month']=df['Start Time'].dt.month
    
    df['day_of_week']=df['Start Time'].dt.weekday_name
    
    df['hour']=df['Start Time'].dt.hour
    
    if month !='all':
        month=sel_months.index(month)
        
        #create new data frame
        df=df.loc[df['month']==month]
        
    if day !='all' :   
        
        df=df.loc[df['day_of_week']==day.title()]
    

    return df
pass


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print("most popular month:{} ".format(popular_month))

    # TO DO: display the most common day of week
    popular_day_of_week=df['day_of_week'].mode()[0]
    print("most popular day:{} ".format(popular_day_of_week))
    

    # TO DO: display the most common start hour
    common_start_hour=df['hour'].mode()[0]
    print("most common start hour:{} ".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print("most commonly used start station : {}".format(popular_start_station))

    # TO DO: display most commonly used end station
    commonly_end_station=df['Start Station'].mode()[0]
    print("most commonly end station : {}".format(commonly_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_combo=df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1)
    print("display most frequent combination of start station and end station trip  {}".format(popular_combo))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("total travel time : {}".format(total_travel_time))

    # TO DO: display mean travel time

    mean_travel_time=df['Trip Duration'].mean()
    print("Mean travel time : {}".format(mean_travel_time))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print("counts of user types : {}".format(user_types))
    

    # TO DO: Display counts of gender
    if (city == 'chicag0')or (city =='new york city'):
        gender=df['Gender'].values_counts()
        print("counts of gender : ",gender)
    
    
        # TO DO: Display earliest, most recent, and most common year of birth
    
        print("earliest year of birth : {}".format(int(df['Birth Year'].min())))
    
        print("most recent year of birth : {} ".format(int(df['Birth Year'].max())))
  
        print("most common year of birth : {}".format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    print(df.head())
    
    user_input=input("\n Type yes to see next row data or enter no to skip(yes/no) \n").lower()
    limit=0
    while (user_input !='no'):
        limit += 5
        print(df.iloc[limit:limit+5])
    
    
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    
	main()
