Summary:	GNOME Application Libs (GAL)
Name:		gal
Version:	0.4.1
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gal/%{name}-%{version}.tar.gz
Patch0:		%{name}-no_version.patch
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-print-devel >= 0.22
BuildRequires:	gnome-vfs-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel >= 0.13
BuildRequires:	libunicode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This the GNOME Application Libs (GAL). This module contains some library functions
that came from Gnumeric and Evolution. The idea is to reuse those
widgets across various larger GNOME applications that might want to
use these widgets.

%package devel
Summary:	gal header files and development documentation
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for the gal libraries.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do bibliotek gal.

%package static
Summary:	gal static libraries
Summary(pl):	Biblioteki statyczne Gtk+
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Gal static libraries.

%description -l pl static
Biblioteki statyczne gal.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
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
%{_datadir}/gal

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
