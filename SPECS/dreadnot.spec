Name:       dreadnot
Version:    0.1.4
Release:    2.2360aa1aa6
Summary:    Dreadnot is a 'one click' deploy tool written in [Node.js](http://www.nodejs.org/).
Requires:   nodejs
Source0:    %{name}-master.zip
Group:      Development/Libraries
License:    Apache License
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Url:        https://github.com/racker/dreadnot

%description
Dreadnot is a 'one click' deploy tool written in [Node.js](http://www.nodejs.org/).

%prep
%setup -n %{name}-master

%install
%{__mkdir_p} %{buildroot}/opt
%{__cp} -rp $RPM_BUILD_DIR/dreadnot-master %{buildroot}/opt/dreadnot

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
/*
%attr(755, root, root) /opt/dreadnot/bin/dreadnot

%changelog
* Tue Aug 5 2014 Jason Thomas <jthomas@mozilla.com> 0.1.4-2.2360aa1aa6
- Initial package
