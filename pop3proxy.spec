Summary:	pop3.proxy is an application level gateway for the POP3 protocol
Summary(pl):	pop3.proxy jest aplikacyjn± bramk± dla protoko³u POP3.
Name:		pop3proxy
Version:	1.2.0
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://www.quietsche-entchen.de/download/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pop3.proxy is an application level gateway for the POP3 protocol.
Unlike generic TCP proxys (like tcpproxy) it looks into the data
stream watching that client and server fullfill the protocol
specification. pop3.proxy is based on RFC 1939.

%description -l pl
pop3.proxy jest aplikacyjn± bramk± dla protoko³u POP3. W odró¿nieniu
od innych tego typu programów, pop3proxy nadzoruje transmisje
sprawdzaj±c czy klient i serwer spe³niaj± specyfikacje protoko³u (RFC
1939).

%prep
%setup -q -n %{name}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install pop3.proxy $RPM_BUILD_ROOT/%{_sbindir}/
install -d $RPM_BUILD_ROOT%{_mandir}/man1/
install pop3.proxy.1 $RPM_BUILD_ROOT/%{_mandir}/man1/

gzip -9nf README LICENSE rfc1939.txt 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz LICENSE.gz rfc1939.txt.gz
%attr(755,root,root) %{_sbindir}/pop3.proxy
%{_mandir}/man1/*
