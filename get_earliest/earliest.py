def get_earliest(*dates):
    splitted_dates = [f'{y}{m}{d}' for m,d,y in (date.split("/") for date in dates)]
    min_date = sorted(splitted_dates)[0]
    return f'{min_date[4:6]}/{min_date[6:]}/{min_date[:4]}'
