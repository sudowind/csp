import random

from celery import shared_task
from celery.task import periodic_task
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from djcelery.models import PeriodicTask, CrontabSchedule

from cstasker.models import Task, UserTask, UserQuestionnaire, Questionnaire
from utils.auth import login_required
from utils.utils import gen_ut_id, send_notification

from django.utils import timezone


def gen_task(user, task):
    ut_id = gen_ut_id()
    publish_time = datetime.now()
    # end_time = publish_time + timedelta(seconds=10)
    end_time = publish_time + timedelta(hours=5)
    user_task = UserTask(task=task, user=user, status=0, publish_time=publish_time, end_time=end_time,
                         ut_id=ut_id)
    user_task.save()
    schedule = CrontabSchedule.objects.create(
        minute=end_time.minute + 1,
        hour=end_time.hour,
        day_of_month=end_time.day,
    )
    PeriodicTask.objects.create(
        crontab=schedule,
        name='auto finish task {}'.format(ut_id),
        task='cstasker.task.finish_user_task',
        args=[ut_id]
    )


def gen_questionnaire(user, questionnaire):
    uq_id = gen_ut_id()
    publish_time = datetime.now()
    # publish_time = timezone.now()
    end_time = publish_time + timedelta(hours=5)
    # end_time = publish_time + timedelta(days=1)
    user_questionnaire = UserQuestionnaire(questionnaire=questionnaire, user=user, status=0,
                                           publish_time=publish_time, end_time=end_time, uq_id=uq_id)
    user_questionnaire.save()
    schedule = CrontabSchedule.objects.create(
        minute=end_time.minute + 1,
        hour=end_time.hour,
        day_of_month=end_time.day
    )
    PeriodicTask.objects.create(
        crontab=schedule,
        name='auto finish questionnaire {}'.format(uq_id),
        task='cstasker.task.finish_user_questionnaire',
        args=[uq_id]
    )


@shared_task
def add(x, y):
    return x + y


@shared_task
def hello():
    print('hello celery')


@login_required
@shared_task
def gen_task_for_user(user):
    # print(user)
    task = Task.objects.filter(type=0)[0]
    # print(task)
    # publish_time = datetime.now()
    # end_time = publish_time + timedelta(days=1)
    # user_task = UserTask(task=task, user=user, publish_time=publish_time, end_time=end_time)
    # user_task.save()
    gen_task(user, task)


@shared_task
def gen_task_for_all():
    task = Task.objects.all()
    users = User.objects.all()
    for u in users:
        index = random.randint(0, len(task) - 1)
        gen_task(u, task[index])
    send_notification("新的任务")


@shared_task
def gen_questionnaire_for_all():
    questionnaire = Questionnaire.objects.all()
    print(questionnaire)
    users = User.objects.all()
    for u in users:
        index = random.randint(0, len(questionnaire) - 1)
        gen_questionnaire(u, questionnaire[index])
    send_notification("新的问卷")


@shared_task
def finish_user_task(ut_id):
    print(ut_id)
    task = UserTask.objects.filter(ut_id=int(ut_id), status__in=[0, 2])
    if len(task) > 0:
        task[0].status = 5
        task[0].save()


@shared_task
def finish_user_questionnaire(uq_id):
    uq = UserQuestionnaire.objects.filter(uq_id=int(uq_id), status__in=[0])
    if len(uq) > 0:
        uq[0].status = 2
        uq[0].save()


# @periodic_task(run_every=timedelta(seconds=10))
# def some_task():
#     print('periodic task starts')
