from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from stockmarket.models import StockMarket, StockQuery
from stockmarket.forms import StockMarketForm, StockQueryForm
import xlwt


def about(request):
    stock_list = StockMarket.objects.all()
    print(stock_list)
    return render(request, 'stockmarket/base.html', {'stock_list': stock_list})


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = stock_sheet' + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('stock_sheet')
    row_num = 0

    columns = ['Stock Id', 'Username', 'Query']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    rows = StockQuery.objects.all().values_list('stock_id', 'username', 'query')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num])
    wb.save(response)
    return response


def add_query(request):
    if request.method == 'POST':
        form = StockQueryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock  query has been added "))
            return redirect('about')
    return redirect('about')






def add_stock(request):
    if request.method == 'POST':
        form = StockMarketForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added "))
            return redirect('add_stock')
    else:
        ticker = StockMarket.objects.all()
        return render(request, 'stockmarket/add_stock.html', {'ticker': ticker})
