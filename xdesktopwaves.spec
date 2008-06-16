%define name xdesktopwaves
%define version 1.3
%define release %mkrel 3

Summary: Create water effect on your X background
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/Other
Url: http://xdesktopwaves.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libx11-devel

%description
Xdesktopwaves is a cellular automata setting the background of your X Windows
desktop under water. Windows and mouse are like ships on the sea. Each
movement of these ends up in moving water waves. You can even have rain
and/or storm stirring up the water.

%prep
%setup -q

%build
%make CFLAGS="-I%{_prefix}/X11R6/include %optflags"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot{%_bindir,%_mandir/man1}

%make install BINDIR=%buildroot%_bindir MAN1DIR=%buildroot%{_mandir}/man1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_bindir/%name
%_mandir/man1/%{name}*


