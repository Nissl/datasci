    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        passenger_sex = passenger['Sex']
        passenger_class  = passenger['Pclass']
        passenger_age = passenger['Age']
        if passenger_sex == 'female':
            predictions[passenger_id] = 1
        elif passenger_class == 1 and passenger_age < 18:
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions