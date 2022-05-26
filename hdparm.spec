Summary:	A utility for displaying and/or setting hard disk parameters
Name:		hdparm
Version:	9.63
Release:	2
License:	BSD
Group:		System/Kernel and hardware
Url:		http://sourceforge.net/projects/hdparm/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/hdparm/%{name}-%{version}.tar.gz
Patch0:		hdparm-9.49-increase-readahead-max-value-to-1048576.patch
Patch2:		hdparm-9.43-close_fd.patch
Patch3:		hdparm-9.43-get_geom.patch
Provides:	/sbin/hdparm

%description
Hdparm is a useful system utility for setting (E)IDE hard drive parameters. For
example, hdparm can be used to tweak hard drive performance and to spin down
hard drives for power conservation.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build binprefix=%{_prefix} CC=%{__cc} CFLAGS="%{optflags} -Oz" LDFLAGS="%{build_ldflags}" STRIP=/bin/true

%install
%make_install binprefix=%{_prefix}
install -m644 hdparm.8 -D %{buildroot}%{_mandir}/man8/hdparm.8
install -m644 debian/hdparm.conf -D %{buildroot}%{_sysconfdir}/hdparm.conf
install -m644 debian/hdparm.conf.5 -D %{buildroot}%{_mandir}/man5/hdparm.conf.5

%files
%doc hdparm.lsm Changelog README.acoustic
%config(noreplace) %{_sysconfdir}/hdparm.conf
%{_sbindir}/hdparm
%doc %{_mandir}/man5/hdparm.conf.5*
%doc %{_mandir}/man8/hdparm.8*
