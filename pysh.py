#!/usr/bin/env python

import time, cmd, sys, os, urllib2, requests, subprocess, zipfile, tarfile, gzip
from parser import BetterParser
from printcolors import PrintColors as pc


class Shell(cmd.Cmd):

  def __init__(self):
    cmd.Cmd.__init__(self)
    self._sh = BetterParser()
    self._sh.environ['HOME'] = os.environ['HOME']
    self.did_quit = False
    self.did_clear_buffer = False
  
  def reload_shell(self):
    shell = Shell()
    shell.prompt = shell.prompt = pc.WARNING + str(os.getcwd().replace(os.environ['HOME'], '~')) + pc.ENDC + pc.bFAIL + ' >  ' + pc.ENDC
    shell.cmdloop() 

  def sh(self, arg_string):
    try:
      return self._sh.parse('. ' + arg_string)[1:]
    except SyntaxError, error:
      print pc.FAIL + "\tSyntaxError: " + pc.ENDC, error

  def do_quit(self, args):
    print(pc.HEADER+"\tBye" + pc.ENDC + "\nSession ended:\t" + subprocess.check_output('date'))
    self.did_quit = True
    sys.exit()

  def do_exit(self, args):
    print(pc.WARNING+"\tBye" + pc.ENDC + "\nSession ended:\t" + subprocess.check_output('date'))
    self.did_quit = True
    self.did_quit = True
    sys.exit()

  def do_clear(self, args):
    os.system('clear')

  def do_pwd(self, args):
    print subprocess.check_output('pwd')

  def do_cd(self, args):
    argv = self.sh(args)
    if len(argv) > 1:
      print("\t{}ERROR:{}\t{}cd{} expects one arguement, but you didn't do that.{}\n\tUSAGE:{}\t{}cd{} /path/to/destination/".format(
	pc.bFAIL  ,pc.ENDC, 
        pc.OKGREEN,pc.ENDC,
	pc.HEADER ,pc.ENDC,
	pc.OKBLUE ,pc.ENDC
			)
	)
      self.reload_shell()
    destination = os.environ['HOME'] if not(len(argv)) else argv[-1].replace('~', os.environ['HOME'])
    os.chdir(destination)
    self.reload_shell() 
  
  def do_mkdir(self, args):
    argv = self.sh(args)
    map(os.makedirs, map(os.path.abspath, argv))
 
  def do_ls(self, args):
    argv = self.sh(args)
    target = '.' if len(argv) == 0 else argv[-1]
    # check for -a
    if '-a' in argv:
      for file_ in [elem for elem in os.listdir(target)]: print('\t'+file_)
    # filter hidden files
    for file_ in [elem for elem in os.listdir(target) if not(elem.startswith('.'))]: print('\t'+file_)

  #def do_argtest(self, args):
   # print self.sh(args)

  def do_curl(self, args):
    print(pc.OKGREEN+'\tcurl '+pc.ENDC+
	  'will be ready soon.  For now, try '+
	  pc.OKGREEN+'wget'+pc.ENDC+'.'
	)

  def do_wget(self, args):
    argv = self.sh(args)
    for url in argv:
      file_name = url.split('/')[-1]
      response = urllib2.urlopen(url)
      file_ = open(file_name, 'wb')
      meta = response.info()
      file_size = int(meta.getheaders("Content-Length")[0]) 
      print(	"Downloading: {}".format(file_name)+'\n',
		"Bytes: {}".format(file_size)+'\n' )
      file_size_dl = 0
      block_size = 8192
      while True:
        buffer = response.read(block_size)
        if not buffer:
          break
      file_size_dl += len(buffer)
      file_.write(buffer)
      status = r"%10d [%3.2f%%]" % (file_size_dl, file_size * 100. / file_size)
      status = status + chr(8)*(1 + len(status))
      print status,
    file_.close()
   
  def do_grep(self, args):
    argv = self.sh(args)
    for arg in argv:
      target = argv[-1]
    print("grep is coming soon")


  def do_cat(self, args):
    def cat_kernel(argv_):
      for line in open(str(argv_[-1]), 'r').readlines():
        sys.stdout.write(line+'\n')
        try:
          _ = argv_[-2]
        except IndexError:
          break
        if _:
          cat_kernel(argv_[:-1])
    cat_kernel(self.sh(args))

  def do_EOF(self, args):
    return True


  def do_print(self, args):
    argv = self.sh(args)
    string = ''
    for arg in argv:
      string += (arg+' ')
    string += '\n'
    print string,


  def help_print(self):
    from pysh_docstring import print_docstring
    print_doctsring() 
   
  def postcmd(self, stop, args):
    pass # can use this to quit with did_quit 


def main():
  print("\n{}Loading pysh:{}\t{}OK{}\n\t\tType {}help{} for a list of avaiable commands.".format(
	pc.HEADER,pc.ENDC, 
	pc.OKGREEN,pc.ENDC, 
	pc.OKGREEN,pc.ENDC
		)
	)
  shell = Shell()
  shell.prompt = pc.WARNING + str(os.getcwd().replace(os.environ['HOME'], '~')) + pc.ENDC + pc.bFAIL + ' >  ' + pc.ENDC
  shell.cmdloop()
  
if __name__=='__main__':
  main()
