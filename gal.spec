Summary:	GNOME Application Libs (GAL)
Summary(es):	Bibliotecas de Aplicaciones de GNOME (GAL)
Summary(ko):	GNOME �������α׷� ���̺귯��
Summary(pl):	Biblioteki Aplikacji GNOME (GAL)
Summary(pt_BR):	G App Libs: Biblioteca para uso em aplicativos GNOME
Summary(ru):	���������� ��� ��������� ���������� � GNOME
Summary(uk):	��̦����� ��� ������������ �������Ԧ� � GNOME
Name:		gal
Version:	2.1.11
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
# Source0-md5:	b91da3ce23f9edc47dcc52689754b6e1
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-iconv-in-glibc.patch
Patch2:		%{name}-gcc-3.4.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gtk+2-devel >= 2:2.4.3
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.27.1
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.6.1
BuildRequires:	libgnomeui-devel >= 2.6.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
Obsoletes:	gal2
Obsoletes:	libgal19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This the GNOME Application Libs (GAL). This module contains some
library functions that came from Gnumeric and Evolution. The idea is
to reuse those widgets across various larger GNOME applications that
might want to use these widgets.

%description -l es
�stas son las Bibliotecas de Aplicaciones de GNOME (GAL). Este m�dulo
contiene unas funciones provenientes de Gnumeric y Evolution. La
intenci�n es reutilizar estos componentes entre las varias
aplicaciones GNOME grandes que quieran utilizarlos.

%description -l pl
Pakiet zawiera funkcje pochodz�ce z program�w Gnumeric i Evolution.
Ide� tej biblioteki jest u�ywanie tych funkcji i wiget�w w innych
programach GNOME.

%description -l pt_BR
Este m�dulo cont�m algumas fun��es de biblioteca que vinham com o
Gnumeric e com o Evolution. A id�ia � reutilizar estes componentes em
uma s�rie de aplica��es GNOME maiores.

%description -l ru
��� ����� G App Libs (GAL). �� �������� ��������� ������������
�������, ��������� �� Gnumeric � Evolution. ���� � ���, �����
������������ �� ������� � ������ ����������� GNOME, ������� ���
������� ����� �� �����������.

%description -l uk
�� ����� G App Libs (GAL). ��� ͦ����� ���˦ ¦�̦����Φ ����æ�, ��
�������� צ� Gnumeric �� Evolution. ���� � ����, ��� ����������� ��
צ����� � ����� ��������� GNOME, ���� æ צ����� ����� � ����� �
����Ħ.

%package devel
Summary:	gal header files and development documentation
Summary(es):	Ficheros de cabecera y documentaci�n de desarrollo para gal
Summary(ko):	GAL �������α׷��� �����ϱ� ���� ���̺귯���� �������
Summary(pl):	pliki nag��wkowe i dokumentacja gala
Summary(pt_BR):	Arquivos de inclus�o do gal
Summary(ru):	���������� � ������ ��� gal
Summary(uk):	��̦����� �� ������ ��� gal
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libglade2-devel >= 1:2.4.0
Requires:	libgnomeprintui-devel >= 2.6.1
Requires:	libgnomeui-devel >= 2.6.1
Obsoletes:	gal2-devel
Obsoletes:	libgal19-devel

%description devel
Header files and development documentation for the gal libraries.

%description devel -l es
Ficheros de cabecera y documentaci�n de desarrollo para las
bibliotecas gal.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do bibliotek gal.

%description devel -l pt_BR
Arquivos de inclus�o necess�rios para compilar os aplicativos que usam
o gal.

%description devel -l ru
���� ����� �������� ����������� ���������� � ����� ���������� ���
���������� �������� � �������������� gal.

%description devel -l uk
��� ����� ͦ����� ����Ȧ�Φ ¦�̦����� �������� �� ����� �������˦�
��� �������� ������� � ������������� gal.

%package static
Summary:	gal static libraries
Summary(es):	Bibliotecas est�ticas de gal
Summary(pl):	Biblioteki statyczne gala
Summary(pt_BR):	Bibliotecas est�ticas do gal
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	gal2-static

%description static
Gal static libraries.

%description static -l es
Bibliotecas est�ticas de gal.

%description static -l pl
Biblioteki statyczne gal.

%description static -l pt_BR
Bibliotecas est�ticas do gal.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

mv -f po/{no,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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

%find_lang %{name}-2.2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-2.2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/gal-2.2

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
