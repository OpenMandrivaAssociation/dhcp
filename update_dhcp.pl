#!/usr/bin/perl -W

#----------------------------------------------------------------------
# copyright (C) 2001 Florin Grad
# 
# This is a really silly program that is supposed to allow an update of 
# a dhcp-2* server to a dhcp-3* server
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#       
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#       
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
#------------------------------------------------------------------------

#search for a ddns-update-style entry in /etc/dhcpd.conf file
my $conf_file = "/etc/dhcpd.conf"; #$ARGV[0];
my $conf_file_orig = "/etc/dhcpd.conf.orig";
my $i=0;
open (DHCPCONF, "< $conf_file") or die "Can't open the $conf_file file for reading";
while (<DHCPCONF>) {
	if (/ddns-update-style/) {
		$i++;
	};
};
close (DHCPCONF);

if ($i == 0) {  #we are on a dhcp-2 
	rename("$conf_file","$conf_file_orig") || die "Can't rename $conf_file: $!";
	open (DHCPCONF, "> $conf_file") or die "Can't open the $conf_file file for writing";	
	print DHCPCONF "ddns-update-style none;\n";
	open (DHCPCONF_ORIG, "< $conf_file_orig") or die "Can't open the $conf_file_orig file for reading";
		while (<DHCPCONF_ORIG>) {
			print DHCPCONF "$_";	
		};
	close (DHCPCONF_ORIG);
	close (DHCPCONF);
}
