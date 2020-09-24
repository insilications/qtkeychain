#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtkeychain
Version  : 0.9.1
Release  : 4
URL      : https://github.com/frankosterfeld/qtkeychain/archive/v0.9.1.tar.gz
Source0  : https://github.com/frankosterfeld/qtkeychain/archive/v0.9.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: qtkeychain-data = %{version}-%{release}
Requires: qtkeychain-lib = %{version}-%{release}
Requires: qtkeychain-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : qttools-dev

%description
QtKeychain
==========
QtKeychain is a Qt API to store passwords and other secret data securely. How the data is stored depends on the platform:

%package data
Summary: data components for the qtkeychain package.
Group: Data

%description data
data components for the qtkeychain package.


%package dev
Summary: dev components for the qtkeychain package.
Group: Development
Requires: qtkeychain-lib = %{version}-%{release}
Requires: qtkeychain-data = %{version}-%{release}
Provides: qtkeychain-devel = %{version}-%{release}

%description dev
dev components for the qtkeychain package.


%package lib
Summary: lib components for the qtkeychain package.
Group: Libraries
Requires: qtkeychain-data = %{version}-%{release}
Requires: qtkeychain-license = %{version}-%{release}

%description lib
lib components for the qtkeychain package.


%package license
Summary: license components for the qtkeychain package.
Group: Default

%description license
license components for the qtkeychain package.


%prep
%setup -q -n qtkeychain-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545360918
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1545360918
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtkeychain
cp COPYING %{buildroot}/usr/share/package-licenses/qtkeychain/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qt5/translations/qtkeychain_de.qm
/usr/share/qt5/translations/qtkeychain_ro.qm

%files dev
%defattr(-,root,root,-)
/usr/include/qt5keychain/keychain.h
/usr/include/qt5keychain/qkeychain_export.h
/usr/lib64/cmake/Qt5Keychain/Qt5KeychainConfig.cmake
/usr/lib64/cmake/Qt5Keychain/Qt5KeychainConfigVersion.cmake
/usr/lib64/cmake/Qt5Keychain/Qt5KeychainLibraryDepends-relwithdebinfo.cmake
/usr/lib64/cmake/Qt5Keychain/Qt5KeychainLibraryDepends.cmake
/usr/lib64/libqt5keychain.so
/usr/lib64/qt5/mkspecs/modules/qt_Qt5Keychain.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqt5keychain.so.0.9.1
/usr/lib64/libqt5keychain.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtkeychain/COPYING
