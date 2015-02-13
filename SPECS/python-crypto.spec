%{?scl:%scl_package python-crypto}
%{!?scl:%global pkg_name %{name}}
%{?el5:%define _without_egg_info 1}
%{?el4:%define _without_egg_info 1}
%{?el3:%define _without_egg_info 1}
%{?el2:%define _without_egg_info 1}

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pycrypto

Summary: Collection of cryptographic algorithms and protocols for python
Name: %{?scl_prefix}python-crypto
Version: 2.6.1
Release: 2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: https://www.dlitz.net/software/pycrypto/
Source: http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
BuildRequires: python >= 2.2
Requires: python >= 2.2
Obsoletes: pycrypto <= %{version}
Provides: pycrypto <= %{version}

%description
pycrypto is a collection of cryptographic algorithms and protocols,
implemented for use from Python. Among the contents of the package:

    * Hash functions: MD2, MD4, RIPEMD.
    * Block encryption algorithms: AES, ARC2, Blowfish, CAST, DES, Triple-DES, IDEA, RC5.
    * Stream encryption algorithms: ARC4, simple XOR.
    * Public-key algorithms: RSA, DSA, ElGamal, qNEW.
    * Protocols: All-or-nothing transforms, chaffing/winnowing.
    * Miscellaneous: RFC1751 module for converting 128-key keys into a set of English words, primality testing.

%prep
%setup -n %{real_name}-%{version}

%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}

%install
%{__rm} -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{?scl:"}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKS ChangeLog README TODO LEGAL/
%{_libdir}/python?.?/site-packages/Crypto
%{!?_without_egg_info:%{_libdir}/python?.?/site-packages/pycrypto-%{version}-py*.egg-info}

%changelog
* Fri Feb 13 2015 Jason Thomas <jthomas@mozilla.com> - 2.6.1-2
- Add scl support.

* Tue Jun 17 2014 Dag Wieers <dag@wieers.com> - 2.6.1-1
- Updated to release 2.6.1.

* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Updated to release 2.0.1.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 1.9-0.a6
- Initial package. (using DAR)
