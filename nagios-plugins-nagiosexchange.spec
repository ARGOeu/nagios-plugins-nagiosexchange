%define dir /usr/libexec/argo-monitoring/probes/nagiosexchange

Summary: Nagios probes from Nagios Exchange.
Name: nagios-plugins-nagiosexchange
Version: 1.0.0
Release: 1%{?dist}
License: ASL 2.0
Group: Network/Monitoring
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{dir}
install --mode 755 src/*  ${RPM_BUILD_ROOT}%{dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{dir}

%changelog
* Tue Oct 03 2017 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-1%{?dist}
- Initial version
