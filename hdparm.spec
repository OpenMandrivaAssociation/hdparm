Summary:	A utility for displaying and/or setting hard disk parameters
Name:		hdparm
Version:	9.43
Release:	2
License:	BSD
Group:		System/Kernel and hardware
URL:		http://sourceforge.net/projects/hdparm/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/hdparm/%name-%version.tar.gz
Source1:	hdparm-sysconfig

%description
Hdparm is a useful system utility for setting (E)IDE hard drive parameters. For
example, hdparm can be used to tweak hard drive performance and to spin down
hard drives for power conservation.

%prep
%setup -q

%build
%serverbuild
%make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="%{ldflags}" STRIP=/bin/true

%install
%makeinstall_std
install -m0644 hdparm.8 -D %{buildroot}%{_mandir}/man8/hdparm.8
install -m0644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/sysconfig/harddisks

%files
%doc hdparm.lsm Changelog README.acoustic
%config(noreplace) %{_sysconfdir}/sysconfig/harddisks
/sbin/hdparm
%{_mandir}/man8/hdparm.8*
