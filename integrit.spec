Summary:	integrit is a file verification system
Summary(pl):	System weryfikacji plików
Name:		integrit 
Version:	2.03
%define		patchlevel 02
Release:	0.1
License:	GPL v2
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
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
%patch0 -p1

%build
%configure
%{__make} 
%{__make} aux

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes INSTALL examples/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo
echo 'It is recommended that the binary be copied to a secure location and'
echo "  re-copied to %{_prefix}/sbin at runtime or run directly"
echo "  from the secure medium."

%files
%defattr(644,root,root,755)
%doc *.gz examples/*.gz
%{_mandir}/man1/i-ls.1*
%{_mandir}/man1/i-viewdb.1*
%{_mandir}/man1/integrit.1*
%attr(755,root,root) %{_sbindir}/integrit
%attr(755,root,root) %{_sbindir}/i-viewdb
%attr(755,root,root) %{_bindir}/i-ls
