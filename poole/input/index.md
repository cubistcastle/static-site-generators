
title: home
menu-position: 0
---

## Welcome to Poole

In Poole you write your pages in [markdown][md]. It's easier to write
markdown than HTML.

Here is some inline Python:

{%
print "Hello, World"
%}

In a build, Poole copies every file from the *input* directory to the *output*
directory. During that process every markdown file (ending with *md*, *mkd*,
*mdown* or *markdown*) is converted to HTML using the project's `page.html`
as a skeleton.

[md]: http://daringfireball.net/projects/markdown/


# Dynamic handling

This site was last rebuilt on {{ today() }}
