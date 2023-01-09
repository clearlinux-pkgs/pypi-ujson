#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ujson
Version  : 5.7.0
Release  : 43
URL      : https://files.pythonhosted.org/packages/43/1a/b0a027144aa5c8f4ea654f4afdd634578b450807bb70b9f8bad00d6f6d3c/ujson-5.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/43/1a/b0a027144aa5c8f4ea654f4afdd634578b450807bb70b9f8bad00d6f6d3c/ujson-5.7.0.tar.gz
Summary  : Ultra fast JSON encoder and decoder for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-ujson-filemap = %{version}-%{release}
Requires: pypi-ujson-lib = %{version}-%{release}
Requires: pypi-ujson-license = %{version}-%{release}
Requires: pypi-ujson-python = %{version}-%{release}
Requires: pypi-ujson-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-scons
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# UltraJSON
[![PyPI version](https://img.shields.io/pypi/v/ujson.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/ujson)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/ujson.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/ujson)
[![PyPI downloads](https://img.shields.io/pypi/dm/ujson.svg)](https://pypistats.org/packages/ujson)
[![GitHub Actions status](https://github.com/ultrajson/ultrajson/workflows/Test/badge.svg)](https://github.com/ultrajson/ultrajson/actions)
[![codecov](https://codecov.io/gh/ultrajson/ultrajson/branch/main/graph/badge.svg)](https://codecov.io/gh/ultrajson/ultrajson)
[![DOI](https://zenodo.org/badge/1418941.svg)](https://zenodo.org/badge/latestdoi/1418941)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

%package filemap
Summary: filemap components for the pypi-ujson package.
Group: Default

%description filemap
filemap components for the pypi-ujson package.


%package lib
Summary: lib components for the pypi-ujson package.
Group: Libraries
Requires: pypi-ujson-license = %{version}-%{release}
Requires: pypi-ujson-filemap = %{version}-%{release}

%description lib
lib components for the pypi-ujson package.


%package license
Summary: license components for the pypi-ujson package.
Group: Default

%description license
license components for the pypi-ujson package.


%package python
Summary: python components for the pypi-ujson package.
Group: Default
Requires: pypi-ujson-python3 = %{version}-%{release}

%description python
python components for the pypi-ujson package.


%package python3
Summary: python3 components for the pypi-ujson package.
Group: Default
Requires: pypi-ujson-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(ujson)

%description python3
python3 components for the pypi-ujson package.


%prep
%setup -q -n ujson-5.7.0
cd %{_builddir}/ujson-5.7.0
pushd ..
cp -a ujson-5.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673283810
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ujson
cp %{_builddir}/ujson-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-ujson/0a8a0c4dd38dfac034078c7f3e0c16ff489d6646 || :
cp %{_builddir}/ujson-%{version}/deps/double-conversion/COPYING %{buildroot}/usr/share/package-licenses/pypi-ujson/8d434c9c1704b544a8b0652efbc323380b67f9bc || :
cp %{_builddir}/ujson-%{version}/deps/double-conversion/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ujson/8d434c9c1704b544a8b0652efbc323380b67f9bc || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-ujson

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ujson/0a8a0c4dd38dfac034078c7f3e0c16ff489d6646
/usr/share/package-licenses/pypi-ujson/8d434c9c1704b544a8b0652efbc323380b67f9bc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
