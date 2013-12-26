# -*- coding: utf-8 -*-
from celery import task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from football.local import EMAIL_HOST_USER


@task
def send_mail_about_forecast(context, user_email):
    html = get_template('email.html')
    text = get_template('email.txt')
    subject, to = unicode(u'Администратор сайта www.ovz.ru ответил на ваш вопрос'), unicode(user_email)
    html_content = html.render(context)
    text_content = text.render(context)
    email = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, [to])
    email.attach_alternative(html_content, "text/html")
    return email.send()
