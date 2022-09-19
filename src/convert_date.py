from datetime import datetime, timedelta


def get_correct_date(date):
    
    now = datetime.now()

    if 'minute' in date:
        date = date.split(' ')
        if date[0].isnumeric():
            minutes = int(date[0])
        else:
            minutes = int(date[1])
        now -= timedelta(minutes=minutes)

        day = now.strftime("%d")
        month = now.strftime("%m")
        year = now.strftime("%Y")
        return f'{day}-{month}-{year}'

    elif 'hour' in date:       
        date = date.split(' ')

        if date[0].isnumeric():
            hours = int(date[0])
        else:
            hours = int(date[1])
        now -= timedelta(hours=hours)

        day = now.strftime("%d")
        month = now.strftime("%m")
        year = now.strftime("%Y")
        return f'{day}-{month}-{year}'

    elif 'Yesterday' in date:
        now -= timedelta(days=1)

        day = now.strftime("%d")
        month = now.strftime("%m")
        year = now.strftime("%Y")
        return f'{day}-{month}-{year}'

    else:
        date = date.replace('/', '-')
        return date