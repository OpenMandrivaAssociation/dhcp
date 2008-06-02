%define _catdir /var/cache/man

Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) server/relay agent/client
Name:		dhcp
Epoch:		2
Version:	3.0.6
Release:	%mkrel 5
License:	Distributable
Group:		System/Servers
URL:		http://www.isc.org/dhcp.html
Source0:	ftp://ftp.isc.org/isc/%{name}/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.isc.org/isc/%{name}/%{name}-%{version}.tar.gz.sha512.asc
Source2:	dhcpd.conf
Source3:	dhcpd.init
Source4:	dhcp-dynamic-dns-examples.tar.bz2
Source5:	dhcrelay.init
Source6:	update_dhcp.pl
Source7:	dhcpreport.pl
Source8:	dhcpd-chroot.sh
Patch0:		dhcp-3.0.5-ifup.patch
# http://home.ntelos.net/%7Emasneyb/dhcp-3.0.1rc14-ldap-patch
# http://www.newwave.net/~masneyb/dhcp-3.0.3-ldap-patch
Patch1:		dhcp-3.0.4-ldap.diff
# (oe) http://www.episec.com/people/edelkind/patches/
Patch2:		dhcp-3.0.1-paranoia.diff
Patch4:		dhcp-3.0.1-default-timeout.patch
BuildRequires:	perl groff-for-man openldap-devel
Provides:	dhcpd
Obsoletes:	dhcpd
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package	common
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) server
Group:		System/Servers

%description	common
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

%package	doc
Summary:	Documentation about the ISC DHCP server/client
Group:		System/Servers

%description	doc
This package contains RFC/API/protocol documentation about the ISC
DHCP server and client.

DHCP (Dynamic Host Configuration Protocol) is a protocol which allows 
individual devices on an IP network to get their own network 
configuration information (IP address, subnetmask, broadcast address, 
etc.) from a DHCP server.  The overall purpose of DHCP is to make it 
easier to administer a large network.  The dhcp package includes the 
DHCP server and a DHCP relay agent.

%package	server
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) server
Group:		System/Servers
Requires:	dhcp-common = %{epoch}:%{version}
Requires(post):	rpm-helper
Requires(preun): rpm-helper
Obsoletes:	dhcp
Provides:	dhcp

%description	server
DHCP server is the Internet Software Consortium (ISC) DHCP server for various
UNIX operating systems. It allows a UNIX mac hine to serve DHCP requests from
the network.

You should install dhcp-server if you want to set up a DHCP server on your
network. You will also need to install the base dhcp package.

%package	client
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) client
Group:		System/Servers
Requires:	dhcp-common = %{epoch}:%{version}

%description	client
DHCP client is the Internet Software Consortium (ISC) DHCP client for various
UNIX operating systems.  It allows a UNIX mac hine to obtain it's networking
parameters from a DHCP server.

You should install dhcp-client if you want to use the ISC DHCP client instead
of the Red Hat DHCP client, pump, or dhcpcd, or dhcpxd. You will also need to
install the base dhcp package.

%package	relay
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) relay
Group:		System/Servers
Requires:	dhcp-common = %{epoch}:%{version}
Requires(post):	rpm-helper
Requires(preun): rpm-helper

%description	relay
DHCP relay is the Internet Software Consortium (ISC) relay agent for DHCP
packets. It is used on a subnet with DHCP clients to "relay" their requests
to a subnet that has a DHCP server on it. Because DHCP packets can be
broadcast, they will not be routed off of the local subnet. The DHCP relay
takes care of this for the client. You will need to set the environment
variable SERVERS and optionally OPTIONS in /etc/sysconfig/dhcrelay before
starting the server.

%package	devel
Summary:	Development headers and libraries for the dhcpctl API
Group:		Development/Other
Requires:	dhcp-common = %{epoch}:%{version}

%description	devel
DHCP devel contains all of the libraries and headers for developing with the
Internet Software Consortium (ISC) dhcpctl API.

%prep

%setup -q -n %{name}-%{version} -a4
%patch0 -p1 -b .ifup
%patch1 -p1 -b .dhcp-ldap
%patch2 -p1 -b .paranoia
%patch4 -p1 -b .default-timeout

cat << EOF >site.conf
VARDB=%{_localstatedir}/lib/dhcp
LIBDIR=%{_libdir}
INCDIR=%{_includedir}
ADMMANDIR=%{_mandir}/man8
FFMANDIR=%{_mandir}/man5
LIBMANDIR=%{_mandir}/man3
USRMANDIR=%{_mandir}/man1
EOF
cat << EOF >>includes/site.h
#define _PATH_DHCPD_PID		"%{_var}/run/dhcpd/dhcpd.pid"
#define _PATH_DHCPD_DB		"%{_localstatedir}/lib/dhcp/dhcpd.leases"
#define _PATH_DHCLIENT_DB	"%{_localstatedir}/lib/dhcp/dhclient.leases"
EOF

