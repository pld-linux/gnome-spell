Summary:	Gnome Spell is GNOME/Bonobo component for spell checking
Summary(pl):	Gnome Spell to element GNOME/Bonobo do kontroli pisowni
Name:		gnome-spell
Version:	0.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gnome-spell/%{name}-%{version}.tar.gz
Patch0:		%{name}-pspell4.patch
BuildRequires:	ORBit-devel
BuildRequires:	bonobo-devel >= 0.28
BuildRequires:	gnome-libs-devel
BuildRequires:	oaf-devel
BuildRequires:	pspell-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
%patch -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/oaf/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/idl/*
