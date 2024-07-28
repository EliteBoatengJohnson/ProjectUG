from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Item_Category, Claim, Report
from .forms import ReportForm,ClaimForm

def home(request):
    categories = Item_Category.objects.all()
    recent_items = Item.objects.filter(status='found').order_by('-created')[:10]
    return render(request, 'home.html', {'categories': categories, 'recent_items': recent_items})

def category_detail(request, slug):
    category = get_object_or_404(Item_Category, slug=slug)
    items = Item.objects.filter(category=category, status='found')
    return render(request, 'category_detail.html', {'category': category, 'items': items})

def item_detail(request, id, slug):
    item = get_object_or_404(Item, id=id, slug=slug)
    return render(request, 'item_detail.html', {'item': item})

@login_required
def report_item(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.reporter = request.user
            item.save()
            return redirect('item_detail', id=item.id, slug=item.slug)
    else:
        form = ReportForm()
    return render(request, 'report_item.html', {'form': form})

@login_required
def claim_detail(request, id):
    claim = get_object_or_404(Claim, id=id)
    return render(request, 'claim_detail.html', {'claim': claim})

@login_required
def claim_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.item = item
            claim.claimant = request.user
            claim.save()
            return redirect('claim_detail', id=claim.id)
    else:
        form = ClaimForm()
    return render(request, 'claim_item.html', {'form': form, 'item': item})

def report_detail(request, id):
    report = get_object_or_404(Report, id=id)
    return render(request, 'report_detail.html', {'report': report})