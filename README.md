static-site-generators
======================

A mini-review of static site generators.

History
-------

I maintain a number of websites which are simple in nature, by which I mean entirely static.  Initially I wrote and maintained these "by hand", editing raw HTML in my favourite editor.

Over time I wrote a simple templating tool which would allow me to wrap pages of HTML in a layout.  My tool was called `webgen` and because I'd started with manual HTML it didn't include any shortcuts such as textile, markdown, or similar formatters.  Instead it would wrap simple files of HTML in a layout and output the final site.

I used my tool on several sites and over time I made several site-specific tweaks to allow me to have dynamic menus, different layouts on different sections of the sites, etc.

Finally I rationalized all the different versions, tidied it up, and released it as [Templer](https://github.com/skx/templer).


My Requirements
---------------

Like many people approaching the use of a static site generator I had only a few simple requirements:

* The tool must allow me to separate the content and the layout.
* Different pages/sections of the site must be able to use a different layout.
* There must be support for both global and per-page variables.
* Conditionals, loops, and similar would be great but are not strictly required.
* Conditional file inclusion is absolutely required though.
* Handling symlinks in the input tree is required.
* Working "in-place" is a bonus, as it makes migration easier.


Testing Methodology
-------------------

For each of the available tools I'm going to write a simple site.  This site will
include at least two layouts, a conditional file inclusion, and a number of symlinks.

Any tool which is successfully used will be given a pass.  Any tool which fails on one or more of the requirements will be given a failure mark.


Available Tools
---------------

* jekyll
* hyde
* mako
* nanoc
* pelican
* poole
* tahchee
* webby
* webgen
* wml



poole
------

[poole](https://bitbucket.org/obensonne/poole) is a static site generator which is written in Python, and uses markdown.


Links
-----

* [Poll: What's your favorite static site generator?generator](http://news.ycombinator.com/item?id=4857473)
* [32 Static Website Genertors](http://iwantmyname.com/blog/2011/02/list-static-website-generators.html)