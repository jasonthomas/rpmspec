%{?nodejs_find_provides_and_requires}

Name:       npm
Version:    1.4.28
Release:    1
Summary:    Node.js Package Manager
License:    Artistic 2.0
Group:      Development/Tools
URL:        http://npmjs.org/
Source0:    http://registry.npmjs.org/npm/-/npm-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires: nodejs-devel

%description
npm is a package manager for node.js. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.

%prep
%setup -q

%nodejs_fixdep ansi 0.2
%nodejs_fixdep semver 2.1
%nodejs_fixdep cmd-shim 1.1
%nodejs_fixdep request '>2.16 <3'

#remove bundled modules
rm -rf node_modules

# delete windows stuff
rm bin/npm.cmd bin/node-gyp-bin/node-gyp.cmd

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/npm
cp -pr bin lib cli.js package.json %{buildroot}%{nodejs_sitelib}/npm/

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/npm/bin/npm-cli.js %{buildroot}%{_bindir}/npm

# ghosted global config files
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/npmrc
touch %{buildroot}%{_sysconfdir}/npmignore

# install to mandir
ln -sf %{_defaultdocdir}/%{name}-%{version} %{buildroot}%{nodejs_sitelib}/npm/doc
ln -sf %{_defaultdocdir}/%{name}-%{version}/html %{buildroot}%{nodejs_sitelib}/npm/html

%nodejs_symlink_deps

# probably needs network, need to investigate further
#%%check
#%%__nodejs test/run.js
#%%tap test/tap/*.js

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/npm
%ghost %{_sysconfdir}/npmrc
%ghost %{_sysconfdir}/npmignore
%{_bindir}/npm
%doc AUTHORS doc html README.md LICENSE

%changelog
* Mon Oct 20 2014 Jason Thomas <jthomas@mozilla.com> - 1.4.28-1
- Update to latest release.

* Mon Apr 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.6-5
- backport fix for traceback encountered when using "npm search" (RHBZ#1087065)

* Thu Aug 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.6-4
- remove unnecessary symlink to mandir
  fixes upgrade path from certain older versions of npm

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.6-2
- license changed from MITNFA to Artistic 2.0

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.6-1
- new upstream release 1.3.6

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.3-1
- new upstream release 1.3.3
- fixes insecure temporary directory generation (CVE-2013-4116; RHBZ#983917)

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.0-1
- new upstream release 1.3.0
- use system paths for manual pages and documentation (RHBZ#953051)

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.17-6
- restrict to compatible arches

* Wed Apr 17 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.17-5
- Fix manpage names so that npm help finds them

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.17-4
- add EPEL dependency generation macro

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.17-3
- rebuilt

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.17-2
- revert a change that adds a dep (that only affects Windows anyway)
- fix bogus date in changelog warning

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.17-1
- new upstream release 1.2.17

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.14-2
- fix dependencies

* Mon Mar 11 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.2.14-1
- New upstream release 1.2.14
- Bring npm up to the latest to match the Node.js 0.10.0 release

* Wed Feb 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.10-2
- fix dep for updated read-package-json

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.10-1
- new upstream release 1.2.10

* Sat Jan 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.1-2
- fix rpmlint warnings

* Fri Jan 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.1-1
- new upstream release 1.2.1
- fix License tag

* Thu Jan 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-1
- new upstream release 1.2.0

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.70-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.70-1
- new upstream release 1.1.70

* Wed May 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.19-1
- New upstream release 1.1.19

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.18-1
- New upstream release 1.1.18

* Fri Apr 06 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.16-1
- New upstream release 1.1.16

* Mon Apr 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.15-1
- New upstream release 1.1.15

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.14-1
- New upstream release 1.1.14

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.13-2
- new dependencies fstream-npm, uid-number, and fstream-ignore (indirectly)

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.13-1
- new upstream release 1.1.13

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.12-1
- new upstream release 1.1.12

* Thu Mar 15 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.9-1
- new upstream release 1.1.9

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-1
- new upstream release 1.1.4

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.2-1
- new upstream release 1.1.2

* Sat Feb 11 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-2
- fix node_modules symlink

* Thu Feb 09 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-1
- new upstream release 1.1.1

* Sun Jan 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2.3
- new upstream release 1.1.0-3

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2.2
- missing Group field for EL5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-1.2
- new upstream release 1.1.0-2

* Thu Nov 17 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.106-1
- new upstream release 1.0.106
- ship manpages again

* Thu Nov 10 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.105-1
- new upstream release 1.0.105
- use relative symlinks instead of absolute
- fixes /usr/bin/npm symlink on i686

* Mon Nov 07 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.104-1
- new upstream release 1.0.104
- adds node 0.6 support

* Wed Oct 26 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.101-2
- missing Requires on nodejs-request
- Require compilers too so native modules build properly

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.101-1
- new upstream release
- use symlink /usr/lib/node_modules -> /usr/lib/nodejs instead of patching

* Thu Aug 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.26-2
- rebuilt with fixed nodejs_fixshebang macro from nodejs-devel-0.4.11-3

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.26-1
- initial package
