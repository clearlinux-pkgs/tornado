#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tornado
Version  : 4.5.3
Release  : 41
URL      : https://pypi.debian.net/tornado/tornado-4.5.3.tar.gz
Source0  : https://pypi.debian.net/tornado/tornado-4.5.3.tar.gz
Summary  : Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.
Group    : Development/Tools
License  : Apache-2.0
Requires: tornado-python3
Requires: tornado-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
==================

%package python
Summary: python components for the tornado package.
Group: Default
Requires: tornado-python3

%description python
python components for the tornado package.


%package python3
Summary: python3 components for the tornado package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tornado package.


%prep
%setup -q -n tornado-4.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523309381
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
