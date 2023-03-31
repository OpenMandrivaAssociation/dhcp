%global _disable_rebuild_configure 1

%define major_version 4.4.3
%define patch_version P1

Name:		dhcp
Epoch:		3
Version:	%{major_version}%{patch_version}
Release:	2
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) server/relay agent/client
License:	Distributable
Group:		System/Servers
URL:		http://www.isc.org/software/dhcp
Source0:	ftp://ftp.isc.org/isc/%{name}/%{major_version}%{?patch_version:-%{patch_version}}/%{name}-%{major_version}%{?patch_version:-%{patch_version}}.tar.gz
Source1:	dhcp.sysusers
Source2:	dhcpd.conf
Source3:	dhcpd6.conf
Source4:	dhcp-dynamic-dns-examples.tar.bz2
Source7:	dhcpreport.pl
Source8:	dhcpd-chroot.sh
# (eugeni) dhclient-exit-hooks script
Source9:	dhclient-exit-hooks
Source10:	draft-ietf-dhc-ldap-schema-01.txt
Source12:	dhcpd.service
Source14:	dhcpd6.service
Source16:	dhcrelay.service
Source17:	dhcpd.tmpfiles
Source18:	dhclient.tmpfiles
Source19:	dhcrelay.tmpfiles
# fedora patches
Patch0:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0001-change-bug-url.patch
Patch1:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0002-additional-dhclient-options.patch
Patch2:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0003-Handle-releasing-interfaces-requested-by-sbin-ifup.patch
Patch3:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0004-Support-unicast-BOOTP-for-IBM-pSeries-systems-and-ma.patch
Patch4:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0005-Change-default-requested-options.patch
Patch5:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0006-Various-man-page-only-fixes.patch
Patch6:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0007-Change-paths-to-conform-to-our-standards.patch
Patch7:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0008-Make-sure-all-open-file-descriptors-are-closed-on-ex.patch
Patch8:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0009-Fix-garbage-in-format-string-error.patch
Patch9:		https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0010-Handle-null-timeout.patch
Patch10:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0011-Drop-unnecessary-capabilities.patch
Patch11:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0012-RFC-3442-Classless-Static-Route-Option-for-DHCPv4-51.patch
Patch12:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0013-DHCPv6-over-PPP-support-626514.patch
Patch13:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0014-IPoIB-support-660681.patch
Patch14:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0015-Add-GUID-DUID-to-dhcpd-logs-1064416.patch
Patch15:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0016-Turn-on-creating-sending-of-DUID.patch
Patch16:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0017-Send-unicast-request-release-via-correct-interface.patch
Patch17:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0018-No-subnet-declaration-for-iface-should-be-info-not-e.patch
Patch18:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0019-dhclient-write-DUID_LLT-even-in-stateless-mode-11563.patch
Patch19:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0020-Discover-all-hwaddress-for-xid-uniqueness.patch
Patch20:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0021-Load-leases-DB-in-non-replay-mode-only.patch
Patch21:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0022-dhclient-make-sure-link-local-address-is-ready-in-st.patch
Patch22:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0023-option-97-pxe-client-id.patch
Patch23:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0024-Detect-system-time-changes.patch
Patch24:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0025-bind-Detect-system-time-changes.patch
Patch25:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0026-Add-dhclient-5-B-option-description.patch
Patch26:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0027-Add-missed-sd-notify-patch-to-manage-dhcpd-with-syst.patch
Patch27:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/0028-Use-system-getaddrinfo-for-dhcp.patch
Patch28:	https://src.fedoraproject.org/rpms/dhcp/raw/rawhide/f/CVE-2021-25220.patch
# OpenMandriva patches
Patch100:	dhcp-4.4.3-compile.patch
BuildRequires:	groff-for-man
BuildRequires:	openldap-devel
#BuildRequires:	bind-devel
BuildRequires:	pkgconfig(krb5)
BuildRequires:	pkgconfig(libsasl2)
BuildRequires:	pkgconfig(com_err)
BuildRequires:	pkgconfig(systemd)

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
BuildArch:	noarch

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
BuildArch:	noarch

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
Requires:	dhcp-common >= %{EVRD}
%systemd_requires
Requires(pre):	systemd

%description	server
DHCP server is the Internet Software Consortium (ISC) DHCP server for various
UNIX operating systems. It allows a UNIX mac hine to serve DHCP requests from
the network.

You should install dhcp-server if you want to set up a DHCP server on your
network. You will also need to install the base dhcp package.

%package	client
Summary:	The ISC DHCP (Dynamic Host Configuration Protocol) client
Group:		System/Servers
Requires:	dhcp-common >= %{EVRD}
Provides:	dhcp-client-daemon
Requires:	hostname
%systemd_requires

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
Requires:	dhcp-common >= %{EVRD}
%systemd_requires

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
Requires:	dhcp-common >= %{EVRD}

%description	devel
DHCP devel contains all of the libraries and headers for developing with the
Internet Software Consortium (ISC) dhcpctl API.

