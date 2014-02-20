    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        passenger_sex = passenger['Sex']
        passenger_class  = passenger['Pclass']
        passenger_age = passenger['Age']
        passenger_parch = passenger['Parch']
        passenger_sbsp = passenger['SibSp']
        passenger_fare = passenger['Fare']
        if passenger_sex == 'female':
            predictions[passenger_id] = 1
        elif passenger_class < 3 and passenger_age < 18 and passenger_parch > 0:
            predictions[passenger_id] = 1
        elif passenger_class == 1 and passenger_sex == "male" and passenger_fare > 300 and passenger_parch == 0:
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions


    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        print passenger
    return predictions