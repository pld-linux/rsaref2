Summary:	RSAREF(TM): A Cryptographic Toolkit
Summary(pl.UTF-8):   RSAREF(TM): Biblioteka kryptograficzna
Name:		rsaref2
Version:	2.0
Release:	1
License:	distributable
Group:		Development/Libraries
Source0:	%{name}.tar.gz
# Source0-md5:	0b474c97bf1f1c0d27e5a95f1239c08d
Patch0:		%{name}-makefiles.patch
URL:		http://www.rsasecurity.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The name "RSAREF" means "RSA reference". RSA Laboratories intends
RSAREF to serve as a portable, educational, reference implementation
of cryptography.

%description -l pl.UTF-8
Nazwa "RSAREF" oznacza "RSA reference". Intencją RSA Laboratories było
dostarczenie łatwej do przeniesienia, edukacyjnej, referencyjnej
implementacji kryptografii.

%package devel
Summary:	rsaref2 Library Development
Summary(pl.UTF-8):   Część dla programistów biblioteki rsaref2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The rsaref2-devel package contains the header files and some
documentation needed to develop application with rsaref2.

%description devel -l pl.UTF-8
Pakiet rsaref2-devel zawiera pliki nagłówkowe i dokumentację,
potrzebne do kompilowania aplikacji korzystających z rsaref2

%package static
Summary:	Static rsaref2 Library
Summary(pl.UTF-8):   Statyczna biblioteka rsaref2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static rsaref2 library.

%description static -l pl.UTF-8
Statyczna biblioteka rsaref2.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -C install/unix
%{__make} -C install/unix clean
%{__make} -C install/unix -f makefile.shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_includedir}/rsaref2
install -d $RPM_BUILD_ROOT%{_libdir}

install install/unix/rdemo $RPM_BUILD_ROOT%{_bindir}/rsa-rdemo
install install/unix/dhdemo $RPM_BUILD_ROOT%{_bindir}/rsa-dhdemo

install install/unix/librsaref2.so $RPM_BUILD_ROOT%{_libdir}/librsaref2.so.%{version}
install install/unix/rsaref.a $RPM_BUILD_ROOT%{_libdir}/librsaref2.a
install source/*.h $RPM_BUILD_ROOT%{_includedir}/rsaref2

ln -sf %{_libdir}/librsaref2.so.%{version} $RPM_BUILD_ROOT%{_libdir}/librsaref2.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/librsaref2.so.%{version}

%files devel
%defattr(644,root,root,755)
%{_libdir}/librsaref2.so
%{_includedir}/rsaref2/*
%doc doc/*

%files static
%defattr(644,root,root,755)
%{_libdir}/librsaref2.a
