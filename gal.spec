Summary:	GNOME Application Libs (GAL)
Summary(pl):	Biblioteki Aplikacji GNOME (GAL)
Summary(pt_BR):	G App Libs: Biblioteca para uso em aplicativos GNOME
Summary(ru):	Библиотека для составных документов в GNOME
Summary(uk):	Б╕бл╕отека для компонентних документ╕в в GNOME
Name:		gal
Version:	1.99.1
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.99/%{name}-%{version}.tar.bz2
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libgnomeprint-devel >= 2.2.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	intltool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgal19


%description
This the GNOME Application Libs (GAL). This module contains some
library functions that came from Gnumeric and Evolution. The idea is
to reuse those widgets across various larger GNOME applications that
might want to use these widgets.

%description -l pl
Pakiet zawiera funkcje pochodz╠ce z programСw Gnumeric i Evolution.
Ide╠ tej biblioteki jest u©ywanie tych funkcji i wigetСw w innych
programach GNOME.

%description -l pt_BR
Este mСdulo contИm algumas funГУes de biblioteca que vinham com o
Gnumeric e com o Evolution. A idИia И reutilizar estes componentes em
uma sИrie de aplicaГУes GNOME maiores.

%description -l ru
Это пакет G App Libs (GAL). Он содержит некоторые библиотечные
функции, пришедшие из Gnumeric и Evolution. Идея в том, чтобы
использовать их виджеты в других приложениях GNOME, которым эти
виджеты могли бы пригодиться.

%description -l uk
Це пакет G App Libs (GAL). В╕н м╕стить деяк╕ б╕бл╕отечн╕ функц╕╖, що
походять в╕д Gnumeric та Evolution. ╤дея в тому, щоб використати ╖х
в╕джети в ╕нших програмах GNOME, яким ц╕ в╕джети могли б стати в
нагод╕.

%package devel
Summary:	gal header files and development documentation
Summary(pl):	pliki nagЁСwkowe i dokumentacja gala
Summary(pt_BR):	Arquivos de inclusЦo do gal
Summary(ru):	Библиотеки и хедеры для gal
Summary(uk):	Б╕бл╕отеки та хедери для gal
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk+2-devel
Requires:	libgnomeprint-devel
Requires:	libglade2-devel
Obsoletes:	libgal19-devel

%description devel
Header files and development documentation for the gal libraries.

%description devel -l pl
Pliki nagЁСwkowe i dokumentacja do bibliotek gal.

%description devel -l pt_BR
Arquivos de inclusЦo necessАrios para compilar os aplicativos que usam
o gal.

%description devel -l ru
Этот пакет содержит необходимые библиотеки и файлы заголовков для
разработки программ с использованием gal.

%description devel -l uk
Цей пакет м╕стить необх╕дн╕ б╕бл╕отеки розробки та файли заголовк╕в
для розробки програм з використанням gal.

%package static
Summary:	gal static libraries
Summary(pl):	Biblioteki statyczne gala
Summary(pt_BR):	Bibliotecas estАticas do gal
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Gal static libraries.

%description static -l pl
Biblioteki statyczne gal.

%description static -l pt_BR
Bibliotecas estАticas do gal.

%prep
%setup -q

%build
%configure \
	--enable-static 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.so
%{_libdir}/gtk-2.0/modules/lib*.la
%{_datadir}/*
%{_pkgconfigdir}/gal-2.0.pc

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
