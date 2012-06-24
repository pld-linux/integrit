Summary:	integrit is a file verification system
Summary(pl):	System weryfikacji plik�w
Name:		integrit
Version:	3.01
%define		patchlevel	03
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://download.sourceforge.net/integrit/%{name}-%{version}.%{patchlevel}.tar.gz
Source1:	%{name}.conf
Patch0:		%{name}-DESTDIR.patch
URL:		http://integrit.sourceforge.net/
Vendor:		Ed L Cashin <ecashin@users.sourceforge.net>
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_pkglibdir	/var/lib/%{name}

%description
integrit is a simple yet secure alternative to products like tripwire.
It has a small memory footprint, uses up to date cryptographic
algorithms, and has features that make sense (like including the MD5
checksum of newly generated databases in the report).

%description -l pl
integrit to prosta, bezpieczna alternatywa dla produkt�w typu
tripwire. Ma ma�e zu�ycie pami�ci, u�ywa aktualnych algorytm�w
kryptograficznych, ma sensowne mo�liwo�ci (typu do��czanie do raportu
sumy kontrolnej MD5 nowo generowanych baz).

%prep
%setup -q -n %{name}-%{version}
%patch0	-p1

%build
%{__autoconf}
cd hashtbl
%{__autoconf}
cd ..
%configure
%{__make}
%{__make} utils

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_pkglibdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes INSTALL examples/*
%{_datadir}/info/integrit.info*
%{_mandir}/man1/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%attr(750,root,root) %dir %{_pkglibdir}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
