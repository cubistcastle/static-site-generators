static-site-generators
======================

This is a mini-review of static site generators using those that were previously recommended to me on [my blog](http://blog.steve.org.uk).

I'm happy to receive updates, corrections, or suggestions of further tools to review.  Please just fork this repository and submit a pull request.




History
-------

I maintain a number of websites which are simple in nature, by which I mean entirely static.  Initially I wrote and maintained these "by hand", editing raw HTML in my favourite editor.

Over time I wrote a simple templating tool which would allow me to wrap pages of HTML in a layout.  My tool was called `webgen` and because I'd started with manual HTML it didn't include any shortcuts such as textile, markdown, or similar formatters.  Instead it would wrap simple files of HTML in a layout and output the final site.

I used my tool on several sites and over time I made several site-specific tweaks to allow me to have dynamic menus, different layouts on different sections of the sites, etc.

Finally I rationalized all the different versions, tidied it up, and released it as [Templer](https://github.com/skx/templer).




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



Available Tools
---------------

* jekyll
* hyde
* [nanoc](#nanoc)
* pelican
* [poole](#poole)
* [templer](#templer)
* tahchee
* [webby](#webby)
* [webgen](#webgen)
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



webgen
------

[webgen](http://webgen.rubyforge.org/) is another Ruby-based project, which is easily installed via:

      $ sudo gem install webgen

webgen is pretty flexible and easily allowed me to vary the template used on a per-page basis.  It also allowed me to add dynamic content with ease.   I liked the notion it had of "blocks" which could be inserted on a per-page basis.

Unfortunately webgen also failed to correctly handle symlinks:

* Symlinks to files were replaced with copies.
* Symlinks to directories were just ignored.



webby
-----

[webby](http://webby.rubyforge.org/) is a simple static site generator written in Ruby.  Installation is as simple as:

      $ sudo gem install webby

I generated a sample site and built it via:

      $ webby-gen website webby
      $ cd webby && webby

At this point I received a cryptic error and aborted the test.  The repository contains the generated site, but no changes have been made.



Links
-----

These are here mostly to give a starting point for future generators to examine
once my initial list is completed.


* [Poll: What's your favorite static site generator?](http://news.ycombinator.com/item?id=4857473)
* [32 Static Website Genertors](http://iwantmyname.com/blog/2011/02/list-static-website-generators.html)
