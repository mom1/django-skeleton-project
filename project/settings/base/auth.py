# -*- coding: utf-8 -*-
# @Author: Maximus
# @Date:   2017-07-07 11:34:49
# @Last Modified by:   Maximus
# @Last Modified time: 2017-07-07 11:35:01
# Authentication Settings
from django.core.urlresolvers import reverse_lazy

AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")
