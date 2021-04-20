%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?dlrn}
%global upstream_name ansible-collections-openstack.cloud
%else
%global upstream_name ansible-collections-openstack
%endif

Name:           ansible-collections-openstack
Version:        1.3.0
Release:        2%{?dist}
Summary:        Openstack Ansible collections
License:        GPLv3+ and BSD
URL:            https://opendev.org/openstack/ansible-collections-openstack
Source0:        https://github.com/openstack/%{name}/archive/%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python3-pbr
BuildRequires:  python3-devel

Requires:       ansible >= 2.8.0
Requires:       python3-openstacksdk >= 0.13.0

%description
Openstack Ansible collections

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
%py3_build

%install
%py3_install

%files

%doc README.md
%license COPYING
%{python3_sitelib}/ansible_collections_openstack.cloud-*.egg-info
%{_datadir}/ansible/collections/ansible_collections/openstack/

%changelog
* Thu Apr 08 2021 Sagi Shnaidman <sshnaidm@redhat.com> 1.3.0-2
- RPM package fixes

* Mon Apr 05 2021 Sagi Shnaidman <sshnaidm@redhat.com> 1.3.0-1
- Initial package


