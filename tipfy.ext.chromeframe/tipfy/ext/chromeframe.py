# -*- coding: utf-8 -*-
"""
    tipfy.ext.chromeframe
    ~~~~~~~~~~~~~~~~~~~~~

    Implements the server side requirements for Chrome Frame usage in clients.

    :copyright: 2010 Lee Olayvar.
    :license: MIT, see LICENSE.txt for more details.
"""
from __future__ import absolute_import

from tipfy import request
from genshi import Markup

default_config = {
    'gcf_enable_mode':'header',
    'gcf_required':False,
    'gcf_prompt_message':('Google Code Frame is required to view this page. '
                          '<a href="http://www.google.com/chromeframe/eula.html">Click here</a> to install it.'),
    'gcf_prompt_css':'''
        .chromeFrameInstallDefaultStyle {
            width: 100%; /* default is 800px */
            border: 5px solid blue;
        }
    ''',
    'gcf_prompt_script':'''
        <!--[if IE]>
            <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/chrome-frame/1/CFInstall.min.js"></script>
            <style>
                %(prompt_css)s
            </style>
            <div id="prompt">
                %(prompt_message)s
            </div>
            <script>
                window.attachEvent("onload", function() {
                    CFInstall.check({
                        mode: "inline",
                        node: "prompt"
                    });
                });
            </script>
        <![endif]-->
    '''
}

class ChromeFrameMiddleware(object):
    def pre_dispatch_handler(self):
        context = request.context
        
        if default_config['gcf_enable_mode'] == 'meta':
            context['gcf_meta'] = Markup('<meta http-equiv="X-UA-Compatible" content="chrome=1">')
        
        if default_config['gcf_required']:
            context['gcf_prompt_script'] = Markup(default_config['gcf_prompt_script'] % {
                'prompt_message':default_config['gcf_prompt_message'],
                'prompt_css':default_config['gcf_prompt_css'],
            })
    
    def post_dispatch_handler(self, response):
        if default_config['gcf_enable_mode'] != 'meta':
            response.headers['X-UA-Compatible'] = 'chrome=1'
        return response
