from django.shortcuts import render
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from reading_count.utils import get_seven_days_read_data, get_today_hot_data
from blog.models import Blog


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)
    today_hot_data = cache.get('today_hot_data')
    if today_hot_data is None:
        today_hot_data = get_today_hot_data(blog_content_type)
        cache.set('today_hot_data', today_hot_data, 60*60)
    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = today_hot_data
    return render(request, 'home.html', context)
