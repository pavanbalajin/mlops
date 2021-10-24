from django.http import JsonResponse
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import joblib
# Create your views here.
class Test(APIView):

    def get(self, request):

        return JsonResponse({"key": "Hello World"})
		
    def post(self, request):
	
        sepal_length = request.data['sepal_length']
        sepal_width = request.data['sepal_width'] 
        petal_length = request.data['petal_length'] 
        petal_width = request.data['petal_width'] 
        print(os.getcwd())
        print("Hi")
        model = joblib.load(os.path.join('./models/svm.pkl'))
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        if (prediction == 0) :
                predicted_class = 'Iris-setosa'
        elif (prediction == 1):
                predicted_class = 'Iris-versicolor'
        else:
                 predicted_class = 'Iris-virginica'

        return JsonResponse({
            'Prediction': predicted_class
        })
class FileHandling(APIView):

    def post(self, request):

        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage()
        path_image_1 = fs.save(os.path.join(settings.BASE_DIR, "learning" , pdf_file.name), pdf_file)
        return JsonResponse({"status":"file saved"})


