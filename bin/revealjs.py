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
          .reveal section img { display: block; margin: 15px auto; }
          .reveal section embed { display: block; margin: 15px auto; background: rgba(255, 255, 255, 0.12); border: 4px solid #eee; box-shadow: 0 0 10px rgba(0, 0, 0, 0.15); }
          .reveal pre { font-size: 0.5em; width: auto; }
          .reveal pre code { color: white; white-space: pre-wrap; line-height: 1.3em; }

          .reveal pre, .reveal pre code { color: #cccccc; background-color: #303030; }
          .reveal pre code > span.kw { color: #f0dfaf; } /* Keyword */
          .reveal pre code > span.dt { color: #dfdfbf; } /* DataType */
          .reveal pre code > span.dv { color: #dcdccc; } /* DecVal */
          .reveal pre code > span.bn { color: #dca3a3; } /* BaseN */
          .reveal pre code > span.fl { color: #c0bed1; } /* Float */
          .reveal pre code > span.ch { color: #dca3a3; } /* Char */
          .reveal pre code > span.st { color: #cc9393; } /* String */
          .reveal pre code > span.co { color: #7f9f7f; } /* Comment */
          .reveal pre code > span.ot { color: #efef8f; } /* Other */
          .reveal pre code > span.al { color: #ffcfaf; } /* Alert */
          .reveal pre code > span.fu { color: #efef8f; } /* Function */
          .reveal pre code > span.er { color: #c3bf9f; } /* Error */
          .reveal pre code > span.wa { color: #7f9f7f; font-weight: bold; } /* Warning */
          .reveal pre code > span.cn { color: #dca3a3; font-weight: bold; } /* Constant */
          .reveal pre code > span.sc { color: #dca3a3; } /* SpecialChar */
          .reveal pre code > span.vs { color: #cc9393; } /* VerbatimString */
          .reveal pre code > span.ss { color: #cc9393; } /* SpecialString */
          .reveal pre code > span.im { } /* Import */
          .reveal pre code > span.va { } /* Variable */
          .reveal pre code > span.cf { color: #f0dfaf; } /* ControlFlow */
          .reveal pre code > span.op { color: #f0efd0; } /* Operator */
          .reveal pre code > span.bu { } /* BuiltIn */
          .reveal pre code > span.ex { } /* Extension */
          .reveal pre code > span.pp { color: #ffcfaf; font-weight: bold; } /* Preprocessor */
          .reveal pre code > span.at { } /* Attribute */
          .reveal pre code > span.do { color: #7f9f7f; } /* Documentation */
          .reveal pre code > span.an { color: #7f9f7f; font-weight: bold; } /* Annotation */
          .reveal pre code > span.cv { color: #7f9f7f; font-weight: bold; } /* CommentVar */
          .reveal pre code > span.in { color: #7f9f7f; font-weight: bold; } /* Information */

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
					//{ src: 'http://s.zys.me/js/revealjs/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
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

