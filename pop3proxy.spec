Summary:	pop3.proxy is an application level gateway for the POP3 protocol
Summary(pl):	pop3.proxy jest aplikacyjn± bramk± dla protoko³u POP3
Name:		pop3proxy
Version:	1.2.0
Release:	4
License:	GPL
Group:		Applications/Networking
Source0:	http://www.quietsche-entchen.de/download/%{name}-%{version}.tar.gz
# Source0-md5:	9e6bf2493f1c12edaa11c97b7ef8d657
Source1:	%{name}.inetd
URL:		http://www.quietsche-entchen.de/software/pop3.proxy.html
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	rc-inetd >= 0.8.1
Provides:	pop3daemon
Conflicts:	proxytools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1,/etc/sysconfig/rc-inetd}

install pop3.proxy $RPM_BUILD_ROOT%{_sbindir}
install pop3.proxy.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/pop3proxy

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q rc-inetd reload

%postun
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

%files
%defattr(644,root,root,755)
%doc README rfc1939.txt
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/pop3proxy
%attr(755,root,root) %{_sbindir}/pop3.proxy
%{_mandir}/man1/*
