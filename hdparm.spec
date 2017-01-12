Summary:	A utility for displaying and/or setting hard disk parameters
Name:		hdparm
Version:	9.50
Release:	1
License:	BSD
Group:		System/Kernel and hardware
Url:		http://sourceforge.net/projects/hdparm/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/hdparm/%{name}-%{version}.tar.gz

# derived from debian
Source10:	hdparm.conf
Source11:	hdparm.conf.5
Source12:	hdparm-functions
Source13:	hdparm.udev
Source14:	hdparm-udev-scripts
Source15:	hdparm-systemd-sleep
Source16:	95hdparm-apm

Patch0:		hdparm-9.49-increase-readahead-max-value-to-1048576.patch
Patch1:		hdparm-9.43-ditch_dead_code.patch
Patch2:		hdparm-9.43-close_fd.patch
Patch3:		hdparm-9.43-get_geom.patch

%description
Hdparm is a useful system utility for setting (E)IDE hard drive parameters. For
example, hdparm can be used to tweak hard drive performance and to spin down
hard drives for power conservation.

%prep
%setup -q
%patch0 -p1 -b .setra~
%patch1 -p1 -b .dead_code~
%patch2 -p1 -b .fd~
%patch3 -p1 -b .geom~

%build
%serverbuild
make CC=%{__cc} CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" STRIP=/bin/true

%install
%makeinstall_std

install -m644 hdparm.8 -D %{buildroot}%{_mandir}/man8/hdparm.8

install -m755 %{SOURCE10} -D %{buildroot}%{_sysconfdir}/hdparm.conf
install -m755 %{SOURCE11} -D %{buildroot}%{_mandir}/man5/hdparm.conf.5

install -m755 %{SOURCE12} -D %{buildroot}%{_libexecdir}/hdparm-functions

install -m755 %{SOURCE13} -D %{buildroot}/lib/udev/rules.d/95-hdparm.rules
install -m755 %{SOURCE14} -D %{buildroot}/lib/udev/hdparm
install -m755 %{SOURCE15} -D %{buildroot}/lib/systemd/system-sleep/hdparm

%files
%doc hdparm.lsm Changelog README.acoustic
%config(noreplace) %{_sysconfdir}/hdparm.conf
/sbin/hdparm
%{_mandir}/man5/hdparm.conf.5*
%{_mandir}/man8/hdparm.8*
%{_libexecdir}/hdparm-functions
/lib/udev/rules.d/95-hdparm.rules
/lib/udev/hdparm
/lib/systemd/system-sleep/hdparm
