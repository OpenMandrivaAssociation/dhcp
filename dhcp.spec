%define plevelversion 1

%if %plevelversion < 1
%undefine plevel
%else
%define plevel P%{plevelversion}
%endif

%define _catdir /var/cache/man

Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) server/relay agent/client
Name:		dhcp
Epoch:		3
Version:	4.2.3
Release:	1.P%{plevelversion}.1
License:	Distributable
Group:		System/Servers
URL:		http://www.isc.org/software/dhcp
Source0:	ftp://ftp.isc.org/isc/%{name}/%{name}-%{version}/%{name}-%{version}%{?plevel:-%{plevel}}.tar.gz
Source1:	ftp://ftp.isc.org/isc/%{name}/%{name}-%{version}/%{name}-%{version}%{?plevel:-%{plevel}}.tar.gz.sha512.asc
Source2:	dhcpd.conf
Source4:	dhcp-dynamic-dns-examples.tar.bz2
Source7:	dhcpreport.pl
Source8:	dhcpd-chroot.sh
# (eugeni) dhclient-exit-hooks script
Source9:	dhclient-exit-hooks
Source10:	draft-ietf-dhc-ldap-schema-01.txt
Source11:	dhcpd.init
Source12:	dhcpd.service
Source13:	dhcpd6.init
Source14:	dhcpd6.service
Source15:	dhcrelay.init
Source16:	dhcrelay.service
# mageia patches
Patch100:	dhcp-4.2.2-ifup.patch
Patch101:	dhcp-4.2.2-fix-format-errors.patch
# prevents needless deassociation, working around mdv bug #43441
Patch102:	dhcp-4.1.1-prevent_wireless_deassociation.patch
# fedora patches
Patch8:		dhcp-4.2.2-xen-checksum.patch
Patch15:	dhcp-4.2.2-missing-ipv6-not-fatal.patch
Patch17:	dhcp-4.2.0-add_timeout_when_NULL.patch
Patch18:	dhcp-4.2.1-64_bit_lease_parse.patch
BuildRequires:	groff-for-man
BuildRequires:	openldap-devel

%description 
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows 
individual devices on an IP network to get their own network configuration
information (IP address, subnetmask, broadcast address, etc.) from a DHCP
server. The overall purpose of DHCP is to make it easier to administer a 
large network. The dhcp package includes the DHCP server and a DHCP relay
agent. You will also need to install the dhcp-client or dhcpcd package,
or pump or dhcpxd, which provides the DHCP client daemon, on client machines.

If you want the DHCP server and/or relay, you will also need to install the
dhcp-server and/or dhcp-relay packages.

%package common
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) server
Group:		System/Servers

%description common
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows 
individual devices on an IP network to get their own network 
configuration information (IP address, subnetmask, broadcast address, 
etc.) from a DHCP server.  The overall purpose of DHCP is to make it 
easier to administer a large network.  The dhcp package includes the 
DHCP server and a DHCP relay agent.

You will also need to install the dhcp-client or dhcpcd package, or pump or
dhcpxd, which provides the DHCP client daemon, on  client machines. If you
want the DHCP server and/or relay, you will also need to install the
dhcp-server and/or dhcp-relay packages.

%package doc
Summary:	Documentation about the ISC DHCP server/client
Group:		System/Servers

%description doc
This package contains RFC/API/protocol documentation about the ISC
DHCP server and client.

DHCP (Dynamic Host Configuration Protocol) is a protocol which allows 
individual devices on an IP network to get their own network 
configuration information (IP address, subnetmask, broadcast address, 
etc.) from a DHCP server.  The overall purpose of DHCP is to make it 
easier to administer a large network.  The dhcp package includes the 
DHCP server and a DHCP relay agent.

%package server
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) server
Group:		System/Servers
Requires:	dhcp-common >= %{epoch}:%{version}-%{release}
Requires(post):	rpm-helper
Requires(preun): rpm-helper

%description server
DHCP server is the Internet Software Consortium (ISC) DHCP server for various
UNIX operating systems. It allows a UNIX mac hine to serve DHCP requests from
the network.

You should install dhcp-server if you want to set up a DHCP server on your
network. You will also need to install the base dhcp package.

%package client
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) client
Group:		System/Servers
Requires:	dhcp-common >= %{epoch}:%{version}-%{release}

