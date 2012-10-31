==================================
Django support for Sublime Text 2
==================================
Overview
--------

Extended by me to add in `Tidy Django Tags` command on the command palette. Fixes the spacing in the tags to be consistent, if you have other team members that don't add spacing around the tags.

Also deleted the Python snippets which I found useless.

Installation
------------

1. Clone this repo
2. Put the contents of this repo directly inside:

 - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
 - Windows: %APPDATA%/Sublime Text 2/Packages/
 - Linux: ~/.config/sublime-text-2/Packages

Or use PackageControl.

Snippets for Django templates
------------------------------
=============== ======================================================
 Abbreviation                        Tag
=============== ======================================================
 autoescape      ``{% autoescape %} {% autoescape %}``
 block           ``{% block %} {% endblock %}``
 comment         ``{% comment %} {% endcomment %}``
 csrf            ``{% csrf_token %}``
 cycle           ``{% cycle %}``
 debug           ``{% debug %}``
 ext             ``{% extends "" %}``
 extends         ``{% extends "" %}``
 filter          ``{% filter %} {% endfilter %}``
 firstof         ``{% firstof %}``
 for             ``{% for in %} {% endfor %}``
 fore            ``{% for in %} {% empty %} {% endfor %}``
 if              ``{% if %} {% endif %}``
 ifchanged       ``{% ifchanged %} {% endifchanged %}``
 ife             ``{% if %} {% else %} {% endif %}``
 ifelse          ``{% if %} {% else %} {% endif %}``
 ifeq            ``{% ifequal %} {% endifequal %}``
 ifequal         ``{% ifequal %} {% endifequal %}``
 ifnotequal      ``{% ifnotequal %} {% endifnotequal %}``
 inc             ``{% include %}``
 include         ``{% include %}``
 load            ``{% load %}``
 now             ``{% now "" %}``
 regroup         ``{% regroup by as %}``
 spaceless       ``{% spaceless %} {% endspaceless %}``
 ssi             ``{% ssi %}``
 templatetag     ``{% templatetag %}``
 url             ``{% url %}``
 widthratio      ``{% widthratio %}``
 with            ``{% with as %} {% endwith %}``
 trans           ``{% trans %}``
 blocktrans		 ``{% blocktrans with as %} {% endblocktrans %}``
=============== ======================================================

...and some non-official stuff:

=============== ======================================================
 Abbreviation                        Tag
=============== ======================================================
 super           ``{{ block.super }}``
 extrahead       ``{% block extrahead %} {% endblock extrahead %}``
 extrastyle      ``{% block extrastyle %} {% endblock extrastyle %}``
 v		         ``{{ }}``
 tag		     ``{% %}``
 static          ``{{ STATIC_URL }}``
 media           ``{{ MEDIA_URL }}``
===============
