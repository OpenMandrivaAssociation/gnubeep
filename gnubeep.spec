%define name gnubeep
%define version 1.4
%define release %mkrel 6

Summary: Produce sound trough the speaker
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://www.nettwerked.co.uk/code/gnubeep/index.html
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

