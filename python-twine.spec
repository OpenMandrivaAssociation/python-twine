Name:		python-twine
Version:	7.0.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/t/twine/twine-%{version}.tar.gz
Summary:	Twine is a utility for publishing Python packages on PyPI
URL:		https://pypi.org/project/twine/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%description
Collection of utilities for publishing packages on PyPI.

%files
%{_bindir}/twine
%{py_sitedir}/twine
%{py_sitedir}/twine-*.*-info
