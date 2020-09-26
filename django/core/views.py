from django.shortcuts import render
from .models import Category, Product, Evaluation
from django.http import HttpResponse
from django.db.models import Avg

def home(request):
    products = Product.objects.order_by('name')
    categories = Category.objects.order_by('name')
    evaluations = Evaluation.objects.values('product_id').order_by('product_id').annotate(average = Avg('evaluation'))

    dict_evaluations = {}
    for evaluation in evaluations:
        dict_evaluations[evaluation.get("product_id")] = evaluation.get("average")

    context = {
        'categories': categories,
        'products': products,
        'evaluations': dict_evaluations
    }
    
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    return render(request, 'core/contact.html')

def product_evaluation(request):
    if request.is_ajax() and request.POST:
        evaluator_name = request.POST.get('evaluator_name')
        evaluator_email = request.POST.get('evaluator_email')
        evaluator_comment = request.POST.get('evaluator_comment')
        evaluator_evaluation = request.POST.get('evaluator_evaluation')
        product_id = request.POST.get('product_id')

        evaluation_object = {
            'evaluator_name': evaluator_name,
            'evaluator_email': evaluator_email,
            'evaluator_comment': evaluator_comment,
            'evaluator_evaluation': evaluator_evaluation,
            'product_id': product_id
        }
    
        evaluation = Evaluation()
        evaluation.intialize_object(evaluation_object)
        evaluation.save()
    return HttpResponse()


