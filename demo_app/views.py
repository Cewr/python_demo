from django.shortcuts import render
# from django.urls.base import is_valid_path
from . models import Topic, Entry

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'demo_app/index.html')


# @login_required(login_url='/users/login/')
@login_required
def topics(request):
    """显示所有的主题"""
    # ls = Topic.objects.order_by('date_added')
    ls = Topic.objects.filter(owner=request.user).order_by('date_added')

    context = {'ls': ls}
    return render(request, 'demo_app/topics.html', context)


def topicsAndItem(request, topic_id):
    """显示特定主题详情"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    # ls = Topic.objects.order_by('date_added')
    ls = Topic.objects.filter(owner=request.user).order_by('date_added')
    # 确定请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404

    context = {'topic': topic, 'entries': entries, 'ls': ls}
    return render(request, 'demo_app/topics.html', context)


def newTopic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交新数据：创建一个新表单
        form = TopicForm()
    else:
        # POST 提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            # form.save()
            # 关联到当前用户
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            # 重定向到页面 topics
            return HttpResponseRedirect(reverse('demo_app:topics'))

    content = {'form': form}
    return render(request, 'demo_app/new_topic.html', content)


def newEntry(request, topic_id):
    """再特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交新数据：创建一个新表单
        form = EntryForm()
    else:
        # POST 提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic

            new_entry.save()

            # 重定向到页面 topics/id
            return HttpResponseRedirect(reverse('demo_app:topics_item', args=[topic_id]))

    content = {'topic': topic, 'form': form}
    return render(request, 'demo_app/new_entry.html', content)


def editEntry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    #
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST 提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()

            # 重定向到页面 topics/id
            return HttpResponseRedirect(reverse('demo_app:topics_item', args=[topic.id]))

    content = {'topic': topic, 'form': form, 'entry': entry}
    return render(request, 'demo_app/edit_entry.html', content)
