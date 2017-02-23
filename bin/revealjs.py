# -*- coding: utf-8 -*-

import sys

import os
import tempfile
import subprocess

TEMPLATE = u'''
<!doctype html>
<html lang="zh">

	<head>
		<meta charset="utf-8">

		<title>%(title)s</title>

		<meta name="apple-mobile-web-app-capable" content="yes">
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

		<link rel="stylesheet" href="http://s.zys.me/js/revealjs/css/reveal.css">
		<link rel="stylesheet" href="http://s.zys.me/js/revealjs/css/theme/league.css" id="theme">

		<!-- Theme used for syntax highlighting of code -->
		<link rel="stylesheet" href="http://s.zys.me/js/revealjs/lib/css/zenburn.css">

		<!--[if lt IE 9]>
		<script src="http://s.zys.me/js/revealjs/lib/js/html5shiv.js"></script>
		<![endif]-->

        <style type="text/css">
          .reveal { color: #ddd; }
          .reveal h1 { font-size: 1.5em; color: white; }
          .reveal h2 { font-size: 1.2em; color: white; }
          .reveal h3 { font-size: 0.7em; color: white; }
          .reveal h4 { font-size: 0.5em; }
          .reveal h1 { text-shadow: 2px 2px 2px gray; }
          .reveal p { text-align: left; font-size: 0.8em; line-height: 1.3em; }
          .reveal li { font-size: 0.8em; margin: 0.5em 0; }
          .reveal code { color: #52E852; }
          .reveal strong, .reveal b { color: #FF1E1E; font-weight: normal; }
          .reveal em { color: #F9843E; font-style: normal; }

        </style>
	</head>

	<body>
		<div class="reveal">
			<!-- Any section element inside of this container is displayed as a slide -->
			<div class="slides">
                        %(main)s
                        </div>
                </div>

		<script src="http://s.zys.me/js/revealjs/lib/js/head.min.js"></script>
		<script src="http://s.zys.me/js/revealjs/js/reveal.js"></script>

		<script>

			// More info https://github.com/hakimel/reveal.js#configuration
			Reveal.initialize({
				controls: true,
				progress: true,
				history: true,
				center: true,

				transition: 'slide', // none/fade/slide/convex/concave/zoom

				// More info https://github.com/hakimel/reveal.js#dependencies
				dependencies: [
					{ src: 'http://s.zys.me/js/revealjs/lib/js/classList.js', condition: function() { return !document.body.classList; } },
					{ src: 'http://s.zys.me/js/revealjs/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
					{ src: 'http://s.zys.me/js/revealjs/plugin/zoom-js/zoom.js', async: true },
					{ src: 'http://s.zys.me/js/revealjs/plugin/notes/notes.js', async: true },
                    { src: 'http://s.zys.me/js/revealjs/plugin/math/math.js', async: true }
				]
			});

		</script>

	</body>
</html>
'''


def convert(source, type, target):
    tf = tempfile.mktemp()
    with open(tf, 'wb') as f: f.write(source.encode('utf8'))
    out = subprocess.check_output(['pandoc',
                                   '--email-obfuscation=none',
                                   '-f', type,
                                   '-t', target,
                                   tf], close_fds=True)
    os.remove(tf)
    return out



if(len(sys.argv) < 3):
    print 'revealjs.py IN_FILE OUT_FILE'
    sys.exit(1)


in_file = sys.argv[1]
out_file = sys.argv[2]


with open(in_file, 'rb') as f:
    data = f.read().decode('utf8')
    head, data = data.split('\n\n', 1)
    title, user, _ = head.split('\n', 2)

data = convert(data, 'markdown_github', 'revealjs').decode('utf8')
pre = u'''
<section class="slide level1">
  <h1>%s</h1>
  <h4>%s</h4>
</section>
''' % (title, user)
data = pre + data
html = TEMPLATE % {'title': title, 'main': data}


with open(out_file, 'wb') as f:
    f.write(html.encode('utf8'))