%build
%serverbuild
echo 'int main() { return sizeof(void *) != 8; }' | gcc -xc - -o is_ptr64
./is_ptr64 && PTR64_FLAGS="-DPTRSIZE_64BIT"

./configure --copts "$RPM_OPT_FLAGS $PTR64_FLAGS -DPARANOIA -DCL_DEFAULT_TIMEOUT=60 -DLDAP_DEPRECATED"

#-DEARLY_CHROOT

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_localstatedir}/lib/dhcp
install -d %{buildroot}%{_var}/run/dhcpd

%makeinstall_std

install -m0755 %{SOURCE3} %{buildroot}%{_initrddir}/dhcpd
install -m0755 %{SOURCE5} %{buildroot}%{_initrddir}/dhcrelay
install -m0755 %{SOURCE6} %{SOURCE7} %{SOURCE8} %{buildroot}%{_sbindir}/
install -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/
install -m0755 contrib/dhcpd-conf-to-ldap.pl %{buildroot}%{_sbindir}/

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

touch %{buildroot}%{_localstatedir}/lib/dhcp/dhcpd.leases
touch %{buildroot}%{_localstatedir}/lib/dhcp/dhclient.leases

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

%post server
%_post_service dhcpd
# New dhcpd lease file
if [ ! -f %{_localstatedir}/lib/dhcp/dhcpd.leases ]; then
    touch %{_localstatedir}/lib/dhcp/dhcpd.leases
fi

if [ $1 = 0 ]; then
	%{_initrddir}/dhcpd start
fi

#update an eventual installed dhcp-2* server
if [ -f %{_sysconfdir}/dhcpd.conf ]; then
	perl %{_sbindir}/update_dhcp.pl
fi

%preun server
%_preun_service dhcpd

%postun server
if [ "$1" -ge "1" ]; then
    /sbin/service dhcpd condrestart >/dev/null 2>&1  
fi

%post relay
%_post_service dhcrelay

%preun relay
%_preun_service dhcrelay

%postun relay
if [ "$1" -ge "1" ]; then
    /sbin/service dhcrelay condrestart >/dev/null 2>&1
fi
		 
%post client
touch /var/lib/dhcp/dhclient.leases

%postun client
rm -rf /var/lib/dhcp/dhclient.leases

%clean
rm -rf %{buildroot}

%files common
%defattr(-,root,root)
%doc README README.ldap RELNOTES Changelog-LDAP
%doc contrib/3.0b1-lease-convert
%dir %{_localstatedir}/lib/dhcp
%{_mandir}/man5/dhcp-options.5*

%files doc
%defattr(-,root,root)
%doc doc/*

%files server
%defattr(-,root,root)
%doc server/dhcpd.conf tests/failover contrib/dhcp.schema
%{_initrddir}/dhcpd
%config(noreplace) %{_sysconfdir}/dhcpd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/dhcpd
%config(noreplace) %ghost %{_localstatedir}/lib/dhcp/dhcpd.leases
%{_sbindir}/dhcpd
%{_sbindir}/update_dhcp.pl
%{_sbindir}/dhcpreport.pl
%{_sbindir}/dhcpd-conf-to-ldap.pl
%{_sbindir}/dhcpd-chroot.sh
%{_bindir}/omshell
%{_mandir}/man1/omshell.1*
%{_mandir}/man3/omapi.3*
%{_mandir}/man5/dhcpd.conf.5*
%{_mandir}/man5/dhcpd.leases.5*
%{_mandir}/man5/dhcp-eval.5*
%{_mandir}/man8/dhcpd.8*
%dir %{_var}/run/dhcpd

%files relay
%defattr(-,root,root)
%{_initrddir}/dhcrelay
%config(noreplace) %{_sysconfdir}/sysconfig/dhcrelay
%{_sbindir}/dhcrelay
%{_mandir}/man8/dhcrelay.8*

%files client
%defattr(-,root,root)
%doc client/dhclient.conf
%config(noreplace) %ghost %{_localstatedir}/lib/dhcp/dhclient.leases
%attr (0755,root,root) /sbin/dhclient-script
/sbin/dhclient
%{_mandir}/man5/dhclient.conf.5*
%{_mandir}/man5/dhclient.leases.5*
%{_mandir}/man8/dhclient.8*
%{_mandir}/man8/dhclient-script.8*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*
%{_mandir}/man3/*
