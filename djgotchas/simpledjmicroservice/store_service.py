#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Store Micro Service
"""

# https://stackoverflow.com/questions/32866578/single-file-django-drf-project
# https://stackoverflow.com/questions/1297873/how-do-i-write-a-single-file-django-application
# https://arunrocks.com/django-application-in-one-file/
# To run -> python store_service.py runserver 0.0.0.0:4000

import os
import sys
import json
import logging
from django.conf import settings
from django.urls import path
from elasticsearch_dsl.search import Search
from elasticsearch import Elasticsearch, ConnectionError


# ==================== Application Configuration Start ======================== #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# use base_dir as import root
sys.path[0] = os.path.dirname(BASE_DIR)

# the current folder name will also be our app
APP_LABEL = os.path.basename(BASE_DIR)


settings.configure(
    DEBUG=os.environ.get('DEBUG', 'on') == 'on',
    SECRET_KEY=os.environ.get('SECRET_KEY', os.urandom(32)),
    ALLOWED_HOSTS=os.environ.get('ALLOWED_HOSTS', 'localhost').split(','),
    ROOT_URLCONF=__name__,
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        ],
    INSTALLED_APPS=[
        APP_LABEL,
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, "templates"), ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
    STATIC_URL='/static/',
    STATICFILES_DIRS=[
        os.path.join(BASE_DIR, "static"),
    ],
    STATIC_ROOT=os.path.join(BASE_DIR, "static_root"),
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s|%(asctime)s|%(module)s|%(process)d|%(thread)d|%(message)s',
                'datefmt' : "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s|%(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': 'application.log',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'DM': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True,
                'formatter':'verbose'
            },
        },
    },
    REST_FRAMEWORK={
        'DEFAULT_RENDERER_CLASSES': (
                'rest_framework.renderers.JSONRenderer',
                'rest_framework.renderers.BrowsableAPIRenderer',
            ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAdminUser',
        ],
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10
    }
)

# ==================== Application Configuration End ============================== #


# ============================ Elastic Connection Start =========================== #


logger = logging.getLogger('DM')


class ElasticConnection:

    @staticmethod
    def get_elastic_connection():

        """
            Elastic server connection
            create connection that will automatically inspect the cluster to get
            the list of active nodes
        """

        with open('config/digitmarketconfig.json') as json_config:
            config_data = json.load(json_config)

        if config_data['IS_AWS_ELASTIC_CONNECTION']:
            try:
                es = Elasticsearch([config_data['HAYSTACK_CONNECTION_URL']])
            except ConnectionError:
                logger.error('Error occured during elasticsearch connection')
                es = None
        else:
            full_url = config_data['HAYSTACK_CONNECTION_URL'].split(":")
            elastic_host = ":".join(full_url[:2])
            elastic_port = full_url[-1][:-1]
            try:
                es = Elasticsearch(hosts=elastic_host, port=elastic_port)
            except ConnectionError:
                logger.error('Error occured during elasticsearch connection')
                es = None
        return es

# ============================ Elastic Connection Start =========================== #


from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework import serializers


class FetchStoreSerializer(serializers.Serializer):

    """
        Fetch store API serializer
    """

    store_id = serializers.IntegerField(
                        required=True,
                        error_messages={'required': u'Please pass the store id'})


class FetchStore(GenericAPIView):

    authentication_classes = ()
    permission_classes = ()

    def dispatch(self, request, *args, **kwargs):
        self.es = ElasticConnection.get_elastic_connection()
        return super(FetchStore, self).dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        return FetchStoreSerializer

    def get(self, request):

        """
            API to fetch store

            @params: store_id: integer
            @returns: Retrive store information
        """

        result = {}
        store_id = int(request.query_params.get('store_id'))
        serializer = FetchStoreSerializer(data=request.query_params)
        if serializer.is_valid():
            search = Search(using=self.es, index="store_data_index")
            search = search.filter("match", store_id=store_id)
            data = search.execute().to_dict()
            if data['hits']['hits']:
                result['status'] = True
                result['data'] = data['hits']['hits'][0]['_source']
            else:
                result['status'] = False
                result['message'] = 'No data found for the give store id'
            status_code = status.HTTP_200_OK
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            result = {'status': False, 'message': serializer.errors}
        return Response(result, status=status_code)


urlpatterns = [
    path('api/fetch-store', FetchStore.as_view()),
]


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
