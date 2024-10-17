%define name gnubeep
%define version 1.4
%define release 9

Summary: Produce sound trough the speaker
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: https://www.nettwerked.co.uk/code/gnubeep/index.html
BuildRoot: %{_tmppath}/%{name}-buildroot
ExclusiveArch: x86_64 %{ix86}

%description
gnubeep is a simple program written in C to generate `beeps`
by programming the system's internal PIT (programmable interrupt
timer) directly via the I/O ports. I have so many times needed to
generate custom tones in shell scripts and programs, and when '\a'
doesn't suffice, this can be a problem which requires overcoming.
For this reason, I decided to write gnubeep.
 
One of the prime reasons I saw fit to release this piece of software
was to serve as an example of how to program the PIT for sound in Linux. 

%prep
%setup -q

%build

gcc $RPM_OPT_FLAGS -o gnubeep gnubeep.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
install -m 755 gnubeep %buildroot%_bindir/gnubeep

install -m 644 %name.1 %buildroot%_mandir/man1/%name.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BUGS INSTALL LICENSE README
%_bindir/gnubeep
%_mandir/man1/%name.1*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-8mdv2011.0
+ Revision: 619197
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4-7mdv2010.0
+ Revision: 429265
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.4-6mdv2009.0
+ Revision: 246482
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4-4mdv2008.1
+ Revision: 136454
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 21:04:59 (53667)
- rebuild

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 21:01:05 (53666)
Import gnubeep

* Sun Apr 30 2006 Emmanuel Blindauer <blindauer@mandriva.org> 1.4-3mdk
- fix ExclusiveArch

* Fri May 13 2005 Olivier Thauvin <nanardon@mandriva.org> 1.4-2mdk
- birthday rebuild

* Thu Apr 15 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.4-1mdk
- 1.4

* Fri Apr 09 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.3-1mdk
- 1.3

* Tue Mar 30 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2-1mdk
- 1.2

* Sat Jan 24 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.8-1mdk
- 0.8

* Wed Jan 07 2004 Olivier Thauvin <nanardon@klama.mandrake.org> 0.6patch-1mdk
- 0.6
- remove patch1, merge upstream

* Tue Jan 06 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.5-1mdk
- 1st mdk spec

