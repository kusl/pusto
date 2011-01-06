from naya.helpers import marker


REDIRECTS = (
    ('/post/avtozagruzka-klassov-v-prilozheniyah-na-zend-framework/',
    'blog/2008/09/25/avtozagruzka-klassov-v-prilozheniyah-na-zend-framework',
    'r/zf-autoload'),
    ('/post/unikalniy-nick/', 'r/nick'),
)


@marker.defaults()
def defaults():
    return {
        'theme': {'path_suffix': '_data'},
        'jinja': {'path_suffix': '_data'}
    }


@marker.route('/<path:path>')
def redirector(app, path):
    path = path.rstrip('/')
    for paths in REDIRECTS:
        if path in paths:
            return app.redirect(paths[0])
    app.abort(404)