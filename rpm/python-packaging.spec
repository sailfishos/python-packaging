# Specify --with bootstrap to build in bootstrap mode
# This mode is needed, because python3-rpm-generators need packaging
%bcond_with bootstrap

Name:           python-packaging
Version:        21.3
Release:        1
Summary:        Core utilities for Python packages
License:        BSD-2-Clause OR Apache-2.0
URL:            https://github.com/sailfishos/python-packaging
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with bootstrap}
BuildRequires:  python3-setuptools
%endif

%description
python-packaging provides core utilities for Python packages like utilities for
dealing with versions, specifiers, markers etc.}

%package -n python3-packaging
Summary:        %{summary}

%if %{with bootstrap}
Provides:       python3dist(packaging) = %{version}
Provides:       python%{python3_version}dist(packaging) = %{version}
Requires:       python(abi) = %{python3_version}
%endif

%description -n python3-packaging
python-packaging provides core utilities for Python packages like utilities for
dealing with versions, specifiers, markers etc.}

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires -r
%endif

%build
%if %{with bootstrap}
%py3_build
%else
%pyproject_wheel
%endif

%install
%if %{with bootstrap}
mkdir -p %{buildroot}%{python3_sitelib}
%py3_install
echo '%{python3_sitelib}/packaging*' > %{pyproject_files}
%else
%pyproject_install
%pyproject_save_files packaging
%endif

%files -n python3-packaging -f %{pyproject_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst CHANGELOG.rst CONTRIBUTING.rst
