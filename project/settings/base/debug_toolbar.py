DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
}
INTERNAL_IPS = ['127.0.0.1']

if DEBUG:
    # noinspection PyUnboundLocalVariable
    INSTALLED_APPS = INSTALLED_APPS + (
        'debug_toolbar',
    )

    # noinspection PyUnboundLocalVariable
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
