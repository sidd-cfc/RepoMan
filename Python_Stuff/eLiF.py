Goals = 25  # Set Goals to a non-numeric value

if isinstance(Goals, int):  # Check if Goals is an integer
    if Goals >= 20:
        print('Good attacker')
    elif Goals >= 10:
        print('You are an Okish attacker')
    elif Goals < 10:
        print('You are trash bro')
else:
    print('Just retire')
