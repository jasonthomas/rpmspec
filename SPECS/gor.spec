Name:       gor
Version:    0.14.1
Release:    1
Summary:    Goreplay
Source0:    https://github.com/buger/gor/releases/download/v%{version}/%{name}_v%{version}_x64.tar.gz
Group:      Applications/Engineering
License:    LGPL
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Url:        https://github.com/buger/gor

%description

Gor is an open-source tool for capturing and replaying live HTTP traffic into a test environment in order to continuously test your system with real data. It can be used to increase confidence in code deployments, configuration changes and infrastructure changes.

Now you can test your code on real user sessions in an automated and repeatable fashion. No more falling down in production!

%prep
%setup -qc -n gor

%install
%{__mkdir_p} %{buildroot}/opt
%{__cp} -rp $RPM_BUILD_DIR/gor %{buildroot}/opt/gor

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
/*
%attr(755, root, root) /opt/gor/gor

%changelog
* Mon Aug 1 2016 Jason Thomas <jthomas@mozilla.com> 0.14.1
- Initial package
