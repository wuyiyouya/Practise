#!/usr/bin/python
# coding = utf-8

''' Download latest 3.3.1 OVS and ovmm build '''

import os
import sys
import subprocess
import urllib2
import re
import time

# Query LATEST directory
baseurl = 'http://ca-server1.us.oracle.com/ovm-autobuild/'
testVer = '3.3.1'
latesturl = 'http://ca-server1.us.oracle.com/ovm-autobuild/ovm-%s-trunk-daily/%s' % (testVer[:-2], 'LATEST/')

# Version
version = '3.3.1'

# downloadPath
downloadPath = '/vt/iso/OVM/' + 'OVM_' + version[:-2] + '/' + 'OVM_' + version + '/'

blockSize = 1022

# To match ovs and ovmm installation file
ovsPat = re.compile('OVS-%s\D+(\d{1,4})' % (version)).search
ovmPat = re.compile('ovmm-%s\D+(\d{1,4})' % (version)).search

# print 'ovsPat = %s, ovmPat = %s' % (ovsPat, ovmPat)

def main():
	# To get ovs and ovm build
	response = urllib2.urlopen(latesturl)
	html = response.read()
	response.close()

	ovsVer = ovsPat(html).groups()[0]
	ovmVer = ovmPat(html).groups()[0]

	ovsBuild = 'OVS-3.3.1-trunk-%s.iso' % (ovsVer)
	ovmBuild = 'ovmm-3.3.1-installer-OracleLinux-b%s.iso' % (ovmVer)
	 
	fileList = []
	fileList.append(ovsBuild)
	fileList.append(ovmBuild)

	# ans = raw_input('Do you want to download ' + ovsBuild + ' ? (Y/y)')
	# if ans.upper() == 'Y':
	# 	fileList.append(ovsBuild)

	# ans = raw_input('Do you want to download ' + ovmBuild + ' ? (Y/y)')
	# if ans.upper() == 'Y':
	# 	fileList.append(ovmBuild)

	if len(fileList) != 0:
		for f in fileList:
			download(latesturl+f, downloadPath+f)

def getUrlFileSize(url):
	response = urllib2.urlopen(url)
	meta = response.info()
	response.close()
	return int(meta.getheaders("Content-Length")[0])

def download(lf, df):
	if not fileExist(df):
		print 'Start to download %s' % (lf)
		fileSize = getUrlFileSize(lf)
		p = runCmd('lftp -c pget -n 10 %s -o %s' % (lf, df))
		while(True):
			
			if not p.poll():
				time.sleep(2)
				q = runCmd('ls -s %s' % (df))
				q.wait()
				# block count
				dwlSize = int(q.stdout.readline().split(' ')[0]) * blockSize
				progressBar(lf, dwlSize, fileSize)

			if p.poll() == 0:
				print '%s download completed' % (lf)
				break

def runCmd(cmd):
	return subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

def progressBar(f, dwlSize, fileSize):
	perc = int(float(dwlSize)/fileSize * 100)
	sys.stdout.write('%s %d/%d %2d%% downloaded\r' % (f.split('/')[-1], dwlSize, fileSize, perc))
	sys.stdout.flush()

def fileExist(f):
	p = runCmd('ls %s' % (f))
	p.wait()
	if p.poll() == 0:
		print '%s existed, no need to download' % (f)
		return True
	return False


if __name__ == '__main__':
	main()

