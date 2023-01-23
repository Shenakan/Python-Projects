def main():
    print(show_bibliograpy(request_dates()))

def show_bibliograpy(dates):
    return f'- Name: {dates[0]} \n' \
           f'- Birthday: {dates[1]} \n' \
           f'- Address: {dates[2]} \n' \
           f'- Goal: {dates[3]} '

def request_dates():
    dates = []
    dates.append(input("Enter your first and last name: "))

    while (len(dates[0]) <= 1):
        dates[0]=input("The name is not right, please enter again: ")

    dates.append(input("Enter your birthday: "))
    dates.append(input("Enter your address: "))
    dates.append(input("Enter your goal: "))

    return dates

if __name__ == '__main__':
    main()