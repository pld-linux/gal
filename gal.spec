Summary:	GNOME Application Libs (GAL)
Summary(ko):	GNOME 응용프로그램 라이브러리
Summary(pl):	Biblioteki Aplikacji GNOME (GAL)
Summary(pt_BR):	G App Libs: Biblioteca para uso em aplicativos GNOME
Summary(ru):	隋쫄�鞫탸� 켈� 遝戇죽槐� 켓坑考塊窘 � GNOME
Summary(uk):	數쫄┩旽個 켈� 蓋辜鷗턱仝�� 켓坑考塊┹ � GNOME
Name:		gal
Version:	1.99.10
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.99/%{name}-%{version}.tar.bz2
# Source0-md5:	72284a1e174329cb42149ae327f43995
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.3.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libgnomeprint-devel >= 2.2.0
BuildRequires:	libgnomeprintui-devel >= 2.2.1
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel
Obsoletes:	gal2
Obsoletes:	libgal19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This the GNOME Application Libs (GAL). This module contains some
library functions that came from Gnumeric and Evolution. The idea is
to reuse those widgets across various larger GNOME applications that
might want to use these widgets.

%description -l pl
Pakiet zawiera funkcje pochodz켧e z program�w Gnumeric i Evolution.
Ide� tej biblioteki jest u퓓wanie tych funkcji i wiget�w w innych
programach GNOME.

%description -l pt_BR
Este m�dulo cont�m algumas fun寤es de biblioteca que vinham com o
Gnumeric e com o Evolution. A id�ia � reutilizar estes componentes em
uma s�rie de aplica寤es GNOME maiores.

%description -l ru
璜� 僅愾� G App Libs (GAL). 停 遝컵壟�� 壙蓋冬籠� 쪼쫄�鞫텡槐�
팹珖촁�, 妗�北콕�� �� Gnumeric � Evolution. 用턺 � 冬�, 師苟�
�唐驅媒窘죤� �� 慄켯텃� � 켠朗�� 妗�卿領炚騎 GNOME, 蓋冬籠� 卜�
慄켯텃� 賈핍� 쬔 妗�하케潼堂.

%description -l uk
矢 僅愾� G App Libs (GAL). 憚� 稽戇�潼 컵麒� 짝쫄┩旽奢� 팹珖챈�, 粉
饉훰켜潼 屢� Gnumeric 讀 Evolution. 뗑턺 � 冬鼓, 粉� 慄蓋虜戇죤� ㎹
屢켯텃� � ┧排� 妗逑怒皐� GNOME, 麒�� 챈 屢켯텃� 賈핍� � 戇죤� �
适하칡.

%package devel
Summary:	gal header files and development documentation
Summary(ko):	GAL 응용프로그램을 개발하기 위한 라이브러리와 헤더파일
Summary(pl):	pliki nag농wkowe i dokumentacja gala
Summary(pt_BR):	Arquivos de inclus�o do gal
Summary(ru):	隋쫄�鞫탸� � 훅컵籠 켈� gal
Summary(uk):	數쫄┩旽漑 讀 훅컵虜 켈� gal
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	libglade2-devel
Requires:	libgnomeprintui-devel >= 2.2.1
Requires:	libgnomeui-devel >= 2.3.3.1-2
Obsoletes:	gal2-devel
Obsoletes:	libgal19-devel

%description devel
Header files and development documentation for the gal libraries.

%description devel -l pl
Pliki nag농wkowe i dokumentacja do bibliotek gal.

%description devel -l pt_BR
Arquivos de inclus�o necess�rios para compilar os aplicativos que usam
o gal.

%description devel -l ru
璜鞫 僅愾� 遝컵壟�� 壙苟훰케梏� 쪼쫄�鞫탸� � 팁奸� 憫하卿率窘 켈�
怒撲좌鞫漑 妗逑怒袴 � �唐驅媒窘죔�터 gal.

%description devel -l uk
矢� 僅愾� 稽戇�潼 壙苟홀켑� 짝쫄┩旽漑 碌撲苟漑 讀 팁奸� 憫하卿率┹
켈� 碌撲苟漑 妗逑怒� � 慄蓋虜戇죔罫� gal.

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
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/lib*.{la,a}

%find_lang %{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}-%{version}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
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
