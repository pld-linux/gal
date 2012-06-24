Summary:	GNOME Application Libs (GAL)
Summary(pl):	Biblioteki Aplikacji GNOME (GAL)
Summary(pt_BR):	G App Libs: Biblioteca para uso em aplicativos GNOME
Summary(ru):	���������� ��� ��������� ���������� � GNOME
Summary(uk):	��̦����� ��� ������������ �������Ԧ� � GNOME
Name:		gal
Version:	0.21
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/mirror/gnome.org/sources/gal/%{version}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-no_version.patch
Patch1:		%{name}-no_macros_in_AC_OUTPUT.patch
Patch2:		%{name}-am15.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.12
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	gnome-vfs-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libglade-devel >= 0.13
BuildRequires:	libglade-gnome-devel >= 0.13
BuildRequires:	libtool
BuildRequires:	libunicode-devel
BuildRequires:	libxml-devel
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgal19

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
Summary(pl):	pliki nag��wkowe i dokumentacja gala
Summary(pt_BR):	Arquivos de inclus�o do gal
Summary(ru):	���������� � ������ ��� gal
Summary(uk):	��̦����� �� ������ ��� gal
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gdk-pixbuf-gnome-devel
Requires:	gnome-print-devel
Requires:	libglade-gnome-devel
Obsoletes:	libgal19-devel

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
Requires:	%{name}-devel = %{version}

%description static
Gal static libraries.

%description static -l pl
Biblioteki statyczne gal.

%description static -l pt_BR
Bibliotecas est�ticas do gal.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
%patch2 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/etable
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade
%{_datadir}/%{name}/html
%{_datadir}/%{name}/%{version}/pixmaps

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
