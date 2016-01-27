#!/usr/bin/env python

from printcolors import PrintColors as pc

def print_docstring():
  fstring = """
{bfail}{command}{endc}			{bwarning}User Commands{endc}			{bfail}{command}{endc}

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
	
{warning}AUTHOR{endc}\n\tWritten by Torbjorn Granlund and Richard M. Stallman.
		""".format(bfail 	 = pc.bFAIL,
				okblue 	 = pc.OKBLUE, 
				okgreen  = pc.OKGREEN,
				endc 	 = pc.ENDC,
				warning  = pc.WARNING,
				bwarning = pc.bWARNING,
				header 	 = pc.HEADER,
				command	 ='cat',
				one_liner="con{warning}cat{endc}enate files and print them on the standard output.".format(warning = pc.WARNING,endc = pc.ENDC ))
  
  print(fstring)


if __name__ == '__main__':
  print_docstring()

