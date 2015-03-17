%define name python-PyJWT
%define pythonname PyJWT-mozilla
%define version 0.1.4.2
%define unmangled_version 0.1.4.2
%define release 1

%define __os_install_post\
%( rpm --eval %%__os_install_post)\
( cd $RPM_BUILD_ROOT; find . -type f | sed -e 's/^.//') > INSTALLED_FILES
Summary: JSON Web Token implementation in Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{pythonname}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Url: https://github.com/rtilder/pyjwt

%description
A Python implementation of JSON Web Token draft 01.

This is Mozilla's fork of PyJWT which adds RSA algorithms, fixes some timing attacks, and makes a few other adjustments. It is used in projects such as webpay.

%prep
%setup -n %{pythonname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(0644,root,root,0755)

%changelog
* Fri Jul 25 2014 Jason Thomas <jthomas@mozilla.com> 0.1.4.2
- Initial package
