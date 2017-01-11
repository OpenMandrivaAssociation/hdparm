Summary:	A utility for displaying and/or setting hard disk parameters
Name:		hdparm
Version:	9.50
Release:	1
License:	BSD
Group:		System/Kernel and hardware
Url:		http://sourceforge.net/projects/hdparm/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/hdparm/%name-%version.tar.gz
Source1:	hdparm-sysconfig
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

install -m0644 hdparm.8 -D %{buildroot}%{_mandir}/man8/hdparm.8
install -m0644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/sysconfig/harddisks

%files
%doc hdparm.lsm Changelog README.acoustic
%config(noreplace) %{_sysconfdir}/sysconfig/harddisks
/sbin/hdparm
%{_mandir}/man8/hdparm.8*
