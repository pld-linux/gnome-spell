Summary:	GNOME Spell is GNOME/Bonobo component for spell checking
Summary(pl):	GNOME Spell to element GNOME/Bonobo do kontroli pisowni
Name:		gnome-spell
Version:	1.0.5
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-spell/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	ba4dd33cb150b670756e456066bd7434
Patch0:		%{name}-enable-deprecated.patch
Patch1:		%{name}-locale-names.patch
BuildRequires:	ORBit2-devel
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Spell is GNOME/Bonobo component for spell checking. In current
version it contains GNOME::Spell::Dictionary object, which provides
spell checking dictionary (see Spell.idl for exact API definition).
It's based on pspell package.

%description -l pl
GNOME Spell to element GNOME/Bonobo do kontroli pisowni. W tej wersji
zawiera obiekt GNOME::Spell::Dictionary, udostêpniaj±cy s³ownik do
sprawdzania pisowni (definicja API w Spell.idl). Bazuje na pakiecie
pspell.

%package devel
Summary:	Development resources for gnome-spell
Summary(pl):	Zasoby dla programistów gnome-spell
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development resources for gnome-spell.

%description devel -l pl
Zasoby dla programistów gnome-spell.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}.lang
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libgnome-spell-component*.*.so
%{_libdir}/bonobo/servers/*
%{_datadir}/control-center-2.0/icons/*
%{_datadir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%{_libdir}/%{name}/libgnome-spell-component.so
%{_libdir}/%{name}/lib*.la
%{_datadir}/idl/*
