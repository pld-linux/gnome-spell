Summary:	Gnome Spell is GNOME/Bonobo component for spell checking
Summary(pl):	Gnome Spell to element GNOME/Bonobo do kontroli pisowni
Name:		gnome-spell
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-spell/0.4/%{name}-%{version}.tar.gz
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 0.28
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRequires:	oaf-devel
BuildRequires:	pspell-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Gnome Spell is GNOME/Bonobo component for spell checking. In current
version it contains GNOME::Spell::Dictionary object, which provides
spell checking dictionary (see Spell.idl for exact API definition).
It's based on pspell package.

%description -l pl
Gnome Spell to element GNOME/Bonobo do kontroli pisowni. W tej wersji
zawiera obiekt GNOME::Spell::Dictionary, udostêpniaj±cy s³ownik do
sprawdzania pisowni (definicja API w Spell.idl). Bazuje na pakiecie
pspell.

%package devel
Summary:	Development resources for gnome-spell
Summary(pl):	Zasoby dla programistów gnome-spell
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development resources for gnome-spell.

%description devel -l pl
Zasoby dla programistów gnome-spell.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/oaf/*
%{_datadir}/gnome-spell
%{_datadir}/locale/*/*/*

%files devel
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%{_datadir}/idl/*
