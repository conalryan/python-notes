from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from MyFirstDjangoApp.blog.models import posts
from .forms import StockQuoteForm
from yahoo_finance import Share

def home(request):
    # form to get stok quote
    form = StockQuoteForm
    # Get all of the content from db then filter to only get first 10 blog posts
    entries = posts.objects.all()[:10]
    
    return render_to_response('index.html', {'posts' : entries, 'form' : form})

def quote(request):
    stockSymbol = request.GET['stock']
    stock = Share(stockSymbol)
    form = StockQuoteForm()
    context = {
               "form": form, 
               "stock": stockSymbol, 
               "price": stock.get_price(),
               "change": stock.get_change(),
               "volume": stock.get_volume(),
               "cap": stock.get_market_cap()
               }
    template = "quote.html"
    
    return render(request, template, context)

