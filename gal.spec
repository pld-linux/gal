
Summary:	GNOME Application Libs (GAL)
Summary(ko):	GNOME �������α׷� ���̺귯��
Summary(pl):	Biblioteki Aplikacji GNOME (GAL)
Summary(pt_BR):	G App Libs: Biblioteca para uso em aplicativos GNOME
Summary(ru):	���������� ��� ��������� ���������� � GNOME
Summary(uk):	��̦����� ��� ������������ �������Ԧ� � GNOME
Name:		gal
Version:	1.99.8
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.99/%{name}-%{version}.tar.bz2
# Source0-md5:	2f3323decf2bbfa11d32f97998e044d9
Patch0:		%{name}-am17.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libgnomeprint-devel >= 2.2.0
BuildRequires:	libgnomeprintui-devel >= 2.2.1
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgal19
Obsoletes:	gal2

%description
This the GNOME Application Libs (GAL). This module contains some
library functions that came from Gnumeric and Evolution. The idea is
to reuse those widgets across various larger GNOME applications that
might want to use these widgets.

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
Summary(ko):	GAL �������α׷��� �����ϱ� ���� ���̺귯���� �������
Summary(pl):	pliki nag��wkowe i dokumentacja gala
Summary(pt_BR):	Arquivos de inclus�o do gal
Summary(ru):	���������� � ������ ��� gal
Summary(uk):	��̦����� �� ������ ��� gal
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	libgnomeprintui-devel >= 2.2.1
Requires:	libgnomeui-devel >= 2.2.0
Requires:	libglade2-devel
Obsoletes:	libgal19-devel
Obsoletes:	gal2-devel

%description devel
Header files and development documentation for the gal libraries.

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
Summary(pl):	Biblioteki statyczne gala
Summary(pt_BR):	Bibliotecas est�ticas do gal
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}
Obsoletes:	gal2-static

%description static
Gal static libraries.

%description static -l pl
Biblioteki statyczne gal.

%description static -l pt_BR
Bibliotecas est�ticas do gal.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
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
rm -f $RPM_BUILD_ROOT/%{_libdir}/gtk-2.0/modules/lib*.{la,a}

%find_lang %{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}-%{version}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.so
%{_datadir}/gal-2.0

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
