%bcond_without	uclibc

Summary:	A utility for displaying and/or setting hard disk parameters
Name:		hdparm
Version:	9.43
Release:	12
License:	BSD
Group:		System/Kernel and hardware
Url:		http://sourceforge.net/projects/hdparm/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/hdparm/%name-%version.tar.gz
Source1:	hdparm-sysconfig
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif

%description
Hdparm is a useful system utility for setting (E)IDE hard drive parameters. For
example, hdparm can be used to tweak hard drive performance and to spin down
hard drives for power conservation.

%package -n	uclibc-%{name}
Summary:	A utility for displaying and/or setting hard disk parameters (uClibc build)
Group:		System/Kernel and hardware

%description -n	uclibc-%{name}
Hdparm is a useful system utility for setting (E)IDE hard drive parameters. For
example, hdparm can be used to tweak hard drive performance and to spin down
hard drives for power conservation.

%prep
%setup -q
mkdir .uclibc
cp -a * .uclibc

%build
%serverbuild
%if %{with uclibc}
%make -C .uclibc CC=%{uclibc_cc} CFLAGS="%{uclibc_cflags}" LDFLAGS="%{ldflags}" STRIP=/bin/true
%endif
%make CC=%{__cc} CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" STRIP=/bin/true



%install
%makeinstall_std
%if %{with uclibc}
%makeinstall_std -C .uclibc sbindir=%{uclibc_root}/sbin
%endif
install -m0644 hdparm.8 -D %{buildroot}%{_mandir}/man8/hdparm.8
install -m0644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/sysconfig/harddisks

%files
%doc hdparm.lsm Changelog README.acoustic
%config(noreplace) %{_sysconfdir}/sysconfig/harddisks
/sbin/hdparm
%{_mandir}/man8/hdparm.8*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}/sbin/hdparm
%endif
