Summary:	integrit is a file verification system
Summary(pl):	System weryfikacji plików
Name:		integrit
Version:	3.01
%define		patchlevel	03
Release:	1
License:	GPL v2
Vendor:		Ed L Cashin <ecashin@users.sourceforge.net>
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.%{patchlevel}.tar.gz
# Source0-md5:	626f9a3ed4ab0901d5518597c8573af1
Source1:	%{name}.conf
Patch0:		%{name}-DESTDIR.patch
URL:		http://integrit.sourceforge.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}
%define		_pkglibdir	/var/lib/%{name}

%description
integrit is a simple yet secure alternative to products like tripwire.
It has a small memory footprint, uses up to date cryptographic
algorithms, and has features that make sense (like including the MD5
checksum of newly generated databases in the report).

%description -l pl
integrit to prosta, bezpieczna alternatywa dla produktów typu
tripwire. Ma ma³e zu¿ycie pamiêci, u¿ywa aktualnych algorytmów
kryptograficznych, ma sensowne mo¿liwo¶ci (typu do³±czanie do raportu
sumy kontrolnej MD5 nowo generowanych baz).

%prep
%setup -q
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
%{_datadir}/info/integrit.info*
%doc README Changes INSTALL examples
%{_mandir}/man1/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%attr(750,root,root) %dir %{_pkglibdir}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