%prep
# Not using %%autosetup because we need to untar
# the bind tarball before applying patches
%setup -qn %{name}-%{major_version}%{?patch_version:-%{patch_version}}
cd bind
tar xf bind.tar.gz
ln -s bind-9* bind
cd ..
%autopatch -p1

# Update paths in all man pages
for page in client/dhclient.conf.5 client/dhclient.leases.5 \
            client/dhclient-script.8 client/dhclient.8 ; do
	sed -i -e 's|CLIENTBINDIR|%{_sbindir}|g' \
	       -e 's|RUNDIR|%{_localstatedir}/run|g' \
	       -e 's|DBDIR|%{_localstatedir}/lib/dhclient|g' \
	       -e 's|ETCDIR|%{dhcpconfdir}|g' $page
done
 
for page in server/dhcpd.conf.5 server/dhcpd.leases.5 server/dhcpd.8 ; do
	sed -i -e 's|CLIENTBINDIR|%{_sbindir}|g' \
	       -e 's|RUNDIR|%{_localstatedir}/run|g' \
	       -e 's|DBDIR|%{_localstatedir}/lib/dhcpd|g' \
	       -e 's|ETCDIR|%{dhcpconfdir}|g' $page
done
 
sed -i -e 's|/var/db/|%{_localstatedir}/lib/dhcpd/|g' contrib/dhcp-lease-list.pl

install -m0644 %{SOURCE10} doc

%build
%serverbuild
autoreconf -fiv
%configure \
	--sbindir=%{_bindir} \
	--enable-paranoia --enable-early-chroot --enable-binary-leases \
	--with-ldap --with-ldapcrypto --with-ldap-gssapi \
	--with-srv-lease-file=%{_var}/lib/dhcpd/dhcpd.leases \
	--with-srv6-lease-file=%{_var}/lib/dhcpd/dhcpd6.leases \
	--with-cli-lease-file=%{_var}/lib/dhclient/dhclient.leases \
	--with-cli6-lease-file=%{_var}/lib/dhclient/dhclient6.leases \
	--with-srv-pid-file=/run/dhcpd/dhcpd.pid \
	--with-srv6-pid-file=/run/dhcpd/dhcpd6.pid \
	--with-cli-pid-file=/run/dhclient/dhclient.pid \
	--with-cli6-pid-file=/run/dhclient/dhclient6.pid \
	--with-relay-pid-file=/run/dhcrelay/dhcrelay.pid \
	--disable-static --with-systemd --enable-log-pid \
	--enable-paranoia --enable-early-chroot \
	--enable-binary-leases

# (tpg) disable parallel build
%config_update
%make_build -j1

%install
%make_install

# Install correct dhclient-script
install -m 755 client/scripts/linux %{buildroot}%{_bindir}/dhclient-script

install -d %{buildroot}%{_unitdir}
install -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/dhcpd.service
install -m 644 %{SOURCE14} %{buildroot}%{_unitdir}/dhcpd6.service
install -m 644 %{SOURCE16} %{buildroot}%{_unitdir}/dhcrelay.service

install -D -p -m 644 %{SOURCE17} %{buildroot}%{_tmpfilesdir}/dhcpd.conf
install -D -p -m 644 %{SOURCE18} %{buildroot}%{_tmpfilesdir}/dhclient.conf
install -D -p -m 644 %{SOURCE19} %{buildroot}%{_tmpfilesdir}/dhcrelay.conf
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/dhcp.conf

install -m 755 %{SOURCE7} %{SOURCE8} %{buildroot}%{_bindir}
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}
install -m 755 contrib/ldap/dhcpd-conf-to-ldap %{buildroot}%{_bindir}

# install exit-hooks script to /etc/
install -m 755 %{SOURCE9} %{buildroot}%{_sysconfdir}

install -d %{buildroot}%{_sysconfdir}/sysconfig
cat > %{buildroot}%{_sysconfdir}/sysconfig/dhcpd <<EOF
# You can set here various option for dhcpd

# Which configuration file to use.
# CONFIGFILE="/etc/dhcpd.conf"

# Where to store the lease state information.
# LEASEFILE="/var/lib/dhcpd/dhcpd.leases"

# Define INTERFACES to limit which network interfaces dhcpd listens on.
# The default null value causes dhcpd to listen on all interfaces.
#INTERFACES=""

# Define OPTIONS with any other options to pass to the dhcpd server.
# See dhcpd(8) for available options and syntax.
OPTIONS="-q"
EOF

cat > %{buildroot}%{_sysconfdir}/sysconfig/dhcpd6 <<EOF
# You can set here various option for dhcpd

# Which configuration file to use.
# CONFIGFILE="/etc/dhcpd6.conf"

# Where to store the lease state information.
# LEASEFILE="/var/lib/dhcpd/dhcpd6.leases"

# Define INTERFACES to limit which network interfaces dhcpd listens on.
# The default null value causes dhcpd to listen on all interfaces.
#INTERFACES=""

# Define OPTIONS with any other options to pass to the dhcpd server.
# See dhcpd(8) for available options and syntax.
OPTIONS="-q"
EOF

