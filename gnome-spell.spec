Summary:	Gnome Spell is GNOME/Bonobo component for spell checking
Name:		gnome-spell
Version:	0.1
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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

%package devel
Summary:	Development resources for gnome-spell
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development resources for gnome-spell.

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
