


def user_temp_input():
    __temp = float(input('What is the temperature? '))
    return __temp
def temp_messurment_select():
    __select = input('Fahrenheit or Celsius (F/C)? ').lower()
    if __select == 'f' or __select == 'c':
        __mesurment = __select
    else:
        print('Please select valid option.')
        temp_messurment_select()
    return __mesurment
def convert_to_c(wind):
    __f = wind
    __c = (__f - 32) * (5/9)
    return __c


def wind_chill_factor(temperature):
    __t = temperature
    for __v in range(1,61):
        __wind_chill = 35.74 + 0.6215 * __t -35.75 * (__v**0.16) + (0.4275* __t * (__v ** 0.16))
        if __v == 5 or __v == 10 or __v == 15 or __v == 20 or __v == 25 or __v ==30 or __v == 35 or __v == 40 or __v == 45 or __v == 50 or __v == 55 or __v ==60:
            if f_or_c == 'f':
                print(f'At Temperature {__t:.0f} º{f_or_c.upper()}, and wind speed of {__v} mph, the windchill is: {__wind_chill:.2f} º{f_or_c.upper()}')
            elif f_or_c == 'c':
                __c_wind_chill = convert_to_c(__wind_chill)
                print(f'At Temperature {__t:.0f} º{f_or_c.upper()}, and wind speed of {__v} mph, the windchill is: {__c_wind_chill:.2f} º{f_or_c.upper()}')


temp = user_temp_input()
f_or_c = temp_messurment_select()
wind_chill_factor(temp)