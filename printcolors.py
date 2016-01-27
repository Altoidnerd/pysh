#!/usr/bin/env python

class PrintColors:
  DIR		= '\033[96m'    
  HEADER	= '\033[95m'
  OKBLUE 	= '\033[94m'
  WARNING 	= '\033[93m'
  OKGREEN 	= '\033[92m'
  FAIL 		= '\033[91m'
  bDIR		= '\033[1;96m'    
  bHEADER	= '\033[1;95m'    
  bOKBLUE 	= '\033[1;94m'
  bWARNING	= '\033[1;93m'
  bOKGREEN	= '\033[1;92m'
  bFAIL		= '\033[1;91m'
  ENDC 		= '\033[0m'
  
  def test_pcolors(self):
    print("\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10\n{11}".format(
		self.DIR+"DIR"+self.ENDC,
		self.HEADER+"HEADER"+self.ENDC,
                self.OKBLUE+"OK"+self.ENDC, 
                self.WARNING+"WARNING"+self.ENDC,
                self.OKGREEN+"OK"+self.ENDC,
  		self.FAIL+"FAIL"+self.ENDC, 
		self.bDIR+"DIR"+self.ENDC,
                self.bHEADER+"HEADER"+self.ENDC,
                self.bOKBLUE+"OK"+self.ENDC, 
                self.bWARNING+"WARNING"+self.ENDC,
                self.bOKGREEN+"OK"+self.ENDC,
  		self.bFAIL+"FAIL"+self.ENDC ))
 
  def disable(self):
    self.HEADER = ''
    self.OKBLUE = ''
    self.OKGREEN = ''
    self.WARNING = ''
    self.FAIL = ''
    self.ENDC = ''

def main():
  pc = PrintColors()
  print("\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}\n{11}".format(
		pc.DIR+"DIR"+pc.ENDC,
		pc.HEADER+"HEADER"+pc.ENDC,
                pc.OKBLUE+"OK"+pc.ENDC, 
                pc.WARNING+"WARNING"+pc.ENDC,
                pc.OKGREEN+"OK"+pc.ENDC,
  		pc.FAIL+"FAIL"+pc.ENDC, 
		pc.bDIR+"DIR"+pc.ENDC,
                pc.bHEADER+"HEADER"+pc.ENDC,
                pc.bOKBLUE+"OK"+pc.ENDC, 
                pc.bWARNING+"WARNING"+pc.ENDC,
                pc.bOKGREEN+"OK"+pc.ENDC,
  		pc.bFAIL+"FAIL"+pc.ENDC ))

if __name__ == '__main__':
  main()
