#!/usr/bin/env python

# Author: Suman Srinivasan 
# Last release: Sep 25, 2012
# License: GPL v3

# Modified from https://github.com/cwholt/sd-plugin-resque/blob/master/Resque.py

import socket 

class ThriftUp:
	def __init__(self, agent_config, checks_logger, raw_config):
		self.agent_config = agent_config
		self.checks_logger = checks_logger
		self.raw_config = raw_config

	def run(self):
		stats = {}
		stats['thrift_up'] = 0
		s = socket.socket()
		address = '127.0.0.1'
		port = 9090 
		try:
			s.connect((address, port)) 
			stats['thrift_up'] = 1
		except Exception, e:
			stats['thrift_up'] = 0 
		return stats

if __name__ == '__main__':
	thrift = ThriftUp(None, None, None)
	print thrift.run()
