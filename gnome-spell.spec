Summary: Gnome Spell is GNOME/Bonobo component for spell checking.
Name: gnome-spell
Version: 0.1
Release: 2mdk
Source0: ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.bz2
Copyright: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libpspell3-devel ORBit-devel libbonobo2-devel liboaf-devel gnome-libs-devel

%description
Gnome Spell is GNOME/Bonobo component for spell checking. In current 0.1 version
it contains GNOME::Spell::Dictionary object, which provides spell checking dictionary
(see Spell.idl for exact API definition). It's based on pspell package.


%prep
%setup -q

%build
%configure

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog NEWS AUTHORS
%{_bindir}/*
%{_datadir}/idl/*
%{_datadir}/oaf/*

%changelog
* Wed Jan 24 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1-2mdk
- Recompiled with oaf 0.6.2

* Tue Jan  2 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1-1mdk
- First Mandrake package

# end of file