install -d %{buildroot}%{_var}/lib/dhcpd
touch %{buildroot}%{_var}/lib/dhcpd/dhcpd.leases
touch %{buildroot}%{_var}/lib/dhcpd/dhcpd6.leases
install -d %{buildroot}%{_var}/lib/dhclient
touch %{buildroot}%{_var}/lib/dhclient/dhclient.leases

# Copy sample conf files into position (called by doc macro)
cp -p doc/examples/dhclient-dhcpv6.conf client/dhclient6.conf.example
cp -p doc/examples/dhcpd-dhcpv6.conf server/dhcpd6.conf.example

cat > %{buildroot}%{_sysconfdir}/sysconfig/dhcrelay <<EOF
# Define DHCRELAYARGS with a list of one or more DHCP servers where
# See dhcrelay(8) for available options and syntax.
# Define at the end the servers with a list of one or more DHCP servers where
# DHCP packets are to be relayed to and from.  This is mandatory. Replace xxxx with them
#DHCRELAYARGS="-q -iu eth0 -id eth1 192.168.1.1"
DHCRELAYARGS="-q"
EOF

find . -type d -exec chmod 0755 {} \;
find . -type f -exec chmod 0644 {} \;

rm -rf doc/ja_JP.eucJP

# remove empty files
find -size 0 |grep ldap | xargs rm -rf 

# remove unwanted file
rm -f %{buildroot}%{_sysconfdir}/dhclient.conf.example
rm -f %{buildroot}%{_sysconfdir}/dhcpd.conf.example
rm -f %{buildroot}%{_libdir}/*.a

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-dhcp-server.preset << EOF
enable dhcpd.service
EOF

cat > %{buildroot}%{_presetdir}/86-dhcp-relay.preset << EOF
enable dhcrelay.service
EOF

%pre server
%sysusers_create_package %{name} %{SOURCE1}

%post server
# New dhcpd lease file
if [ ! -f %{_var}/lib/dhcpd/dhcpd.leases ]; then
    touch %{_var}/lib/dhcpd/dhcpd.leases
fi

if [ ! -f %{_var}/lib/dhcpd/dhcpd6.leases ]; then
    touch %{_var}/lib/dhcpd/dhcpd6.leases
fi

%post client
touch %{_var}/lib/dhclient/dhclient.leases

%postun client
rm -rf %{_var}/lib/dhclient/dhclient.leases

%files common
%doc README contrib/ldap/README.ldap RELNOTES
%doc contrib/3.0b1-lease-convert
%doc %{_mandir}/man5/dhcp-options.5*

%files doc
%doc doc/*

%files server
%doc server/dhcpd*.conf.example tests/failover contrib/ldap/dhcp.schema
%{_sysusersdir}/dhcp.conf
%{_presetdir}/86-dhcp-server.preset
%{_unitdir}/dhcpd.service
%{_unitdir}/dhcpd6.service
%{_tmpfilesdir}/dhcpd.conf
%config(noreplace) %{_sysconfdir}/dhcpd.conf
%config(noreplace) %{_sysconfdir}/dhcpd6.conf
%config(noreplace) %{_sysconfdir}/dhclient-exit-hooks
%config(noreplace) %{_sysconfdir}/sysconfig/dhcpd
%config(noreplace) %{_sysconfdir}/sysconfig/dhcpd6
%{_bindir}/dhcpd
%{_bindir}/dhcpreport.pl
%{_bindir}/dhcpd-conf-to-ldap
%{_bindir}/dhcpd-chroot.sh
%{_bindir}/omshell
%doc %{_mandir}/man1/omshell.1*
%doc %{_mandir}/man3/omapi.3*
%doc %{_mandir}/man5/dhcpd.conf.5*
%doc %{_mandir}/man5/dhcpd.leases.5*
%doc %{_mandir}/man5/dhcp-eval.5*
%doc %{_mandir}/man8/dhcpd.8*
%dir %{_var}/lib/dhcpd
%config(noreplace) %ghost %{_var}/lib/dhcpd/dhcpd.leases
%config(noreplace) %ghost %{_var}/lib/dhcpd/dhcpd6.leases

%files relay
%{_presetdir}/86-dhcp-relay.preset
%{_unitdir}/dhcrelay.service
%{_tmpfilesdir}/dhcrelay.conf
%config(noreplace) %{_sysconfdir}/sysconfig/dhcrelay
%{_bindir}/dhcrelay
%doc %{_mandir}/man8/dhcrelay.8*

%files client
%doc client/dhclient*.conf.example
%attr (0755,root,root) %{_bindir}/dhclient-script
%{_tmpfilesdir}/dhclient.conf
%{_bindir}/dhclient
%doc %{_mandir}/man5/dhclient.conf.5*
%doc %{_mandir}/man5/dhclient.leases.5*
%doc %{_mandir}/man8/dhclient.8*
%doc %{_mandir}/man8/dhclient-script.8*
%dir %{_var}/lib/dhclient
%config(noreplace) %ghost %{_var}/lib/dhclient/dhclient.leases

%files devel
%{_includedir}/*
%doc %{_mandir}/man3/dhcpctl.3.*
