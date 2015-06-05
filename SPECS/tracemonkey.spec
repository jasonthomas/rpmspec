Name: tracemonkey
Version:  40.0a2
Release:  1%{?dist}
Summary:  SpiderMonkey is Mozilla's JavaScript engine written in C/C++
Group: Development/Tools
License: MPL2
URL: https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey
Source0: https://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-aurora/jsshell-linux-x86_64.zip
Requires: nspr

%description
SpiderMonkey is Mozilla's JavaScript engine written in C/C++. It is used in various Mozilla products, including Firefox, and is available under the MPL2.

%prep
rm -rf %{name}-%{version}
%{__mkdir} %{name}-%{version}
unzip %{SOURCE0} -d %{name}-%{version}

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{_bindir}
%{__install} -m 755 js %{buildroot}/%{_bindir}/tracemonkey

%files
%{_bindir}/*

%changelog
* Fri Jun 5 2015 Jason Thomas <jthomas@mozila.com> 40.0a2-1
- New upstream version
