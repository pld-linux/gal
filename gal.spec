Summary:	GNOME Application Libs (GAL)
Summary(pl):	Biblioteki Aplikacji GNOME (GAL)
Summary(pt_BR):	G App Libs: Biblioteca para uso em aplicativos GNOME
Name:		gal
Version:	0.18
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gal/%{name}-%{version}.tar.bz2
Patch0:		%{name}-no_version.patch
Patch1:		%{name}-no_macros_in_AC_OUTPUT.patch
Patch2:		%{name}-am15.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.12
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	gnome-vfs-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel >= 0.13
BuildRequires:	libtool
BuildRequires:	libunicode-devel
BuildRequires:	libxml-devel
BuildRequires:	xml-i18n-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This the GNOME Application Libs (GAL). This module contains some
library functions that came from Gnumeric and Evolution. The idea is
to reuse those widgets across various larger GNOME applications that
might want to use these widgets.

%description -l pl
Pakiet zawiera funkcje pochodz±ce z programów Gnumeric i Evolution.
Ide± tej biblioteki jest u¿ywanie tych funkcji i wigetów w innych
programach GNOME.

%description -l pt_BR
Este módulo contém algumas funções de biblioteca que vinham com o
Gnumeric e com o Evolution. A idéia é reutilizar estes componentes em
uma série de aplicações GNOME maiores.

%package devel
Summary:	gal header files and development documentation
Summary(pl):	pliki nag³ówkowe i dokumentacja gala
Summary(pt_BR):	Arquivos de inclusão do gal
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for the gal libraries.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do bibliotek gal.

%description -l pt_BR devel 
Arquivos de inclusão necessários para compilar os aplicativos que usam
o gal.

%package static
Summary:	gal static libraries
Summary(pl):	Biblioteki statyczne gala
Summary(pt_BR):	Bibliotecas estáticas do gal
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Gal static libraries.

%description -l pl static
Biblioteki statyczne gal.

%description -l pt_BR static
Bibliotecas estáticas do gal.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/etable
%dir %{_datadir}/gal
%{_datadir}/gal/glade

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/gal

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
