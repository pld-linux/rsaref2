Summary:	RSAREF(TM): A Cryptographic Toolkit
Summary(pl):	RSAREF(TM): Biblioteka kryptograficzna
Name:		rsaref2 		
Version:	2.0
Release:	1
License:	distributable
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Source0:	%{name}.tar.gz
Patch0:		%{name}-makefiles.patch
URL:		http://www.rsasecurity.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The name "RSAREF" means "RSA reference". RSA Laboratories intends
RSAREF to serve as a portable, educational, reference implementation
of cryptography.

%description -l pl
Nazwa "RSAREF" oznacza "RSA reference". Intencj╠ RSA Laboratories 
byЁo dostarczenie Ёatwej do przeniesienia, edukacyjnej, 
referencyjnej implementacji kryptografii.

%package -n rsaref2-devel
Summary:	rsaref2 Library Development 
Summary(pl):	CzЙ╤Ф dla programistСw biblioteki rsaref2
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	rsaref2

%description -n rsaref2-devel
The rsaref2-devel package contains the header files and some
documentation needed to develop application with rsaref2.

%description -n rsaref2-devel -l pl
Pakiet rsaref2-devel zawiera pliki nagЁСwkowe i dokumentacjЙ,
potrzebne do kompilowania aplikacji korzystaj╠cych z rsaref2

%package -n rsaref2-static
Summary:	Static rsaref2 Library 
Summary(pl):	Statyczna biblioteka rsaref2
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	rsaref2-devel 

%description -n rsaref2-static
Static rsaref2 library.

%description -n rsaref2-static -l pl
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

ln -s %{_libdir}/librsaref2.so.%{version} $RPM_BUILD_ROOT%{_libdir}/librsaref2.so

gzip -9nf doc/* 

%post -p /sbin/ldconfig 
%postun -p /sbin/ldconfig 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_libdir}/librsaref2.so.%{version}

%files -n rsaref2-devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/librsaref2.so
%attr(644,root,root) %{_includedir}/rsaref2/* 
%doc doc/*.gz

%files -n rsaref2-static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/librsaref2.a
