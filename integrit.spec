Summary:	integrit is a file verification system
Summary(pl):	System weryfikacji plików
Name:		integrit
Version:	3.01
%define		patchlevel	03
Release:	0.2
License:	GPL v2
Group:		Applications/System
Source0:	http://download.sourceforge.net/integrit/%{name}-%{version}.%{patchlevel}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://integrit.sourceforge.net/
Vendor:		Ed L Cashin <ecashin@users.sourceforge.net>
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes INSTALL examples/*
%{_datadir}/info/integrit.info*
%{_mandir}/man1/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
