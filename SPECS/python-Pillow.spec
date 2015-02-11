%{?scl:%scl_package python-Pillow}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}python-Pillow
Version:        2.3.0
Release:        1%{?dist}
Summary:        Python Imaging Library (Fork)
Group:          Development/Languages
License:        Standard PIL License
URL:            http://pypi.python.org/pypi/Pillow
Source0:        http://pypi.python.org/packages/source/v/Pillow/Pillow-%{version}.zip
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Pillow is the “friendly” PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

%prep
%setup -q -n Pillow-%{version}

%build
# Build code
%{?scl:scl enable %{scl} "}
python setup.py build
%{?scl:"}

%install
rm -rf $RPM_BUILD_ROOT
%{?scl:scl enable %{scl} "}
python setup.py install --skip-build --root $RPM_BUILD_ROOT
%{?scl:"}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc docs/*rst PKG-INFO
%{_libdir}/python?.?/site-packages/
%{_bindir}/*

%changelog
* Wed Feb 11 2015 Jason Thomas <jthomas@mozilla.com> - 2.3.0-1
- Initial build.
