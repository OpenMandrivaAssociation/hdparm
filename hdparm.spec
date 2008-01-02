%define	name	hdparm
%define version 7.7
%define	rel	1
%define release %mkrel %{rel}

Summary:	A utility for displaying and/or setting hard disk parameters
Name:		hdparm
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		System/Kernel and hardware
URL:		http://sourceforge.net/projects/hdparm/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/hdparm/%name-%version.tar.bz2
Source1:	hdparm-sysconfig
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Hdparm is a useful system utility for setting (E)IDE hard drive
parameters.  For example, hdparm can be used to tweak hard drive
performance and to spin down hard drives for power conservation.

%prep
%setup -q

%build
perl -pi -e "s/-O2/$RPM_OPT_FLAGS/" Makefile
make clean
%make

%install
rm -fr $RPM_BUILD_ROOT
install -m0755 hdparm -D $RPM_BUILD_ROOT/sbin/hdparm
install -m0644 hdparm.8 -D $RPM_BUILD_ROOT%{_mandir}/man8/hdparm.8
install -m0644 %{SOURCE1} -D $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/harddisks

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc hdparm.lsm Changelog README.acoustic
/sbin/hdparm
%{_mandir}/man8/hdparm.8*
%config(noreplace) %{_sysconfdir}/sysconfig/harddisks
