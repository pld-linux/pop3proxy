Summary:	pop3.proxy is an application level gateway for the POP3 protocol
Summary(pl):	pop3.proxy jest aplikacyjn± bramk± dla protoko³u POP3
Name:		pop3proxy
Version:	1.2.0
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://www.quietsche-entchen.de/download/%{name}-%{version}.tar.gz
Source1:	%{name}.inetd
Provides:	pop3daemon
Prereq:		rc-inetd >= 0.8.1
URL:		http://www.quietsche-entchen.de/software/pop3.proxy.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	proxytools

%description
pop3.proxy is an application level gateway for the POP3 protocol.
Unlike generic TCP proxys (like tcpproxy) it looks into the data
stream watching that client and server fulfil the protocol
specification. pop3.proxy is based on RFC 1939.

%description -l pl
pop3.proxy jest aplikacyjn± bramk± dla protoko³u POP3. W odró¿nieniu
od innych tego typu programów, pop3proxy nadzoruje transmisjê
sprawdzaj±c czy klient i serwer spe³niaj± specyfikacjê protoko³u (RFC
1939).

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1,/etc/sysconfig/rc-inetd}

install pop3.proxy $RPM_BUILD_ROOT%{_sbindir}
install pop3.proxy.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/pop3proxy

gzip -9nf README rfc1939.txt 

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun
if [ "$1" = "0" -a -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi
    
%files
%defattr(644,root,root,755)
%doc *.gz
%attr(640,root,root) %config %verify(not size mtime md5) /etc/sysconfig/rc-inetd/pop3proxy
%attr(755,root,root) %{_sbindir}/pop3.proxy
%{_mandir}/man1/*
