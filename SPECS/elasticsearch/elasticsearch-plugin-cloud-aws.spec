%define debug_package %{nil}
%define base_install_dir %{_datadir}/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-cloud-aws
Version:        2.6.0
Release:        1%{?dist}
Summary:        AWS Cloud Plugin for ElasticSearch
Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/elasticsearch/elasticsearch-cloud-aws
Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-cloud-aws/elasticsearch-cloud-aws-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 1.6.0

%description
The Amazon Web Service (AWS) Cloud plugin allows to use AWS API for the unicast discovery mechanism and add S3 repositories.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/cloud-aws

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins
%{__install} -D -m 755 plugins/cloud-aws/elasticsearch-cloud-aws-%{version}.jar %{buildroot}/%{base_install_dir}/plugins/cloud-aws/elasticsearch-cloud-aws.jar
%{__install} -m 755 plugins/cloud-aws/*.jar -t %{buildroot}/%{base_install_dir}/plugins/cloud-aws

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/cloud-aws
%{base_install_dir}/plugins/cloud-aws/*

%changelog

* Mon Aug 3 2015 Jason Thomas jthomas@mozila.com 2.6.0-1
- Initial package
