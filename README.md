static-site-generators
======================

This is a mini-review of static site generators.

If you have updates/corrections then please feel free to submit pull requests.


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

For each of the available tools I'm going to write a simple site, which will be
bundled into this repository.  The site will attempt to satisfy each of the
requirements - and if it the tool is judged to fail further work will be stopped.

Within this repository you'll find one sub-directory per tool, along with an
accompanying Makefile.  Each project will have two targets:

* `make`
   * Build the site.
* `make clean`
   * Clean the site.

Installing the actual tools is beyond the scope of this document.


Available Tools
---------------

* jekyll
* hyde
* mako
* [nanoc](#nanoc]
* pelican
* [poole](#poole)
* [templer](#templer)
* tahchee
* webby
* webgen
* wml



nanoc
-----

[nanoc](http://nanoc.stoneship.org/) is a simple static site generator written in Ruby.  Installation is as simple as:

      $ sudo gem install nanoc

nanoc allows dynamic code to be added to your pages, in ruby.   There is a _great_ extension infrastructure, and simple things such as tags are supported natively.

Using a flexible "routing" system you can specify different types of processing, and specify per-page layouts.

Unfortunately nanoc fails my requirements because it is broken with regard to symbolic link handling - as the sample site demonstrates.


poole
------

[poole](https://bitbucket.org/obensonne/poole) is a static site generator which is written in Python, and uses markdown for text processing.  Installation of the tool is as simple as cloning a repository, and adding it to your PATH.

poole  allows dynamic content to be written in the input files (in Python).  The output of the python will appear inline, and there is also the ability to generate simple stub functions in the `macros.py` file.  This functionality is sufficient to allow file-inclusion, and similar dynamic handling.

Unfortunately poole fails to meet the requirements for two reasons:

* There is a single, global, layout.  You cannot choose a different layout on a per-page basis.
* The tool is broken with regard to symlinks, as the sample project demonstrates.


Templer
-------

[Templer](https://github.com/skx/templer) is my home-made solution, and satisfies my requirements.  It is included for completeness only.


Links
-----

* [Poll: What's your favorite static site generator?generator](http://news.ycombinator.com/item?id=4857473)
* [32 Static Website Genertors](http://iwantmyname.com/blog/2011/02/list-static-website-generators.html)