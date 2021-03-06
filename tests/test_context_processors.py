from __future__ import unicode_literals

from inspect import cleandoc
from flask_genshi import render_response


def test_updates_context(app):
    """Render calls update the template context with context processors"""
    with app.test_request_context():

        @app.context_processor
        def inject_rudolf():
            return dict(rudolf="The red-nosed reindeer")

        rendered = render_response("context.html")

        # Remove leading indentation and encode since `render_response` returns bytes
        expected_data = cleandoc(
            """
            <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
            <pre>rudolf = The red-nosed reindeer</pre>
            """
        ).encode("UTF-8")

        assert rendered.mimetype == "text/html"
        assert rendered.data == expected_data
