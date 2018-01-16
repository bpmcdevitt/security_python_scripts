#!/usr/bin/env python3
# python object for nmap scans

import nmap

# good link of cheat sheet for nmap cmds - https://highon.coffee/blog/nmap-cheat-sheet/


class NmapUtility(nmap.PortScanner):
    """ Subclass nmap.PortScanner, with some added functionality """

    def __init__(self, hostname=False):
        if hostname:
            self.hostname = hostname

    def scan_hosts(self, hosts):
        """ Scan a list of hosts """
        pass

    def ping_sweep(self, hosts):
        """ Ping sweep a list of hosts """
        self.scan(hosts=hosts, arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, self[x]['status']['state'])
                      for x in self.all_hosts()]
        for host, status in hosts_list:
            print('{0}:{1}'.format(host, status))

    def nmap_version(self):
        """ Get nmap version being used """

        return self.nmapVersion()

    def command_line(self):
        """ Run nmap.command_line """

        return self.command_line

    def cipher_check(self, hostname, portrange):
        """ Run --script ssl-enum-ciphers on hostname """

        return self.scan(hostname,
                         portrange,
                         arguments='--script ssl-enum-ciphers')

    def get_csv(self):
        """ Run scan.csv() """

        return self.csv()

    def all_tcp(self, hostname=False):
        """ Get all ports for tcp protocol in sorted output """
        if hostname:
            return self[hostname].all_tcp()

        return self[self.hostname].all_tcp()

    def all_udp(self, hostname=False):
        """ Get all ports for udp protocol in sorted output
        requires scanHost() or scan() to be run first
        """
        if hostname:
            return self[hostname].all_udp()

        return self[self.hostname].all_udp()

    def banner_grab(self, portrange, hostname=False):
        """ Grab banners from ports """

        if hostname:
            return self.scan(hostname, portrange,
                             arguments='-sV --script=banner')

        return self.scan(self.hostname, portrange,
                         arguments='-sV --script=banner')

    def check_sql_inj(self, portrange, hostname=False):
        """ Check for sql injection """
        
        if hostname:
            return self.scan(hostname,
                             portrange,
                             arguments='--script=http-sql-injection')

        return self.scan(self.hostname,
                         portrange,
                         arguments='--script=http-sql-injection')


    def dns_brute_force(self, portrange, hostname=False):

        if hostname:
            return self.scan(hostname, portrange,
                             arguments='--script dns-brute.nse')

        return self.scan(self.hostname, portrange,
                         arguments='--script dns-brute.nse')

