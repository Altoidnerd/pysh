#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from printcolors import PrintColors as pc

def print_docstring():
  fstring = """
{bfail}{command}(1){endc}			{bwarning}User Commands{endc}			{bfail}{command}(1){endc}

{warning}NAME{endc}

	{bfail}{command}{endc} - {one_liner}

{warning}SYNPOSIS{endc}
	{bfail}{command}{endc} [{okblue}OPTION{endc}]... [{okgreen}FILE{endc}]...

{warning}DESCRIPTIPION{endc}
	Con{bfail}cat{endc}enate {okblue}FILE(s){endc}, or standard input, to standard output.

	{okblue}-A{endc}, {okblue}--show-all{endc}
		equivalent to {okblue}-vET{endc}
	
	{okblue}-b{endc}, {okblue}--number-nonblank{endc}
		number nonempty output lines, overrides {okblue}-n

	{okblue}-e{endc}	equivalent to {okblue}-vE{endc}

	{okblue}-E{endc}, {okblue}--show-ends{endc}
		display $ at the end of each line

	{okblue}-n{endc}, {okblue}--number{endc}
		number all output lines

	{okblue}-s{endc}, {okblue}--squeeze-blank{endc}
		supress repeated empty output lines

	{okblue}-t{endc}	equivalent to {okblue}-vT{endc}

	{okblue}-T{endc}, {okblue}--show-tabs{endc}
		display {header}TAB{endc} characters as {header}^I{endc}
	
	{okblue}-u{endc}	(ignored)

	{okblue}-v{endc}, {okblue}--show-nonprinting{endc}
		use {header}^{endc} and {header}M-{endc} notation, except for LFD and TAB

	{okblue}--help{endc}  display this help and exit

	{okblue}--version{endc}
		output version informatiomn and exit

	With no {okgreen}FILE{endc}, or when {okgreen}FILE{endc} is {okgreen}-{endc}, read standard input.

{warning}EXAMPLES{endc}
	{bfail}{command}{endc}{endc} f - g
		Output f's contents, then standard inpit, then g's contents

	{bfail}{command}{endc} 	Copy standard input to standard output
	
{warning}AUTHOR{endc}
	Written by Torbjorn Granlund and Richard M. Stallman.

{warning}REPORTING BUGS{endc}
       Report cat bugs to bug-coreutils@gnu.org
       GNU coreutils home page: <http://www.gnu.org/software/coreutils/>
       General help using GNU software: <http://www.gnu.org/gethelp/>
       Report cat translation bugs to <http://translationproject.org/team/>

{warning}COPYRIGHT{endc}
       Copyright © 2013 Free Software Foundation, Inc.  License GPLv3+: GNU
       GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and  redistribute  it.
       There is NO WARRANTY, to the extent permitted by law.

{warning}SEE ALSO{endc}
       {fail}tac(1){endc}
	""".format(bfail = pc.bFAIL,
		okblue 	 = pc.OKBLUE, 
		okgreen  = pc.OKGREEN,
		endc 	 = pc.ENDC,
		warning  = pc.WARNING,
		bwarning = pc.bWARNING,
		header 	 = pc.HEADER,
		fail	 = pc.FAIL,
		command	 ='cat',
		one_liner='con{fail}cat{endc}enate files and print them on the standard output.'.format(fail=pc.FAIL, endc=pc.ENDC))
  print(fstring)

if __name__=='__main__':
  print_docstring()
  