%description client
DHCP client is the Internet Software Consortium (ISC) DHCP client for various
UNIX operating systems.  It allows a UNIX mac hine to obtain it's networking
parameters from a DHCP server.

You should install dhcp-client if you want to use the ISC DHCP client instead
of the Red Hat DHCP client, pump, or dhcpcd, or dhcpxd. You will also need to
install the base dhcp package.

%package relay
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) relay
Group:		System/Servers
Requires:	dhcp-common >= %{epoch}:%{version}-%{release}
Requires(post):	rpm-helper
Requires(preun): rpm-helper

%description relay
DHCP relay is the Internet Software Consortium (ISC) relay agent for DHCP
packets. It is used on a subnet with DHCP clients to "relay" their requests
to a subnet that has a DHCP server on it. Because DHCP packets can be
broadcast, they will not be routed off of the local subnet. The DHCP relay
takes care of this for the client. You will need to set the environment
variable SERVERS and optionally OPTIONS in /etc/sysconfig/dhcrelay before
starting the server.

%package devel
Summary:	Development headers and libraries for the dhcpctl API
Group:		Development/Other
Requires:	dhcp-common >= %{epoch}:%{version}-%{release}

%description devel
DHCP devel contains all of the libraries and headers for developing with the
Internet Software Consortium (ISC) dhcpctl API.

%prep

%setup -q -n %{name}-%{version}%{?plevel:-%{plevel}}

%patch100 -p1 -b .ifup
%patch101 -p1 -b .format_not_a_string_literal_and_no_format_arguments
%patch102 -p1 -b .prevent_wireless_deassociation

# Handle Xen partial UDP checksums
%patch8 -p1 -b .xen
# If the ipv6 kernel module is missing, do not segfault
# (Submitted to dhcp-bugs@isc.org - [ISC-Bugs #19367])
%patch15 -p1 -b .noipv6
# Handle cases in add_timeout() where the function is called with a NULL
# value for the 'when' parameter
%patch17 -p1 -b .dracut
# Ensure 64-bit platforms parse lease file dates & times correctly
%patch18 -p1 -b .64-bit_lease_parse

install -m0644 %{SOURCE10} doc

%build
%serverbuild
%configure2_5x --enable-paranoia --enable-early-chroot \
    --with-ldapcrypto \
    --with-srv-lease-file=%{_var}/lib/dhcp/dhcpd.leases \
    --with-srv6-lease-file=%{_var}/lib/dhcp/dhcpd6.leases \
    --with-cli-lease-file=%{_var}/lib/dhcp/dhclient.leases \
    --with-cli6-lease-file=%{_var}/lib/dhcp/dhclient6.leases \
    --with-srv-pid-file=%{_var}/run/dhcpd/dhcpd.pid \
    --with-srv6-pid-file=%{_var}/run/dhcpd/dhcpd6.pid \
    --with-cli-pid-file=%{_var}/run/dhclient.pid \
    --with-cli6-pid-file=%{_var}/run/dhclient6.pid \
    --with-relay-pid-file=%{_var}/run/dhcrelay.pid

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_initrddir}
install -d %{buildroot}/lib/systemd/system
install -d %{buildroot}%{_var}/lib/dhcp
install -d %{buildroot}%{_var}/run/dhcpd

%makeinstall_std

# Install correct dhclient-script
%{__mkdir} -p %{buildroot}/sbin
%{__mv} %{buildroot}%{_sbindir}/dhclient %{buildroot}/sbin/dhclient
%{__install} -p -m 0755 client/scripts/linux %{buildroot}/sbin/dhclient-script

install -m0755 %{SOURCE11} %{buildroot}%{_initrddir}/dhcpd
install -m0755 %{SOURCE13} %{buildroot}%{_initrddir}/dhcpd6
install -m0755 %{SOURCE15} %{buildroot}%{_initrddir}/dhcrelay
install -m 644 %{SOURCE12} %{buildroot}/lib/systemd/system/dhcpd
install -m 644 %{SOURCE14} %{buildroot}/lib/systemd/system/dhcpd6
install -m 644 %{SOURCE16} %{buildroot}/lib/systemd/system/dhcrelay
install -m0755 %{SOURCE7} %{SOURCE8} %{buildroot}%{_sbindir}/
install -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/
install -m0755 contrib/ldap/dhcpd-conf-to-ldap %{buildroot}%{_sbindir}/

