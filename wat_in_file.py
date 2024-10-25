#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Informal test of options in files. Run it all or comment
    out some sections

options
    .all to include all available information
    .caller to show how and where the inspection was called (works in files, not REPL)
    .code to reveal the source code of a function, method, or class
    .dunder to display dunder attributes (starting with __)
    .gray to disable colorful output in the console
    .long to show non-abbreviated values and docstrings
    .nodocs to hide documentation for functions and classes
    .ret to return the inspected object
    .short or .s to hide the attributes (variables and methods inside the object)
    .str to return the output string instead of printing it

https://github.com/russ-hensel?tab=repositories

"""

import sys
import wat

def short_function( x, y ):
    """
    short function for inspection
    """
    return x * y


issues    = []


try:
    what   = ">>>>>>>>>>>>>>>> all next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, all = True )
except:
    print( "that didn't work")
    issues.append( what )


try:
    what   = ">>>>>>>>>>>>>>>> caller next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, caller = True )
except:
    print( "that didn't work")
    issues.append( what )


try:
    what   = ">>>>>>>>>>>>>>>> code next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, code = True )
except:
    print( "that didn't work")
    issues.append( what )


try:
    what   = ">>>>>>>>>>>>>>>> dunder next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, dunder = True )
except:
    print( "that didn't work")
    issues.append( what )


try:
    what   = ">>>>>>>>>>>>>>>> gray next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, gray = True )
except:
    print( "that didn't work <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    issues.append( what )


try:
    what   = ">>>>>>>>>>>>>>>> long next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, long = True )
except:
    print( "that didn't work")
    issues.append( what )


try:
    what   = ">>>>>>>>>>>>>>>> nodocs next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, nodocs = True )
except:
    print( "that didn't work")
    issues.append( what )


try:
    what   = ">>>>>>>>>>>>>>>> ret next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, ret = True )
except:
    print( "that didn't work")
    issues.append( what )


try:
    what   = ">>>>>>>>>>>>>>>> short next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, short = True )
except:
    print( "that didn't work")
    issues.append( what )


try:
    what   = ">>>>>>>>>>>>>>>> str next >>>>>>>>>>>>>>>>>>>"
    print( f"{'\n\n' }{what}" )
    wat( short_function, all= True, str = True )
except:
    print( "that didn't work")
    issues.append( what )


# ---- and we are done except
print( "\nHad an exception with:" )
for i_issue in issues:
    print( i_issue )