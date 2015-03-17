%{?scl:%scl_package python-cryptography}
%{!?scl:%global pkg_name %{name}}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Name: %{?scl_prefix}python-cryptography
Version: 0.8
Release: 1%{?dist}
Source0: http://pypi.python.org/packages/source/p/cryptography/cryptography-%{version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Url: https://github.com/pyca/cryptography
BuildRequires: libffi-devel, python-devel, openssl-devel

%description
cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Our goal is for it to be your “cryptographic standard library”. It supports Python 2.6-2.7, Python 3.2+, and PyPy.

%prep
%setup -qn cryptography-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{?scl:"}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/python?.?/site-packages/

%changelog
* Tue Mar 17 2015 Jason Thomas <jthomas@mozilla.com> - 0.8-1
- Initial package.
