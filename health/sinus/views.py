from django.shortcuts import render
def determine_sinus_stage(symptoms):
    if symptoms.get('nasalCongestion'):
        if symptoms.get('thickDischarge') or symptoms.get('facialPain') or symptoms.get('headache'):
            if symptoms.get('soreThroat') or symptoms.get('fatigue') or symptoms.get('fever') or symptoms.get('badBreath') or symptoms.get('toothache'):
                return 'Severe Sinus Infection'
            else:
                return 'Moderate Sinus Infection'
        else:
            return 'Mild Sinus Infection'
    else:
        return 'No Sinus Infection'

def symptom_check(request):
    if request.method == 'POST':
        symptoms = {
            'nasalCongestion': bool(request.POST.get('nasalCongestion')),
            'thickDischarge': bool(request.POST.get('thickDischarge')),
            'facialPain': bool(request.POST.get('facialPain')),
            'headache': bool(request.POST.get('headache')),
            'senseOfSmell': bool(request.POST.get('senseOfSmell')),
            'cough': bool(request.POST.get('cough')),
            'soreThroat': bool(request.POST.get('soreThroat')),
            'fatigue': bool(request.POST.get('fatigue')),
            'fever': bool(request.POST.get('fever')),
            'badBreath': bool(request.POST.get('badBreath')),
            'toothache': bool(request.POST.get('toothache')),
        }
        
        stage = determine_sinus_stage(symptoms)
        return render(request, 'result.html', {'stage': stage})
    
    return render(request, 'index.html')
