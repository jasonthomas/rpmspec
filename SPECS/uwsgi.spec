Name:           uwsgi
Version:        2.0.8
Release:        1
Summary:        Fast, self-healing, application container server
Group:          System Environment/Daemons
License:        GPLv2
URL:            http://projects.unbit.it/uwsgi
Source0:        http://projects.unbit.it/downloads/%{name}-%{version}.tar.gz
Patch0:         uwsgi_trick_chroot_rpmbuild.patch
Patch1:         uwsgi_fix_rpath.patch
BuildRequires:  python2-devel, libxml2-devel, libuuid-devel, ruby, ruby-devel
BuildRequires:  libyaml-devel, perl-devel, pcre-devel, perl-ExtUtils-Embed

%description
uWSGI is a fast (pure C), self-healing, developer/sysadmin-friendly
application container server.  Born as a WSGI-only server, over time it has
evolved in a complete stack for networked/clustered web applications,
implementing message/object passing, caching, RPC and process management.
It uses the uwsgi (all lowercase, already included by default in the Nginx
and Cherokee releases) protocol for all the networking/interprocess
communications.  Can be run in preforking mode, threaded,
asynchronous/evented and supports various form of green threads/co-routine
(like uGreen and Fiber).  Sysadmin will love it as it can be configured via
command line, environment variables, xml, .ini and yaml files and via LDAP.
Being fully modular can use tons of different technology on top of the same
core.

%package -n %{name}-devel
Summary:  uWSGI - Development header files and libraries
Group:    Development/Libraries
Requires: %{name}

%description -n %{name}-devel
This package contains the development header files and libraries
for uWSGI extensions

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="%{optflags}" python uwsgiconfig.py --build

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
%{__install} -p -m 0755 uwsgi %{buildroot}%{_sbindir}
%{__install} -p -m 0644 *.h %{buildroot}%{_includedir}/%{name}

%pre
getent group uwsgi >/dev/null || groupadd -r uwsgi
getent passwd uwsgi >/dev/null || \
    useradd -r -g uwsgi -d '/etc/uwsgi' -s /sbin/nologin \
    -c "uWSGI Service User" uwsgi


%files
%defattr(-,root,root)
%{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}
%doc LICENSE README
%attr(0755,uwsgi,uwsgi) %{_localstatedir}/log/%{name}
%attr(0755,uwsgi,uwsgi) %{_localstatedir}/run/%{name}

%files -n %{name}-devel
%{_includedir}/%{name}

%changelog
* Thu Oct 09 2014 Jason Thomas <jthomas@mozilla.com> - 2.0.7-1
- Upgraded to latest stable upstream version

* Sat Sep 06 2014 Alan Chalmers <alan.chalmers@gmail.com> - 2.0.7
- Upgraded to latest stable upstream version

* Thu Jun 19 2014 Aleks Bunin <sbunin@gmail.com> - 2.0.5.1-2
- Restored cgi plugin

* Tue Jun 03 2014 Sergey Morozov <sergey.morozov@corp.mail.ru> - 2.0.5.1-1
- Build now inherits "base" buildconf with only python, rack and psgi plugins
- Removed wiki doc
- Upgraded to latest stable upstream version

* Thu Apr 19 2012 Aleks Bunin <sbunin@gmail.com> - 1.1.2-1
- RHEL 6 Support (removed not compatible plugins)
- Upgraded to latest stable upstream version

* Sun Feb 19 2012 Jorge A Gallegos <kad@blegh.net> - 1.0.4-1
- Addressing issues from package review feedback
- s/python-devel/python2-devel
- Make the libdir subdir owned by -plugins-common
- Upgraded to latest stable upstream version

* Mon Feb 06 2012 Jorge A Gallegos <kad@blegh.net> - 1.0.2.1-2
- Fixing 'unstripped-binary-or-object'

* Thu Jan 19 2012 Jorge A Gallegos <kad@blegh.net> - 1.0.2.1-1
- New upstream version

* Thu Dec 08 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.9.3-1
- New upstream version

* Sun Oct 09 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.9.2-2
- Don't download the wiki page at build time

* Sun Oct 09 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.9.2-1
- Updated to latest stable version
- Correctly linking plugin_dir
- Patches 1 and 2 were addressed upstream

* Sun Aug 21 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.8.3-3
- Got rid of BuildRoot
- Got rid of defattr()

* Sun Aug 14 2011 Jorge Gallegos <kad@blegh.net> - 0.9.8.3-2
- Added uwsgi_fix_rpath.patch
- Backported json_loads patch to work with jansson 1.x and 2.x
- Deleted clean steps since they are not needed in fedora

* Sun Jul 24 2011 Jorge Gallegos <kad@blegh.net> - 0.9.8.3-1
- rebuilt
- Upgraded to latest stable version 0.9.8.3
- Split packages

* Sun Jul 17 2011 Jorge Gallegos <kad@blegh.net> - 0.9.6.8-2
- Heavily modified based on Oskari's work

* Mon Feb 28 2011 Oskari Saarenmaa <os@taisia.fi> - 0.9.6.8-1
- Initial.
