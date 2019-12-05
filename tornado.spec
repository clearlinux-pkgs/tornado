#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tornado
Version  : 6.0.3
Release  : 57
URL      : https://files.pythonhosted.org/packages/30/78/2d2823598496127b21423baffaa186b668f73cd91887fcef78b6eade136b/tornado-6.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/30/78/2d2823598496127b21423baffaa186b668f73cd91887fcef78b6eade136b/tornado-6.0.3.tar.gz
Summary  : Clone of a C64 game, the goal is to destroy the opponent's house with certain weather phenomena
Group    : Development/Tools
License  : Apache-2.0
Requires: tornado-license = %{version}-%{release}
Requires: tornado-python = %{version}-%{release}
Requires: tornado-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Running the Tornado Facebook example
====================================
To run this example, you must register a Facebook application with a
Connect URL set to the domain the this demo will be running on
(i.e. http://localhost:8888/ by default).  The API key and secret
for this application must be passed on the command line:

%package license
Summary: license components for the tornado package.
Group: Default

%description license
license components for the tornado package.


%package python
Summary: python components for the tornado package.
Group: Default
Requires: tornado-python3 = %{version}-%{release}

%description python
python components for the tornado package.


%package python3
Summary: python3 components for the tornado package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tornado package.


%prep
%setup -q -n tornado-6.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561363981
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tornado
cp LICENSE %{buildroot}/usr/share/package-licenses/tornado/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tornado/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
