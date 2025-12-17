Name:		python-twine
Version:	6.1.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/t/twine/twine-%{version}.tar.gz
Summary:	Twine is a utility for publishing Python packages on PyPI
URL:		https://pypi.org/project/twine/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python-readme_renderer
BuildRequires:	python-id
BuildSystem:	python
BuildArch:	noarch

%description
%sumamry

%files
%{_bindir}/twine
%{py_sitedir}/twine
%{py_sitedir}/twine-*.*-info
