Name:           calamares
Version:        0
Release:        0
License:        GPL-3.0
Group:          System/Base
Summary:        Distribution-independent installer framework
URL:            https://calamares.io
Source0:        %{name}-%{version}.tar.gz
Patch0:         calamares-xdg-su.patch

# Main
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(python3)
BuildRequires:  libboost_python3-devel
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  libqt5-linguist-devel
Requires:       dmidecode
Requires:       xdg-utils
Requires:       calamares-branding = %{version}

# Welcome module
Requires:       upower
Requires:       NetworkManager

# Partition module
BuildRequires:  extra-cmake-modules
BuildRequires:  kcoreaddons-devel
BuildRequires:  kconfig-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kservice-devel
BuildRequires:  kpmcore-devel
BuildRequires:  pkgconfig(libparted)
BuildRequires:  pkgconfig(libatasmart)
BuildRequires:  kparts-devel

# Webview module
BuildRequires:  pkgconfig(Qt5WebEngine)

# Bootloader module
Requires:       grub2

# Unpackfs module
Requires:       rsync
Requires:       squashfs

%description
Calamares is an installer framework. By design it is very customizable,
in order to satisfy a wide variety of needs and use cases.

%define library_name libcalamares

%package -n %library_name
Summary:        Shared library for %{name}
License:        GPL-3.0
Group:          System/Libraries

%description -n %library_name
Calamares is an installer framework. By design it is very customizable,
in order to satisfy a wide variety of needs and use cases.

This package holds the shared library for %{name}.

%package devel
Requires:       %{library_name} = %{version}
Summary:        Development files for %{name}
License:        GPL-3.0
Group:          Development/Libraries/C and C++

%description devel
Calamares is an installer framework. By design it is very customizable,
in order to satisfy a wide variety of needs and use cases.

This package holds the development files for %{name}.

%package branding-upstream
Summary:        Upstream branding for Calamares installer
Group:          System/Base
Provides:       calamares-branding = %{version}
Supplements:    packageand(calamares:branding-upstream)
Conflicts:      otherproviders(calamares-branding)
Requires:       calamares = %{version}

%description branding-upstream
Calamares is an installer framework. By design it is very customizable,
in order to satisfy a wide variety of needs and use cases.

This package provides upstream branding for %{name}.

%lang_package

%prep
%autosetup

%build
%cmake \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo"
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file -r %{name} Qt System PackageManager

%find_lang calamares-dummypythonqt
%find_lang calamares-python

%post   -n %{library_name} -p /sbin/ldconfig
%postun -n %{library_name} -p /sbin/ldconfig

%files
%doc LICENSE AUTHORS
%{_bindir}/calamares
%{_mandir}/man8/calamares.8*
%{_datadir}/applications/calamares.desktop
%{_datadir}/icons/hicolor/scalable/apps/calamares.svg
%dir %{_datadir}/calamares/

%files -n %{library_name}
%{_libdir}/libcalamares.so.*
%{_libdir}/libcalamaresui.so.*
%{_libdir}/calamares/

%files devel
%{_includedir}/libcalamares/
%{_libdir}/libcalamares.so
%{_libdir}/libcalamaresui.so
%{_libdir}/cmake/Calamares/

%files branding-upstream
%{_datadir}/calamares/settings.conf
%{_datadir}/calamares/modules/
%{_datadir}/calamares/branding/
%{_datadir}/calamares/qml/

%files lang -f calamares-dummypythonqt.lang -f calamares-python.lang

%changelog