# install exit-hooks script to /etc/
install -m0755 %{SOURCE9} %{buildroot}%{_sysconfdir}/

cat > %{buildroot}%{_sysconfdir}/sysconfig/dhcpd <<EOF
# You can set here various option for dhcpd

# Which configuration file to use.
# CONFIGFILE="/etc/dhcpd.conf"

# Where to store the lease state information.
# LEASEFILE="/var/lib/dhcp/dhcpd.leases"

# Define INTERFACES to limit which network interfaces dhcpd listens on.
# The default null value causes dhcpd to listen on all interfaces.
#INTERFACES=""

# Define OPTIONS with any other options to pass to the dhcpd server.
# See dhcpd(8) for available options and syntax.
OPTIONS="-q"

EOF

touch %{buildroot}%{_var}/lib/dhcp/dhcpd.leases
touch %{buildroot}%{_var}/lib/dhcp/dhclient.leases

cat > %{buildroot}%{_sysconfdir}/sysconfig/dhcrelay <<EOF
# Define SERVERS with a list of one or more DHCP servers where
# DHCP packets are to be relayed to and from.  This is mandatory.
#SERVERS="10.11.12.13 10.9.8.7"
SERVERS=""

# Define OPTIONS with any other options to pass to the dhcrelay server.
# See dhcrelay(8) for available options and syntax.
#OPTIONS="-q -i eth0 -i eth1"
OPTIONS="-q"
EOF

find . -type d -exec chmod 0755 {} \;
find . -type f -exec chmod 0644 {} \;

rm -rf doc/ja_JP.eucJP

# remove empty files
find -size 0 |grep ldap | xargs rm -rf 

# remove unwanted file
rm -f %{buildroot}%{_sysconfdir}/dhclient.conf

%post server
%_post_service dhcpd
# New dhcpd lease file
if [ ! -f %{_var}/lib/dhcp/dhcpd.leases ]; then
    touch %{_var}/lib/dhcp/dhcpd.leases
fi

%preun server
%_preun_service dhcpd

%post relay
%_post_service dhcrelay

%preun relay
%_preun_service dhcrelay

%post client
touch /var/lib/dhcp/dhclient.leases

%postun client
rm -rf /var/lib/dhcp/dhclient.leases

%files common
%doc README contrib/ldap/README.ldap RELNOTES
%doc contrib/3.0b1-lease-convert
%dir %{_var}/lib/dhcp
%{_mandir}/man5/dhcp-options.5*

%files doc
%doc doc/*

%files server
%doc server/dhcpd.conf tests/failover contrib/ldap/dhcp.schema
%{_initrddir}/dhcpd
%{_initrddir}/dhcpd6
/lib/systemd/system/dhcpd
/lib/systemd/system/dhcpd6
%config(noreplace) %{_sysconfdir}/dhcpd.conf
%config(noreplace) %{_sysconfdir}/dhclient-exit-hooks
%config(noreplace) %{_sysconfdir}/sysconfig/dhcpd
%config(noreplace) %ghost %{_var}/lib/dhcp/dhcpd.leases
%{_sbindir}/dhcpd
%{_sbindir}/dhcpreport.pl
%{_sbindir}/dhcpd-conf-to-ldap
%{_sbindir}/dhcpd-chroot.sh
%{_bindir}/omshell
%{_mandir}/man1/omshell.1*
%{_mandir}/man5/dhcpd.conf.5*
%{_mandir}/man5/dhcpd.leases.5*
%{_mandir}/man5/dhcp-eval.5*
%{_mandir}/man8/dhcpd.8*
%dir %{_var}/run/dhcpd

%files relay
%{_initrddir}/dhcrelay
/lib/systemd/system/dhcrelay
%config(noreplace) %{_sysconfdir}/sysconfig/dhcrelay
%{_sbindir}/dhcrelay
%{_mandir}/man8/dhcrelay.8*

%files client
%doc client/dhclient.conf
%config(noreplace) %ghost %{_var}/lib/dhcp/dhclient.leases
%attr (0755,root,root) /sbin/dhclient-script
/sbin/dhclient
%{_mandir}/man5/dhclient.conf.5*
%{_mandir}/man5/dhclient.leases.5*
%{_mandir}/man8/dhclient.8*
%{_mandir}/man8/dhclient-script.8*

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_mandir}/man3/*
