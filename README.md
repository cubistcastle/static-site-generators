static-site-generators
======================

This is a mini-review of static site generators using those that were previously recommended to me on [my blog](http://blog.steve.org.uk).

I'm happy to receive updates, corrections, or suggestions of further tools to review.  Please just fork this repository and submit a pull request.




History
-------

I maintain a number of websites which are simple in nature, by which I mean entirely static.  Initially I wrote and maintained these "by hand", editing raw HTML in my favourite editor.

Over time I wrote a simple templating tool which would allow me to wrap pages of HTML in a layout.  My tool was called `webgen` and because I'd started with manual HTML it didn't include any shortcuts such as textile, markdown, or similar formatters.  Instead it would wrap simple files of HTML in a layout and output the final site.

I used my tool on several sites and over time I made several site-specific tweaks to allow me to have dynamic menus, different layouts on different sections of the sites, etc.

Finally I rationalized all the different versions, tidied it up, and released it as [Templer](https://github.com/skx/templer).  (It now supports plugins which allowed me to add support for both Textile & Markdown input.)




My Requirements
---------------

Like many people approaching the use of a static site generator I have a few requirements
which shouldn't be too unreasonable:

* The tool must allow me to separate the content and the layout.
   * Different pages/sections of the site must be able to use a different layout.
* There must be support for both global and per-page variables.
   * Conditionals, loops, and similar would be great but are not strictly required.
   * Conditional file inclusion is absolutely required though.
* Working "in-place" is a bonus, as it makes migration easier.
* Handling symlinks in the input tree is required.




Testing Methodology
-------------------

For each of the available tools I'm going to write a simple site, which will be
bundled into this repository.  The site will attempt to satisfy each of the
requirements.  That means:

* There should be at least two pages of content.
     * The two pages should use a different layout.
* The pages should use a page-specific variable.
* There should be a conditional file inclusion, if possible.
* Some of the input tree should use symbolic links.
     * Ideally two forms - a symlink to a file, and a symlink to a directory.

Within this repository you'll find one sub-directory for each tool I tested, along with an
accompanying Makefile.  Each project will have two targets:

* `make build`
   * Build the site using the appropriate tool.
* `make clean`
   * Clean the site.

Installing the actual tools is beyond the scope of this document.

If any project satisfies my requirements 100% it will receive full rating, otherwise
they will be rated on a scale of 1-5 based on the flexibility, documentation and
utility of the project.


Conclusion
----------

Many of the tools reviewed contained common concepts, which I used to inspire
myself when I was rationalizing the divergent copies of my own tool (initially
named 'webgen', later renamed to 'templer').

The notion of a page containing meta-data, and per-page variables is the most
obvious thing the different tools had in common, but even command line flags
were frequently the same.

The common stumbling block for most of these tools was the handling of symbolic links:

* Symlinks to directories.
    * These would frequently be ignored.
* Symlinks to files.
   * These would frequently be replaced with literal copies.

Unfortunately I've gotten into the routine and habit of using symlinks for
versioning purposes - so I might have `jquery.js` be a symlink to
`jquery-1.8.3.js`, for example.  In a real sense failures to handle symlinks
might not be a deal-breaker for others, but for me it meant that I couldn't
port my sites to a different tool and have 100% identical output.

Having consistently reproducable output and having a tool generate content I
could make already seemed to be the bear minimum I could expect before I
started making changes.

Despite the failure to be suitable for my specific needs I'd have no hesitation
in recommending the tools which scored 3+.  Many of the projects referenced here
are very well regarded, and I can see why - good documentation, good flexibility,
and the freedom to create interesting sites with ease.



Available Tools
---------------

* [hakyll](#hakyll)
* hyde
    * TODO: http://ringce.com/hyde
* [jekyll](#jekyll)
* [nanoc](#nanoc)
* [pelican](#pelican)
* [poole](#poole)
* [templer](#templer)
* tahchee
    * TODO: https://github.com/sebastien/tahchee
* [webby](#webby)
* [webgen](#webgen)
* wml
    * TODO: http://thewml.org/
* [wintersmith](#wintersmith)


hakyll
------

[hakyll](http://jaspervdj.be/hakyll/) is the most unusual generator upon our list, being written in Haskell.  That language is alien to me, but despite this it didn't seem like it would be too hard to get started with as the available tutorials covered things well.

Installation first required a haskell environment, then the installation of the tool itself:

      $ sudo apt-get install ghc6 cabal-install
      $ sudo cabal update
      $ sudo cabal install hakyll

Sadly the installation, via `cabal install ..` failed and haskell is too alien to me to debug further.  I suspect this will get better for the Wheezy release of Debian [as native packages ara available](http://packages.debian.org/search?keywords=hakyll).

Steve-Rating: 1/5.  I suspect this tool would score 4/5 if it were installable by myself.


jekyll
------

[jekyll](https://github.com/mojombo/jekyll) is the first of our Ruby-based projects.  This is packaged as a gem, and can be installed via:

      $ sudo gem install jeykll

Jejyll is unlike several of the other static-site generators I've examined in the sense that it had no helper to build a new site.  This made getting started a little more complex than I'd have wished, but that said it was flexible and a very well-documented project.

The initial aim of creating per-page layouts was easily achieved, but sadly I ruled it out because each of the symbolic links I created in the input-directory was ignored which resulted in instant-failure against my requirement list.

Jekyll seems well-regarded and with an excellent collection of [available plugins](https://github.com/mojombo/jekyll/wiki/plugins) I can see why.  It doesn't hurt that there are many online guides which cover it in-depth, for example [moving from wordpress to jekyll](http://paulstamatiou.com/how-to-wordpress-to-jekyll).

Steve-Rating: 4/5.



nanoc
-----

[nanoc](http://nanoc.stoneship.org/) is a simple static site generator written in Ruby.  Installation is as simple as:

      $ sudo gem install nanoc

nanoc allows dynamic code to be added to your pages, in ruby.   There is a _great_ extension infrastructure, and simple things such as tags are supported natively.

Using a flexible "routing" system you can specify different types of processing, and specify per-page layouts.

nanoc, as of release 3.6.3, has improved support for symbolic links.  Functionally this seems to work, but symbolic links are not preserved.  Given a file "foo-1.2.3.js" and "foo.js" being a symlink to it then two files are created - rather than one file and a symlink.

Steve-Rating: 4/5.


pelican
-------

[pelican](http://docs.getpelican.com/en/3.1.1/) is a python-based site-generator which is easily installed upon a Debian host:

        $ sudo apt-get install python-pip
        $ sudo pip install pelican

The software is very well documented, and I found it pleasant to work with, however it was a struggle to use it for generating a static site.  Instead it is more focussed upon being a blogging platform.  If you look at the sample project you'll see the difference immediately:

* Although I could create the static output /steve.html & /about.html the index.html was made up of the pair of them.
   * i.e. The front-page showed the most-recent articles and I couldn't disable that.
* Static assets weren't copied into the output tree.
   * For example my jquery file, and the /robots.txt file.

Steve-Rating: 4/5.  As a blogging platform it looks excellent.  Many plugins, an attractive theme, and good handling for feeds and similar.

For a static site?  Less useful.



poole
------

[poole](https://bitbucket.org/obensonne/poole) is a static site generator which is written in Python, and uses markdown for text processing.  Installation of the tool is as simple as cloning a repository, and adding it to your PATH.

poole  allows dynamic content to be written in the input files (in Python).  The output of the python will appear inline, and there is also the ability to generate simple stub functions in the `macros.py` file.  This functionality is sufficient to allow file-inclusion, and similar dynamic handling.

Unfortunately poole fails to meet the requirements for two reasons:

* There is a single, global, layout.  You cannot choose a different layout on a per-page basis.
* The tool is broken with regard to symlinks, as the sample project demonstrates.


Steve-Rating: 3/5 - It lost a point for being married to the idea that a site would have
a single layout-template.



Templer
-------

[Templer](https://github.com/skx/templer) is my home-made solution, and satisfies my requirements.  It is included for completeness only.



webgen
------

[webgen](http://webgen.rubyforge.org/) is another Ruby-based project, which is easily installed via:

      $ sudo gem install webgen

webgen is pretty flexible and easily allowed me to vary the template used on a per-page basis.  It also allowed me to add dynamic content with ease.   I liked the notion it had of "blocks" which could be inserted on a per-page basis.

Unfortunately webgen also failed to correctly handle symlinks:

* Symlinks to files were replaced with copies.
* Symlinks to directories were just ignored.

Steve-Rating: 4/5




webby
-----

[webby](http://webby.rubyforge.org/) is a simple static site generator written in Ruby.  Installation is as simple as:

      $ sudo gem install webby

I generated a sample site and built it via:

      $ webby-gen website webby
      $ cd webby && webby

At this point I received a cryptic error and aborted the test.  The repository contains the generated site, but no changes have been made.

Steve-Rating: 1/5 - It works for others, but when I installed it and couldn't even understand the error message it generated I couldn't take it seriously.



wintersmith
-----------

[wintersmith](http://wintersmith.io/) is a static site generator written in Javascript, and built upon [node.js](http://nodejs.org).  **NOTE**: You can serve the output statically, node.js is used for building not for serving/hosting.

Installation is simple if you have node already present:

        $ sudo npm install wintersmith -g

I generated the new site via:

        $ wintersmith  new ~/git/static-site-generators/wintersmith
        initializing new wintersmith site in /home/skx/git/static-site-generators/wintersmith using template blog
        warn npm: package.json my-blog@0.0.1 No repository field.
        typogr@0.5.2 node_modules/typogr
        underscore@1.4.4 node_modules/underscore
        moment@2.0.0 node_modules/moment
        done!

Once created the site was built from the `./contents/` directory into the `./build` output directory.

Once again wintersmith failed the symbolic link.  Symlinked resources were copied literally.  Otherwise it did very well, the github repository contains good examples, and the project is very flexible with regards to views, plugins etc.  Creating per-page layouts is trivial.

Steve-Rating: 4/5
