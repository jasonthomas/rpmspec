%define debug_package %{nil}
%define base_install_dir %{_datadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-analysis-stempel
Version:        2.4.3
Release:        1%{?dist}
Summary:        ElasticSearch plugin for Lucene Stempel (Polish) Analysis
Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-analysis-stempel
Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-analysis-stempel/elasticsearch-analysis-stempel-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 1.4.5

%description
The Stempel (Polish) Analysis plugin integrates Lucene stempel (polish) analysis module into elasticsearch.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/analysis-stempel

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/analysis-stempel/elasticsearch-analysis-stempel-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/analysis-stempel/elasticsearch-analysis-stempel.jar
%{__install} -m 755 plugins/analysis-stempel/lucene-*.jar -t %{buildroot}/%{base_install_dir}/plugins/analysis-stempel

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/analysis-stempel
%{base_install_dir}/plugins/analysis-stempel/*

%changelog
* Thu Jul 22 2015 Jason Thomas <jthomas@mozila.com> 2.4.3-1
- New upstream version

* Tue Jan 7 2015 Jason Thomas <jthomas@mozila.com> 2.3.0-1
- Initial package.
