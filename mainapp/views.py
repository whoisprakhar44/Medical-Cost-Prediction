from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res=0
    if request.method=='POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['sex'] 
        bmi = request.POST['bmi']
        child = request.POST['child']
        smoker = request.POST['smoker'] 
        region = request.POST['region'] 

        if name !='':
            df = pd.DataFrame(columns=['age', 'sex', 'bmi', 'children',	'smoker', 'region'])

            df_1 = {'age': float(age), 'sex': int(gender), 'bmi': float(bmi), 'children': int(child),
                   'smoker': int(smoker), 'region': int(region)}

            df = df.append(df_1, ignore_index=True)

            pickle_in = 'mainapp/MedicalCost_rf.pkl'
            model = pickle.load(open(pickle_in, 'rb'))
            pred = model.predict(df)
            print(pred)
        else:
            return redirect('homepage')
    else:
        pass
    return render(request, 'index.html', {'response' : res})