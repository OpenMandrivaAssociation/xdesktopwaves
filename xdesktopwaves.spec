%define _empty_manifest_terminate_build 0

Summary: Create water effect on your X background
Name: xdesktopwaves
Version: 1.4
Release: 1
Source0: https://sourceforge.net/projects/xdesktopwaves/files/xdesktopwaves/xdesktopwaves-%{version}.tar.gz
License: GPL
Group: Graphical desktop/Other
Url: http://xdesktopwaves.sourceforge.net/
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)

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




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.3-4mdv2010.0
+ Revision: 435074
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3-3mdv2009.0
+ Revision: 222249
- BuildRequires libxext-devel
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Jul 26 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 07/26/06 20:17:43 (42246)
- rebuild
- update buildrequires

* Wed Jul 26 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 07/26/06 20:08:52 (42240)
Import xdesktopwaves

* Fri Mar 04 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.3-1mdk
- 1.3

* Tue Dec 07 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2-1mdk
- 1.2

* Sat Nov 20 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0-1mdk
- First mdk spec

