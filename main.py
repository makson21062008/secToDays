def convert(seconds):
    weeks = seconds // (7 * (24 * 3600))
    seconds %= 7 * 24
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %=60
    print(f'{weeks}:{days}:{hours}:{minutes}:{seconds}')

sec = int(input('введите кол-во секунд'))
convert(sec)
