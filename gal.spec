Summary:	GNOME Application Libs (GAL)
Summary(es.UTF-8):	Bibliotecas de Aplicaciones de GNOME (GAL)
Summary(ko.UTF-8):	GNOME 응용프로그램 라이브러리
Summary(pl.UTF-8):	Biblioteki Aplikacji GNOME (GAL)
Summary(pt_BR.UTF-8):	G App Libs: Biblioteca para uso em aplicativos GNOME
Summary(ru.UTF-8):	Библиотека для составных документов в GNOME
Summary(uk.UTF-8):	Бібліотека для компонентних документів в GNOME
Name:		gal
Version:	2.4.3
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gal/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	de9ef290fd614a1057e26e31bc294142
Patch0:		%{name}-iconv-in-glibc.patch
Patch1:		%{name}-gcc-3.4.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	libgnomecanvas >= 2.10.2
Obsoletes:	gal2
Obsoletes:	libgal19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This the GNOME Application Libs (GAL). This module contains some
library functions that came from Gnumeric and Evolution. The idea is
to reuse those widgets across various larger GNOME applications that
might want to use these widgets.

%description -l es.UTF-8
Éstas son las Bibliotecas de Aplicaciones de GNOME (GAL). Este módulo
contiene unas funciones provenientes de Gnumeric y Evolution. La
intención es reutilizar estos componentes entre las varias
aplicaciones GNOME grandes que quieran utilizarlos.

%description -l pl.UTF-8
Pakiet zawiera funkcje pochodzące z programów Gnumeric i Evolution.
Ideą tej biblioteki jest używanie tych funkcji i wigetów w innych
programach GNOME.

%description -l pt_BR.UTF-8
Este módulo contém algumas funções de biblioteca que vinham com o
Gnumeric e com o Evolution. A idéia é reutilizar estes componentes em
uma série de aplicações GNOME maiores.

%description -l ru.UTF-8
Это пакет G App Libs (GAL). Он содержит некоторые библиотечные
функции, пришедшие из Gnumeric и Evolution. Идея в том, чтобы
использовать их виджеты в других приложениях GNOME, которым эти
виджеты могли бы пригодиться.

%description -l uk.UTF-8
Це пакет G App Libs (GAL). Він містить деякі бібліотечні функції, що
походять від Gnumeric та Evolution. Ідея в тому, щоб використати їх
віджети в інших програмах GNOME, яким ці віджети могли б стати в
нагоді.

%package devel
Summary:	gal header files and development documentation
Summary(es.UTF-8):	Ficheros de cabecera y documentación de desarrollo para gal
Summary(ko.UTF-8):	GAL 응용프로그램을 개발하기 위한 라이브러리와 헤더파일
Summary(pl.UTF-8):	pliki nagłówkowe i dokumentacja gala
Summary(pt_BR.UTF-8):	Arquivos de inclusão do gal
Summary(ru.UTF-8):	Библиотеки и хедеры для gal
Summary(uk.UTF-8):	Бібліотеки та хедери для gal
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libglade2-devel >= 1:2.5.1
Requires:	libgnomeprintui-devel >= 2.10.2
Requires:	libgnomeui-devel >= 2.10.0-2
Obsoletes:	gal2-devel
Obsoletes:	libgal19-devel

%description devel
Header files and development documentation for the gal libraries.

%description devel -l es.UTF-8
Ficheros de cabecera y documentación de desarrollo para las
bibliotecas gal.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek gal.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão necessários para compilar os aplicativos que usam
o gal.

%description devel -l ru.UTF-8
Этот пакет содержит необходимые библиотеки и файлы заголовков для
разработки программ с использованием gal.

%description devel -l uk.UTF-8
Цей пакет містить необхідні бібліотеки розробки та файли заголовків
для розробки програм з використанням gal.

%package static
Summary:	gal static libraries
Summary(es.UTF-8):	Bibliotecas estáticas de gal
Summary(pl.UTF-8):	Biblioteki statyczne gala
Summary(pt_BR.UTF-8):	Bibliotecas estáticas do gal
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	gal2-static

%description static
Gal static libraries.

%description static -l es.UTF-8
Bibliotecas estáticas de gal.

%description static -l pl.UTF-8
Biblioteki statyczne gal.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas do gal.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p0

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	--disable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# shutup check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/lib*.{la,a}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}-2.4

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-2.4.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/gal-2.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
